# Using inventory valuation

<a id="inventory-reporting-using-inventory-val"></a>

*Inventory valuation* is a quintessential accounting procedure that calculates the value of on-hand
stock. Once determined, the inventory valuation amount is then incorporated into a company's overall
value.

In Odoo, this process can be conducted manually— by warehouse employees physically counting the
products— or automatically through the database.

## Định giá tồn kho tự động

To use Odoo to automatically generate a trail of inventory valuation entries, first navigate to the
Product Categories list by going to Inventory app ‣ Configuration
‣ Product Categories and select the desired product category. On the form, set the
Inventory Valuation as Automated and the Costing Method to any
of the three options.

#### SEE ALSO
[Set up inventory valuation](inventory_valuation_config.md)

In order to understand how moving products in and out of stock affects the company's overall value,
consider the following product and stock moves scenario below.

### Receive a product

Để theo dõi giá trị của các sản phẩm sắp nhập, chẳng hạn như một *bảng* đơn giản, hãy cấu hình danh mục sản phẩm trên chính sản phẩm đó. Để tiến hành, đi đến Ứng dụng Tồn kho ‣ Sản phẩm ‣ Sản phẩm và nhấp vào sản phẩm mong muốn. Trên biểu mẫu sản phẩm, nhấp vào biểu tượng ➡️ (mũi tên phải) bên cạnh trường Danh mục sản phẩm, mở ra liên kết nội bộ để chỉnh sửa danh mục sản phẩm. Tiếp theo, đặt Phương pháp tính chi phí là Nhập trước xuất trước (FIFO) và Định giá tồn kho là Tự động.

Next, assume 10 tables are purchased at a price of $10.00, each. The  for
those tables will show the subtotal of the purchase as $100, plus any additional costs or taxes.

![Purchase order with 10 tables products valued at $10.00 each.](applications/inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation/purchase-order.png)

After selecting Validate on the , the Valuation
smart button is enabled. Clicking on this button displays a report showing how the inventory
valuation for the table was affected by this purchase.

#### IMPORTANT
[Developer mode](../../../../general/developer_mode.md#developer-mode) **must** be turned on to see the Valuation
smart button.

![See Valuation smart button on a receipt, with Developer mode enabled.](applications/inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation/valuation-smart-button.png)

For a comprehensive dashboard that includes the inventory valuation of all product shipments,
inventory adjustments, and warehouse operations, refer to the [stock valuation report](#inventory-management-reporting-valuation-report).

### Deliver a product

In the same logic, when a table is shipped to a customer and leaves the warehouse, the stock
valuation decreases. The Valuation smart button on the ,
likewise, displays the stock valuation record as it does on a .

![Decreased stock valuation after a product is shipped.](applications/inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation/decreased-stock-valuation.png)

<a id="inventory-management-reporting-valuation-report"></a>

## Inventory valuation report

To view the current value of all products in the warehouse, first turn on [Developer mode](../../../../general/developer_mode.md#developer-mode) and navigate to Inventory app ‣ Reporting ‣ Valuation. The
Stock Valuation dashboard displays detailed records of products with the
Date, Quantity, Unit Value, and Total Value of the
inventory.

#### IMPORTANT
[Developer mode](../../../../general/developer_mode.md#developer-mode) **must** be enabled to see the Valuation
option under Reporting.

![Inventory valuation report showing multiple products.](applications/inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation/inventory-valuation-products.png)

The Valuation At Date button, located in the top-left corner of the Stock
Valuation page, reveals a pop-up window. In this pop-up, the inventory valuation of products
available during a prior specified date can be seen and selected.

### Update product unit price

For any company: lead times, supply chain failures, and other risk factors can contribute to
invisible costs. Although Odoo attempts to accurately represent the stock value, *manual valuation*
serves as an additional tool to update the unit price of products.

#### IMPORTANT
Manual valuation is intended for products that can be purchased and received for a cost greater
than 0, or have product categories set with Costing Method set as either
Average Cost (AVCO) or First In First Out (FIFO).

![Add manual valuation of stock value to a product.](applications/inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation/add-manual-valuation.png)

Tạo bút toán định giá thủ công trên trang chủ Định giá tồn kho bằng cách đầu tiên đi đến Ứng dụng Tồn kho ‣ Báo cáo ‣ Định giá. Tiếp theo, để bật tính năng  *định giá lại sản phẩm*, chọn Nhóm theo ‣ Sản phẩm để sắp xếp tất cả bản ghi theo sản phẩm. Nhấp vào biểu tượng ▶️ (tam giác xổ xuống) màu xám để hiển thị các dòng định giá tồn kho bên dưới, cũng như nút ➕ (dấu cộng) màu xanh dương ở bên phải.

Click the teal + (plus) button to open up the Product Revaluation form.
Here, the inventory valuation for a product can be recalculated, by increasing or decreasing the
unit price of each product.

#### NOTE
The ▶️ (drop-down triangle) and ➕ (plus) buttons are only visible after
grouping entries by product.

![Product revaluation form adding a value of $1.00 with the reason being inflation.](applications/inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation/product-revaluation.png)

### Inventory valuation journal entries

In Odoo, automatic inventory valuation records are also recorded in the Accounting
app ‣ Accounting ‣ Journal Entries dashboard. On this comprehensive list of accounting entries,
inventory valuation records are identified by checking values in the Journal column, or
looking for the Reference column value which matches the warehouse operation reference
(e.g. `WH/IN/00014` for receipts).

Clicking on an inventory valuation journal entry opens a *double-entry accounting* record. These
records are generated by Odoo to track the change of value in inventory valuation as products are
moved in and out of the warehouse.

#### SEE ALSO
[Odoo Tutorial: Inventory Valuation](https://www.odoo.com/slides/slide/2795/share)
