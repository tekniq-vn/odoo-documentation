# Số lô

*Lots* are one of the two ways to identify and track products in Odoo. They typically represent a
specific batch of products that were received, stored, shipped, or manufactured in-house.

Manufacturers assign lot numbers to groups of products sharing common properties, facilitating
end-to-end traceability through their lifecycles.

Lots are useful for managing large quantities of manufactured or received products, aiding in
tracing items back to their group, particularly for product recalls or [expiration dates](expiration_dates.md).

#### SEE ALSO
[Sử dụng số sê-ri để theo dõi sản phẩm](serial_numbers.md)

## Bật số lô & sê-ri

To track products using lots, enable the *Lots & Serial Numbers* feature. Go to the
Inventory app ‣ Configuration ‣ Settings, scroll down to the
Traceability section, and tick the checkbox next to Lots & Serial Numbers.
Then, click Save.

#### SEE ALSO
- [Tracking expiration dates](expiration_dates.md)
- [Print GS1 barcodes for lots and serial numbers](../../../barcode/operations/gs1_usage.md#barcode-operations-gs1-lots)

![Enabled lots and serial numbers feature in inventory settings.](lots/enabled-lots-setting.png)

<a id="inventory-management-track-products-by-lots"></a>

## Track by lots

Once the Lots & Serial Numbers feature is activated, configure individual products to be
tracked using lots. To do this, go to Inventory app ‣ Products ‣ Products, and
choose a product to configure.

On the product form, go to the Inventory tab. In the Traceability section,
select the By Lots option in the Tracking field. Now, new or existing lot
numbers can be assigned to newly-received or manufactured batches of this product.

#### SEE ALSO
[Ngày hết hạn](expiration_dates.md)

#### IMPORTANT
If a product has stock on-hand prior to activating tracking by lots or serial numbers, a warning
message appears. Use an [inventory adjustment](reassign.md) to assign lot numbers to existing
products in stock.

![Enabled tracking by lots feature on product form.](lots/tracking-product-form.png)

## Assign lots for shipping and receiving

Assign new lot numbers to [incoming goods](#inventory-product-management-assign-lots) on the
receipt form. When shipping [outgoing goods](#inventory-product-management-assign-lots-delivery), select products with specific lot numbers on
the delivery order form.

<a id="inventory-product-management-assign-lots"></a>

### On receipts

Assigning new or existing lot numbers to incoming goods can be done directly on receipts.

To begin, go to the Purchase app to [create and confirm](https://www.youtube.com/watch?v=o_uI718P1Dc) a  for products tracked by lot numbers. Then,
click the Receipt smart button that appears at the top of the page to navigate to the
warehouse receipt form.

#### NOTE
Alternatively, navigate to an existing receipt by going to the Inventory app,
clicking the Receipts Kanban card, and choosing the desired receipt.

#### IMPORTANT
Clicking Validate before assigning a lot number triggers an error, indicating that a
lot number **must** be assigned before validating the receipt.

![Add lot/serial number user error popup.](lots/user-error.png)

On the receipt form, on the product line in the Operations tab, select the <i class="fa fa-list"></i> (list) icon
to the right of the product that is tracked by lot numbers.

![Show the bulleted list icon on the product line.](lots/list-icon.png)

Doing so opens the Open: Stock move pop-up window, where the Lot/Serial
Number and Quantity are assigned.

The two ways to assign lot numbers: **manually** and **importing**.

#### Manual assignment

To manually assign lot numbers, click Add a line. Input the Lot/Serial
Number, Store To location for the lot, Quantity, and Destination
Package, if any.

#### NOTE
To assign multiple lot numbers, or store to multiple locations, click Add a line, and
type a new Lot/Serial Number for additional quantities. Repeat until the total in the
Quantity column matches the Demand at the top.

![Assign lot number detailed operations popup.](lots/assign-lots-popup.png)

#### Import lots

In the Open: Stock move pop-up window, click Import Serials/Lots, then paste
the bulk lot numbers, in the Lots/Serial numbers field.

![List of lot numbers copied on excel spreadsheet.](lots/lots-excel-spreadsheet.png)![Lot numbers copied to the lot number line.](lots/bulk-sn.png)

Tick the Keep current lines checkbox to generate *additional* lot numbers in the
Open: Stock move pop-up window. To replace the lot numbers in the list, leave the
Keep current lines option unticked.

Cuối cùng, nhấp vào Tạo.

Once all product quantities have been assigned a lot number, click Save to close the
pop-up window. Then, click Validate on the receipt form.

#### SEE ALSO
[Traceability report for lot numbers](#inventory-product-management-lot-traceability)

<a id="inventory-product-management-assign-lots-delivery"></a>

### On delivery orders

Odoo makes it possible to specify which lot numbers for a product are chosen for outgoing shipment
on a delivery order form.

To begin, create or select an existing quotation from the Sales app. After
confirming the , the Delivery smart button becomes available. Click the
Delivery smart button to view the warehouse receipt form for that specific .

#### NOTE
Alternatively, navigate to delivery orders by going to the Inventory app, and
clicking the Delivery Orders kanban card.

Clicking the Delivery smart button opens the the delivery order form, where lot numbers
are picked for delivery. In the Operations tab, click the <i class="fa fa-list"></i> (list) icon to the right of
the product that is tracked by lot numbers. Clicking that icon reveals a Open: Stock
move pop-up window.

In the pop-up window, the chosen lot number and its storage location is displayed in the
Pick From column, with the with the full Quantity taken from that specific
lot (if there is enough stock in that particular lot).

If there is insufficient stock in that lot, or if partial quantities of the Demand
should be taken from multiple lots, change the Quantity directly.

#### NOTE
The lot automatically chosen for delivery orders varies, depending on the selected removal
strategy (, , or ). It also depends on the ordered quantity, and whether the lot's
on-hand quantity is enough to fulfill the order.

#### SEE ALSO
[Removal strategies](../../shipping_receiving/removal_strategies.md)

Repeat the above steps to select enough lots to fulfill the Demand, and click
Save to close the pop-up window. Lastly, click the Validate button on the
 to deliver the products.

![Popup for source lot number on sales order.](lots/pick-from-lots.png)

#### SEE ALSO
[Traceability report for lot numbers](#inventory-product-management-lot-traceability)

## Quản lý lô

Manage and view existing lot numbers for products in the Lot/Serial Numbers dashboard by
going to Inventory app ‣ Products ‣ Lots/Serial Numbers.

By default, lot numbers are grouped by product, and selecting the drop-down menu for each product
displays the existing lot numbers. Select a lot number to [modify or add details](#inventory-product-management-edit-lot) linked to the lot. Lot numbers can also be [created](#inventory-product-management-create-new-lot) from this page, by clicking the New
button.

![Show the "Lot/Serial Number" dashboard.](lots/lot-dashboard.png)

<a id="inventory-product-management-edit-lot"></a>

### Modify lot

Clicking a lot from the Lot/Serial Number dashboard reveals a separate page where
additional information can be provided about the lot.

On the lot number form, the following fields can be modified:

- Lot/Serial Number: change the lot number linked to the Product
- Internal Reference: records an alternative lot/serial number used within the warehouse
  that differs from the one used by the supplier manufacturer.
- Company: specify the company where the lot number is available.
- Description: add extra details about the lot or serial number in this text field.

#### IMPORTANT
On existing lots, the Product and On Hand Quantity fields **cannot** be
modified, as the lot numbers are linked with existing stock moves.

![Show the lot number form.](lots/lot-number.png)

#### SEE ALSO
[Set expiration dates for lots](expiration_dates.md)

#### Add property

To add custom fields to lots for enhanced traceability, there are two methods of adding properties
on a lot number form:

1. Click the <i class="fa fa-cog"></i> (cog) icon at the top-left of the page, then select
   <i class="fa fa-cogs"></i> Add Properties from the drop-down menu.
2. Click the <i class="fa fa-plus"></i> Add a Property button, located below the existing fields.

Name and [configure the new field](../../../../productivity/knowledge/properties.md). Once
finished, enter the property value in the new field.

#### SEE ALSO
[Configuring custom properties](../../../../productivity/knowledge/properties.md)

<a id="inventory-product-management-create-new-lot"></a>

### Reserve lot number for a product

To create a lot number for a product, begin by going to Inventory app ‣ Products
‣ Lot/Serial Numbers, and click New.

#### IMPORTANT
Creating a lot number reserves it for a product but **does not** assign it. To assign lot
numbers, refer to the section on [assigning lot numbers on receipts](#inventory-product-management-assign-lots).

Once the new Lot/Serial Number is generated, click the blank field next to
Product to reveal a drop-down menu. From this menu, select the product to which this new
number will be assigned.

After a new lot number has been created, saved, and assigned to the desired product, the lot number
is saved as an existing lot number linked to the product, and can be selected when [assigning
lot numbers to products on a receipt](#inventory-product-management-assign-lots), or when making an
inventory adjustment.

## Manage lots for different operations types

By default, new lots can only be created when receiving products, and existing lot numbers cannot
be used. For sales orders, only existing lot numbers can be utilized, and new ones cannot be created
on the delivery order.

To change the ability to use new (or existing) lot numbers on any operation type, go to the
Inventory app ‣ Configuration ‣ Operations Types, and select the desired
operation type.

On the operation type form, under the Lots/Serial Numbers section, tick the
Create New checkbox to enable new lot numbers to be created during this operation type.
Choose Use Existing ones if only existing lot numbers can be selected.

![Enabled traceability setting on operations type form.](lots/operation-type-form.png)

<a id="inventory-product-management-lot-traceability"></a>

## Truy xuất nguồn gốc

Manufacturers and companies can refer to traceability reports to see the entire lifecycle of a
product: where it came from, when it arrived, where it was stored, who it went to (and when).

To see the full traceability of a product, or group by lots, go to the Inventory app
‣ Products ‣ Lots/Serial Numbers. Doing so reveals the Lots/Serial Numbers
dashboard.

From here, products with lot numbers assigned to them will be listed by default, and can be expanded
to show the lot numbers those products have assigned to them.

To group by lots, begin by removing any filters in the Search... bar. Then, click the
<i class="fa fa-caret-down"></i> (caret down) icon to open a drop-down menu of Filters,
Group By options, and Favorites. Under the Group By section,
click the Add Custom Group option, and select Lot/Serial Number from the
drop-down menu.

Doing so reorganizes all the records on the page to display all existing lots and serial numbers,
and can be expanded to show all quantities of products with that assigned number.

![Lots and serial numbers traceability report.](lots/group-by-number.png)

### Traceability report

To view a full stock moves report for a lot number, select the lot number line from the
Lots/Serial Number dashboard. On the lot number form, click the Traceability
smart button.

![Show the Traceability Report for a lot, that displays the stock moves.](lots/traceability-report.png)

#### SEE ALSO
[Theo dõi sản phẩm](../product_tracking.md)
