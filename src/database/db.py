"""Module kết nối và khởi tạo cơ sở dữ liệu SQLite."""

import sqlite3
from pathlib import Path
from typing import Union

SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"


def get_connection(db_path: Union[str, Path]) -> sqlite3.Connection:
    """Tạo kết nối SQLite mới với khóa ngoại bật sẵn và trả về bản ghi dạng Row."""
    path_str = str(db_path)
    if path_str != ":memory:":
        Path(path_str).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path_str)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(db_path: Union[str, Path]) -> None:
    """Khởi tạo cấu trúc 6 bảng và dữ liệu mẫu từ schema.sql."""
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn = get_connection(db_path)
    try:
        conn.executescript(schema_sql)
        conn.commit()
    finally:
        conn.close()


def get_db_summary(db_path: Union[str, Path]) -> dict[str, object]:
    """Lấy danh sách các bảng và số lượng bản ghi mẫu hiện có trong CSDL."""
    conn = get_connection(db_path)
    try:
        table_rows = conn.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type = 'table' AND name NOT LIKE 'sqlite_%' "
            "ORDER BY name;"
        ).fetchall()
        tables = [row["name"] for row in table_rows]

        dining_tables_count = 0
        menu_items_count = 0
        if "dining_tables" in tables:
            dining_tables_count = conn.execute(
                "SELECT COUNT(*) AS cnt FROM dining_tables;"
            ).fetchone()["cnt"]
        if "menu_items" in tables:
            menu_items_count = conn.execute(
                "SELECT COUNT(*) AS cnt FROM menu_items;"
            ).fetchone()["cnt"]

        return {
            "tables": tables,
            "table_count": len(tables),
            "dining_tables_count": dining_tables_count,
            "menu_items_count": menu_items_count,
        }
    finally:
        conn.close()
