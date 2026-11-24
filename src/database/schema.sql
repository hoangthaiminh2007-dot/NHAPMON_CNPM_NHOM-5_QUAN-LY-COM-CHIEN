-- Schema CSDL SQLite cho Hệ thống Quản lý và Đặt món Quán Cơm Chiên (Nhóm 5)
PRAGMA foreign_keys = ON;

-- 1. Bảng tài khoản nhân sự
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    full_name TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('ADMIN', 'WAITER', 'KITCHEN', 'CASHIER')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bảng thực đơn món ăn & đồ uống
CREATE TABLE IF NOT EXISTS menu_items (
    item_id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    price REAL NOT NULL CHECK (price > 0),
    category TEXT NOT NULL,
    image_url TEXT DEFAULT '',
    available INTEGER NOT NULL DEFAULT 1 CHECK (available IN (0, 1))
);

-- 3. Bảng danh sách bàn ăn
CREATE TABLE IF NOT EXISTS dining_tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_number INTEGER NOT NULL UNIQUE CHECK (table_number > 0),
    capacity INTEGER NOT NULL DEFAULT 4 CHECK (capacity > 0),
    status TEXT NOT NULL DEFAULT 'Trống' CHECK (status IN ('Trống', 'Đang phục vụ', 'Chờ thanh toán'))
);

-- 4. Bảng đơn đặt món theo bàn
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_id INTEGER NOT NULL,
    waiter_id INTEGER,
    status TEXT NOT NULL DEFAULT 'OPEN' CHECK (status IN ('OPEN', 'COMPLETED', 'CANCELLED')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (table_id) REFERENCES dining_tables(id),
    FOREIGN KEY (waiter_id) REFERENCES users(id)
);

-- 5. Bảng chi tiết từng món trong đơn hàng
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    menu_item_id TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL CHECK (unit_price > 0),
    note TEXT DEFAULT '',
    kitchen_status TEXT NOT NULL DEFAULT 'Chờ chế biến'
        CHECK (kitchen_status IN ('Chờ chế biến', 'Đang chế biến', 'Hoàn thành')),
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(item_id)
);

-- 6. Bảng hóa đơn thanh toán
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL UNIQUE,
    cashier_id INTEGER,
    subtotal REAL NOT NULL CHECK (subtotal >= 0),
    discount REAL NOT NULL DEFAULT 0 CHECK (discount >= 0),
    surcharge REAL NOT NULL DEFAULT 0 CHECK (surcharge >= 0),
    total_amount REAL NOT NULL CHECK (total_amount >= 0),
    amount_received REAL NOT NULL CHECK (amount_received >= 0),
    change_amount REAL NOT NULL DEFAULT 0 CHECK (change_amount >= 0),
    payment_method TEXT NOT NULL DEFAULT 'Tiền mặt' CHECK (payment_method IN ('Tiền mặt', 'Chuyển khoản')),
    paid_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (cashier_id) REFERENCES users(id)
);

-- Dữ liệu mẫu ban đầu (idempotent) phục vụ kiểm thử khung Sprint 0
INSERT OR IGNORE INTO dining_tables (id, table_number, capacity, status) VALUES
    (1, 1, 4, 'Trống'),
    (2, 2, 4, 'Trống'),
    (3, 3, 4, 'Trống'),
    (4, 4, 4, 'Trống'),
    (5, 5, 6, 'Trống'),
    (6, 6, 6, 'Trống');

INSERT OR IGNORE INTO menu_items (item_id, name, price, category, image_url, available) VALUES
    ('M01', 'Cơm chiên Dương Châu', 35000, 'Cơm chiên', '', 1),
    ('M02', 'Cơm chiên hải sản', 45000, 'Cơm chiên', '', 1),
    ('M03', 'Cơm chiên bò trứng', 48000, 'Cơm chiên', '', 1),
    ('D01', 'Trà đá', 5000, 'Đồ uống', '', 1);
