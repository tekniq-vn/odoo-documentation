# Resupply subcontractor

In manufacturing, subcontracting is the process of a company engaging a third-party manufacturer, or\
subcontractor, to manufacture products that are then sold by the contracting company.

In Odoo, the _Resupply Subcontractor on Order_ route is used to deliver the necessary components for\
a subcontracted product to the subcontractor, each time a purchase order (PO) for that product is\
confirmed.

The subcontractor then uses the components to manufacture the desired product, before shipping it\
back to the contracting company, or dropshipping it to the end customer.

#### IMPORTANT

It is necessary to understand the differences between the _Resupply Subcontractor on Order_ and\
the _Dropship Subcontractor on Order_ routes.

While both routes are used to supply a subcontractor with the components required for\
manufacturing a product, they differ in how the components are sourced.

When using _Resupply Subcontractor on Order_, components are shipped from the warehouse of the\
contracting company.

When using _Dropship Subcontractor on Order_, components are purchased from a vendor and shipped\
directly to the subcontractor.

The choice of which route to use depends upon the specific requirements of the subcontracting\
company and their subcontractors.

See the [Dropship to subcontractor](subcontracting_dropship.md) documentation for a full overview of the *Dropship
Subcontractor on Order* route.

## Cấu hình

To use the _Resupply Subcontractor on Order_ route, navigate to Manufacturing app\
‣ Configuration ‣ Settings, and enable the checkbox next to Subcontracting, under\
the Operations heading.

Once the _Subcontracting_ setting is enabled, it is also necessary to properly configure the\
subcontracted product, the product's bill of materials (BoM), and the components listed on the\
.

### Cấu hình sản phẩm

To configure a product for the _Resupply Subcontractor on Order_ route, navigate to\
Inventory app ‣ Products ‣ Products, and select a product, or create a new one\
by clicking New.

Select the Purchase tab, and add the product's subcontractor as a vendor by clicking\
Add a line, selecting the subcontractor in the Vendor drop-down menu, and\
entering a price in the Price field.

#### NOTE

The value entered in the Price field on the Purchase tab of the of the\
subcontracted product's page is the amount paid to the subcontractor for the manufacturing of the\
product.

This does not represent the total cost of the product, which includes other elements, like the\
cost of the product's components.

Then, click on the Inventory tab to configure a route that determines what happens to\
the finished product, once it has been manufactured by the subcontractor.

If the finished product is shipped back to the contracting company, make sure that the\
Buy route is selected. In addition, select the Replenish on Order (MTO)\
route to automatically create a for the product upon confirmation of a sales order (SO), unless\
there is enough stock on-hand to fulfill the .

If the finished product is shipped directly to the customer by the subcontractor, make sure that\
only the Dropship route is selected.

### Configure BoM

To configure a for the _Resupply Subcontractor on Order_ route, click the Bill of\
Materials smart button on the product's page, and select the .

Alternatively, navigate to Manufacturing app ‣ Products ‣ Bills of Materials,\
and select the for the subcontracted product.

#### SEE ALSO
For a full overview of  configuration, see the [Bill of materials](../basic_setup/bill_configuration.md) documentation.

For a full overview of configuration, see the [Bill of materials](applications/inventory_and_mrp/manufacturing/basic_setup/bill_configuration.md) documentation.

In the BoM Type field, select the Subcontracting option. Then, add one or\
more subcontractors in the Subcontractors field that appears below.

![The "BoM Type" field on a BoM, configured to manufacture the product using subcontracting.](../../../../.gitbook/assets/bom-type2.png)

Finally, make sure that all necessary components are specified on the Components tab. To\
add a new component, click Add a line, select the component in the Component\
drop-down menu, and specify the required quantity in the Quantity field.

### Configure components

To configure components for the _Resupply Subcontractor on Order_ route, navigate to each component\
from the by selecting the component's name in the Components tab, and clicking the\
➡️ (right arrow) button to the right of the name.

Alternatively, navigate to each component by going to Inventory app ‣ Products ‣\
Products, and selecting the component.

On the component product form, click on the Inventory tab and select the\
Resupply Subcontractor on Order route in the Routes section.

Repeat the process for every component that must be sent to the subcontractor.

## Resupply subcontractor on order workflow

The resupply subcontractor on order workflow consists of up to five steps:

1. Create an for the subcontracted product; doing so creates a to purchase the product\
   from the subcontractor.
2. Confirm the created in the previous step, or create a new ; doing so creates a _Resupply_\
   _Subcontractor_ order, as well as a receipt order or a dropship order.
3. Process the _Resupply Subcontractor_ order once components for the subcontracted product have\
   been sent to the subcontractor.
4. Process the receipt once the subcontractor has finished manufacturing the subcontracted product,\
   and shipped it back to the contracting company **OR** process the dropship order to ship the\
   product directly to the customer.
5. If the workflow was started by creating an , and the finished product is not dropshipped to\
   the end customer, process the delivery order once the product is shipped to the customer.

The specific number of steps depends on the reason that the subcontracted product is being purchased\
from the subcontractor.

If the reason is to fulfill a specific customer order, the process starts with creating an , and\
ends with delivering the product to the customer, or having the subcontractor dropship it to them.

If the reason is to increase the quantity of stock on-hand, the process starts with creating a ,\
and ends with receiving the product into inventory.

#### IMPORTANT

While the _Resupply Subcontractor on Order_ route can be used to automatically resupply a\
subcontractor upon confirmation of a , it is also possible to create a resupply order\
manually. This workflow is useful when it is necessary to resupply the subcontractor without\
creating a .

To resupply a subcontractor manually, navigate to the Inventory app, and click\
on the Resupply Subcontractor card. Create a new _Resupply Subcontractor_ order by\
clicking New.

In the Delivery Address field, select the subcontractor to whom the components should\
be sent.

Then, add each component to the Operations tab by clicking Add a line,\
selecting the component in the Product drop-down field, and specifying a quantity in\
the Demand field.

Finally, click Mark as Todo to register the order. Once the components have been sent\
to the subcontractor, click Validate to confirm that the order has been sent.

### Create SO

It is only necessary to complete this step if the product is being purchased from the subcontractor\
to fulfill a customer need. If the product is being purchased to increase the quantity of stock\
on-hand, move on to the next step.

To create a new , navigate to Sales app ‣ Orders ‣ Orders, and click\
New.

Select the customer in the Customer drop-down menu. Then, click Add a\
product on the Order Lines tab, select a subcontracted product in the\
Product drop-down menu, and enter a quantity in the Quantity field.

Click Confirm to confirm the , at which point a Purchase smart button\
appears at the top of the page. This opens the created to purchase the subcontracted product\
from the subcontractor.

#### NOTE

An for the product only creates a if the _Replenish on Order (MTO)_ route is enabled on\
the product's page, **and** there is not enough stock of the product on-hand to fulfill the .

If there is enough stock on-hand, confirming an for the product instead creates a delivery\
order, because Odoo assumes that the is fulfilled using the stock in the warehouse.

This is not the case for subcontracted products that are dropshipped to the end customer. In that\
case, a is **always** created, even if there is enough stock on-hand.

### Process PO

If a was created in the previous step, navigate to Purchase app --> Orders -->\
Purchase Orders, and select the . Then, click Confirm Order to confirm it.

If a was not created in the previous step, do so now by navigating to Purchase\
app ‣ Orders ‣ Purchase Orders, and clicking New.

Begin filling out the by selecting a subcontractor from the Vendor drop-down menu.\
In the Products tab, click Add a product to create a new product line.\
Select a subcontracted product in the Product field, and enter the quantity in the\
Quantity field. Finally, click Confirm Order to confirm the .

When a is confirmed for a product that requires resupplying a subcontractor with components, a\
receipt or dropship order is automatically created, and can be accessed from the corresponding\
Receipt or Dropship smart button that appears at the top of the .

In addition, a _Resupply Subcontractor_ order is created to ship the required components to the\
subcontractor. This order can also be accessed from the , by clicking the Resupply\
smart button at the top of the page.

![A PO for a Resupply Subcontractor on Order product, with Resupply and Receipt smart
buttons at the top of the page.](../../../../.gitbook/assets/subcontractor-po2.png)

### Process Resupply Subcontractor order

Once the subcontracted product's components have been sent to the subcontractor, navigate to\
Purchase app ‣ Orders ‣ Purchase Orders, and select the .

Click the Resupply smart button at the top of the screen to open the _Resupply_\
_Subcontractor_ order, and click Validate to confirm that the components have been sent\
to the subcontractor.

Alternatively, navigate to the Inventory app, click the # To Process\
button on the Resupply Subcontractor card, and select the _Resupply Subcontractor_\
order. Then, click Validate to confirm that the components have been sent to the\
subcontractor.

### Process receipt or dropship order

Once the subcontractor has finished manufacturing the product, they either ship it to the\
contracting company, or dropship it to the end customer, depending on how the product was[configured](subcontracting_resupply.md#manufacturing-workflows-subcontracting-resupply-product-config).

#### Process receipt

If the subcontractor ships the finished product to the contracting company, once it has been\
received, navigate to Purchase app ‣ Orders ‣ Purchase Orders, and select the\
.

Click the Receive Products button at the top of the , or the Receipt\
smart button at the top of the page, to open the receipt. Then, click Validate at the\
top of the receipt to enter the product into inventory.

#### Process dropship order

If the subcontractor dropships the product, once they have sent it, navigate to\
Purchase app ‣ Orders ‣ Purchase Orders, and select the .

Select the Dropship smart button at the top of the page to open the dropship order, and\
click Validate at the top of the order to confirm that the product has been sent to the\
customer.

### Process delivery order

If the subcontracting workflow was started by a customer , and the finished product was **NOT**\
dropshipped to the customer, but rather delivered to the contracting company, it is necessary to\
ship the product to the customer, and process the delivery order.

Once the product has been shipped to the customer, navigate to the Sales app, and\
select the . Select the Delivery smart button at the top of the page to open the\
delivery order, and click Validate on the order to confirm that the product has been\
shipped to the customer.
