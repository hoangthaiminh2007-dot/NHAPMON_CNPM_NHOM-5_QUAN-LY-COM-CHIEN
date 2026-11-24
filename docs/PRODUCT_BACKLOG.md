# Product Backlog — Hệ thống Quản lý và Đặt món Quán Cơm Chiên (Nhóm 5)

Tài liệu này đồng bộ 1-1 với cột **Product Backlog** trên bảng Trello của nhóm:  
- **Trello Board:** https://trello.com/b/YFeM5jjH/nh%C3%B3m-5-h%E1%BB%87-th%E1%BB%91ng-qu%E1%BA%A3n-l%C3%BD-c%C6%A1m-chi%C3%AAn
- **GitHub Repository:** https://github.com/hoangthaiminh2007-dot/NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN

---

## 1. Quy ước Độ ưu tiên & Story Points

- **Độ ưu tiên (Priority):**
  - **P1 - Cao (Nhãn Đỏ):** Tính năng cốt lõi (MVP), cần hoàn thành sớm nhất để quán vận hành được luồng đặt món → bếp → thanh toán → thống kê và bảo mật cơ bản.
  - **P2 - Trung bình (Nhãn Cam):** Tính năng mở rộng nâng cao trải nghiệm vận hành (quản lý bàn, sửa/hủy món, giảm giá/phụ thu).
  - **P3 - Thấp (Nhãn Vàng):** Tính năng hỗ trợ đối soát, tiện ích bổ sung (tra cứu hóa đơn, xuất CSV).
- **Điểm số (Story Points - Fibonacci):** `1, 2, 3, 5, 8, 13` — đánh giá dựa trên độ phức tạp nghiệp vụ, giao diện, cơ sở dữ liệu và số lượng kiểm thử cần thiết.

---

## 2. Bảng tổng hợp Product Backlog (10 User Stories — 47 SP)

| Mã US | Tên User Story | Độ ưu tiên | Story Points | Dự kiến phụ trách | Sprint dự kiến | Trạng thái hiện tại |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| **US-01** | Quản lý thực đơn các món cơm chiên | P1 - Cao | 5 | Hoàng Thái Minh (`@hoangthaiminh2007-dot`) | Sprint 1 | Đã có core logic Chương 4 (`src/menu_service.py`); Sprint 1 tích hợp Web + SQLite |
| **US-02** | Nhân viên đặt món nhanh tại bàn cho khách | P1 - Cao | 8 | Nguyễn Đinh Mạnh (`@manhhk6782-wq`) | Sprint 1 | Chờ hoàn thành core logic Chương 4 (Issue #2), sau đó tích hợp Web + SQLite |
| **US-03** | Màn hình bếp theo dõi & cập nhật trạng thái chế biến | P1 - Cao | 5 | Lê Văn Chương (`@chuonglevan186-prog`) | Sprint 1 | Đã có core logic Chương 4 (`src/kitchen_service.py`); Sprint 1 tích hợp Web + SQLite |
| **US-04** | Thanh toán đơn hàng & xuất hóa đơn cho bàn ăn | P1 - Cao | 5 | Đào Hữu Thiện (`@tdaohuu4-glitch`) | Sprint 1 | Đã có core logic Chương 4 (`src/billing_service.py`); Sprint 1 tích hợp Web + SQLite |
| **US-05** | Chủ quán xem báo cáo & thống kê doanh thu ngày/tháng | P1 - Cao | 5 | Đặng Tuấn Kiệt (`@dangkiet-web`) | Sprint 1 | Đã có core logic Chương 4 (`src/report_service.py`); Sprint 1 tích hợp Web + SQLite |
| **US-06** | Đăng nhập & phân quyền tài khoản nhân sự | P1 - Cao | 5 | Hoàng Thái Minh (`@hoangthaiminh2007-dot`) | Sprint 2 | Chưa bắt đầu (Planned) |
| **US-07** | Quản lý danh sách & trạng thái bàn ăn | P2 - TB | 3 | Nguyễn Đinh Mạnh (`@manhhk6782-wq`) | Sprint 2 | Chưa bắt đầu (Planned) |
| **US-08** | Chỉnh sửa, gọi thêm hoặc hủy món trong đơn đang mở | P2 - TB | 5 | Lê Văn Chương (`@chuonglevan186-prog`) | Sprint 2 | Chưa bắt đầu (Planned) |
| **US-09** | Áp dụng khuyến mãi / giảm giá & phụ thu khi thanh toán | P2 - TB | 3 | Đào Hữu Thiện (`@tdaohuu4-glitch`) | Sprint 2 | Chưa bắt đầu (Planned) |
| **US-10** | Tra cứu lịch sử hóa đơn & xuất báo cáo CSV | P3 - Thấp | 3 | Đặng Tuấn Kiệt (`@dangkiet-web`) | Sprint 2 | Chưa bắt đầu (Planned) |
| **Tổng** | **10 User Stories** | — | **47 SP** | **5 thành viên** | **2 Sprint** | — |

---

## 3. Thống kê phân bổ khối lượng dự kiến theo thành viên

| Thành viên | Tài khoản GitHub | Các US phụ trách | Số US | Tổng Story Points |
| :--- | :--- | :--- | :---: | :---: |
| Hoàng Thái Minh | `@hoangthaiminh2007-dot` | US-01 (5), US-06 (5) | 2 | **10 SP** |
| Nguyễn Đinh Mạnh | `@manhhk6782-wq` | US-02 (8), US-07 (3) | 2 | **11 SP** |
| Lê Văn Chương | `@chuonglevan186-prog` | US-03 (5), US-08 (5) | 2 | **10 SP** |
| Đào Hữu Thiện | `@tdaohuu4-glitch` | US-04 (5), US-09 (3) | 2 | **8 SP** |
| Đặng Tuấn Kiệt | `@dangkiet-web` | US-05 (5), US-10 (3) | 2 | **8 SP** |

---

## 4. Đặc tả chi tiết từng User Story & Tiêu chí Chấp nhận (Acceptance Criteria)

### US-01: Quản lý thực đơn các món cơm chiên
- **Độ ưu tiên:** P1 - Cao | **Story Points:** 5 | **Phụ trách:** Hoàng Thái Minh | **Sprint:** 1
- **User Story:** Là một chủ quán cơm chiên, tôi muốn thêm, sửa, xóa và cập nhật trạng thái còn/hết món trong thực đơn, để nhân viên và khách hàng luôn xem được danh sách món chính xác.
- **Tiêu chí chấp nhận (AC):**
  1. Thêm/sửa/xóa món gồm: Tên món, Giá bán, Danh mục, Ảnh minh họa, Trạng thái (Còn món/Hết món).
  2. Khi đánh dấu "Hết món" thì tự động khóa không cho chọn món đó khi đặt món tại bàn.
  3. Báo lỗi rõ ràng nếu tên món bị bỏ trống/trùng hoặc giá bán <= 0.
  4. Hỗ trợ lọc danh sách món theo danh mục và trạng thái còn món.

### US-02: Nhân viên đặt món nhanh tại bàn cho khách
- **Độ ưu tiên:** P1 - Cao | **Story Points:** 8 | **Phụ trách:** Nguyễn Đinh Mạnh | **Sprint:** 1
- **User Story:** Là một nhân viên phục vụ, tôi muốn chọn số bàn và chọn các món cơm chiên khách gọi ngay trên hệ thống, để chuyển đơn xuống bếp nhanh chóng và tránh ghi nhầm món.
- **Tiêu chí chấp nhận (AC):**
  1. Cho phép chọn bàn trống, thêm nhiều món cơm chiên/đồ uống, nhập số lượng và ghi chú (ít cay, thêm trứng, không hành...).
  2. Tự động hiển thị tạm tính và không cho chọn món đang ở trạng thái "Hết món".
  3. Khi bấm "Gửi đơn", đơn hàng chuyển sang trạng thái "Chờ chế biến" và hiển thị ngay sang màn hình bếp.
  4. Báo lỗi nếu chưa chọn số bàn hoặc đơn hàng chưa có món nào.

### US-03: Màn hình bếp theo dõi & cập nhật trạng thái chế biến
- **Độ ưu tiên:** P1 - Cao | **Story Points:** 5 | **Phụ trách:** Lê Văn Chương | **Sprint:** 1
- **User Story:** Là một nhân viên bếp, tôi muốn xem danh sách các phiếu món cơm chiên theo thứ tự đặt và cập nhật trạng thái chế biến, để phục vụ đúng thứ tự và giúp nhân viên bàn biết món nào đã xong.
- **Tiêu chí chấp nhận (AC):**
  1. Hiển thị danh sách phiếu món theo thứ tự đặt trước xếp trên kèm số bàn, tên món, số lượng, ghi chú.
  2. Chỉ cho phép chuyển trạng thái đúng luồng: "Chờ chế biến" → "Đang chế biến" → "Hoàn thành".
  3. Không cho phép nhảy cóc trạng thái (từ "Chờ chế biến" sang thẳng "Hoàn thành").
  4. Cập nhật trạng thái hiển thị ngay cho nhân viên phục vụ khi món hoàn thành.

### US-04: Thanh toán đơn hàng & xuất hóa đơn cho bàn ăn
- **Độ ưu tiên:** P1 - Cao | **Story Points:** 5 | **Phụ trách:** Đào Hữu Thiện | **Sprint:** 1
- **User Story:** Là một thu ngân, tôi muốn tính tổng tiền đơn hàng của bàn và xuất hóa đơn thanh toán, để thu tiền khách nhanh chóng và chính xác.
- **Tiêu chí chấp nhận (AC):**
  1. Tự động tính tổng tiền dựa trên số lượng và đơn giá từng món trong đơn hàng.
  2. Hỗ trợ chọn phương thức thanh toán Tiền mặt (tự động tính tiền thừa) hoặc Chuyển khoản.
  3. Sau khi xác nhận thanh toán, lưu hóa đơn vào CSDL và trả bàn về trạng thái "Trống".
  4. Không cho phép thanh toán đơn trống hoặc khi số tiền khách đưa nhỏ hơn tổng tiền.

### US-05: Chủ quán xem báo cáo & thống kê doanh thu ngày/tháng
- **Độ ưu tiên:** P1 - Cao | **Story Points:** 5 | **Phụ trách:** Đặng Tuấn Kiệt | **Sprint:** 1
- **User Story:** Là một chủ quán cơm chiên, tôi muốn xem báo cáo doanh thu và các món bán chạy theo ngày/tháng, để nắm bắt tình hình kinh doanh và chuẩn bị nguyên liệu hợp lý.
- **Tiêu chí chấp nhận (AC):**
  1. Hiển thị tổng số đơn đã thanh toán (`COMPLETED`), tổng số món và tổng doanh thu theo ngày/tháng.
  2. Thống kê Top các món cơm chiên bán chạy nhất theo số lượng và doanh thu.
  3. Cho phép lọc thống kê theo khoảng ngày bắt đầu – ngày kết thúc.
  4. Báo lỗi nếu ngày bắt đầu lớn hơn ngày kết thúc hoặc sai định dạng ngày.

### US-06: Đăng nhập & phân quyền tài khoản nhân sự
- **Độ ưu tiên:** P1 - Cao | **Story Points:** 5 | **Phụ trách:** Hoàng Thái Minh | **Sprint:** 2
- **User Story:** Là một chủ quán cơm chiên, tôi muốn hệ thống có đăng nhập và phân quyền theo vai trò nhân sự, để bảo mật dữ liệu doanh thu và mỗi bộ phận chỉ thao tác đúng chức năng của mình.
- **Tiêu chí chấp nhận (AC):**
  1. Hỗ trợ 4 vai trò: Chủ quán (`ADMIN`), Phục vụ (`WAITER`), Bếp (`KITCHEN`), Thu ngân (`CASHIER`).
  2. Mật khẩu lưu trữ dưới dạng băm (`hash`) an toàn và kiểm tra hợp lệ khi đăng nhập.
  3. Phân quyền truy cập đúng màn hình theo vai trò (chỉ Chủ quán xem được báo cáo doanh thu và sửa thực đơn).
  4. Hiển thị thông báo lỗi rõ ràng khi sai tài khoản/mật khẩu và cho phép đăng xuất.

### US-07: Quản lý danh sách & trạng thái bàn ăn
- **Độ ưu tiên:** P2 - Trung bình | **Story Points:** 3 | **Phụ trách:** Nguyễn Đinh Mạnh | **Sprint:** 2
- **User Story:** Là một nhân viên phục vụ/chủ quán, tôi muốn quản lý danh sách bàn ăn và xem trực quan trạng thái từng bàn, để sắp xếp chỗ ngồi nhanh và tránh nhầm lẫn bàn đang có khách.
- **Tiêu chí chấp nhận (AC):**
  1. Cho phép thêm, sửa, xóa số bàn và sức chứa (số ghế) của từng bàn.
  2. Hiển thị trực quan trạng thái từng bàn: `Trống` / `Đang phục vụ` / `Chờ thanh toán`.
  3. Không cho phép xóa bàn đang có đơn hàng chưa thanh toán.
  4. Hỗ trợ thao tác chuyển bàn cho khách khi cần thiết.

### US-08: Chỉnh sửa, gọi thêm hoặc hủy món trong đơn đang mở
- **Độ ưu tiên:** P2 - Trung bình | **Story Points:** 5 | **Phụ trách:** Lê Văn Chương | **Sprint:** 2
- **User Story:** Là một nhân viên phục vụ, tôi muốn chỉnh sửa, gọi thêm hoặc hủy món trong đơn đang mở của bàn, để đáp ứng kịp thời khi khách thay đổi nhu cầu.
- **Tiêu chí chấp nhận (AC):**
  1. Cho phép gọi thêm món vào đơn hiện tại của bàn và gửi phiếu bổ sung xuống màn hình bếp.
  2. Cho phép hủy món nếu món đó vẫn đang ở trạng thái "Chờ chế biến".
  3. Khóa thao tác hủy món khi bếp đã chuyển sang "Đang chế biến" hoặc "Hoàn thành".
  4. Tự động tính và cập nhật lại tổng tiền tạm tính của đơn hàng sau khi thêm/hủy.

### US-09: Áp dụng khuyến mãi / giảm giá & phụ thu khi thanh toán
- **Độ ưu tiên:** P2 - Trung bình | **Story Points:** 3 | **Phụ trách:** Đào Hữu Thiện | **Sprint:** 2
- **User Story:** Là một thu ngân, tôi muốn áp dụng giảm giá và phụ thu (như hộp mang về, thêm topping) khi thanh toán, để tính đúng số tiền khách cần trả trong các dịp khuyến mãi.
- **Tiêu chí chấp nhận (AC):**
  1. Hỗ trợ áp dụng giảm giá theo phần trăm (%) hoặc số tiền cố định (VND) và các khoản phụ thu.
  2. Đảm bảo tổng tiền cuối cùng sau giảm giá không nhỏ hơn 0 đồng.
  3. Hiển thị chi tiết khoản giảm giá và phụ thu rõ ràng trên hóa đơn xuất ra.
  4. Báo lỗi nếu mã/mức giảm giá không hợp lệ (giảm quá 100%, số âm hoặc hết hạn).

### US-10: Tra cứu lịch sử hóa đơn & xuất báo cáo CSV
- **Độ ưu tiên:** P3 - Thấp | **Story Points:** 3 | **Phụ trách:** Đặng Tuấn Kiệt | **Sprint:** 2
- **User Story:** Là một chủ quán/thu ngân, tôi muốn tra cứu lại lịch sử hóa đơn cũ và xuất báo cáo doanh thu ra file CSV, để đối soát số liệu khi cần và lưu trữ trên Excel.
- **Tiêu chí chấp nhận (AC):**
  1. Cho phép tìm kiếm hóa đơn theo mã hóa đơn, số bàn hoặc ngày thanh toán.
  2. Cho phép mở xem chi tiết danh sách món, giảm giá và tổng tiền của từng hóa đơn cũ.
  3. Hỗ trợ nút "Xuất CSV" để tải về báo cáo doanh thu đúng định dạng UTF-8 mở được bằng Excel.
