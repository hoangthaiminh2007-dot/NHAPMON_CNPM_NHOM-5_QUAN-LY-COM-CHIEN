"""Module đặt món tại bàn cho Quán Cơm Chiên (Issue #2)."""

from dataclasses import dataclass, field

TABLE_AVAILABLE = "Trống"
TABLE_OCCUPIED = "Đang phục vụ"
ORDER_DRAFT = "Nháp"
ORDER_PENDING = "Chờ chế biến"


@dataclass
class DiningTable:
    """Đại diện cho một bàn ăn trong quán."""

    table_number: int
    capacity: int = 4
    status: str = TABLE_AVAILABLE


@dataclass
class OrderItem:
    """Đại diện cho một món ăn đã chọn trong đơn đặt món tại bàn."""

    item_id: str
    name: str
    price: float
    quantity: int
    note: str = ""

    @property
    def subtotal(self) -> float:
        """Thành tiền của dòng món ăn."""
        return self.price * self.quantity


@dataclass
class TableOrder:
    """Đại diện cho đơn đặt món tại một bàn."""

    order_id: str
    table_number: int
    items: list[OrderItem] = field(default_factory=list)
    status: str = ORDER_DRAFT

    @property
    def total_amount(self) -> float:
        """Tổng tiền tạm tính của toàn bộ đơn hàng."""
        return sum(item.subtotal for item in self.items)


class OrderService:
    """Quản lý chọn bàn, thêm/xóa món, tính tạm tính và gửi đơn xuống bếp."""

    def __init__(self, table_count: int = 10) -> None:
        if isinstance(table_count, bool) or not isinstance(table_count, int) or table_count <= 0:
            raise ValueError("Số lượng bàn phải là số nguyên lớn hơn 0.")
        self._tables: dict[int, DiningTable] = {
            num: DiningTable(table_number=num) for num in range(1, table_count + 1)
        }
        self._orders: dict[str, TableOrder] = {}
        self._next_seq: int = 1

    @staticmethod
    def _validate_text(value: str, field_name: str) -> str:
        cleaned = value.strip() if isinstance(value, str) else ""
        if not cleaned:
            raise ValueError(f"{field_name} không được để trống.")
        return cleaned

    def _require_draft_order(self, order_id: str) -> TableOrder:
        order = self.get_order(order_id)
        if order.status != ORDER_DRAFT:
            raise ValueError("Đơn hàng đã được gửi xuống bếp, không thể chỉnh sửa.")
        return order

    def list_tables(self, only_available: bool = False) -> list[DiningTable]:
        """Trả về danh sách các bàn trong quán (hỗ trợ lọc bàn trống)."""
        tables = list(self._tables.values())
        if only_available:
            return [t for t in tables if t.status == TABLE_AVAILABLE]
        return tables

    def get_table(self, table_number: int) -> DiningTable:
        """Lấy thông tin một bàn theo số bàn."""
        if isinstance(table_number, bool) or not isinstance(table_number, int) or table_number <= 0:
            raise ValueError("Số bàn phải lớn hơn 0.")
        if table_number not in self._tables:
            raise KeyError(f"Không tìm thấy bàn số {table_number}.")
        return self._tables[table_number]

    def create_order(self, table_number: int) -> TableOrder:
        """Tạo đơn đặt món mới cho một bàn đang trống và đánh dấu bàn đang phục vụ."""
        table = self.get_table(table_number)
        if table.status != TABLE_AVAILABLE:
            raise ValueError(f"Bàn số {table_number} hiện không trống.")

        order_id = f"ORD-{self._next_seq:03d}"
        self._next_seq += 1
        order = TableOrder(order_id=order_id, table_number=table_number)
        self._orders[order_id] = order
        table.status = TABLE_OCCUPIED
        return order

    def get_order(self, order_id: str) -> TableOrder:
        """Lấy thông tin đơn hàng theo mã đơn."""
        if order_id not in self._orders:
            raise KeyError(f"Không tìm thấy đơn hàng '{order_id}'.")
        return self._orders[order_id]

    def add_item(
        self,
        order_id: str,
        item_id: str,
        name: str,
        price: float,
        quantity: int,
        note: str = "",
        available: bool = True,
    ) -> OrderItem:
        """Thêm món ăn vào đơn hàng nháp và gộp số lượng nếu trùng món và ghi chú."""
        order = self._require_draft_order(order_id)
        if not available:
            raise ValueError(f"Món '{name}' hiện đã hết, không thể đặt.")

        clean_id = self._validate_text(item_id, "Mã món")
        clean_name = self._validate_text(name, "Tên món")
        if isinstance(price, bool) or not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Đơn giá món phải lớn hơn 0.")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Số lượng món phải lớn hơn 0.")

        clean_note = note.strip() if isinstance(note, str) else ""
        for existing in order.items:
            if existing.item_id == clean_id and existing.note == clean_note:
                existing.quantity += quantity
                return existing

        item = OrderItem(
            item_id=clean_id,
            name=clean_name,
            price=float(price),
            quantity=quantity,
            note=clean_note,
        )
        order.items.append(item)
        return item

    def remove_item(self, order_id: str, item_id: str) -> OrderItem:
        """Xóa một món khỏi đơn hàng nháp theo mã món."""
        order = self._require_draft_order(order_id)
        for index, item in enumerate(order.items):
            if item.item_id == item_id:
                return order.items.pop(index)
        raise KeyError(f"Không tìm thấy món '{item_id}' trong đơn '{order_id}'.")

    def calculate_total(self, order_id: str) -> float:
        """Tính tổng tiền tạm tính hiện tại của đơn hàng."""
        order = self.get_order(order_id)
        return order.total_amount

    def submit_order(self, order_id: str) -> TableOrder:
        """Xác nhận gửi đơn hàng xuống bếp và chuyển trạng thái sang Chờ chế biến."""
        order = self._require_draft_order(order_id)
        if not order.items:
            raise ValueError("Không thể gửi đơn hàng khi chưa có món nào.")
        order.status = ORDER_PENDING
        return order
