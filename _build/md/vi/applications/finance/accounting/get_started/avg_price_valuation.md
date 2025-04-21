# Average price on returned goods

<a id="inventory-avg-cost-definition"></a>

*Average cost valuation* (AVCO) is an inventory valuation method that evaluates cost based on the
total cost of goods bought or produced during a period, divided by the total number of items
on-hand. Inventory valuation is used to:

- reflect the value of a company's assets;
- keep track of the amount of unsold goods;
- account for monetary value in goods that have yet to generate profit;
- report on flow of goods throughout the quarter.

Because  uses the weighted average to evaluate the cost, it is a good fit for companies that
sell only a few different products in large quantities. In Odoo, this costing analysis is
*automatically updated* each time products are received.

Thus, when shipments are returned to their supplier, Odoo automatically generates accounting entries
to reflect the change in inventory valuation. However, Odoo does **not** automatically update the
 calculation, because [this can potentially create inconsistencies with inventory
valuation](#inventory-avg-price-leaving-inventory).

#### NOTE
This document addresses a specific use case for theoretical purposes. For instructions on how to
set up and use , refer to the [inventory valuation configuration](../../../inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config.md)
doc.

#### SEE ALSO
- [Using inventory valuation](../../../inventory_and_mrp/inventory/product_management/inventory_valuation/using_inventory_valuation.md)
- [Other inventory valuation methods](../../../inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config.md#inventory-warehouses-storage-costing-methods)

## Cấu hình

To use average cost inventory valuation on a product, navigate to Inventory ‣
Configuration ‣ Product Categories and select the category that will be using . On the
product category page, set Costing Method to `Average Cost (AVCO)` and
Inventory Valuation to `Automated`.

#### SEE ALSO
[Inventory valuation configuration](../../../inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config.md)

## Using average cost valuation

The average cost method adjusts the inventory valuation when products are received in the warehouse.
This section explains how it works, but if the explanation is unnecessary, skip to the [return
to supplier use case](#inventory-avg-cost-return) section.

<a id="inventory-avg-cost-formula"></a>

### Công thức

When new products arrive, the new average cost for each product is recomputed using the formula:

$$
Avg~Cost = \frac{(Old~Qty \times Old~Avg~Cost) + (Incoming~Qty \times Purchase~Price)}{Final~Qty}

$$

- **Old Qty**: product count in stock before receiving the new shipment;
- **Old Avg Cost**: calculated average cost for a single product from the previous inventory
  valuation;
- **Incoming Qty**: count of products arriving in the new shipment;
- **Purchase Price**: estimated price of products at the reception of products (since vendor bills
  may arrive later). The amount includes not only the price for the products, but also added costs,
  such as shipping, taxes, and [landed costs](../../../inventory_and_mrp/inventory/product_management/inventory_valuation/landed_costs.md). At
  reception of the vendor bill, this price is adjusted;
- **Final Qty**: quantity of on-hand stock after the stock move.

<a id="inventory-avg-cost-definite-rule"></a>

#### IMPORTANT
When products leave the warehouse, the average cost **does not** change. Read about why the
average cost valuation is **not** adjusted [here](#inventory-avg-price-leaving-inventory).

<a id="inventory-avg-cost-math-table"></a>

### Compute average cost

To understand how the average cost of a product changes with each shipment, consider the following
table of warehouse operations and stock moves. Each is a different example of how the average cost
valuation is affected.

| Hoạt động                    | Incoming Value   | Giá trị tồn kho   |   SL hiện có | Avg Cost   |
|------------------------------|------------------|-------------------|--------------|------------|
|                              |                  | $0                |            0 | $0         |
| Receive 8 tables at $10/unit | 8 \* $10         | 80$               |            8 | $10        |
| Receive 4 tables at $16/unit | 4 \* $16         | $144              |           12 | $12        |
| Deliver 10 tables            | -10 \* $12       | $24               |            2 | $12        |

<a id="inventory-avg-cost-ex-1"></a>

#### Product delivery (use case)

For outgoing shipments, [outbound products have no effect on the average cost valuation](#inventory-avg-cost-definite-rule). Although the average cost valuation is not recalculated, the
inventory value still decreases because the product is removed from stock and delivered to the
customer location.

<a id="inventory-avg-cost-return"></a>

## Return items to supplier (use case)

Because the price paid to suppliers can differ from the price the product is valued at with the
 method, Odoo handles returned items in a specific way.

1. Products are returned to suppliers at the original purchase price, but;
2. The internal cost valuation remains unchanged.

The above [example table](#inventory-avg-cost-math-table) is updated as follows:

| Hoạt động                    | Qty\*Avg Cost   | Giá trị tồn kho   |   SL hiện có | Avg Cost   |
|------------------------------|-----------------|-------------------|--------------|------------|
|                              |                 | $24               |            2 | $12        |
| Return 1 table bought at $10 | -1 \* $12       | $12               |            1 | $12        |

In other words, returns to vendors are perceived by Odoo as another form of a product exiting the
warehouse. To Odoo, because the table is valued at $12 per unit, the inventory value is reduced by
`$12` when the product is returned; the initial purchase price of `$10` is unrelated to the table's
average cost.

<a id="inventory-avg-price-leaving-inventory"></a>

### Eliminate stock valuation errors in outgoing products

Inconsistencies can occur in a company's inventory when the average cost valuation is recalculated
on outgoing shipments.

To demonstrate this error, the table below displays a scenario in which 1 table is shipped to a
customer and another is returned to a supplier at the purchased price.

| Hoạt động                                | SL\*Giá   | Giá trị tồn kho   | SL hiện có   | Avg Cost   |
|------------------------------------------|-----------|-------------------|--------------|------------|
|                                          |           | $24               | 2            | $12        |
| Ship 1 product to customer               | -1 \* $12 | $12               | 1            | $12        |
| Return 1 product initially bought at $10 | -1 \* $10 | **$2**            | **0**        | $12        |

In the final operation above, the final inventory valuation for the table is `$2` even though there
are `0` tables left in stock.

## Kế toán Anglo-Saxon

Bên cạnh việc sử dụng , các công ty áp dụng **kế toán Anglo-Saxon** còn duy trì tài khoản tạm giữ để theo dõi số tiền phải trả nhà cung cấp. Khi nhà cung cấp giao hàng, **giá trị tồn kho** tăng theo giá nhập hàng của sản phẩm đã nhập kho. Tài khoản tạm giữ (gọi là **nhập kho**) được ghi có và chỉ đối chiếu khi nhận được hóa đơn mua hàng.

#### SEE ALSO
- [Anglo-Saxon vs. Continental](../../../inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config.md#inventory-warehouses-storage-accounting-types)

Bảng dưới đây phản ánh các bút toán và tài khoản kế toán. Tài khoản *nhập kho* lưu trữ số tiền dự kiến sẽ thanh toán cho nhà cung cấp khi hóa đơn mua hàng vẫn chưa được nhận. Để cân đối tài khoản khi trả lại sản phẩm có sự chênh lệch giữa giá trị **định giá** của sản phẩm và giá mua thực tế, một tài khoản *chênh lệch giá* sẽ được tạo ra.

<a id="inventory-avg-price-price-table"></a>

| Hoạt động                              | Stock Input   | Price Diff   | Giá trị tồn kho   |   SL hiện có | Avg Cost   |
|----------------------------------------|---------------|--------------|-------------------|--------------|------------|
|                                        |               |              | $0                |            0 | $0         |
| Receive 8 tables at $10                | ($80)         |              | 80$               |            8 | $10        |
| Receive vendor bill $80                | $0            |              | 80$               |            8 | $10        |
| Receive 4 tables at $16                | ($64)         |              | $144              |           12 | $12        |
| Receive vendor bill $64                | $0            |              | $144              |           12 | $12        |
| Deliver 10 tables to customer          | $0            |              | $24               |            2 | $12        |
| Return 1 table initially bought at $10 | **$10**       | **$2**       | **$12**           |            1 | $12        |
| Receive vendor refund $10              | $0            | $2           | $12               |            1 | $12        |

### Product reception

#### Tóm tắt

Tại thời điểm nhận hàng, Odoo đảm bảo rằng các công ty có thể thanh toán cho hàng hóa đã mua bằng cách chuyển trước một khoản tiền tương ứng với giá trị của hàng hóa nhận được vào [tài khoản nợ phải trả](cheat_sheet.md), **Nhập kho**. Sau đó, khi nhận hóa đơn, số tiền trong tài khoản tạm giữ này sẽ được chuyển sang *Tài khoản phải trả*. Việc chuyển tiền vào tài khoản này có nghĩa là hóa đơn đã được thanh toán. **Nhập kho** sẽ được đối chiếu khi nhận được hóa đơn mua hàng.

Inventory valuation is a method of calculating how much each in-stock product is worth internally.
Since there is a difference between the price the product is **valuated at** and the price the
product was actually **purchased for**, the **Inventory Valuation** account is unrelated to the
crediting and debiting operations of the **Stock Input** account.

To conceptualize all this, follow the breakdown below.

#### Accounts balanced at received products

In this example, a company starts with zero units of a product, `table`, in stock. Then, 8 tables
are received from the vendor:

1. The **Stock Input** account stores `$80` of credit owed to the vendor. The amount in this account
   is unrelated to the inventory value.
2. `$80` worth of tables came **in** (**debit** the *Inventory Value* account `$80`), and
3. `$80` must be paid **out** for received goods (**credit** the *Stock Input* account `$80`).

##### Trong Odoo

Odoo generates an accounting journal entry when shipments that use  costing method are
received. Configure a Price Difference Account by selecting the ➡️ (arrow)
icon next to the Product Category field on the product page.

Under Account Properties, create a new Price Difference Account by typing in
the name of the account and clicking Create and Edit. Then set the account
Type as `Expenses`, and click Save.

![Create price difference account.](applications/finance/accounting/get_started/avg_price_valuation/create-price-difference.png)

Then, receive the shipment in the *Purchase* app or *Inventory* app, and navigate to the
Accounting app ‣ Accounting ‣ Journal Entries. In the list, find the
Reference that matches the warehouse reception operation for the relevant product.

![Show accounting entry of 8 tables from the list.](applications/finance/accounting/get_started/avg_price_valuation/search-for-entry-of-tables.png)

Click on the line for 8 tables. This accounting journal entry shows that when the 8 tables were
received, the `Stock Valuation` account increased by `$80`. Conversely, the **Stock Input** account
(set as `Stock Interim (Received)` account by default) is credited `$80`.

![Debit stock valuation and credit stock input 80 dollars.](applications/finance/accounting/get_started/avg_price_valuation/accounting-entry-8-tables.png)

#### Accounts balanced at received vendor bill

In this example, a company starts with zero units of a product, table, in stock. Then, 8 tables are
received from the vendor. When the bill is received from vendor for 8 tables:

1. Use `$80` in the **Stock Input** account to pay the bill. This cancels out and the account now
   holds `$0`.
2. Debit **Stock Input** `$80` (to reconcile this account).
3. Credit **Accounts payable** `$80`. This account stores the amount the company owes others, so
   accountants use the amount to write checks to vendors.

##### Trong Odoo

Once the vendor requests payment, navigate to the Purchase app ‣ Orders ‣
Purchase and select the  for 8 tables. Inside the , select Create Bill.

Switch to the Journal Items tab to view how `$80` is transferred from the holding
account, `Stock Interim (Received)` to `Accounts Payable`. Confirm the bill to record
the payment to the vendor.

![Show bill linked to the purchase order for 8 tables.](applications/finance/accounting/get_started/avg_price_valuation/receive-8-table-bill.png)

### On product delivery

In the [above example table](#inventory-avg-price-price-table), when 10 products are delivered
to a customer, the **Stock Input** account is untouched because there are no new products coming in.
To put it simply:

1. **Inventory valuation** is credited `$120`. Subtracting from inventory valuation represents
   `$120` worth of products exiting the company.
2. Debit **Accounts Receivable** to record revenue from the sale.

![Show journal items linked to sale order.](applications/finance/accounting/get_started/avg_price_valuation/sell-10-tables.png)

### On product return

Trong [bảng ví dụ trên](#inventory-avg-price-price-table), khi trả lại 1 sản phẩm cho nhà cung cấp với giá mua ban đầu là `$10`, công ty mong đợi nhận lại `$10` trong tài khoản **Tài khoản phải trả** từ nhà cung cấp. Tuy nhiên, tài khoản **Tài khoản nhập kho** phải ghi nợ `$12` do giá trung bình tại thời điểm trả hàng là `$12`. Số chênh lệch `$2` được ghi nhận vào tài khoản Tài khoản chênh lệch giá, được thiết lập trong Danh mục sản phẩm của sản phẩm.

#### NOTE
Behavior of *price difference accounts* varies from localization. In this case, the account is
intended to store differences between vendor price and *automated* inventory valuation methods.

Tóm tắt:

1. Debit **Stock Input** account `$10` to move the table from stock to stock input. This move is to
   indicate that the table is to be processed for an outgoing shipment.
2. Debit **Stock Input** an additional `$2` to account for the **Price Difference**.
3. Credit **Stock Valuation** `$12` because the item is leaving the stock.

![2 dollar difference expensed in Price Difference account.](applications/finance/accounting/get_started/avg_price_valuation/expensing-price-difference-account.png)

Once the vendor's refund is received,

1. Credit **Stock Input** account `$10` to reconcile the price of the table.
2. Debit **Accounts Payable** `$10` to have the accountants collect and register the payment in
   their journal.

![Return to get 10 dollars back.](applications/finance/accounting/get_started/avg_price_valuation/return-credit-note.png)
