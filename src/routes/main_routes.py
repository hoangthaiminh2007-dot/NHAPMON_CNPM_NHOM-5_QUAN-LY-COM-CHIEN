"""Blueprint trang chủ và kiểm tra trạng thái hệ thống (Sprint 0)."""

from flask import Blueprint, Response, current_app, jsonify, render_template

from src.database import get_db_summary
from src.routes.helpers import SPRINT_1_MODULES

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home() -> str:
    """Hiển thị trang tổng quan khung dự án và trạng thái CSDL."""
    summary = get_db_summary(current_app.config["DATABASE_PATH"])
    return render_template(
        "index.html",
        db_summary=summary,
        modules=SPRINT_1_MODULES,
    )


@main_bp.route("/health")
def health() -> tuple[Response, int]:
    """Trả về JSON trạng thái hoạt động và danh sách bảng SQLite."""
    summary = get_db_summary(current_app.config["DATABASE_PATH"])
    return (
        jsonify(
            {
                "status": "ok",
                "database": "connected",
                "tables": summary["tables"],
                "table_count": summary["table_count"],
                "dining_tables_count": summary["dining_tables_count"],
                "menu_items_count": summary["menu_items_count"],
            }
        ),
        200,
    )
