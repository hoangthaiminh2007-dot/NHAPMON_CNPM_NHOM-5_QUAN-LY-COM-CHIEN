"""Đăng ký tập trung các Blueprint của ứng dụng Flask."""

from src.routes.billing_routes import billing_bp
from src.routes.kitchen_routes import kitchen_bp
from src.routes.main_routes import main_bp
from src.routes.menu_routes import menu_bp
from src.routes.order_routes import order_bp
from src.routes.report_routes import report_bp

ALL_BLUEPRINTS = [
    main_bp,
    menu_bp,
    order_bp,
    kitchen_bp,
    billing_bp,
    report_bp,
]

__all__ = [
    "ALL_BLUEPRINTS",
    "billing_bp",
    "kitchen_bp",
    "main_bp",
    "menu_bp",
    "order_bp",
    "report_bp",
]
