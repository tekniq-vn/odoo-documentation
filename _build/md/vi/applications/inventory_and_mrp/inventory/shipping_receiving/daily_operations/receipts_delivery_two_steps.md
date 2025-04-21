# Two-step receipt and delivery

Depending on a company's needs, receiving and shipping products in and out of the warehouse might
require multi-step operations. In Odoo *Inventory*, this can be done using *Multi-Step Routes*.

In the two-step receipt process, products are received in an input area, then transferred to stock.
This kind of process for incoming shipments might be beneficial for warehouses with specific storage
locations, such as freezers and refrigerators, secured locked areas, or special aisles and shelves.

Products can be sorted according to where they are going to be stored, and employees can stock all
the products going to a specific location. The products are *not* available for further processing,
until they are transferred into stock.

In the two-step delivery process, products are first picked from their respective location in the
warehouse, then transferred to an output location before being shipped to the customer.

This might be beneficial for companies using a First In, First Out (FIFO), Last In, First Out
(LIFO), or First Expired, First Out (FEFO) removal strategy.

## Cấu hình

In Odoo *Inventory*, both incoming and outgoing shipments are configured to process in one step, by
default. To change these settings, the *Multi-Step Routes* feature must be enabled.

To enable *Multi-Step Routes*, navigate to Inventory app ‣ Configuration ‣
Settings. Under the Warehouse section, tick the checkbox next to Multi-Step
Routes, and click Save. Doing so also activates the Storage Locations
feature.

![Enabled Multi-Step Routes feature in Inventory app settings.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-settings.png)

Next, configure a warehouse for two-step receipts and deliveries. Navigate to
Inventory app ‣ Configuration ‣ Warehouses, and select a warehouse to edit.

Under the Warehouse Configuration tab, set Incoming Shipments to
Receive goods in input and then stock (2 steps), and set Outgoing Shipments
to Send goods in output and then deliver (2 steps).

![Incoming and outgoing shipments set to two-step on warehouse form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-shipments.png)

#### NOTE
Selecting two-step receipts and deliveries automatically creates new *Input* and *Output*
warehouse locations in the database, named `WH/Input` and `WH/Output`, respectively.

To rename or edit these locations, navigate to Inventory app ‣ Configuration
‣ Locations, and select the desired location.

On the location's form, change the Location Name, and make any other necessary
changes.

## Process receipt in two steps (input + stock)

When products are received in two steps, they first move from the vendor location to an input
location. Then, they move from the input location to warehouse stock in the database, upon
validation of a purchase order (PO), and a subsequent internal transfer.

### Tạo đơn mua hàng

To create a , navigate to the Purchase app, and click New. This
opens a blank Request for Quotation (RfQ) form.

Add a vendor in the Vendor field. Then, fill out the various fields on the , as
necessary.

![Filled out new Request for Quotation from vendor.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-new-rfq.png)

Under the Products tab, click Add a product, and select a product to add to
the .

Once ready, click Confirm Order. This moves the  to the Purchase Order
stage.

Once the  is confirmed, a Receipt smart button appears at the top of the form.
Clicking the smart button opens the warehouse receipt (WH/IN) form.

![Delivery smart button for validated purchase order.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-smart-button.png)

### Process receipt

From the warehouse receipt form, the products ordered can be received into the warehouse. To receive
the products, click Validate. Once validated, the receipt moves to the Done
stage, and the products move to the WH/Input location.

![Receipt form for products ordered from vendor.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-receipt-form.png)

Click back to the  (via the breadcrumbs, at the top of the form) to view the  form. On the
product line, the quantity in the Received column now matches the ordered
Quantity.

### Process internal transfer

Once the receipt is validated, an internal transfer is created and ready to process.

To view the internal transfer, navigate to the Inventory app, and locate the
Internal Transfers task card.

Click the # To Process button on the task card to reveal a list of all internal
transfers to process, and select the transfer associated with the previously validated receipt.

Once ready, click Validate to complete the transfer, and move the product from
WH/Input to WH/Stock.

Once the transfer is validated, the products enter inventory, and are available for customer
deliveries or manufacturing orders.

![Internal transfer form for products ordered from vendor.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-internal-transfer.png)

<a id="inventory-shipping-receiving-two-step-delivery"></a>

## Process delivery order in two steps (pick + ship)

When products are delivered in two steps, they move from warehouse stock to an output location.
Then, they move from the output location to a customer location in the database, upon validation of
a picking order, and a subsequent delivery order (DO).

### Create sales order

To create a , navigate to the Sales app, and click New. This
opens a blank sales quotation form.

Add a customer in the Customer field. Then, fill out the various fields on the sales
quotation form, as necessary.

![Filled out new sales order form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-new-sales-order.png)

Under the Order Lines tab, click Add a product, and select a product to add
to the sales order quotation.

Once ready, click Confirm. This moves the quotation to the Sales Order
stage.

Once the  is confirmed, a Delivery smart button appears at the top of the form.
Clicking the smart button opens the warehouse delivery (WH/OUT) form.

![Delivery smart button on validated sales order form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-delivery-button.png)

### Process picking

Once the sales order is confirmed, a picking order is generated and ready to process.

To complete the picking, navigate to the Inventory app, and locate the Pick
task card on the Inventory Overview dashboard. Alternatively, the picking order can also
be accessed via the Delivery smart button at the top of the sales order form.

From the Inventory Overview page, click the # To Process button on the
Pick task card. This reveals a list of all pickings to process.

Click on the picking (WH/PICK) operation associated with the sales order to reveal the picking
order.

![Picking order form for products included in sales order.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-picking-form.png)

Manually set the quantity by changing the value in the Quantity column, to match the
value in the Demand column.

Once ready, click Validate to complete the picking, and move the product from
WH/Stock to WH/Output.

### Process delivery

Once the picking is validated, a delivery order is created, and ready to process. Clicking the
Delivery smart button on the sales order form reveals the newly created delivery order.

Alternatively, to view the delivery order, navigate back to the Inventory Overview page,
via the breadcrumbs, and locate the Delivery Orders task card.

Click the # To Process button on the task card to reveal a list of all delivery orders
to process, and select the order associated with the previously validated picking.

![Delivery order form for products ordered by customer.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps/receipts-delivery-two-steps-delivery-order.png)

To deliver the products, change the value in the Quantity field to match the ordered
quantity in the Demand field.

Once ready, click Validate. Once validated, the delivery order moves to the
Done stage.

#### SEE ALSO
[Inbound and outbound flows](../daily_operations.md)
