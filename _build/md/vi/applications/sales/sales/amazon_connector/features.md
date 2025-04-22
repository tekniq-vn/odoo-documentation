# Amazon Connector features

The *Amazon Connector* synchronizes orders between Amazon and Odoo, which considerably reduces the
amount of time spent manually entering Amazon orders (from the Amazon Seller account) into Odoo. It
also allows users to accurately keep track of Amazon sales in Odoo.

## Tính năng được hỗ trợ

The Amazon Connector is able to:

- Synchronize (Amazon to Odoo) all confirmed orders (both FBA and FBM), and their order items, which
  include:
  - product name, description, and quantity
  - shipping costs for the product
  - gift wrapping charges
- Create any missing partner related to an order in Odoo (contact types supported: contact and
  delivery address).
- Notify Amazon of confirmed shipment in Odoo (FBM) to get paid.
- Synchronize (Odoo to Amazon) all available quantities of your products (FBM).
- Support multiple seller accounts.
- Support multiple marketplaces per seller account.

The following table lists capabilities provided by Odoo when using the Amazon Connector:

|                          | Fulfilled By Amazon (FBA)                                                                                                                                            | Fulfilled By Merchant (FBM)                                                                                                                                                            |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Đơn hàng**             | Synchronize shipped and<br/>canceled orders.                                                                                                                         | Synchronize unshipped and canceled<br/>orders.                                                                                                                                         |
| **Vận chuyển**           | Shipping cost is computed<br/>by Amazon, and included in<br/>the synchronized order.                                                                                 | Shipping cost is computed by Amazon<br/>and included in the synchronized<br/>orders.                                                                                                   |
| Shipping done by Amazon. | A delivery order is automatically<br/>created in Odoo for each new order.<br/>Once it has been processed in Odoo,<br/>the status is then synchronized in<br/>Amazon. |                                                                                                                                                                                        |
| **Bọc quà**              | Handled by Amazon.                                                                                                                                                   | Cost is computed by Amazon, and<br/>included in the synchronized order.<br/>Gift message is added on a line of<br/>the order and on the delivery order.<br/>Then it is up to the user. |
| **Quản lý tồn kho**      | Managed by Amazon, and<br/>synchronized with a virtual<br/>location to follow it in<br/>Odoo.                                                                        | Managed in Odoo Inventory app, and<br/>synchronized with Amazon.                                                                                                                       |
| **Thông báo giao hàng**  | Handled by Amazon.                                                                                                                                                   | Send by Amazon, based on delivery<br/>status synchronized from Odoo.                                                                                                                   |

#### IMPORTANT
The stock synchronization does **not** currently support selling the same product as  *and* .

At times, when stock is sent for all products, it triggers a stock problem with Amazon, where
Amazon incorrectly thinks the  product has some quantity in
.

As a result, Amazon then sells it as , instead of taking from
their own warehouse. Odoo developers are currently working on resolving this issue to avoid
future discrepancies.

#### NOTE
The Amazon Connector is designed to synchronize the data of sales orders. Other actions, such as
downloading monthly fees reports, handling disputes, or issuing refunds, **must** be managed from
the *Amazon Seller Central*, as usual.

#### WARNING
Kể từ ngày 19 tháng 2 năm 2024, tại các thị trường Bắc Mỹ, các đơn hàng  được tạo bằng *Liên kết Amazon* sẽ không chuyển tên khách hàng sang đơn bán hàng/lệnh giao hàng trong Odoo. Điều này là do Amazon hiện tính toán và nộp thuế bán hàng thay mặt người bán. Nói cách khác, thông tin nhận dạng cá nhân của khách hàng sẽ không còn được truyền tải đến người bán sau khi đơn hàng  được tạo.

<a id="amazon-supported-marketplaces"></a>

## Marketplace được hỗ trợ

If a marketplace is not listed in your Amazon marketplaces, it's possible to [add a new
marketplace](applications/sales/sales/amazon_connector/setup.md#amazon-add-new-marketplace).

|        | **North America region**   |
|--------|----------------------------|
| Canada | Amazon.ca                  |
| Mexico | Amazon.com.mx              |
| Hoa Kỳ | Amazon.com                 |

|                | **Khu vực Châu Âu**   |
|----------------|-----------------------|
| Đức            | Amazon.de             |
| Tây Ban Nha    | Amazon.es             |
| Pháp           | Amazon.fr             |
| Vương quốc Anh | Amazon.co.uk          |
| Ý              | Amazon.it             |
| Hà Lan         | Amazon.nl             |

#### SEE ALSO
- [Amazon Connector configuration](applications/sales/sales/amazon_connector/setup.md)
- [Amazon order management](applications/sales/sales/amazon_connector/manage.md)
