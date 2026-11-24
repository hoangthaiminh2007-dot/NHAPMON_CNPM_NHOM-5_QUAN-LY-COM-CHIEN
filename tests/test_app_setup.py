"""Smoke Test kiểm tra khung ứng dụng Flask và CSDL SQLite (Sprint 0) theo AAA."""

import gc
import tempfile
import unittest
from pathlib import Path

from app import create_app
from src.database import get_db_summary, init_db


class TestAppSetup(unittest.TestCase):
    """Kiểm thử khởi tạo CSDL 6 bảng, route trang chủ, /health và 5 Blueprint khung."""

    def test_init_db_creates_all_six_tables(self) -> None:
        # 1. Arrange
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = Path(tmp_dir) / "test_com_chien.db"

            # 2. Act
            init_db(db_path)
            summary = get_db_summary(db_path)

            # 3. Assert
            self.assertEqual(
                summary["tables"],
                [
                    "dining_tables",
                    "invoices",
                    "menu_items",
                    "order_items",
                    "orders",
                    "users",
                ],
            )
            self.assertEqual(summary["table_count"], 6)
            self.assertEqual(summary["dining_tables_count"], 6)
            self.assertEqual(summary["menu_items_count"], 4)
            gc.collect()

    def test_health_endpoint_returns_ok_json(self) -> None:
        # 1. Arrange
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = Path(tmp_dir) / "test_health.db"
            app = create_app({"TESTING": True, "DATABASE_PATH": str(db_path)})
            client = app.test_client()

            # 2. Act
            response = client.get("/health")
            payload = response.get_json()

            # 3. Assert
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(payload)
            self.assertEqual(payload["status"], "ok")
            self.assertEqual(payload["database"], "connected")
            self.assertEqual(payload["table_count"], 6)
            gc.collect()

    def test_home_page_renders_successfully(self) -> None:
        # 1. Arrange
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = Path(tmp_dir) / "test_home.db"
            app = create_app({"TESTING": True, "DATABASE_PATH": str(db_path)})
            client = app.test_client()

            # 2. Act
            response = client.get("/")
            body = response.get_data(as_text=True)

            # 3. Assert
            self.assertEqual(response.status_code, 200)
            self.assertIn("Hệ thống Quản lý và Đặt món Quán Cơm Chiên", body)
            self.assertIn("6 / 6 bảng", body)
            gc.collect()

    def test_module_placeholder_routes_accessible(self) -> None:
        # 1. Arrange
        with tempfile.TemporaryDirectory() as tmp_dir:
            db_path = Path(tmp_dir) / "test_routes.db"
            app = create_app({"TESTING": True, "DATABASE_PATH": str(db_path)})
            client = app.test_client()
            routes = ["/menu", "/orders", "/kitchen", "/billing", "/reports"]

            # 2. Act & 3. Assert
            for route in routes:
                response = client.get(route)
                self.assertEqual(
                    response.status_code,
                    200,
                    f"Route {route} phải trả về HTTP 200",
                )
            gc.collect()


if __name__ == "__main__":
    unittest.main()
