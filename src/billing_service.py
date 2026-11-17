
"""Module xử lý thanh toán và xuất hóa đơn cho Quán Cơm Chiên (Issue #4)."""

from dataclasses import dataclass
from typing import List


@dataclass
class BillItem:
    """Đại diện cho một món ăn trong hóa đơn."""

    name: str
    quantity: int
    price: int


@dataclass
class PaymentReceipt:
    """Lưu kết quả thanh toán."""

    total: int
    amount_received: int
    change: int


class BillingService:
    """Xử lý tính tiền, thanh toán và tạo hóa đơn."""

    def calculate_total(self, items: List[BillItem]) -> int:
        """Tính tổng tiền của đơn hàng."""

        if not items:
            raise ValueError("Đơn hàng không được để trống.")

        total = 0

        for item in items:
            if item.quantity <= 0:
                raise ValueError("Số lượng món phải lớn hơn 0.")

            if item.price < 0:
                raise ValueError("Giá món ăn không được âm.")

            total += item.quantity * item.price

        return total

    def process_payment(
        self,
        items: List[BillItem],
        amount_received: int
    ) -> PaymentReceipt:
        """Thực hiện thanh toán và tính tiền thừa."""

        total = self.calculate_total(items)

        if amount_received < 0:
            raise ValueError("Số tiền khách đưa không hợp lệ.")

        if amount_received < total:
            raise ValueError("Số tiền khách đưa không đủ.")

        change = amount_received - total

        return PaymentReceipt(
            total=total,
            amount_received=amount_received,
            change=change
        )

    def generate_invoice(self, items: List[BillItem]) -> str:
        """Tạo nội dung hóa đơn dạng văn bản."""

        total = self.calculate_total(items)

        invoice = [
            "===== HOA DON QUAN COM CHIEN ====="
        ]

        for item in items:
            subtotal = item.quantity * item.price

            invoice.append(
                f"{item.name} | {item.quantity} x "
                f"{item.price:,} = {subtotal:,} VND"
            )

        invoice.append("-------------------------------")
        invoice.append(f"TONG TIEN: {total:,} VND")
        invoice.append("================================")

        return "\n".join(invoice)

