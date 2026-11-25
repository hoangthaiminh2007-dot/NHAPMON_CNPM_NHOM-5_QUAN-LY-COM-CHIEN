# Tài liệu Thiết kế Cơ sở dữ liệu - Quản lý Quán Cơm Chiên 

## 1. Danh sách các bảng dữ liệu (6 bảng) 
1. **`categories`**: Danh mục phân loại món ăn (Cơm chiên, Nước uống, Món ăn kèm...).
2. **`menu_items`**: Danh sách thực đơn, giá tiền và trạng thái món ăn. 
3. **`dining_tables`**: Quản lý thông tin bàn và trạng thái sử dụng bàn. 
4. **`orders`**: Quản lý các đơn đặt món tại bàn. 
5. **`order_details`**: Quản lý chi tiết các món ăn trong từng đơn đặt. 
6. **`invoices`**: Quản lý thanh toán, hóa đơn và doanh thu.

## 2. Chi tiết Khóa chính (PK) & Khóa ngoại (FK) 
| Tên bảng | Khóa chính (PK) | Khóa ngoại (FK) | Bảng tham chiếu (Reference) | Mối quan hệ | 
| :--- | :--- | :--- | :--- | :---: | 
| **`categories`** | `category_id` | *Không có* | - | 1 - N với `menu_items` | 
| **`menu_items`** | `item_id` | `category_id` | `categories(category_id)` | N - 1 với `categories` | 
| **`dining_tables`** | `table_id` | *Không có* | - | 1 - N với `orders` | 
| **`orders`** | `order_id` | `table_id` | `dining_tables(table_id)` | N - 1 với `dining_tables` | 
| **`order_details`** | `detail_id` | `order_id`, `item_id` | `orders(order_id)`, `menu_items(item_id)` | N - 1 với `orders`, `menu_items` | 
| **`invoices`** | `invoice_id` | `order_id` | `orders(order_id)` | 1 - 1 với `orders` | 

## 3. Sơ đồ Quan hệ Thực thể (ERD) Sơ đồ ERD trực quan được lưu tại đường dẫn: `docs/diagrams/erd.png`.