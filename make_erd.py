import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Tạo tự động thư mục docs/diagrams nếu chưa có
os.makedirs('docs/diagrams', exist_ok=True)

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

box_color = '#e1f5fe'
edge_color = '#0288d1'

tables = [
    ('CATEGORIES\n- category_id (PK)\n- category_name\n- description', 0.5, 4.5),
    ('MENU_ITEMS\n- item_id (PK)\n- category_id (FK)\n- item_name\n- price\n- status', 4.2, 4.5),
    ('DINING_TABLES\n- table_id (PK)\n- table_number\n- capacity\n- status', 8.2, 4.5),
    ('ORDER_DETAILS\n- detail_id (PK)\n- order_id (FK)\n- item_id (FK)\n- quantity\n- unit_price', 2.3, 1.0),
    ('ORDERS\n- order_id (PK)\n- table_id (FK)\n- created_at\n- status\n- total_amount', 6.0, 1.0),
    ('INVOICES\n- invoice_id (PK)\n- order_id (FK)\n- payment_method\n- final_amount', 9.5, 1.0)
]

for title, x, y in tables:
    rect = patches.FancyBboxPatch(
        (x, y),
        2.2,
        2.2,
        boxstyle='round,pad=0.2',
        facecolor=box_color,
        edgecolor=edge_color,
        linewidth=2
    )
    ax.add_patch(rect)
    ax.text(
        x + 1.1,
        y + 1.1,
        title,
        ha='center',
        va='center',
        fontsize=8,
        fontweight='bold'
    )

plt.title(
    'ERD Diagram - Quan Ly Quan Com Chien (Nhom 5)',
    fontsize=14,
    fontweight='bold'
)

plt.savefig('docs/diagrams/erd.png', dpi=200, bbox_inches='tight')

print("✅ Đã tạo thành công file: docs/diagrams/erd.png")