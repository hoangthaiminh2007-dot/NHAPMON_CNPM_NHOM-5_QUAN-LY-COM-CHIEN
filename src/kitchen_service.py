"""Kitchen Display - Theo dõi trạng thái chế biến món tại bếp (Issue #3)."""

PENDING = "Chờ chế biến"
COOKING = "Đang chế biến"
DONE = "Hoàn thành"

# Thứ tự hợp lệ: chỉ được chuyển sang trạng thái kế tiếp
NEXT_STATUS = {
    PENDING: COOKING,
    COOKING: DONE,
}


class KitchenService:
    def __init__(self):
        # {ticket_id: {"table": int, "dish": str, "status": str}}
        self.tickets = {}
        self._next_id = 1

    def add_ticket(self, table, dish):
        """Nhận món mới từ bàn, trạng thái ban đầu là Chờ chế biến."""
        if table <= 0:
            raise ValueError("Số bàn phải lớn hơn 0")
        if not dish or not dish.strip():
            raise ValueError("Tên món không được để trống")
        ticket_id = self._next_id
        self._next_id += 1
        self.tickets[ticket_id] = {"table": table, "dish": dish, "status": PENDING}
        return ticket_id

    def update_status(self, ticket_id, new_status):
        """Cập nhật trạng thái món, chỉ cho phép chuyển sang bước kế tiếp."""
        if ticket_id not in self.tickets:
            raise KeyError("Không tìm thấy phiếu món")
        current = self.tickets[ticket_id]["status"]
        if NEXT_STATUS.get(current) != new_status:
            raise ValueError(f"Không thể chuyển từ '{current}' sang '{new_status}'")
        self.tickets[ticket_id]["status"] = new_status
        return new_status

    def get_by_status(self, status):
        """Lấy danh sách món theo trạng thái (để hiển thị trên màn hình bếp)."""
        return [t for t in self.tickets.values() if t["status"] == status]