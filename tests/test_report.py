import unittest
from src.report_service import ReportService

class TestReportService(unittest.TestCase):

    def setUp(self):
        self.report_service = ReportService()

    def test_calculate_total_revenue_completed_orders_only(self):
        mock_orders = [
            {'order_id': 1, 'amount': 45000.0, 'status': 'COMPLETED'},
            {'order_id': 2, 'amount': 55000.0, 'status': 'COMPLETED'},
            {'order_id': 3, 'amount': 30000.0, 'status': 'CANCELLED'}
        ]
        expected_revenue = 100000.0
        actual_revenue = self.report_service.calculate_total_revenue(mock_orders)
        self.assertEqual(actual_revenue, expected_revenue)

    def test_filter_orders_by_date_invalid_range_raises_error(self):
        mock_orders = [{'order_id': 1, 'created_date': '2026-11-10'}]
        start_date = '2026-11-20'
        end_date = '2026-11-10'
        with self.assertRaises(ValueError):
            self.report_service.filter_orders_by_date(mock_orders, start_date, end_date)

if __name__ == '__main__':
    unittest.main()