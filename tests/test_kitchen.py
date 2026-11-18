import unittest

from src.kitchen_service import KitchenService, PENDING, COOKING, DONE


class TestKitchenService(unittest.TestCase):

    def test_new_ticket_is_pending(self):
        # Arrange
        kitchen = KitchenService()
        # Act
        ticket_id = kitchen.add_ticket(table=3, dish="Cơm chiên dương châu")
        # Assert
        self.assertEqual(kitchen.tickets[ticket_id]["status"], PENDING)

    def test_update_status_valid_flow(self):
        # Arrange
        kitchen = KitchenService()
        ticket_id = kitchen.add_ticket(2, "Cơm chiên trứng")
        # Act
        kitchen.update_status(ticket_id, COOKING)
        result = kitchen.update_status(ticket_id, DONE)
        # Assert
        self.assertEqual(result, DONE)

    def test_update_status_skip_step_raises_error(self):
        # Arrange
        kitchen = KitchenService()
        ticket_id = kitchen.add_ticket(1, "Cơm chiên hải sản")
        # Act + Assert
        with self.assertRaises(ValueError):
            kitchen.update_status(ticket_id, DONE)  # nhảy cóc từ Chờ sang Hoàn thành

    def test_get_by_status_returns_only_matching(self):
        # Arrange
        kitchen = KitchenService()
        a = kitchen.add_ticket(1, "Cơm chiên bò")
        kitchen.add_ticket(2, "Cơm chiên gà")
        kitchen.update_status(a, COOKING)
        # Act
        cooking = kitchen.get_by_status(COOKING)
        # Assert
        self.assertEqual(len(cooking), 1)
        self.assertEqual(cooking[0]["dish"], "Cơm chiên bò")


if __name__ == "__main__":
    unittest.main()