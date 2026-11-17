
import unittest

from src.billing_service import BillingService, BillItem


class TestBillingService(unittest.TestCase):
    """Kiểm thử các nghiệp vụ thanh toán và hóa đơn."""

    def setUp(self):
        self.service = BillingService()

        self.items = [
            BillItem("Com chien Duong Chau", 2, 35000),
            BillItem("Com chien hai san", 1, 45000)
        ]

    def test_calculate_total(self):
        # 1. Arrange
        expected = 115000

        # 2. Act
        actual = self.service.calculate_total(self.items)

        # 3. Assert
        self.assertEqual(actual, expected)

    def test_process_payment_success(self):
        # 1. Arrange
        amount_received = 150000
        expected_total = 115000
        expected_change = 35000

        # 2. Act
        result = self.service.process_payment(
            self.items, amount_received
        )

        # 3. Assert
        self.assertEqual(result.total, expected_total)
        self.assertEqual(result.amount_received, 150000)
        self.assertEqual(result.change, expected_change)

    def test_process_payment_insufficient(self):
        # 1. Arrange
        amount_received = 100000

        # 2. Act & Assert
        with self.assertRaises(ValueError):
            self.service.process_payment(
                self.items, amount_received
            )

    def test_generate_invoice(self):
        # 1. Arrange
        expected_text = "TONG TIEN: 115,000 VND"

        # 2. Act
        invoice = self.service.generate_invoice(self.items)

        # 3. Assert
        self.assertIn(expected_text, invoice)


if __name__ == "__main__":
    unittest.main()

