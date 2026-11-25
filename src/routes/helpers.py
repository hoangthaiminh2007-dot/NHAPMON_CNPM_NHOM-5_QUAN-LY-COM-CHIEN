"""Module hỗ trợ và danh mục thông tin cho các phân hệ Sprint 1."""

from flask import Blueprint, render_template

SPRINT_1_MODULES: list[dict[str, str]] = [
    {
        "key": "menu",
        "title": "Quản lý Thực đơn",
        "story_id": "US-01 (5 SP)",
        "route": "/menu",
        "owner": "Hoàng Thái Minh",
        "github": "@hoangthaiminh2007-dot",
        "service_file": "src/menu_service.py",
        "route_file": "src/routes/menu_routes.py",
        "summary": "Thêm, sửa, xóa món cơm chiên/đồ uống và cập nhật trạng thái Còn/Hết món.",
    },
    {
        "key": "orders",
        "title": "Đặt món tại bàn",
        "story_id": "US-02 (8 SP)",
        "route": "/orders",
        "owner": "Nguyễn Đình Mạnh",
        "github": "@manhhk6782-wq",
        "service_file": "src/order_service.py",
        "route_file": "src/routes/order_routes.py",
        "summary": "Chọn bàn trống, thêm món kèm ghi chú, tính tạm tính và gửi đơn xuống bếp.",
    },
    {
        "key": "kitchen",
        "title": "Màn hình Bếp",
        "story_id": "US-03 (5 SP)",
        "route": "/kitchen",
        "owner": "Lê Văn Chương",
        "github": "@chuonglevan186-prog",
        "service_file": "src/kitchen_service.py",
        "route_file": "src/routes/kitchen_routes.py",
        "summary": "Hiển thị phiếu món theo thứ tự và chuyển trạng thái Chờ -> Đang chế biến -> Hoàn thành.",
    },
    {
        "key": "billing",
        "title": "Thanh toán & Hóa đơn",
        "story_id": "US-04 (5 SP)",
        "route": "/billing",
        "owner": "Đào Hữu Thiện",
        "github": "@tdaohuu4-glitch",
        "service_file": "src/billing_service.py",
        "route_file": "src/routes/billing_routes.py",
        "summary": "Tính tổng tiền bàn ăn, xử lý tiền mặt/chuyển khoản, lưu hóa đơn và trả bàn trống.",
    },
    {
        "key": "reports",
        "title": "Thống kê Doanh thu",
        "story_id": "US-05 (5 SP)",
        "route": "/reports",
        "owner": "Đặng Tuấn Kiệt",
        "github": "@dangkiet-web",
        "service_file": "src/report_service.py",
        "route_file": "src/routes/report_routes.py",
        "summary": "Báo cáo doanh thu theo ngày/tháng, lọc theo khoảng thời gian và món bán chạy.",
    },
]


def create_placeholder_blueprint(module_key: str) -> Blueprint:
    """Tạo Blueprint khung Sprint 0 cho một phân hệ Sprint 1 dựa trên key."""
    module_info = next(m for m in SPRINT_1_MODULES if m["key"] == module_key)
    bp = Blueprint(module_key, __name__, url_prefix=module_info["route"])

    @bp.route("", strict_slashes=False)
    @bp.route("/", strict_slashes=False)
    def index() -> str:
        return render_template("module_placeholder.html", module=module_info)

    return bp
