# Dropship to subcontractor

In manufacturing, subcontracting is the process of a company engaging a third-party manufacturer, or\
subcontractor, to manufacture products that are then sold by the contracting company.

In Odoo, the _Dropship Subcontractor on Order_ route is used to purchase the necessary components\
for a subcontracted product from the vendor, and have them delivered directly to the subcontractor,\
each time a purchase order (PO) for that product is confirmed.

The subcontractor then uses the components to manufacture the desired product, before shipping it\
back to the contracting company.

#### IMPORTANT

It is necessary to understand the differences between the _Dropship_ and _Dropship Subcontractor_\
_on Order_ routes. While both routes involve dropshipping, they are used for different purposes.

The _Dropship_ route is used to purchase products from a vendor, and have them shipped directly\
to the end customer.

The _Dropship Subcontractor on Order_ route is used to purchase components from a vendor, and\
have them shipped directly to a subcontractor. By default, finished products are then sent from\
the subcontractor back to the contracting company.

However, it is possible to combine both the _Dropship_ and _Dropship Subcontractor on Order_\
routes so they are used for the same product. In this workflow, components are dropshipped to the\
subcontractor, who then ships the finished product directly to the end customer.

This can be achieved by following steps one through five in the [workflow section](subcontracting_dropship.md#manufacturing-workflows-subcontracting-dropship) of this doc.

## Cấu hình

To use the _Dropship Subcontractor on Order_ route, navigate to Manufacturing app\
‣ Configuration ‣ Settings, and enable the checkbox next to Subcontracting, under\
the Operations heading.

Once the _Subcontracting_ setting is enabled, it is also necessary to properly configure the\
subcontracted product, the product's , and the components listed on the .

### Cấu hình sản phẩm

To configure a product for the _Dropship Subcontractor on Order_ route, navigate to\
Inventory app ‣ Products ‣ Products, and select a product, or create a new one\
by clicking New.

Select the Purchase tab, and add the product's subcontractor as a vendor by clicking\
Add a line, selecting the subcontractor in the Vendor drop-down menu, and\
entering a price in the Price field.

Then, click on the Inventory tab to configure a route that determines what happens to\
the finished product, once it has been manufactured by the subcontractor.

If the finished product is shipped back to the contracting company, make sure that the\
Buy route is selected. In addition, select the Replenish on Order (MTO)\
route to automatically create a for the product upon confirmation of a , unless there is\
enough stock on-hand to fulfill the .

If the finished product is shipped directly to the customer by the subcontractor, make sure that\
only the Dropship route is selected.

### Configure bill of materials

To configure a for the _Dropship Subcontractor on Order_ route, click the Bill of\
Materials smart button on the product's page, and select the .

Alternatively, navigate to Manufacturing app ‣ Products ‣ Bills of Materials,\
and select the for the subcontracted product.

#### SEE ALSO

For a full overview of configuration, see the [Bill of materials](../basic_setup/bill_configuration.md) documentation.

In the BoM Type field, select the Subcontracting option. Then, add one or\
more subcontractors in the Subcontractors field that appears below.

![The "BoM Type" field on a BoM, configured to manufacture the product using subcontracting.](../../../../_images/bom-type1.png)

Finally, make sure that all necessary components are specified on the Components tab. To\
add a new component, click Add a line, select the component in the Component\
drop-down menu, and specify the required quantity in the Quantity field.

### Configure Components

To configure components for the _Dropship Subcontractor on Order_ route, navigate to each component\
from the by selecting the component's name in the Components tab, and clicking the\
➡️ (right arrow) button to the right of the name.

Alternatively, navigate to each component by going to Inventory app ‣ Products ‣\
Products, and selecting the component.

On the component product form, select the Purchase tab, and add a vendor by clicking\
Add a line, selecting the vendor in the Vendor field, and adding the price\
they sell the product for in the Price field. This is the vendor that sends components\
to the subcontractor, once they are purchased.

Then, click on the Inventory tab and select the Dropship Subcontractor on\
Order route in the Routes section.

Repeat the process for every component that must be dropshipped to the subcontractor.

## Dropship subcontractor on order workflow

The dropship subcontractor on order workflow consists of up to six steps:

1. Create a sales order (SO) for the subcontracted product; doing so creates a _subcontractor_\
   to purchase the product from the subcontractor.
2. Confirm the created in the previous step, or create a new ; doing so creates a request\
   for quotation (RfQ) to purchase the components from the vendor, as well as a receipt order or a\
   dropship order.
3. Confirm the to turn it into a second (_vendor_ ); doing so creates a _Dropship_\
   _Subcontractor_ order.
4. Process the _Dropship Subcontractor_ order once the vendor has sent the components to the\
   subcontractor.
5. Process the receipt once the subcontractor has finished manufacturing the subcontracted product,\
   and shipped it back to the contracting company **OR** process the dropship order to ship the\
   product directly to the end customer.
6. If the workflow was started by creating an , and the finished product is not dropshipped to\
   the end customer, process the delivery order once the product has been shipped to the customer.

The specific number of steps depends on the reason that the subcontracted product is being purchased\
from the subcontractor.

If the reason is to fulfill a specific customer order, the process starts with creating an SO, and\
ends with delivering the product to the customer, or having the subcontractor dropship it to them.

If the reason is to increase quantity of stock on-hand, the process starts with creating a PO, and\
ends with receiving the product into inventory.

### Tạo một SO

It is only necessary to complete this step if the product is being purchased from the subcontractor\
to fulfill a customer need. If the product is being purchased to increase the quantity of stock\
on-hand, move on to the next step.

To create a new , navigate to Sales app ‣ Orders ‣ Orders, and click\
New.

Select the customer in the Customer drop-down menu. Then, click Add a\
product on the Order Lines tab, select the product in the Product drop-down\
menu, and enter a quantity in the Quantity field.

Click Confirm to confirm the , at which point a Purchase smart button\
appears at the top of the page. This is the _subcontractor_ , or the created to purchase\
the subcontracted product from the subcontractor.

#### NOTE

An for the product only creates a _subcontractor_ if the _Replenish on Order (MTO)_\
route is enabled on the product's page, **and** there is no stock of the product on-hand.

If there is stock on-hand, confirming an for the product will instead create a delivery\
order, because Odoo assumes that the is fulfilled using the stock in the warehouse.

This is not the case for subcontracted products that are dropshipped to the end customer. In that\
case, a _subcontractor_ is **always** created, even if there is stock on-hand.

### Process subcontractor PO

If a _subcontractor_ was not created in the previous step, do so now by navigating to\
Purchase app ‣ Orders ‣ Purchase Orders, and clicking New.

Begin filling out the by selecting a subcontractor from the Vendor drop-down menu.

In the Products tab, click Add a product to create a new product line.\
Select a product produced by the subcontractor in the Product field, and enter the\
quantity in the Quantity field.

Finally, click Confirm Order to confirm the _subcontractor_ .

When a is confirmed for a product that requires dropshipping components to a subcontractor, a\
receipt or dropship order is automatically created, and can be accessed from the corresponding\
Receipt or Dropship smart button that appears at the top of the .

![A subcontractor PO for a Dropship Subcontractor on Order product, with a Receipt smart
button at the top of the page.](../../../../_images/subcontractor-po1.png)

In addition, an is created for the components that are purchased from the vendor and sent to\
the subcontractor. However, the **IS NOT** automatically linked to the _subcontractor_ .

Once the is confirmed and becomes a _vendor_ , a _Dropship Subcontractor_ order is\
created. This order is linked to both the _vendor_ and the _subcontractor_ .

### Xác nhận RFQ của nhà cung cấp

To access the created by confirming the _subcontractor_ , navigate to\
Purchase app ‣ Orders ‣ Requests for Quotation. Select the that lists the\
correct vendor in the Vendor field, and the reference number of the receipt that was\
created after confirming _subcontractor_ , in the Source Document field.

On the , the Deliver To field reads Dropship Subcontractor, and the\
Dropship Address field shows the name of the subcontractor to whom components are being\
dropshipped.

Click Confirm Order to turn the into a _vendor_ , and confirm the purchase of\
components from the vendor. After doing so, a Dropship smart button appears at the top\
of the _vendor_ , and a Resupply smart button appears at the top of th&#x65;_&#x73;ubcontractor_ .

![A vendor PO for the components of a Dropship Subcontractor on Order product, with a
Dropship smart button at the top of the page.](../../../../_images/vendor-po.png)

### Process Dropship Subcontractor order

Once the components have been delivered to the subcontractor, navigate to Purchase\
app ‣ Orders ‣ Purchase Orders, and select the _vendor_ or the _subcontractor_ . Then,\
click the Dropship smart button or the Resupply smart button, respectively.

Clicking either button opens the _Dropship Subcontractor_ order. Click the Validate\
button at the top of the order to confirm that the subcontractor has received the components.

### Process receipt or dropship order

Once the subcontractor has manufactured the finished product, navigate to Purchase\
app ‣ Orders ‣ Purchase Orders, and select the _subcontractor_ .

If the subcontracted product should be received into inventory, once the product arrives, click the\
Receive Products button at the top of the _subcontractor_ to open the receipt.\
Then, click Validate at the top of the receipt to register the product into inventory.

Alternatively, select the Receipt smart button at the top of the _subcontractor_ ,\
and click Validate at the top of the receipt.

If the subcontracted product should be dropshipped, select the Dropship button at the\
top of the page to open the dropship order, and click Validate once the subcontractor\
has sent the product to the customer.

### Process delivery order

If the subcontracting workflow was started by a customer , and the finished product was **not**\
dropshipped to the customer, but rather delivered to the contracting company, it is necessary to\
ship the product to the customer, and process the delivery order.

Once the product has been shipped to the customer, navigate to the Sales app, and\
select the . Select the Delivery smart button at the top of the page to open the\
delivery order, and click Validate to confirm that the product has been shipped to the\
customer.
