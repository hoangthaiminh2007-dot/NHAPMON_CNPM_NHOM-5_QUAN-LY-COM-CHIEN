# Kế hoạch Sprint 0 (Khởi tạo, Phân tích & Thiết lập Dự án) — Nhóm 5

- **Mục tiêu Sprint 0:** Hoàn thiện kỹ Product Backlog (có ưu tiên, Story Points, dự kiến người phụ trách), nghiên cứu & chốt Kiến trúc hệ thống phần mềm, khởi tạo khung project Web App chạy được trên GitHub (`Flask + SQLite 6 bảng`), đưa toàn bộ nhiệm vụ chuẩn bị vào Sprint 0 trên Trello để theo dõi/giao việc và đảm bảo cả 5 thành viên clone/chạy thử thành công trên máy cá nhân.
- **Thời hạn hoàn thành & nộp bài:** **18h00 Thứ 4, ngày 25/11/2026 (GMT+7)** *(hạn nội bộ hoàn thành PR của nhóm: 17h00 Thứ 4)*.
- **Trello Board:** https://trello.com/b/YFeM5jjH/nh%C3%B3m-5-h%E1%BB%87-th%E1%BB%91ng-qu%E1%BA%A3n-l%C3%BD-c%C6%A1m-chi%C3%AAn
- **GitHub Repository:** https://github.com/hoangthaiminh2007-dot/NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN

---

## 1. Báo cáo rà soát tiến độ Chương 4 (Đã hoàn thành 5/5)

Tính đến **24/11/2026**, toàn bộ **5/5 tính năng core logic Chương 4** đã được merge vào `main` trên GitHub:

| Thành viên | Tài khoản GitHub | Nhiệm vụ Chương 4 | Trạng thái GitHub & Test | Trạng thái Trello |
| :--- | :--- | :--- | :--- | :--- |
| **Hoàng Thái Minh** | `@hoangthaiminh2007-dot` | Issue #1 — `src/menu_service.py` + `tests/test_menu.py` | **Đã xong** — PR #6 merged (`2026-11-17`), Issue #1 đã đóng, **5/5 tests PASS** | Đã chuyển `Done` |
| **Nguyễn Đinh Mạnh** | `@manhhk6782-wq` | Issue #2 — `src/order_service.py` + `tests/test_order.py` | **Đã xong** *(Minh làm thay)* — PR #10 merged (`2026-11-24`), **6/6 tests PASS** *(Issue #2 chờ bấm đóng)* | Đã chuyển `Done` |
| **Lê Văn Chương** | `@chuonglevan186-prog` | Issue #3 — `src/kitchen_service.py` + `tests/test_kitchen.py` | **Đã xong** — PR #9 được `@tdaohuu4-glitch` duyệt & merged (`2026-11-20`), Issue #3 đã đóng, **4/4 tests PASS** *(thiếu MSSV)* | Đã chuyển `Done` |
| **Đào Hữu Thiện** | `@tdaohuu4-glitch` | Issue #4 — `src/billing_service.py` + `tests/test_billing.py` | **Đã xong** — PR #7 merged bởi `@dangkiet-web` (`2026-11-17`), **4/4 tests PASS** *(Issue #4 chờ bấm đóng; đã cập nhật MSSV `25S1020101` tại PR #11)* | Đã chuyển `Done` |
| **Đặng Tuấn Kiệt** | `@dangkiet-web` | Issue #5 — `src/report_service.py` + `tests/test_report.py` | **Đã xong** — PR #8 được `@hoangthaiminh2007-dot` duyệt & merged (`2026-11-18`), **8/8 tests PASS** *(Issue #5 chờ bấm đóng, thiếu MSSV)* | Đã chuyển `Done` |

> Tổng kiểm thử hiện có trên nhánh `main`: **31/31 Unit Tests PASS** (27 tests Chương 4 + 4 smoke tests khung Web App Sprint 0).

---

## 2. Phân công Nhiệm vụ Sprint 0 (Theo dõi trên Trello & nộp PR trên GitHub)

| Mã thẻ | Nhiệm vụ Sprint 0 | Phụ trách | SP | Cột trên Trello | Sản phẩm nộp (PR / Kết quả) | Hạn chót |
| :---: | :--- | :--- | :---: | :--- | :--- | :---: |
| **S0-01** | Hoàn thiện Product Backlog (10 US, ưu tiên, Story Points, phân công) | Hoàng Thái Minh | 3 | **Done** | 10 thẻ trên Trello + `docs/PRODUCT_BACKLOG.md` | 25/11 18h00 |
| **S0-05** | Khởi tạo khung Web App Flask + SQLite 6 bảng + 5 Blueprints + Smoke Tests | Hoàng Thái Minh | 3 | **Done** | `app.py`, `src/database/schema.sql`, `src/routes/`, `templates/`, `tests/test_app_setup.py` | 25/11 18h00 |
| **S0-02** | Rà soát `docs/ARCHITECTURE.md` + bổ sung sơ đồ Use Case & luồng trạng thái + MSSV | Minh & **Lê Văn Chương** | 3 | **In Progress** | Chương gửi PR nhánh `docs/sprint0-usecase-diagrams` (`docs/diagrams/` + MSSV) | 25/11 17h00 |
| **S0-03** | Vẽ sơ đồ ERD trực quan từ `schema.sql` & viết mô tả bảng trong `docs/DATABASE.md` + MSSV | **Đặng Tuấn Kiệt** | 3 | **To Do** | Kiệt gửi PR nhánh `docs/sprint0-erd-database` (`docs/diagrams/erd.png` + `docs/DATABASE.md` + MSSV) | 25/11 17h00 |
| **S0-04** | Phác thảo Wireframe 5 màn hình chính & cập nhật MSSV vào `README.md` | **Đào Hữu Thiện** | 3 | **Done** | Đã xong — PR #11 (MSSV `25S1020101`) & PR #12 (5 ảnh trong `docs/wireframes/`) merged (25/11/2026) | 25/11 17h00 |
| **S0-07** | Clone/chạy thử hệ thống (`app.py` + `unittest`) & viết phân tích luồng `US-02` | **Nguyễn Đinh Mạnh** | 3 | **To Do** | Mạnh gửi PR nhánh `docs/sprint0-order-notes` (`docs/ORDER_FLOW_NOTES.md`) + ảnh chụp chạy 31/31 tests | 25/11 17h00 |
| **S0-06** | Cả nhóm `git clone` / `git pull`, cài môi trường, chạy `app.py` & `unittest` | **Cả nhóm (5 người)** | 2 | **In Progress** | Minh đã xác nhận; 4 thành viên còn lại chạy xong và tự tích tên trên thẻ `S0-06` | 25/11 17h00 |

---

## 3. Hướng dẫn Nhanh cho Thành viên Clone / Pull & Chạy thử trên Máy

Mỗi thành viên thực hiện theo các bước sau và tích xác nhận tên mình trong thẻ **S0-06** trên Trello:

```bash
# 1. Clone repo (nếu chưa có trên máy) hoặc pull bản mới nhất
git clone https://github.com/hoangthaiminh2007-dot/NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN.git
cd NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN

# Nếu đã clone trước đó:
git checkout main
git pull origin main

# 2. Tạo và kích hoạt môi trường ảo (khuyến nghị)
python -m venv .venv
# Windows (PowerShell): .\.venv\Scripts\Activate.ps1
# macOS / Linux:       source .venv/bin/activate

# 3. Cài đặt thư viện cần thiết
pip install -r requirements.txt

# 4. Chạy toàn bộ Unit Test để kiểm tra môi trường (kỳ vọng: Ran 31 tests ... OK)
python -m unittest discover -s tests -v

# 5. Khởi chạy thử khung Web App Flask
python app.py
# Mở trình duyệt vào http://127.0.0.1:5000 (và http://127.0.0.1:5000/health)
```
