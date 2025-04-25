# GS1 barcode usage

GS1 barcodes provide a standardized format that barcode scanners can interpret. They encode
information in a [specific structure recognized globally](gs1_nomenclature.md#barcode-operations-gs1), allowing
scanners to understand and process supply chain data consistently.

Odoo *Barcode* interprets and prints GS1 barcodes, automating product identification and tracking
in warehouse operations such as receiving, picking, and shipping.

The following sections contain examples of how Odoo uses GS1 barcodes provided by the business to
identify common warehouse items and automate certain warehouse workflows.

#### IMPORTANT
Odoo **does not** create GS1 barcodes. Businesses must purchase a unique Global Trade Item Number
(GTIN) from GS1. Then, they can combine their existing GS1 barcodes with product and supply chain
information (also provided by GS1) to create barcodes in Odoo.

#### SEE ALSO
- [GTIN mua hàng](https://www.gs1.org/standards/get-barcodes)
- [Phép đặt tên GS1](gs1_nomenclature.md#barcode-operations-gs1)

<a id="barcode-operations-gs1-lots"></a>

## Configure barcodes for product, quantity, and lots

To build a GS1 barcode that contains information about a product, its quantities, and the lot
number, the following barcode patterns and Application Identifiers (A.I.) are used:

| Tên      | Tên quy tắc                         |   A.I. | Mẫu mã vạch                      | Field in Odoo                         |
|----------|-------------------------------------|--------|----------------------------------|---------------------------------------|
| Sản phẩm | Global Trade Item Number<br/>(GTIN) |     01 | (01)(\\d{14})                    | Barcode field on product form         |
| Số lượng | Variable count of items             |     30 | (30)(\\d{0,8})                   | Units field on transfer form          |
| Số LOT   | Batch or lot number                 |     10 | (10)([!"%-/0-9:-?A-Z_a-z]{0,20}) | Lot on Detailed Operations<br/>pop-up |

<a id="barcode-operations-lot-setup"></a>

### Cấu hình

First, [enable product tracking using lots](../../inventory/product_management/product_tracking/lots.md#inventory-management-track-products-by-lots) by
navigating to Inventory app ‣ Configuration ‣ Settings, and checking the box
for Lots & Serial Numbers under the Traceability heading.

Sau đó, thiết lập mã vạch cho sản phẩm bằng cách đi đến biểu mẫu sản phẩm trong Ứng dụng Tồn kho ‣ Sản phẩm ‣ Sản phẩm và chọn sản phẩm mong muốn. Trên biểu mẫu sản phẩm, nhấp vào Chỉnh sửa. Sau đó, trong tab Thông tin chung, điền [Mã số sản phẩm thương mại toàn cầu (GTIN)](https://www.gs1.org/standards/get-barcodes) gồm 14 chữ số vào trường Mã vạch, đây là một mã số nhận dạng được công nhận toàn cầu do tổ chức GS1 cung cấp.

#### IMPORTANT
On the product form, omit the  `01` for  product barcode pattern, as it is only used to
encode multiple barcodes into a single barcode that contains detailed information about the
package contents.

<a id="barcode-operations-lot-setup-on-product"></a>

After activating tracking by lots and serial numbers from the settings page, specify that this
feature is to be applied on each product by navigating to the Inventory tab on the
product form. Under Tracking, choose the By Lots radio button.

![Enable product tracking by lots in the "Inventory" tab of the product form.](../../../../.gitbook/assets/track-by-lots.png)

### Scan barcode on receipt

To ensure accurate lot interpretation in Odoo on product barcodes scanned during a receipt
operation, navigate to the Barcode app to manage the [receipt picking process](receipts_deliveries.md#barcode-operations-scan-received-products).

From the Barcode Scanning dashboard, click the Operations button, then the
Receipts button to view the list of vendor receipts to process. Receipts generated from
 are listed, but new receipt operations can also be created directly
through the Barcode app using the Create button.

On the list of receipts, click on the warehouse operation (`WH/IN`) and scan product barcodes and
lot numbers with a barcode scanner. The scanned product then appears on the list. Use the
✏️ (pencil) button to open a window and manually enter quantities for specific lot
numbers.

<a id="barcode-operations-quantity-ex"></a>

## Configure barcode for product and non-unit quantity

To build a GS1 barcode that contains products measured in a non-unit quantity, like kilograms, for
example, the following barcode patterns are used:

| Tên                    | Tên quy tắc                         | A.I.     | Mẫu mã vạch        | Field in Odoo                     |
|------------------------|-------------------------------------|----------|--------------------|-----------------------------------|
| Sản phẩm               | Global Trade Item Number<br/>(GTIN) | 01       | (01)(\\d{14})      | Barcode field<br/>on product form |
| Số lượng theo kilogram | Variable count of items             | 310[0-5] | (310[0-5])(\\d{6}) | Units field on<br/>transfer form  |

### Scan barcode on receipt

To confirm that quantities are correctly interpreted in Odoo, place an order in the *Purchase* app
using the appropriate unit of measure (UoM) for the quantity of products to be
purchased.

#### SEE ALSO
[Simplify vendor unit conversions with UoMs](../../inventory/product_management/configure/uom.md#inventory-product-replenishment-unit-conversion)

After the order is placed, navigate to the Barcode app to [receive the vendor
shipment](receipts_deliveries.md#barcode-operations-scan-received-products).

## Verify product moves

For additional verification, the quantities of received products are also recorded on the
Product Moves report, accessible by navigating to Inventory app ‣
Reporting ‣ Product Moves.

Các mục trên báo cáo Dịch chuyển sản phẩm được nhóm theo sản phẩm theo mặc định. Để xác nhận số lượng đã nhận, nhấp vào một dòng sản phẩm để mở menu thả xuống có thể thu gọn, hiển thị danh sách các *dòng dịch chuyển tồn kho* cho sản phẩm đó. Dòng dịch chuyển tồn kho mới nhất khớp với số tham chiếu nhập kho (VD: `WH/IN/00013`) và số lượng đã xử lý trong quét mã vạch, chứng tỏ rằng các bản ghi đã xử lý trong ứng dụng *Mã vạch* được lưu trữ chính xác trong *Tồn kho*.

![Reception stock move record for 52.1 kg of peaches.](../../../../.gitbook/assets/stock-moves-peach.png)
