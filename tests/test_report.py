"""Unit Test cho module Báo cáo và Thống kê doanh thu (Issue #5) theo cấu trúc AAA."""

import unittest
from datetime import date

from src.report_service import ReportService


class TestReportService(unittest.TestCase):
    """Kiểm thử tính doanh thu, lọc đơn theo ngày và tổng hợp báo cáo."""

    def setUp(self) -> None:
        self.report_service = ReportService()

    def test_calculate_total_revenue_completed_orders_only(self) -> None:
        # 1. Arrange
        mock_orders = [
            {"order_id": 1, "amount": 45000.0, "status": "COMPLETED"},
            {"order_id": 2, "amount": 55000.0, "status": "COMPLETED"},
            {"order_id": 3, "amount": 30000.0, "status": "CANCELLED"},
        ]
        expected_revenue = 100000.0

        # 2. Act
        actual_revenue = self.report_service.calculate_total_revenue(mock_orders)

        # 3. Assert
        self.assertEqual(actual_revenue, expected_revenue)

    def test_calculate_total_revenue_empty_and_invalid_amount(self) -> None:
        # 1. Arrange
        empty_orders = []
        negative_orders = [{"order_id": 1, "amount": -10000.0, "status": "COMPLETED"}]
        none_amount_orders = [{"order_id": 2, "amount": None, "status": "COMPLETED"}]

        # 2. Act
        empty_total = self.report_service.calculate_total_revenue(empty_orders)

        # 3. Assert
        self.assertEqual(empty_total, 0.0)
        with self.assertRaises(ValueError):
            self.report_service.calculate_total_revenue(negative_orders)
        with self.assertRaises(ValueError):
            self.report_service.calculate_total_revenue(none_amount_orders)

    def test_filter_orders_by_date_valid_range_includes_boundaries(self) -> None:
        # 1. Arrange
        mock_orders = [
            {"order_id": 1, "created_date": "2026-11-09"},
            {"order_id": 2, "created_date": "2026-11-10"},
            {"order_id": 3, "created_date": "2026-11-12T18:30:00"},
            {"order_id": 4, "created_date": date(2026, 11, 11)},
            {"order_id": 5, "created_date": None},
            {"order_id": 6, "created_date": "2026-11-13"},
        ]

        # 2. Act
        filtered = self.report_service.filter_orders_by_date(
            mock_orders, "2026-11-10", "2026-11-12"
        )

        # 3. Assert
        self.assertEqual([order["order_id"] for order in filtered], [2, 3, 4])

    def test_filter_orders_by_date_invalid_range_raises_error(self) -> None:
        # 1. Arrange
        mock_orders = [{"order_id": 1, "created_date": "2026-11-10"}]
        start_date = "2026-11-20"
        end_date = "2026-11-10"

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            self.report_service.filter_orders_by_date(mock_orders, start_date, end_date)

    def test_filter_orders_by_date_invalid_format_raises_error(self) -> None:
        # 1. Arrange
        mock_orders = [{"order_id": 1, "created_date": "2026-11-10"}]

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            self.report_service.filter_orders_by_date(
                mock_orders, "10/11/2026", "2026-11-12"
            )
        with self.assertRaises(ValueError):
            self.report_service.filter_orders_by_date(mock_orders, "", "2026-11-12")

    def test_summarize_daily_revenue_groups_completed_orders(self) -> None:
        # 1. Arrange
        mock_orders = [
            {
                "order_id": 1,
                "amount": 70000.0,
                "status": "COMPLETED",
                "created_date": "2026-11-11",
                "items": [{"name": "Cơm chiên Dương Châu", "quantity": 2}],
            },
            {
                "order_id": 2,
                "amount": 45000.0,
                "status": "COMPLETED",
                "created_date": "2026-11-10",
                "item_count": 1,
            },
            {
                "order_id": 3,
                "amount": 50000.0,
                "status": "CANCELLED",
                "created_date": "2026-11-10",
                "item_count": 2,
            },
            {
                "order_id": 4,
                "amount": 35000.0,
                "status": "COMPLETED",
                "created_date": "2026-11-10T19:15:00",
                "item_count": 1,
            },
        ]

        # 2. Act
        daily = self.report_service.summarize_daily_revenue(mock_orders)

        # 3. Assert
        self.assertEqual(len(daily), 2)
        self.assertEqual(daily[0].period, "2026-11-10")
        self.assertEqual(daily[0].order_count, 2)
        self.assertEqual(daily[0].item_count, 2)
        self.assertEqual(daily[0].total_revenue, 80000.0)
        self.assertEqual(daily[1].period, "2026-11-11")
        self.assertEqual(daily[1].order_count, 1)
        self.assertEqual(daily[1].item_count, 2)
        self.assertEqual(daily[1].total_revenue, 70000.0)

    def test_summarize_monthly_revenue_groups_by_month(self) -> None:
        # 1. Arrange
        mock_orders = [
            {
                "order_id": 1,
                "amount": 100000.0,
                "status": "COMPLETED",
                "created_date": "2026-10-28",
                "item_count": 3,
            },
            {
                "order_id": 2,
                "amount": 55000.0,
                "status": "COMPLETED",
                "created_date": "2026-11-05",
                "item_count": 1,
            },
            {
                "order_id": 3,
                "amount": 45000.0,
                "status": "COMPLETED",
                "created_date": "2026-11-12",
                "item_count": 1,
            },
        ]

        # 2. Act
        monthly = self.report_service.summarize_monthly_revenue(mock_orders)

        # 3. Assert
        self.assertEqual(len(monthly), 2)
        self.assertEqual(monthly[0].period, "2026-10")
        self.assertEqual(monthly[0].total_revenue, 100000.0)
        self.assertEqual(monthly[1].period, "2026-11")
        self.assertEqual(monthly[1].order_count, 2)
        self.assertEqual(monthly[1].item_count, 2)
        self.assertEqual(monthly[1].total_revenue, 100000.0)

    def test_generate_revenue_report_formats_summary_clearly(self) -> None:
        # 1. Arrange
        mock_orders = [
            {
                "order_id": 1,
                "amount": 45000.0,
                "status": "COMPLETED",
                "created_date": "2026-11-10",
                "item_count": 1,
            },
            {
                "order_id": 2,
                "amount": 55000.0,
                "status": "COMPLETED",
                "created_date": "2026-11-11",
                "item_count": 2,
            },
        ]

        # 2. Act
        report = self.report_service.generate_revenue_report(
            mock_orders, start_date="2026-11-10", end_date="2026-11-11"
        )

        # 3. Assert
        self.assertIn("Ky bao cao: 2026-11-10 -> 2026-11-11", report)
        self.assertIn("2026-11-10 | Don: 1 | Mon: 1 | Doanh thu: 45,000 VND", report)
        self.assertIn("2026-11-11 | Don: 1 | Mon: 2 | Doanh thu: 55,000 VND", report)
        self.assertIn("TONG SO DON: 2", report)
        self.assertIn("TONG SO MON: 3", report)
        self.assertIn("TONG DOANH THU: 100,000 VND", report)


if __name__ == "__main__":
    unittest.main()
