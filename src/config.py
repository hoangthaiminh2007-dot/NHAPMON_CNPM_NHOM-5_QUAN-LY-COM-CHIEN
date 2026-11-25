"""Cấu hình ứng dụng Flask cho Hệ thống Quản lý Quán Cơm Chiên."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """Cấu hình mặc định cho môi trường phát triển và chạy thử cục bộ."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-fried-rice-secret-key")
    DATABASE_PATH = os.environ.get(
        "DATABASE_PATH", str(BASE_DIR / "instance" / "com_chien.db")
    )
    TESTING = False
