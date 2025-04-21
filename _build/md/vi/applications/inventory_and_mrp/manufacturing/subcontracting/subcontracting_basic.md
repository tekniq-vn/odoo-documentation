# Basic subcontracting

In manufacturing, subcontracting is the process of a company engaging a third-party manufacturer, or
subcontractor, to manufacture products that are then sold by the contracting company.

In basic subcontracting, the subcontractor is responsible for acquiring the necessary components.
This means that the contracting company only has to worry about what happens to subcontracted
products once they are produced.

Quy trình mua một sản phẩm được sản xuất theo phương thức gia công cơ bản tương tự như quy trình mua một sản phẩm không gia công từ nhà cung cấp. Sự khác biệt chính là cách cấu hình các sản phẩm gia công và việc các sản phẩm gia công cần nhiều thời gian hơn để được gửi từ nhà cung cấp, vì chúng phải được nhà cung cấp sản xuất trước.

## Cấu hình

To use subcontracting in Odoo, navigate to Manufacturing app ‣ Configuration ‣
Settings, and tick the checkbox next to the Subcontracting setting, under the
Operations heading. Then, click Save.

Once the Subcontracting setting is enabled, it is also necessary to properly configure
the subcontracted product, and the product's .

<a id="manufacturing-workflows-subcontracting-basic-product-config"></a>

### Cấu hình sản phẩm

To configure a product for basic subcontracting, navigate to Inventory app ‣
Products ‣ Products, and select a product, or create a new one by clicking New.

On the product form, select the Purchase tab, and add the product's subcontractor as a
vendor by clicking Add a line, selecting the subcontractor in the Vendor
drop-down menu, and entering a price in the Price field.

Then, click on the Inventory tab, and use the Routes field to configure a
route that determines what happens to the finished product once it has been manufactured by the
subcontractor.

If the finished product is shipped back to the contracting company, make sure the Buy
route is selected. In addition, select the Replenish on Order (MTO) route to
automatically create a  for the product upon confirmation of a sales order (SO), unless there is
enough stock on-hand to fulfill the .

If the finished product is shipped directly to the customer by the subcontractor, make sure that
**only** the Dropship route is selected.

### Configure BoM

To configure a  for basic subcontracting, click the Bill of Materials smart button
on the product form, and select the desired .

Alternatively, navigate to Manufacturing app ‣ Products ‣ Bills of Materials,
and select the  for the subcontracted product.

#### SEE ALSO
For a full overview of  configuration, see the [Bill of materials](../basic_setup/bill_configuration.md) documentation.

In the BoM Type field, select the Subcontracting option. Then, add one or
more subcontractors in the Subcontractors field that appears below.

![The "BoM Type" field on a BoM, configured to manufacture the product using subcontracting.](applications/inventory_and_mrp/manufacturing/subcontracting/subcontracting_basic/bom-type.png)

Finally, click on the Miscellaneous tab. In the Manuf. Lead Time field,
enter the number of days it takes the subcontractor to manufacture the product. This number is
factored in when calculating the product's expected arrival date.

#### NOTE
When using basic subcontracting, there is no need to list components in the
Components tab of the , since the components required for manufacturing, and the
means by which they are acquired, are handled by the subcontractor.

## Basic subcontracting workflow

The basic subcontracting workflow consists of up to four steps:

1. Create a sales order (SO) for the subcontracted product; doing so creates a  to purchase the
   product from the subcontractor.
2. Confirm the  created in the previous step, or create a new ; doing so creates a receipt
   order or a dropship order.
3. Process the receipt once the subcontractor has finished manufacturing the subcontracted product,
   and shipped it back to the contracting company, **OR** process the dropship order to ship the
   product directly to the customer.
4. If the workflow was started by creating an , and the finished product is not dropshipped to
   the end customer, process the delivery order once the product is shipped to the customer.

The specific number of steps depends on the reason that the subcontracted product is being purchased
from the subcontractor.

If the reason is to fulfill a specific customer order, the process starts with creating an , and
ends with delivering the product to the customer, or having the subcontractor dropship it to them.

If the reason is to increase the quantity of stock on-hand, the process starts with creating a ,
and ends with receiving the product into inventory.

### Create SO

It is only necessary to complete this step if the product is being purchased from the subcontractor
to fulfill a customer need. If the product is being purchased to increase the quantity of stock
on-hand, move on to the next step.

To create a new , navigate to Sales app ‣ Orders ‣ Orders, and click
New.

Select the customer in the Customer drop-down menu. Then, click Add a
product on the Order Lines tab, select a subcontracted product in the
Product drop-down menu, and enter a quantity in the Quantity field.

Click Confirm to confirm the , at which point a Purchase smart button
appears at the top of the page. This opens the  created to purchase the subcontracted product
from the subcontractor.

#### NOTE
An  for the product only creates a  if the *Replenish on Order (MTO)* route is enabled on
the product's form, **and** there is not enough stock of the product on-hand to fulfill the .

If there is enough stock on-hand, confirming an  for the product creates a delivery order
instead, because Odoo assumes that the  is fulfilled using the stock in the warehouse.

This is not the case for subcontracted products that are dropshipped to the end customer. In that
case, a  is **always** created, even if there is enough stock on-hand.

### Process PO

If a  was created in the previous step, navigate to it by clicking the Purchase
smart button at the top of the , or by going to Purchase app --> Orders --> Purchase
Orders, and selecting the . Then, click Confirm Order to confirm it, and move on to
the next step.

If a  was not created in the previous step, do so now by navigating to Purchase
app ‣ Orders ‣ Purchase Orders, and clicking New.

Begin filling out the  by selecting a subcontractor from the Vendor drop-down menu.
In the Products tab, click Add a product to create a new product line.
Select a subcontracted product in the Product field, and enter the quantity in the
Quantity field. Finally, click Confirm Order to confirm the .

When a  is confirmed for a product manufactured using basic subcontracting, a receipt or
dropship order is automatically created, and can be accessed from the corresponding
Receipt or Dropship smart button that appears at the top of the .

![A PO for a basic subcontracting product, with a Receipt smart button at the top of the page.](applications/inventory_and_mrp/manufacturing/subcontracting/subcontracting_basic/subcontractor-po.png)

### Process receipt or dropship order

Once the subcontractor has finished manufacturing the product, they either ship it to the
contracting company, or dropship it to the end customer, depending on how the product was
[configured](#manufacturing-workflows-subcontracting-basic-product-config).

#### Process receipt

If the subcontractor ships the finished product to the contracting company, once it has been
received, navigate to Purchase app ‣ Orders ‣ Purchase Orders, and select the
.

Click the Receive Products button at the top of the , or the Receipt
smart button at the top of the page, to open the receipt. Then, click Validate at the
top of the receipt to enter the product into inventory.

#### Process dropship order

If the subcontractor dropships the product, once they have sent it, navigate to
Purchase app ‣ Orders ‣ Purchase Orders, and select the .

Select the Dropship smart button at the top of the page to open the dropship order, and
click Validate at the top of the order to confirm that the product has been sent to the
customer.

### Process delivery order

If the subcontracting workflow was started by a customer , and the finished product was **not**
dropshipped to the customer, but rather delivered to the contracting company, it is necessary to
ship the product to the customer, and process the delivery order.

Once the product has been shipped to the customer, navigate to the Sales app, and
select the . Select the Delivery smart button at the top of the page to open the
delivery order, and click Validate on the order to confirm that the product has been
shipped.
