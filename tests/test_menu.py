"""Unit Test cho module Quản lý Thực đơn (Issue #1) áp dụng cấu trúc AAA."""

import unittest

from src.menu_service import MenuItem, MenuService


class TestMenuService(unittest.TestCase):
    """Bộ kiểm thử đơn vị cho MenuService theo cấu trúc AAA."""

    def setUp(self) -> None:
        """Khởi tạo service và dữ liệu mẫu trước mỗi ca kiểm thử."""
        self.service = MenuService()

    def test_add_item_success(self) -> None:
        """TC01: Thêm món ăn hợp lệ thành công (AAA Pattern)."""
        # Arrange (Chuẩn bị)
        item = MenuItem(
            item_id="M01",
            name="Cơm chiên Dương Châu",
            price=35000,
            category="Cơm chiên",
            available=True,
        )

        # Act (Thực hiện)
        result = self.service.add_item(item)

        # Assert (Kiểm chứng)
        self.assertTrue(result)
        self.assertEqual(self.service.count_items(), 1)
        self.assertEqual(self.service.get_item("M01"), item)

    def test_add_duplicate_item_id_fails(self) -> None:
        """TC02: Thêm món trùng ID phải thất bại và báo lỗi."""
        # Arrange
        item1 = MenuItem("M01", "Cơm chiên Dương Châu", 35000, "Cơm chiên")
        item2 = MenuItem("M01", "Cơm chiên hải sản", 40000, "Cơm chiên")
        self.service.add_item(item1)

        # Act & Assert
        with self.assertRaises(ValueError):
            self.service.add_item(item2)

    def test_update_item_price_and_availability(self) -> None:
        """TC03: Cập nhật giá và trạng thái còn món thành công."""
        # Arrange
        item = MenuItem("M02", "Cơm chiên cá mặn", 35000, "Cơm chiên", available=True)
        self.service.add_item(item)

        # Act
        update_result = self.service.update_item("M02", price=38000, available=False)
        updated_item = self.service.get_item("M02")

        # Assert
        self.assertTrue(update_result)
        self.assertIsNotNone(updated_item)
        assert updated_item is not None
        self.assertEqual(updated_item.price, 38000)
        self.assertFalse(updated_item.available)

    def test_delete_item_success(self) -> None:
        """TC04: Xóa món ăn khỏi thực đơn thành công."""
        # Arrange
        item = MenuItem("M03", "Trà đá", 5000, "Đồ uống")
        self.service.add_item(item)

        # Act
        deleted = self.service.delete_item("M03")

        # Assert
        self.assertTrue(deleted)
        self.assertIsNone(self.service.get_item("M03"))
        self.assertEqual(self.service.count_items(), 0)

    def test_search_by_category_and_name(self) -> None:
        """TC05: Tìm kiếm món ăn theo danh mục và từ khóa tên."""
        # Arrange
        self.service.add_item(MenuItem("M01", "Cơm chiên Dương Châu", 35000, "Cơm chiên"))
        self.service.add_item(MenuItem("M02", "Cơm chiên gà xối mỡ", 40000, "Cơm chiên"))
        self.service.add_item(MenuItem("D01", "Trà đào cam sả", 20000, "Đồ uống"))

        # Act
        com_items = self.service.list_by_category("Cơm chiên")
        search_ga = self.service.search_by_name("gà")

        # Assert
        self.assertEqual(len(com_items), 2)
        self.assertEqual(len(search_ga), 1)
        self.assertEqual(search_ga[0].item_id, "M02")


if __name__ == "__main__":
    unittest.main()
