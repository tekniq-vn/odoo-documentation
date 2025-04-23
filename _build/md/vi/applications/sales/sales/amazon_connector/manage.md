# Amazon order management

## Đồng bộ đơn hàng

Orders are automatically fetched from Amazon, and synchronized in Odoo, at regular intervals.

The synchronization is based on the Amazon status: only orders whose status has changed since the
last synchronization are fetched from Amazon. This includes changes on either end (Amazon or Odoo).

For *FBA* (Fulfilled by Amazon), only *Shipped* and *Canceled* orders are fetched.

For *FBM* (Fulfilled by Merchant), the same is done for *Unshipped* and *Canceled* orders. For each
synchronized order, a sales order and customer are created in Odoo (if the customer is not already
registered in the database).

#### NOTE
When an order is canceled in Amazon, and was already synchronized in Odoo, the corresponding
sales order is automatically canceled in Odoo.

## Force synchronization

In order to force the synchronization of an order, whose status has **not** changed since the
previous synchronization, start by activating the [developer mode](../../../general/developer_mode.md#developer-mode). This
includes changes on either end (Amazon or Odoo).

Then, navigate to the Amazon account in Odoo (Sales app ‣ Configuration ‣
Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon Accounts), and modify the date under
Orders Follow-up ‣ Last Order Sync.

Be sure to pick a date that occurs prior to the last status change of the desired order to
synchronize and save. This will ensure synchronization occurs correctly.

## Manage deliveries in FBM

Whenever an FBM (Fulfilled by Merchant) order is synchronized in Odoo, a picking is instantly
created in the *Inventory* app, along with a sales order and customer record. Then, decide to either
ship all the ordered products to the customer at once, or ship products partially using backorders.

When a picking related to the order is confirmed, a notification is then sent to Amazon, who, in
turn, notifies the customer that the order (or a part of it) is on its way.

#### IMPORTANT
Amazon requires users to provide a tracking reference with each delivery. This is needed to
assign a carrier.

If the carrier doesn't automatically provide a tracking reference, one must be set manually. This
rule applies to all Amazon marketplaces.

#### SEE ALSO
[Third-party shipping carriers](../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.md)

<a id="manage-manage-delivery-errors"></a>

### Manage errors when synchronizing deliveries

Sometimes, Amazon can fail to correctly process all the information sent by Odoo. In this case, Odoo
sends an email listing all the shipments that failed and the errors Amazon sent with them. In
addition, these shipments are flagged with a Synchronization with Amazon failed tag.

Usually, the error can be corrected directly in the Amazon backend or in Odoo. If the problem is
corrected in Odoo, synchronize the shipment again using the Retry Amazon Sync button.

#### NOTE
Có thể xảy ra trường hợp Odoo nhận được thông báo từ Amazon nói rằng một số thông tin giao hàng chưa được xử lý, nhưng không nêu rõ lô hàng nào bị ảnh hưởng. Trong trường hợp đó, tất cả các lô hàng ở trạng thái không xác định sẽ được xử lý như thể chúng không đồng bộ hóa được. Khi Odoo nhận được thông báo từ Amazon nói rằng một lô hàng đã được xử lý, thẻ của lô hàng sẽ thay đổi thành :guilabel: `Đã đồng bộ với Amazon`. Để đẩy nhanh quá trình này, trên tài khoản Amazon của bạn, hãy nhấp vào :guilabel: `Đồng bộ đơn hàng` để đồng bộ thủ công các đơn hàng này hoặc nhấp vào :guilabel: `Khôi phục đơn hàng` và nhập Tham chiếu đơn hàng Amazon liên quan.

## Follow deliveries in FBA

When an FBA (Fulfilled by Amazon) order is synchronized in Odoo, a stock move is recorded in the
*Inventory* app for each sales order item. That way, it's saved in the system.

Inventory managers can access these stock moves by navigating to Inventory app ‣
Reporting ‣ Moves History.

For FBA orders, the stock move is automatically created in Odoo by the Amazon connector, thanks to
the shipping status of Amazon. When sending new products to Amazon, the user should manually create
a picking (delivery order) to transfer these products from their warehouse to the Amazon location.

The Amazon location is configurable by accessing the Amazon account managed in Odoo. To access
Amazon accounts in Odoo navigate to Sales app ‣ Configuration ‣ Settings ‣
Connectors ‣ Amazon Sync ‣ Amazon Accounts.

All accounts of the same company use the same Amazon location, by default. However, it is possible
to follow the stock filtered by marketplace.

To do that, first remove the marketplace, where the desired stock to follow separately can be found,
from the list of synchronized marketplaces, which can be found by navigating to
Sales app ‣ Configuration ‣ Settings ‣ Connectors ‣ Amazon Sync ‣ Amazon
Accounts.

Next, create another registration for this account, and remove all marketplaces--- **except** the
marketplace this is desired to be isolated from the others.

Lastly, assign another stock location to the second registration of the account.

## Invoice and register payments

### Xuất hoá đơn

Due to Amazon's policy of not sharing customer email addresses, it is **not** possible to send
invoices directly to Amazon customers from Odoo. However, it **is** possible to manually upload the
generated invoices from Odoo to the Amazon back-end.

Additionally, for B2B clients, it is currently required to manually retrieve VAT numbers from the
Amazon back-end **before** creating an invoice in Odoo.

#### NOTE
For [TaxCloud](../../../finance/accounting/taxes/taxcloud.md) users: invoices created from
Amazon sales orders are **not** synchronized with TaxCloud, since Amazon already includes them in
its own tax report to TaxCloud.

#### WARNING
TaxCloud integration will be decommissioned in Odoo 17+.

### Register payments

Since customers pay Amazon as an intermediary, creating a dedicated *Bank* journal (e.g. named
`Amazon Payments`), with a dedicated *Bank and Cash* intermediary account is recommended.

Additionally, as Amazon makes a single monthly payment, selecting all the invoices linked to a
single payment is necessary when registering payments.

To do that, use the appropriate Journal dedicated to Amazon payments, and select
Batch Deposit as the Payment Method.

Then, select all the generated payments, and click Actions ‣ Create batch payment
‣ Validate.

## Follow Amazon sales in sales reporting

On the Amazon account profile in Odoo, a sales team is set under the Order Follow-up
tab.

This gives quick access to important metrics related to sales reporting. By default, the Amazon
account's sales team is shared between all of the company's accounts.

If desired, the sales team on the account can be changed for another, in order to perform a separate
reporting for the sales of this account.

#### SEE ALSO
- [Amazon Connector features](features.md)
- [Amazon Connector configuration](setup.md)
