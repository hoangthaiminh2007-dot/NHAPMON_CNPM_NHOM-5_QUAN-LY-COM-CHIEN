# Kế hoạch Sprint 0 (Khởi tạo, Phân tích & Thiết lập Dự án) — Nhóm 5

- **Mục tiêu Sprint 0:** Hoàn thiện kỹ Product Backlog (có ưu tiên, Story Points, dự kiến người phụ trách), nghiên cứu & chốt Kiến trúc hệ thống phần mềm, khởi tạo khung project trên GitHub, đưa toàn bộ nhiệm vụ chuẩn bị vào Sprint 0 để theo dõi/giao việc và đảm bảo cả 5 thành viên clone/chạy thử thành công trên máy cá nhân.
- **Thời hạn hoàn thành & nộp bài:** **18h00 Thứ 4, ngày 25/11/2026 (GMT+7)** *(thực hành online)*.
- **Trello Board:** https://trello.com/b/YFeM5jjH/nh%C3%B3m-5-h%E1%BB%87-th%E1%BB%91ng-qu%E1%BA%A3n-l%C3%BD-c%C6%A1m-chi%C3%AAn
- **GitHub Repository:** https://github.com/hoangthaiminh2007-dot/NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN

---

## 1. Báo cáo rà soát tiến độ Chương 4 (Trước Sprint 0)

Tính đến **24/11/2026**, kết quả kiểm tra trên GitHub & Trello như sau:

| Thành viên | Tài khoản GitHub | Nhiệm vụ Chương 4 | Trạng thái GitHub & Test | Trạng thái Trello |
| :--- | :--- | :--- | :--- | :--- |
| **Hoàng Thái Minh** | `@hoangthaiminh2007-dot` | Issue #1 — `src/menu_service.py` + `tests/test_menu.py` | **Đã xong** — PR #6 merged (`2026-11-17`), Issue #1 đã đóng, **5/5 tests PASS** *(cần lưu ý bổ sung review chéo PR sau này)* | Đã chuyển `Done` & tích hoàn thành |
| **Nguyễn Đinh Mạnh** | `@manhhk6782-wq` | Issue #2 — `src/order_service.py` + `tests/test_order.py` | **CHƯA LÀM** — Issue #2 vẫn `OPEN`, chưa có nhánh `feature/table-ordering`, chưa có PR/code/test | Đã chuyển vào `Sprint 0 - To Do` để xử lý dứt điểm |
| **Lê Văn Chương** | `@chuonglevan186-prog` | Issue #3 — `src/kitchen_service.py` + `tests/test_kitchen.py` | **Đã xong** — PR #9 được `@tdaohuu4-glitch` duyệt & merged (`2026-11-20`), Issue #3 đã đóng, **4/4 tests PASS** *(thiếu MSSV trong README)* | Đã chuyển `Done` & tích hoàn thành |
| **Đào Hữu Thiện** | `@tdaohuu4-glitch` | Issue #4 — `src/billing_service.py` + `tests/test_billing.py` | **Đã xong code & PR** — PR #7 merged bởi `@dangkiet-web` (`2026-11-17`), **4/4 tests PASS** *(Issue #4 trên GitHub quên đóng, thiếu MSSV trong README)* | Đã chuyển `Done` & tích hoàn thành |
| **Đặng Tuấn Kiệt** | `@dangkiet-web` | Issue #5 — `src/report_service.py` + `tests/test_report.py` | **Đã xong code & PR** — PR #8 được `@hoangthaiminh2007-dot` duyệt & merged (`2026-11-18`), **8/8 tests PASS** *(Issue #5 trên GitHub quên đóng, thiếu MSSV trong README)* | Đã chuyển `Done` & tích hoàn thành |

> Tổng kiểm thử hiện có trên nhánh `main`: **21/21 Unit Tests PASS**.

---

## 2. Phân công Nhiệm vụ Sprint 0 (Theo dõi trên Trello)

| Mã thẻ | Nhiệm vụ Sprint 0 | Phụ trách | Điểm (SP) | Cột hiện tại trên Trello | Hạn chót |
| :---: | :--- | :--- | :---: | :--- | :---: |
| **S0-01** | Hoàn thiện Product Backlog (10 US, ưu tiên, Story Points, phân công) | Hoàng Thái Minh | 3 | **Done (Hoàn thành)** | 25/11 18h00 |
| **Issue #2** | Hoàn tất phần tồn đọng Chương 4: Đặt món tại bàn (`order_service.py` + test + PR) | Nguyễn Đinh Mạnh | — | **Sprint 0 - To Do** | 25/11 18h00 |
| **S0-02** | Nghiên cứu & lập tài liệu Kiến trúc hệ thống (`docs/ARCHITECTURE.md`) | Hoàng Thái Minh & Lê Văn Chương | 3 | **Sprint 0 - In Progress** | 25/11 18h00 |
| **S0-03** | Thiết kế sơ đồ ERD & tạo file `src/database/schema.sql` mẫu | Đặng Tuấn Kiệt | 3 | **Sprint 0 - To Do** | 25/11 18h00 |
| **S0-04** | Phác thảo Wireframe 5 màn hình chính & cập nhật MSSV vào `README.md` | Đào Hữu Thiện | 3 | **Sprint 0 - To Do** | 25/11 18h00 |
| **S0-05** | Khởi tạo khung Project Web App, `requirements.txt`, đóng Issue #4/#5, đẩy lên GitHub | Hoàng Thái Minh & Lê Văn Chương | 3 | **Sprint 0 - In Progress** | 25/11 18h00 |
| **S0-06** | Cả nhóm `git clone` / `git pull` repo về máy, cài môi trường & chạy thử test | Cả nhóm (5 người) | 2 | **Sprint 0 - In Progress** | 25/11 18h00 |

---

## 3. Hướng dẫn Nhanh cho Thành viên Clone / Pull & Chạy thử trên Máy

Mỗi thành viên thực hiện theo 4 bước sau và tích xác nhận tên mình trong thẻ **S0-06** trên Trello:

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

# 3. Cài đặt thư viện cần thiết cho Web App (Sprint 1)
pip install -r requirements.txt

# 4. Chạy toàn bộ Unit Test để kiểm tra môi trường
python -m unittest discover -s tests -v
```

Nếu kết quả báo `Ran 21 tests ... OK` (hoặc nhiều hơn sau khi Issue #2 được merge), môi trường trên máy bạn đã sẵn sàng cho **Sprint 1**.
