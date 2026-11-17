class ReportService:
    def __init__(self):
        pass      
   
    def calculate_total_revenue(self, orders):         
        if not orders:             
            return 0.0
        total = 0.0         
        for order in orders:             
            if order.get('status') == 'COMPLETED':                 
                total += order.get('amount', 0.0)         
        return total      
    
    def filter_orders_by_date(self, orders, start_date, end_date):         
        if not orders or not start_date or not end_date:             
            return []         
        if start_date > end_date:             
            raise ValueError("Ngày bắt đầu không được lớn hơn ngày kết thúc!")         
        result = []         
        for order in orders:             
            order_date = order.get('created_date', '')             
            if start_date <= order_date <= end_date:                 
                result.append(order)         
        return result