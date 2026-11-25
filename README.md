# Hệ thống Quản lý và Đặt món Quán Cơm Chiên (Nhóm 5)
---

## 1. Tầm nhìn sản phẩm (Product Vision)
Hệ thống hỗ trợ quản lý thực đơn, đặt món nhanh tại bàn, theo dõi tình trạng đơn và thống kê doanh thu hiệu quả cho quán cơm chiên.

Phần mềm hướng tới việc tối ưu hóa quy trình vận hành cho các quán cơm chiên quy mô vừa và nhỏ, giảm thiểu sai sót trong quá trình gọi món thủ công, tăng tốc độ phục vụ tại bàn và cung cấp hệ thống báo cáo doanh thu trực quan, minh bạch cho chủ quán.

---

## 2. Công nghệ & Công cụ sử dụng (Tech Stack)
* **Ngôn ngữ lập trình:** Python (`3.12+`)
* **Web Framework:** Flask (`>=3.0,<4.0`) + Jinja2 (HTML5/CSS3/JS)
* **Cơ sở dữ liệu:** SQLite (`sqlite3`)
* **Testing Framework:** `unittest` (thư viện chuẩn Python, cấu trúc AAA: Arrange - Act - Assert)
* **Quản lý dự án & Mã nguồn:** Git, GitHub, [Trello Board Nhóm 5](https://trello.com/b/YFeM5jjH/nh%C3%B3m-5-h%E1%BB%87-th%E1%BB%91ng-qu%E1%BA%A3n-l%C3%BD-c%C6%A1m-chi%C3%AAn)

---

## 3. Tài liệu Dự án (Sprint 0)
* 📋 **Product Backlog (10 User Stories - 47 SP):** [docs/PRODUCT_BACKLOG.md](docs/PRODUCT_BACKLOG.md)
* 🏗️ **Kiến trúc Hệ thống & CSDL (3-Layer + MVC):** [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
* 🗓️ **Kế hoạch & Phân công Sprint 0:** [docs/SPRINT_0_PLAN.md](docs/SPRINT_0_PLAN.md)
* 🎨 **Wireframe 5 màn hình chính (S0-04):** [docs/wireframes/](docs/wireframes/)
* 📌 **Bảng quản lý công việc Trello:** https://trello.com/b/YFeM5jjH/nh%C3%B3m-5-h%E1%BB%87-th%E1%BB%91ng-qu%E1%BA%A3n-l%C3%BD-c%C6%A1m-chi%C3%AAn

---

## 4. Danh sách thành viên nhóm (5 thành viên)

| STT | Họ và tên | MSSV | Vai trò trong Scrum | Tài khoản GitHub |
| :---: | :--- | :---: | :--- | :--- |
| 1 | Hoàng Thái Minh | 25S1020067 | **Scrum Master** | [@hoangthaiminh2007-dot](https://github.com/hoangthaiminh2007-dot) |
| 2 | Nguyễn Đình Mạnh | 25S1020065 | Developer | [@manhhk6782-wq](https://github.com/manhhk6782-wq) |
| 3 | Lê Văn Chương | *Đang cập nhật* | Developer | [@chuonglevan186-prog](https://github.com/chuonglevan186-prog) |
| 4 | Đào Hữu Thiện | 25S1020101 | Developer | [@tdaohuu4-glitch](https://github.com/tdaohuu4-glitch) |
| 5 | Đặng Tuấn Kiệt | *Đang cập nhật* | Developer | [@dangkiet-web](https://github.com/dangkiet-web) |

---

## 5. Tiến độ Core Logic (Thực hành Chương 4 — 5/5 Hoàn thành)

Mỗi phân hệ được phát triển trên **nhánh `feature/...` riêng từ `main`**, gồm code logic nghiệp vụ + **Unit Test theo cấu trúc AAA**, tạo **Pull Request** và **Merge vào `main`**:

| Issue | Nhiệm vụ (Technical Task) | Thành viên phụ trách | Nhánh Git | File Code & Unit Test | Trạng thái |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **#1** | Quản lý thực đơn món ăn (Menu Management) | `@hoangthaiminh2007-dot` | `feature/menu-management` | `src/menu_service.py`<br>`tests/test_menu.py` | **Đã xong** (PR #6 merged, 5 tests PASS) |
| **#2** | Đặt món tại bàn cho khách hàng (Table Ordering) | `@manhhk6782-wq` *(Minh làm thay)* | `feature/table-ordering` | `src/order_service.py`<br>`tests/test_order.py` | **Đã xong** (PR #10 merged, 6 tests PASS — chờ đóng Issue #2) |
| **#3** | Theo dõi trạng thái chế biến món tại bếp (Kitchen Display) | `@chuonglevan186-prog` | `feature/kitchen-display` | `src/kitchen_service.py`<br>`tests/test_kitchen.py` | **Đã xong** (PR #9 merged, 4 tests PASS) |
| **#4** | Thanh toán và In/Xuất hóa đơn (Checkout & Billing) | `@tdaohuu4-glitch` | `feature/checkout-billing` | `src/billing_service.py`<br>`tests/test_billing.py` | **Đã xong** (PR #7 merged, 4 tests PASS — chờ đóng Issue #4) |
| **#5** | Báo cáo và Thống kê doanh thu (Revenue Reporting) | `@dangkiet-web` | `feature/revenue-reporting` | `src/report_service.py`<br>`tests/test_report.py` | **Đã xong** (PR #8 merged, 8 tests PASS — chờ đóng Issue #5) |

---

## 6. Hướng dẫn Clone, Cài đặt Môi trường, Chạy Web App & Unit Test

```bash
# 1. Clone repository về máy (hoặc git pull origin main nếu đã clone)
git clone https://github.com/hoangthaiminh2007-dot/NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN.git
cd NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN

# 2. Cài đặt thư viện
pip install -r requirements.txt

# 3. Chạy toàn bộ Unit Test (27 test Chương 4 + 4 smoke test khung Web App = 31 tests)
python -m unittest discover -s tests -v

# 4. Khởi chạy khung ứng dụng Web Flask (tự tạo CSDL SQLite 6 bảng tại instance/com_chien.db)
python app.py
# Sau đó mở trình duyệt tại: http://127.0.0.1:5000
```
