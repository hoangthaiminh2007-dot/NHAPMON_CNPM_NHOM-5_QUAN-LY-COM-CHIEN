# Hệ thống Quản lý và Đặt món Quán Cơm Chiên
---

## 1. Tầm nhìn sản phẩm (Product Vision)
Hệ thống hỗ trợ quản lý thực đơn, đặt món nhanh tại bàn, theo dõi tình trạng đơn và thống kê doanh thu hiệu quả cho quán cơm chiên.

Phần mềm hướng tới việc tối ưu hóa quy trình vận hành cho các quán cơm chiên quy mô vừa và nhỏ, giảm thiểu sai sót trong quá trình gọi món thủ công, tăng tốc độ phục vụ tại bàn và cung cấp hệ thống báo cáo doanh thu theo thời gian thực cho chủ quán.

## 2. Các tính năng chính (Key Features)
- [x] Quản lý bàn ăn và trạng thái bàn (Trống / Có khách / Đang dọn dẹp)
- [x] Quản lý thực đơn linh hoạt (Phân loại: Món chính, Món thêm, Topping, Đồ uống đi kèm)
- [x] Đặt món tại bàn và in phiếu chế biến tự động đến quầy bếp
- [x] Quản lý hóa đơn và thanh toán đa phương thức (Tiền mặt, Chuyển khoản QR code)
- [x] Báo cáo và thống kê doanh số bán ra theo ngày / tuần / tháng

## 3. Danh sách thành viên nhóm (Team Members)
| STT | Họ và tên | MSSV | Vai trò | GitHub Username |
| :---: | :--- | :---: | :--- | :--- |
| 1 | Hoàng Thái Minh | 23130198 | Trưởng nhóm | [@hoangthaiminh2007-dot](https://github.com/hoangthaiminh2007-dot) |
| 2 | Thành viên 2 | Đang cập nhật | Thành viên | |
| 3 | Thành viên 3 | Đang cập nhật | Thành viên | |
| 4 | Thành viên 4 | Đang cập nhật | Thành viên | |

## 4. Công nghệ sử dụng (Tech Stack)
- **Frontend / Client UI:** Java Swing / JavaFX
- **Backend Core:** Java SE
- **Database:** MySQL
- **Build Tool & Dependency Management:** Maven
- **Version Control:** Git & GitHub

## 5. Hướng dẫn cài đặt và chạy thử nghiệm (Getting Started)
### Yêu cầu hệ thống (Prerequisites)
- Cài đặt Java Development Kit (JDK) phiên bản 17 trở lên.
- Cài đặt Apache Maven 3.8+.
- Cơ sở dữ liệu MySQL Server 8.0+.

### Các bước khởi chạy dự án (Installation)
1. Clone repository về máy cá nhân:
   ```bash
   git clone https://github.com/hoangthaiminh2007-dot/NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN.git
   ```
2. Chuyển vào thư mục mã nguồn:
   ```bash
   cd NHAPMON_CNPM_NHOM-5_QUAN-LY-COM-CHIEN
   ```
3. Cấu hình cơ sở dữ liệu:
   - Tạo database `quan_ly_com_chien` trong MySQL.
   - Chạy tập lệnh khởi tạo schema và nạp dữ liệu mẫu từ thư mục `database/schema.sql`.
4. Cài đặt các gói phụ thuộc và đóng gói ứng dụng:
   ```bash
   mvn clean install
   ```
5. Khởi chạy ứng dụng:
   ```bash
   mvn exec:java
   ```
