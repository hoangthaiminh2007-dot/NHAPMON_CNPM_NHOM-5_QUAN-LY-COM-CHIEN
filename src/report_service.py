"""Module báo cáo và thống kê doanh thu cho Quán Cơm Chiên (Issue #5)."""

from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Callable, Mapping, Optional, Sequence, Union

DateInput = Union[str, date, datetime]


@dataclass
class RevenueSummary:
    """Lưu kết quả thống kê doanh thu theo từng kỳ (ngày hoặc tháng)."""

    period: str
    order_count: int
    item_count: int
    total_revenue: float


class ReportService:
    """Xử lý tính tổng doanh thu, lọc đơn theo ngày và xuất báo cáo doanh thu."""

    @staticmethod
    def _parse_date(value: Any, field_name: str = "Ngày") -> date:
        if isinstance(value, datetime):
            return value.date()
        if isinstance(value, date):
            return value
        if isinstance(value, str):
            cleaned = value.strip()
            if not cleaned:
                raise ValueError(f"{field_name} không được để trống.")
            if len(cleaned) == 10:
                try:
                    return datetime.strptime(cleaned, "%Y-%m-%d").date()
                except ValueError as exc:
                    raise ValueError(
                        f"{field_name} không đúng định dạng YYYY-MM-DD: '{value}'."
                    ) from exc
            try:
                return datetime.fromisoformat(cleaned).date()
            except ValueError as exc:
                raise ValueError(
                    f"{field_name} không đúng định dạng YYYY-MM-DD: '{value}'."
                ) from exc
        raise ValueError(f"{field_name} có kiểu dữ liệu không hợp lệ.")

    @classmethod
    def _validate_date_range(
        cls, start_date: Any, end_date: Any
    ) -> tuple[date, date]:
        if start_date is None or end_date is None:
            raise ValueError("Ngày bắt đầu và ngày kết thúc không được để trống.")
        parsed_start = cls._parse_date(start_date, "Ngày bắt đầu")
        parsed_end = cls._parse_date(end_date, "Ngày kết thúc")
        if parsed_start > parsed_end:
            raise ValueError("Ngày bắt đầu không được lớn hơn ngày kết thúc!")
        return parsed_start, parsed_end

    @staticmethod
    def _extract_valid_amount(order: Mapping[str, Any]) -> float:
        amount = order.get("amount", 0.0)
        if amount is None or isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError("Số tiền đơn hàng không hợp lệ.")
        if amount < 0:
            raise ValueError("Số tiền đơn hàng không được âm.")
        return float(amount)

    @staticmethod
    def _extract_item_count(order: Mapping[str, Any]) -> int:
        if "item_count" in order and order["item_count"] is not None:
            count = order["item_count"]
            if isinstance(count, bool) or not isinstance(count, int) or count < 0:
                raise ValueError("Số lượng món không hợp lệ.")
            return count

        items = order.get("items")
        if isinstance(items, (list, tuple)):
            total_items = 0
            for item in items:
                qty = item.get("quantity", 1) if isinstance(item, Mapping) else getattr(item, "quantity", 1)
                if isinstance(qty, bool) or not isinstance(qty, int) or qty < 0:
                    raise ValueError("Số lượng món không hợp lệ.")
                total_items += qty
            return total_items

        return 0

    @staticmethod
    def _format_vnd(amount: float) -> str:
        if amount.is_integer():
            return f"{amount:,.0f}"
        return f"{amount:,.2f}"

    def calculate_total_revenue(
        self, orders: Optional[Sequence[Mapping[str, Any]]]
    ) -> float:
        """Tính tổng doanh thu từ các đơn hàng có trạng thái COMPLETED."""
        if not orders:
            return 0.0

        total = 0.0
        for order in orders:
            if order.get("status") == "COMPLETED":
                total += self._extract_valid_amount(order)
        return total

    def filter_orders_by_date(
        self,
        orders: Optional[Sequence[Mapping[str, Any]]],
        start_date: DateInput,
        end_date: DateInput,
    ) -> list[Mapping[str, Any]]:
        """Lọc danh sách đơn hàng nằm trong khoảng [start_date, end_date]."""
        parsed_start, parsed_end = self._validate_date_range(start_date, end_date)
        if not orders:
            return []

        result: list[Mapping[str, Any]] = []
        for order in orders:
            raw_date = order.get("created_date")
            if raw_date is None or (isinstance(raw_date, str) and not raw_date.strip()):
                continue
            order_date = self._parse_date(raw_date, "Ngày tạo đơn")
            if parsed_start <= order_date <= parsed_end:
                result.append(order)
        return result

    def _summarize_by_period(
        self,
        orders: Optional[Sequence[Mapping[str, Any]]],
        period_formatter: Callable[[date], str],
        start_date: Optional[DateInput] = None,
        end_date: Optional[DateInput] = None,
    ) -> list[RevenueSummary]:
        if (start_date is None) != (end_date is None):
            raise ValueError("Cần cung cấp đầy đủ cả ngày bắt đầu và ngày kết thúc.")

        target_orders: Sequence[Mapping[str, Any]]
        if start_date is not None and end_date is not None:
            target_orders = self.filter_orders_by_date(orders, start_date, end_date)
        else:
            target_orders = orders or []

        buckets: dict[str, dict[str, Any]] = {}
        for order in target_orders:
            if order.get("status") != "COMPLETED":
                continue

            raw_date = order.get("created_date")
            if raw_date is None or (isinstance(raw_date, str) and not raw_date.strip()):
                raise ValueError("Đơn hàng đã thanh toán thiếu ngày tạo.")

            order_date = self._parse_date(raw_date, "Ngày tạo đơn")
            period_key = period_formatter(order_date)
            amount = self._extract_valid_amount(order)
            item_count = self._extract_item_count(order)

            if period_key not in buckets:
                buckets[period_key] = {
                    "order_count": 0,
                    "item_count": 0,
                    "total_revenue": 0.0,
                }
            buckets[period_key]["order_count"] += 1
            buckets[period_key]["item_count"] += item_count
            buckets[period_key]["total_revenue"] += amount

        return [
            RevenueSummary(
                period=period,
                order_count=buckets[period]["order_count"],
                item_count=buckets[period]["item_count"],
                total_revenue=buckets[period]["total_revenue"],
            )
            for period in sorted(buckets)
        ]

    def summarize_daily_revenue(
        self,
        orders: Optional[Sequence[Mapping[str, Any]]],
        start_date: Optional[DateInput] = None,
        end_date: Optional[DateInput] = None,
    ) -> list[RevenueSummary]:
        """Tổng hợp số đơn, số lượng món và doanh thu các đơn COMPLETED theo từng ngày."""
        return self._summarize_by_period(
            orders,
            lambda d: d.strftime("%Y-%m-%d"),
            start_date=start_date,
            end_date=end_date,
        )

    def summarize_monthly_revenue(
        self,
        orders: Optional[Sequence[Mapping[str, Any]]],
        start_date: Optional[DateInput] = None,
        end_date: Optional[DateInput] = None,
    ) -> list[RevenueSummary]:
        """Tổng hợp số đơn, số lượng món và doanh thu các đơn COMPLETED theo từng tháng."""
        return self._summarize_by_period(
            orders,
            lambda d: d.strftime("%Y-%m"),
            start_date=start_date,
            end_date=end_date,
        )

    def generate_revenue_report(
        self,
        orders: Optional[Sequence[Mapping[str, Any]]],
        start_date: Optional[DateInput] = None,
        end_date: Optional[DateInput] = None,
    ) -> str:
        """Tạo báo cáo doanh thu dạng văn bản trực quan theo ngày."""
        summaries = self.summarize_daily_revenue(
            orders, start_date=start_date, end_date=end_date
        )

        lines = ["===== BAO CAO DOANH THU QUAN COM CHIEN ====="]
        if start_date is not None and end_date is not None:
            parsed_start, parsed_end = self._validate_date_range(start_date, end_date)
            lines.append(
                f"Ky bao cao: {parsed_start.isoformat()} -> {parsed_end.isoformat()}"
            )

        if not summaries:
            lines.append("Khong co hoa don da thanh toan.")
        else:
            for row in summaries:
                lines.append(
                    f"{row.period} | Don: {row.order_count} | "
                    f"Mon: {row.item_count} | "
                    f"Doanh thu: {self._format_vnd(row.total_revenue)} VND"
                )

        total_orders = sum(row.order_count for row in summaries)
        total_items = sum(row.item_count for row in summaries)
        grand_total = sum(row.total_revenue for row in summaries)

        lines.append("-----------------------------------------")
        lines.append(f"TONG SO DON: {total_orders}")
        lines.append(f"TONG SO MON: {total_items}")
        lines.append(f"TONG DOANH THU: {self._format_vnd(grand_total)} VND")
        lines.append("=========================================")
        return "\n".join(lines)
