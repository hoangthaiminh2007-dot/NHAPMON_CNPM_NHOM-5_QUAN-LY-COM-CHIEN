"""Module quản lý thực đơn món ăn cho Quán Cơm Chiên (Issue #1)."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MenuItem:
    """Đại diện cho một món ăn hoặc đồ uống trong thực đơn."""

    item_id: str
    name: str
    price: float
    category: str
    available: bool = True


class MenuService:
    """Quản lý thêm, sửa, xóa, tìm kiếm và trạng thái món ăn trong thực đơn."""

    def __init__(self) -> None:
        self._items: dict[str, MenuItem] = {}

    @staticmethod
    def _validate_text(value: str, field_name: str) -> str:
        cleaned = value.strip() if isinstance(value, str) else ""
        if not cleaned:
            raise ValueError(f"{field_name} không được để trống")
        return cleaned

    @staticmethod
    def _validate_price(price: float) -> float:
        if price <= 0:
            raise ValueError("Giá món phải lớn hơn 0")
        return float(price)

    def _ensure_unique_name(self, name: str, exclude_id: Optional[str] = None) -> None:
        normalized = name.casefold()
        for item in self._items.values():
            if item.item_id != exclude_id and item.name.casefold() == normalized:
                raise ValueError(f"Món '{name}' đã tồn tại trong thực đơn")

    def add_item(
        self,
        item_id: str,
        name: str,
        price: float,
        category: str,
        available: bool = True,
    ) -> MenuItem:
        """Thêm món mới vào thực đơn sau khi kiểm tra hợp lệ và không trùng lặp."""
        clean_id = self._validate_text(item_id, "Mã món")
        clean_name = self._validate_text(name, "Tên món")
        clean_category = self._validate_text(category, "Danh mục")
        valid_price = self._validate_price(price)

        if clean_id in self._items:
            raise ValueError(f"Mã món '{clean_id}' đã tồn tại")
        self._ensure_unique_name(clean_name)

        item = MenuItem(
            item_id=clean_id,
            name=clean_name,
            price=valid_price,
            category=clean_category,
            available=available,
        )
        self._items[clean_id] = item
        return item

    def get_item(self, item_id: str) -> MenuItem:
        """Lấy thông tin chi tiết của một món theo mã món."""
        if item_id not in self._items:
            raise KeyError(f"Không tìm thấy món có mã '{item_id}'")
        return self._items[item_id]

    def update_item(
        self,
        item_id: str,
        name: Optional[str] = None,
        price: Optional[float] = None,
        category: Optional[str] = None,
        available: Optional[bool] = None,
    ) -> MenuItem:
        """Cập nhật thông tin món ăn đang có trong thực đơn."""
        item = self.get_item(item_id)

        if name is not None:
            clean_name = self._validate_text(name, "Tên món")
            self._ensure_unique_name(clean_name, exclude_id=item_id)
            item.name = clean_name
        if price is not None:
            item.price = self._validate_price(price)
        if category is not None:
            item.category = self._validate_text(category, "Danh mục")
        if available is not None:
            item.available = available

        return item

    def set_availability(self, item_id: str, available: bool) -> MenuItem:
        """Cập nhật trạng thái còn món / hết món."""
        return self.update_item(item_id, available=available)

    def delete_item(self, item_id: str) -> MenuItem:
        """Xóa món khỏi thực đơn theo mã món."""
        item = self.get_item(item_id)
        del self._items[item_id]
        return item

    def list_items(
        self, category: Optional[str] = None, only_available: bool = False
    ) -> list[MenuItem]:
        """Trả về danh sách món ăn, hỗ trợ lọc theo danh mục hoặc trạng thái còn món."""
        result = list(self._items.values())
        if category is not None:
            target = category.strip().casefold()
            result = [item for item in result if item.category.casefold() == target]
        if only_available:
            result = [item for item in result if item.available]
        return result
