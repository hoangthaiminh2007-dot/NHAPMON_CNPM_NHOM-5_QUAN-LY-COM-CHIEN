"""Unit Test cho module Đặt món tại bàn (Issue #2) áp dụng cấu trúc AAA."""

import unittest

from src.order_service import (
    ORDER_DRAFT,
    ORDER_PENDING,
    TABLE_AVAILABLE,
    TABLE_OCCUPIED,
    OrderService,
)


class TestOrderService(unittest.TestCase):
    """Kiểm thử các nghiệp vụ chọn bàn, thêm món, tính tạm tính và gửi đơn."""

    def test_list_tables_returns_all_and_filters_available(self) -> None:
        # 1. Arrange
        service = OrderService(table_count=4)
        service.create_order(table_number=2)

        # 2. Act
        all_tables = service.list_tables()
        available_tables = service.list_tables(only_available=True)

        # 3. Assert
        self.assertEqual(len(all_tables), 4)
        self.assertEqual(len(available_tables), 3)
        self.assertTrue(all(t.status == TABLE_AVAILABLE for t in available_tables))
        self.assertEqual(service.get_table(2).status, TABLE_OCCUPIED)

    def test_create_order_add_items_and_calculate_total(self) -> None:
        # 1. Arrange
        service = OrderService(table_count=5)

        # 2. Act
        order = service.create_order(table_number=1)
        service.add_item(order.order_id, "M01", "Cơm chiên Dương Châu", 35000, 2, note="Ít cay")
        service.add_item(order.order_id, "M01", "Cơm chiên Dương Châu", 35000, 1, note="Ít cay")
        service.add_item(order.order_id, "M02", "Cơm chiên hải sản", 45000, 1)
        total = service.calculate_total(order.order_id)

        # 3. Assert
        self.assertEqual(order.order_id, "ORD-001")
        self.assertEqual(order.table_number, 1)
        self.assertEqual(order.status, ORDER_DRAFT)
        self.assertEqual(len(order.items), 2)
        self.assertEqual(order.items[0].quantity, 3)
        self.assertEqual(total, 150000.0)

    def test_add_unavailable_or_invalid_item_raises_error(self) -> None:
        # 1. Arrange
        service = OrderService(table_count=3)
        order = service.create_order(table_number=1)

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            service.add_item(
                order.order_id,
                "M03",
                "Cơm chiên cua",
                55000,
                1,
                available=False,
            )
        with self.assertRaises(ValueError):
            service.add_item(order.order_id, "M01", "Cơm chiên trứng", 30000, 0)

    def test_submit_order_success_changes_status_to_pending(self) -> None:
        # 1. Arrange
        service = OrderService(table_count=3)
        order = service.create_order(table_number=3)
        service.add_item(order.order_id, "M01", "Cơm chiên bò", 45000, 2, note="Thêm trứng")

        # 2. Act
        submitted = service.submit_order(order.order_id)

        # 3. Assert
        self.assertEqual(submitted.status, ORDER_PENDING)
        self.assertEqual(service.calculate_total(submitted.order_id), 90000.0)

    def test_submit_empty_order_raises_error(self) -> None:
        # 1. Arrange
        service = OrderService(table_count=3)
        order = service.create_order(table_number=1)

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            service.submit_order(order.order_id)

    def test_create_order_on_occupied_or_invalid_table_raises_error(self) -> None:
        # 1. Arrange
        service = OrderService(table_count=3)
        service.create_order(table_number=2)

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            service.create_order(table_number=2)
        with self.assertRaises(ValueError):
            service.create_order(table_number=0)
        with self.assertRaises(KeyError):
            service.create_order(table_number=99)


if __name__ == "__main__":
    unittest.main()
