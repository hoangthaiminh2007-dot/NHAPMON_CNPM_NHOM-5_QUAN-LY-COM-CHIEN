# Hệ thống Quản lý và Đặt món Quán Cơm Chiên
---

## 1. Tầm nhìn sản phẩm (Product Vision)
Hệ thống hỗ trợ quản lý thực đơn, đặt món nhanh tại bàn, theo dõi tình trạng đơn và thống kê doanh thu hiệu quả cho quán cơm chiên.

Phần mềm hướng tới việc tối ưu hóa quy trình vận hành cho các quán cơm chiên quy mô vừa và nhỏ, giảm thiểu sai sót trong quá trình gọi món thủ công, tăng tốc độ phục vụ tại bàn và cung cấp hệ thống báo cáo doanh thu trực quan, minh bạch cho chủ quán.

---

## 2. Các công cụ sử dụng
* **Ngôn ngữ lập trình:** Python (3.12+)
* **Testing Framework:** `unittest` (thư viện  Python, cấu trúc AAA: Arrange - Act - Assert)
* **Công cụ quản lý dự án & Mã nguồn:** Git, GitHub.

---

## 3. Danh sách thành viên nhóm (5 thành viên)

| STT | Họ và tên | MSSV | Vai trò trong Scrum | Tài khoản GitHub |
| :---: | :--- | :---: | :--- | :--- |
| 1 | Hoàng Thái Minh | 25S1020067 | **Scrum Master** | [@hoangthaiminh2007-dot](https://github.com/hoangthaiminh2007-dot) |
| 2 | Nguyễn Đinh Mạnh | 25S1020065 | Developer | [@manhhk6782-wq](https://github.com/manhhk6782-wq) |
| 3 | Lê Văn Chương | *Đang cập nhật* | Developer | [@chuonglevan186-prog](https://github.com/chuonglevan186-prog) |
| 4 | Đào Hữu Thiện | *Đang cập nhật* | Developer | [@tdaohuu4-glitch](https://github.com/tdaohuu4-glitch) |
| 5 | Đặng Tuấn Kiệt | *Đang cập nhật* | Developer | [@dangkiet-web](https://github.com/dangkiet-web) |

---

## 4. Phân công Sprint 1 Mini (Thực hành Chương 4)

Mỗi thành viên tạo **nhánh `feature/...` riêng từ `main`** (không code trực tiếp trên `main`), viết code logic + **tối thiểu 2 Unit Test theo cấu trúc AAA**, tạo **Pull Request** và **Review chéo** cho đồng đội:

| Issue | Nhiệm vụ (Technical Task) | Thành viên phụ trách | Nhánh Git | File Code & Unit Test | Review chéo cho | Ước lượng |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| **#1** | Quản lý thực đơn món ăn (Menu Management) | `@hoangthaiminh2007-dot` | `feature/menu-management` | `src/menu_service.py`<br>`tests/test_menu.py` | `@manhhk6782-wq` | 2h |
| **#2** | Đặt món tại bàn cho khách hàng (Table Ordering) | `@manhhk6782-wq` | `feature/table-ordering` | `src/order_service.py`<br>`tests/test_order.py` | `@chuonglevan186-prog` | 3h |
| **#3** | Theo dõi trạng thái chế biến món tại bếp (Kitchen Display) | `@chuonglevan186-prog` | `feature/kitchen-display` | `src/kitchen_service.py`<br>`tests/test_kitchen.py` | `@tdaohuu4-glitch` | 2.5h |
| **#4** | Thanh toán và In/Xuất hóa đơn (Checkout & Billing) | `@tdaohuu4-glitch` | `feature/checkout-billing` | `src/billing_service.py`<br>`tests/test_billing.py` | `@dangkiet-web` | 2.5h |
| **#5** | Báo cáo và Thống kê doanh thu (Revenue Reporting) | `@dangkiet-web` | `feature/revenue-reporting` | `src/report_service.py`<br>`tests/test_report.py` | `@hoangthaiminh2007-dot` | 2h |

### Chạy toàn bộ Unit Test
```bash
python -m unittest discover -s tests -v
```
