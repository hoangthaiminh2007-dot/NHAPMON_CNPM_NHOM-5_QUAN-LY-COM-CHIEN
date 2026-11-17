"""Unit Test cho module Quản lý Thực đơn (Issue #1) áp dụng cấu trúc AAA."""

import unittest

from src.menu_service import MenuService


class TestMenuService(unittest.TestCase):
    """Kiểm thử các nghiệp vụ thêm, sửa, xóa và lọc món ăn trong MenuService."""

    def test_add_item_success(self) -> None:
        # 1. Arrange
        service = MenuService()

        # 2. Act
        created = service.add_item("M01", "Cơm chiên Dương Châu", 35000, "Cơm chiên")

        # 3. Assert
        self.assertEqual(created.item_id, "M01")
        self.assertEqual(created.name, "Cơm chiên Dương Châu")
        self.assertEqual(created.price, 35000.0)
        self.assertTrue(created.available)
        self.assertEqual(len(service.list_items()), 1)

    def test_add_item_invalid_price_raises_error(self) -> None:
        # 1. Arrange
        service = MenuService()

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            service.add_item("M02", "Cơm chiên trứng", 0, "Cơm chiên")

    def test_add_duplicate_item_raises_error(self) -> None:
        # 1. Arrange
        service = MenuService()
        service.add_item("M01", "Cơm chiên Dương Châu", 35000, "Cơm chiên")

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            service.add_item("M03", "cơm chiên dương châu", 40000, "Cơm chiên")

    def test_update_and_filter_available_items(self) -> None:
        # 1. Arrange
        service = MenuService()
        service.add_item("M01", "Cơm chiên hải sản", 45000, "Cơm chiên")
        service.add_item("D01", "Trà đá", 5000, "Đồ uống")

        # 2. Act
        service.update_item("M01", price=48000)
        service.set_availability("D01", False)
        available_items = service.list_items(only_available=True)

        # 3. Assert
        self.assertEqual(service.get_item("M01").price, 48000.0)
        self.assertEqual(len(available_items), 1)
        self.assertEqual(available_items[0].item_id, "M01")

    def test_delete_item_removes_from_menu(self) -> None:
        # 1. Arrange
        service = MenuService()
        service.add_item("M01", "Cơm chiên bò", 45000, "Cơm chiên")

        # 2. Act
        removed = service.delete_item("M01")

        # 3. Assert
        self.assertEqual(removed.item_id, "M01")
        self.assertEqual(service.list_items(), [])


if __name__ == "__main__":
    unittest.main()
