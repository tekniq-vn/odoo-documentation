# Third-party shipping carriers

<a id="inventory-shipping-third-party"></a>

Users can link third-party shipping carriers to Odoo databases, in order to verify carriers'
delivery to specific addresses, [automatically calculate shipping costs](../setup_configuration.md), and [generate shipping labels](labels.md).

In Odoo, shipping carriers can be applied to a sales order (SO), invoice, or delivery order. For
tips on resolving common issues when configuring shipping connectors, skip to the
[Troubleshooting](#inventory-shipping-receiving-third-party-troubles) section.

#### SEE ALSO
- [Tích hợp DHL](dhl_credentials.md)
- [Sendcloud integration](sendcloud_shipping.md)
- [Tích hợp UPS](ups_credentials.md)

The following is a list of available shipping connectors in Odoo:

| Đơn vị vận chuyển                    | Region availability                         |
|--------------------------------------|---------------------------------------------|
| [FedEx](fedex.md)                    | Tất cả                                      |
| [DHL Express](dhl_credentials.md)    | Tất cả                                      |
| [UPS](ups_credentials.md)            | Tất cả                                      |
| US Postal Service                    | Hoa Kỳ                                      |
| [Sendcloud](sendcloud_shipping.md)   | Some European countries (see details below) |
| [Bpost](bpost.md)                    | Bỉ                                          |
| Easypost                             | Bắc Mỹ                                      |
| Shiprocket                           | Ấn Độ                                       |
| [Starshipit](starshipit_shipping.md) | Australia and New Zealand                   |

#### IMPORTANT
Other services from DHL are **not** supported.

Sendcloud currently supports shipping **from** Austria, Belgium, France, Germany, Italy, the
Netherlands, Spain, and the United Kingdom, and **to** any European country.

## Cấu hình

To ensure proper setup of a third-party shipping carrier with Odoo, follow these steps:

1. [Install the shipping connector](#inventory-shipping-receiving-shipping-connector).
2. [Set up delivery method](#inventory-shipping-receiving-configure-delivery-method).
3. [Activate production environment](#inventory-shipping-receiving-production-env).
4. [Cấu hình kho hàng](#inventory-shipping-receiving-configure-source-address).
5. [Specify weight of products](#inventory-shipping-receiving-configure-weight).

<a id="inventory-shipping-receiving-shipping-connector"></a>

### Install shipping connector

To install shipping connectors, go to Inventory app ‣ Configuration ‣ Settings.

Under the Shipping Connectors section, tick the third-party shipping carrier's checkbox
to install it. Multiple third-party shipping connectors can be selected at once. Then, click
Save.

#### NOTE
[Delivery methods](../setup_configuration.md) can also be integrated with operations in the
*Sales*, *eCommerce*, and *Website* apps. To install, refer to the [install apps and modules](../../../../general/apps_modules.md#general-install) documentation.

![Options of available shipping connectors in Odoo.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/shipping-connectors.png)

<a id="inventory-shipping-receiving-configure-delivery-method"></a>

### Phương thức giao hàng

To configure the API credentials, and activate the shipping carrier, begin by going to
Inventory app ‣ Configuration ‣ Shipping Methods, and select the desired
delivery method.

#### NOTE
The list often includes **two** delivery methods from the same Provider: one for
international shipping and one for domestic shipping.

Additional delivery methods can be created for specific purposes, such as [packaging](../../product_management/configure/packaging.md).

#### SEE ALSO
[Configure delivery methods](../setup_configuration.md)

#### NOTE
Ensure the delivery method is published when it should be available on the *Website* app. To
publish a delivery method on the website, click the desired delivery method, then click the
Unpublished smart button. Doing so changes that smart button to read:
Published.

<a id="inventory-shipping-receiving-shipping-methods-details"></a>

The Shipping Method page contains details about the provider, including:

- Shipping Method (*Required field*): the name of the delivery method (e.g. `FedEx US`,
  `FedEx EU`, etc.).
- Website: configure shipping methods for an *eCommerce* page that is connected to a
  specific website in the database. Select the applicable website from the drop-down menu, or leave
  it blank to apply the method to all web pages.
- Provider (*Required field*): choose the third-party delivery service, like FedEx. Upon
  choosing a provider, the Integration Level, Invoicing Policy and
  Insurance Percentage fields become available.
- Integration Level: choose Get Rate to simply get an [estimated
  shipment cost](#inventory-shipping-receiving-third-party-so) on an  or invoice.

  #### IMPORTANT
  Select Get Rate and Create Shipment to also [generate shipping labels](labels.md).
- Company: if the shipping method should apply to a specific company, select it from the
  drop-down menu. Leave the field blank to apply the method to all companies.
- Delivery Product (*Required field*): the delivery charge name that is added to the
   or invoice.
- Invoicing Policy: select and calculate an Estimated cost of shipping
  directly from the shipping carrier. If the Real cost of shipping is wanted instead,
  refer to [Invoice real shipping costs](invoicing.md) document.
- Margin on Rate: specify an additional percentage amount added to the base shipping
  rate to cover extra costs, such as handling fees, packaging materials, exchange rates, etc.
- Free if order amount is above: enables free shipping for orders surpassing a specified
  amount entered in the corresponding Amount field.
- Insurance Percentage: specify a percentage amount of the shipping costs reimbursed to
  the senders if the package is lost or stolen in transit.

![Screenshot of a FedEx shipping method.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/fedex.png)

In the Configuration tab, fill out the API credential fields (e.g. API key, password,
account number, etc.). Depending on the third-party shipping carrier chosen in the
Provider field, the Configuration tab will contain different required
fields. For more details about configuring specific carriers' credentials, refer to the following
documents:

#### SEE ALSO
- [Thông tin đăng nhập DHL](dhl_credentials.md)
- [Thông tin đăng nhập Sendcloud](sendcloud_shipping.md)
- [Thông tin đăng nhập UPS](ups_credentials.md)

<a id="inventory-shipping-receiving-production-env"></a>

### Production environment

With the delivery method details configured, click the Test Environment smart button to
set it to Production Environment.

#### WARNING
Setting the delivery method to Production creates **real** shipping labels, and users
are at risk of being charged through their carrier account (e.g. UPS, FedEx, etc.) **before**
users charge customers for shipping. Verify all configurations are correct before launching the
delivery method to Production.

![Show the "Test Environment" smart button.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/production.png)

<a id="inventory-shipping-receiving-configure-source-address"></a>

### Warehouse configuration

Ensure the warehouse's Address (including ZIP code) and Phone number are
entered accurately. To do that, go to Inventory app ‣ Configuration ‣
Warehouses, and select the desired warehouse.

On the warehouse configuration page, open the warehouse contact page by clicking the
Company field.

![Highlight the "Company" field.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/internal-link.png)

Verify that the Address and Phone number are correct, as they are required
for the shipping connector to work properly.

![Show company address and phone number.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/company.png)

<a id="inventory-shipping-receiving-configure-weight"></a>

### Khối lượng sản phẩm

For the carrier integration to work properly, specify the weight of products by going to
Inventory app ‣ Products ‣ Products, and selecting the desired product.

Then, switch to the Inventory tab, and define the Weight of the product in
the Logistics section.

![Display the "Weight" field in the Inventory tab of the product form.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/product-weight.png)

<a id="inventory-shipping-receiving-apply-third-party-carrier"></a>

## Apply third-party shipping carrier

Shipping carriers can be applied on a , invoice, or delivery order.

After configuring the third-party carrier's [delivery method](#inventory-shipping-receiving-configure-delivery-method) in Odoo, create or navigate to a quotation
by going to Sales app ‣ Orders ‣ Quotations.

<a id="inventory-shipping-receiving-third-party-so"></a>

### Đơn bán hàng

Để chỉ định đơn vị vận chuyển bên thứ ba và nhận ước tính chi phí vận chuyển, hãy bắt đầu bằng cách truy cập Ứng dụng Bán hàng ‣ Đơn hàng ‣ Báo giá. Tạo hoặc chọn một báo giá hiện có, sau đó thêm chi phí vận chuyển thông qua đơn vị vận chuyển bên thứ ba vào báo giá bằng cách nhấp vào nút Thêm vận chuyển ở góc dưới bên phải của tab Chi tiết đơn hàng.

![Show the "Add shipping" button at the bottom of a quotation.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/add-shipping.png)

In the resulting Add a shipping method pop-up window, select the intended carrier from
the Shipping Method drop-down menu. The Cost field is automatically filled
based on:

- the amount specified in the Total Order Weight field (if it is not provided, the sum
  of [product weights](#inventory-shipping-receiving-configure-weight) in the order is used)
- the distance between the warehouse's [source address](#inventory-shipping-receiving-configure-source-address) and the customer's address.

<a id="inventory-shipping-receiving-third-party-rate"></a>

After selecting a third-party provider in the Shipping Method field, click
Get Rate in the Add a shipping method pop-up window to get the estimated
cost through the shipping connector. Then, click the Add button to add the delivery
charge to the  or invoice.

#### SEE ALSO
[Charge customers for shipping after product delivery](invoicing.md)

<a id="inventory-shipping-receiving-third-party-do"></a>

### Delivery order

For users making shipments without installing the *Sales* app, assign the shipping carrier to the
delivery order, by first going to the Inventory app. Then, from the
Inventory Overview dashboard, select the Delivery Orders operation type, and
choose the desired delivery order that is not already marked as Done or
Cancelled.

In the Additional info tab, set the Carrier field to the desired third-party
shipping carrier. When the delivery method is set to [production mode](#inventory-shipping-receiving-configure-delivery-method), a Tracking Reference is
provided.

#### SEE ALSO
[Generate shipping labels](labels.md)

![Show the delivery order's "Additional info" tab.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/delivery-info.png)

<a id="inventory-shipping-receiving-third-party-troubles"></a>

## Khắc phục sự cố

Since shipping connectors can sometimes be complex to set up, here are some checks to try when
things are not working as expected:

1. Ensure the [warehouse information](#inventory-shipping-receiving-configure-source-address)
   (e.g., address and phone number) in Odoo is correct **and** matches the records saved in the
   shipping provider's website.
2. Verify that the [package type](../../product_management/configure/package.md#inventory-warehouses-storage-package-type) and parameters
   are valid for the shipping carrier. To check, ensure the shipment can be directly created on the
   shipping carrier's website.
3. When encountering a price mismatch between Odoo's estimated cost and the provider's charge, first
   ensure the delivery method is set to [production environment](#inventory-shipping-receiving-production-env).

   Then, create the shipment in both the carrier's website and Odoo, and verify the prices are the
   same across Odoo, the shipping provider, and in the *debug logs*.

### Nhật ký gỡ lỗi

Track shipping data inconsistencies by activating debug logging. To do that, go to the delivery
method's configuration page (Inventory app ‣ Configuration ‣ Shipping
Method), and select the desired shipping method. Click the No Debugging smart button to
activate Debug Requests.

![Show the "No Debug" smart button.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/no-debug.png)

With Debug Requests activated, each time the shipping connector is used to estimate the
cost of shipping, records are saved in the Logging report. To access the report, turn on
[developer mode](../../../../general/developer_mode.md#developer-mode), and go to Settings app ‣ Technical ‣
Database Structure section ‣ Logging.

#### NOTE
Logs are created for a shipping method each time the [Get Rate](#inventory-shipping-receiving-third-party-rate) button is clicked on 
and invoices, **and** when a customer adds the shipping carrier to their order through the
*Website* app.

![Show how to find the "Logging" option from the "Technical" menu.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/log.png)

Click the *HTTP request* line item to open a detailed page, and verify the correct information is
sent from Odoo to the shipping carrier. In the *HTTP response*, verify that the same information is
received.

![Show debug request history in Settings > Technical > Logging.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper/logging.png)
