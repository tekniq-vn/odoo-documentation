# One-step receipt and delivery

In Odoo *Inventory*, both incoming and outgoing shipments are configured to process in one step, by
default. This means purchases will be received directly into stock, and deliveries will be moved
directly from stock to customers.

## Cấu hình

To configure one-step receipts and deliveries for a warehouse, navigate to Inventory
app ‣ Configuration ‣ Warehouses, and select a warehouse to edit.

Under the Warehouse Configuration tab, set Incoming Shipments to
Receive goods directly (1 step), and set Outgoing Shipments to
Deliver goods directly (1 step).

![Incoming and outgoing shipments set to one-step on warehouse form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step/receipts-delivery-one-step-warehouse-settings.png)

#### NOTE
Since one-step receipt and delivery is the default for incoming and outgoing shipments in Odoo,
the *Multi-Step Routes* feature is *not* required.

However, for the Shipments settings to appear on a warehouse form, the feature
**must** be enabled.

To enable *Multi-Step Routes*, navigate to Inventory app ‣ Configuration ‣
Settings. Under the Warehouse section, tick the checkbox next to
Multi-Step Routes, and click Save. Doing so also activates the
Storage Locations feature.

<a id="inventory-receipts-delivery-one-step-wh"></a>

## Nhận hàng trực tiếp (1 bước)

When products are received in one step, they will move from the vendor location to warehouse stock
in the database immediately upon validation of a purchase order (PO).

### Tạo đơn mua hàng

To create a , navigate to the Purchase app, and click New. This
opens a blank Request for Quotation (RfQ) form.

Add a vendor in the Supplier field. Then, fill out the various fields on the , as
necessary.

![Filled out new request for quotation form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step/receipts-delivery-one-step-new-rfq.png)

Under the Products tab, click Add a product, and select a product to add to
the .

Once ready, click Confirm Order. This moves the  to the Purchase Order
stage.

Once the  is confirmed, a Receipt smart button appears at the top of the form.
Clicking the smart button opens the warehouse receipt (WH/IN) form.

![Receipt smart button on confirmed purchase order form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step/receipts-delivery-one-step-receipt-smart-button.png)

### Process receipt

From the warehouse receipt form, the products ordered can be received into the warehouse. To receive
the products, click Validate. Once validated, the receipt moves to the Done
stage.

![Validated warehouse receipt in Done stage.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step/receipts-delivery-one-step-done-receipt.png)

Click back to the  (via the breadcrumbs, at the top of the form) to view the  form. On the
product line, the quantity in the Received column now matches the ordered
Quantity.

<a id="inventory-delivery-one-step"></a>

## Giao hàng trực tiếp (1 bước)

When products are delivered in one step, they will move from warehouse stock to the customer
location in the database immediately upon validation of a sales order (SO).

### Create sales order

To create a , navigate to the Sales app, and click New. This
opens a blank sales quotation form.

Add a customer in the Customer field. Then, fill out the various fields on the sales
quotation form, as necessary.

![Filled out new sales quotation form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step/receipts-delivery-one-step-new-sales-order.png)

Under the Product tab, click Add a product, and select a product to add to
the sales order quotation.

Once ready, click Confirm. This moves the quotation to the Sales Order
stage.

Once the  is confirmed, a Delivery smart button appears at the top of the form.
Clicking the smart button opens the warehouse delivery (WH/OUT) form.

![Delivery smart button on confirmed sales order form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step/receipts-delivery-one-step-delivery-button.png)

### Process delivery

From the warehouse delivery form, the products ordered by the customer can be delivered from the
warehouse. To deliver the products, change the value in the Quantity field to match the
ordered quantity in the Demand field.

Once ready, click Validate. Once validated, the delivery order moves to the
Done stage.

![Validated delivery order in Done stage.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step/receipts-delivery-one-step-done-delivery.png)

Click back to the  (via the breadcrumbs, at the top of the form) to view the  form. On the
product line, the quantity in the Delivered column now matches the ordered
Quantity.

#### SEE ALSO
[Inbound and outbound flows](../daily_operations.md)
