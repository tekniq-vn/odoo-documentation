# Yêu cầu báo giá

Odoo's requests for quotation (RFQs) feature in the **Purchase** app standardizes ordering products
from multiple vendors with varying prices and delivery times.

 are documents companies send to vendors requesting product pricing. In Odoo, once the vendor
approves the , the purchase order (PO) is confirmed to align on lead times and pricing.

## Cấu hình

### Sản phẩm

To auto-populate product information and prices on an , configure products by going to
Purchase app ‣ Products ‣ Products. Select an existing product, or create a
new one by selecting New. Doing so opens the product form, where various sales and
purchasing data can be configured.

To configure purchasable products, tick the Can be purchased checkbox, under the product
name. Then, go to the Inventory tab, and enable the Buy route.

![Required configuration for purchasable products.](applications/inventory_and_mrp/purchase/manage_deals/rfq/product-vendor-pricelist-config.png)

<a id="purchase-manage-deals-vendor-pricelist"></a>

### Vendor pricelist

In the Purchase tab of the product form, input the vendor and their price, to have this
information auto-populate on an  each time the product is listed.

#### SEE ALSO
[Import vendor pricelist](../products/pricelist.md)

Default columns include Quantity, Price, and Delivery Lead Time,
but other columns like, Product Variant or Discounts, can also be enabled.

To enable or disable columns, click the <i class="oi oi-settings-adjust"></i> (additional options)
icon on the right side of the header row to reveal a drop-down menu of additional columns that can
be added (or removed) from the Purchase tab.

#### NOTE
Alternatively, prices and delivery lead times for existing products can be added in bulk by
going to Purchase app ‣ Configuration ‣ Vendor Pricelists. Click
New in the top-left corner. In the Vendor section of the pricelist form
that appears, add the product information as it pertains to the vendor.

## Order products

With products and prices configured, follow these steps to create and send  to make purchases
for the company.

### dashboard

To get started, navigate to Purchase app ‣ Orders ‣ Requests for Quotation.

The Requests for Quotation dashboard displays an overview of the company's ,
, and their status. The top of the screen breaks down all  in the company, as well as
individual ones (where the user is the buyer) with a summary of their status.

The top-right corner also provides a quick report of the company's recent purchases by total value,
lead times, and number of  sent.

Additionally, the dashboard includes buttons for:

- To Send: orders in the  stage that have not been sent to the vendor.
- Waiting:  that have been sent by email, and are waiting on vendor confirmation.
- Late:  or  where the Order Deadline has passed.

![RFQ dashboard with orders and order statuses.](applications/inventory_and_mrp/purchase/manage_deals/rfq/rfq-dashboard.png)

In addition to various view options, the Requests for Quotation dashboard provides
Filters and Group By options, accessible via the search bar drop-down menu.

#### SEE ALSO
[Tìm kiếm, lọc, và nhóm bản ghi](../../../essentials/search.md)

### Tạo  mới

To create a new , click the New button on the top-left corner of the
Requests for Quotation dashboard to reveal a new  form.

Start by assigning a Vendor.

The Vendor Reference field points to the sales and delivery order numbers sent by the
vendor. This comes in handy once products are received, and the  needs to be matched to the
delivery order.

The Blanket Order field refers to long-term purchase agreements on recurring orders with
set pricing. To view and configure blanket orders, head to Purchase app ‣ Orders
‣ Purchase agreements.

The Currency can be changed, if purchasing products from a vendor in another country.

Next, configure an Order Deadline, which is the date by which the vendor must confirm
their agreement to supply the products.

#### NOTE
After the Order Deadline is exceeded, the  is marked as late, but the products
can still be ordered.

Expected Arrival is automatically calculated based on the Order Deadline
and vendor lead time. Tick the checkbox for Ask confirmation to ask for signage at
delivery.

With the [Storage Locations feature](../../inventory/warehouses_storage/inventory_management/use_locations.md) activated,
the Deliver to field appears, with options for the order shipment.

Select the receiving warehouse address here, or select Dropship to indicate that this
order is to be shipped directly to the end customer. When Dropship is selected, the
Dropship address field is enabled. Contact names auto-populate here from the
**Contacts** app.

#### Products tab

In the Products tab, add the products to be ordered. Click Add a product,
and type in the product name, or select the item from the drop-down menu.

To create a new product and add it, type the new product name in the Product column,
select Create [product name] from the resulting drop-down menu, and manually add the
unit price. Or, select Create and edit... to be taken to the product form for that new
item.

Catalog can also be selected to navigate to a product menu from the chosen vendor. From
here, products can be added to the cart.

#### NOTE
To make adjustments to products and prices, access the product form by clicking the
<i class="oi oi-arrow-right"></i> (right arrow) icon that becomes available upon hovering over
the Product name.

### Send

Clicking Send by Email reveals a Compose Email pop-up window, with a
Purchase: Request for Quotation template loaded, ready to send to the vendor's email
address (configured in the **Contacts** app).

After crafting the desired message, click Send. Once sent, the  moves to the
RFQ Sent stage.

Clicking Print RFQ downloads a PDF of the .

### Xác nhận đơn hàng

Clicking Confirm Order directly transforms the  into an active .

Once an  is confirmed, it creates a .

On the new , the Order Deadline field changes to Confirmation Date,
which displays the date and time the user confirmed the order.

Depending on the user's chosen configuration in the **Purchase** app settings, a *vendor bill* is
created once products have been ordered or received. For more information, refer to the
documentation on [managing vendor bills](manage.md).

#### NOTE
After an order is placed, clicking Receive Products records the reception of new
products into the database.

#### NOTE
With the **Inventory** app installed, confirming a  automatically creates a receipt document,
with the product information and expected arrival dates automatically populated.

#### SEE ALSO
[Manage vendor bills](manage.md)
