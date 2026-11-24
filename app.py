"""Điểm khởi chạy ứng dụng Web Flask cho Hệ thống Quản lý Quán Cơm Chiên."""

import os
from typing import Any, Mapping, Optional

from flask import Flask

from src.config import Config
from src.database import init_db
from src.routes import ALL_BLUEPRINTS


def create_app(test_config: Optional[Mapping[str, Any]] = None) -> Flask:
    """Khởi tạo và cấu hình ứng dụng Flask (Application Factory)."""
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config is not None:
        app.config.from_mapping(test_config)

    init_db(app.config["DATABASE_PATH"])

    for blueprint in ALL_BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app


if __name__ == "__main__":
    application = create_app()
    debug_enabled = os.environ.get("FLASK_DEBUG", "1") == "1"
    application.run(host="127.0.0.1", port=5000, debug=debug_enabled)
