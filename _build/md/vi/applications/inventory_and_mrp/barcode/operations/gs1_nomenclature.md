# GS1 barcode nomenclature

[GS1 nomenclature](https://www.gs1us.org/) consolidates various product and supply chain data into
a single barcode. Odoo takes in [unique Global Trade Item Numbers](https://www.gs1.org/standards/get-barcodes) (GTIN), purchased by businesses, to enable global
shipping, sales, and eCommerce product listing.

Configure GS1 nomenclature to scan barcodes of sealed boxes and identify essential product
information, such as , lot number, quantity information, and more.

#### IMPORTANT
 are unique product identification that **must** be [purchased from GS1](https://www.gs1.org/standards/get-barcodes) to use GS1 barcodes.

#### SEE ALSO
- [All GS1 barcodes](https://www.gs1.org/standards/barcodes/application-identifiers)
- [Odoo's default GS1 rules](#barcode-operations-default-gs1-nomenclature-list)
- [Why's my barcode not working?](#barcode-operations-troubleshooting)

<a id="barcode-operations-set-up-barcode-nomenclature"></a>

## Set up barcode nomenclature

To use GS1 nomenclature, navigate to the Inventory app ‣ Configuration ‣
Settings. Then under the Barcode section, check the Barcode Scanner box.
Next, select Barcode Nomenclature ‣ Default GS1 Nomenclature from the default
barcode nomenclature options.

![Choose GS1 from dropdown and click the external link to see the list of GS1 rules.](gs1_nomenclature/setup-gs1-nomenclature.png)

The list of GS1 *rules* and *barcode patterns* Odoo supports by default is accessible by clicking
the ➡️ (arrow) icon to the right of the Barcode Nomenclature selection.

In the Open: Nomenclature pop-up table, view and edit the GS1 Rule Names
available in Odoo. The table contains all the information that can be condensed with a GS1 barcode,
along with the corresponding Barcode Pattern.

<a id="barcode-operations-create-gs1-barcode"></a>

## Use GS1 barcodes in Odoo

Để nhận dạng sản phẩm bằng mã vạch GS1 trong Odoo, doanh nghiệp cần có một [GTIN duy nhất](https://www.gs1.org/standards/get-barcodes) làm định danh sản phẩm phân biệt quốc tế được mua từ GS1.  này được kết hợp với thông tin sản phẩm cụ thể theo *mẫu mã vạch* được GS1 quy định. Cách sắp xếp chữ số và chữ cái trong mẫu mã vạch phải tuân thủ quy ước GS1 để hệ thống toàn cầu có thể đọc chính xác dọc theo chuỗi cung ứng.

Mỗi mã vạch bắt đầu bằng một [mã ứng dụng](https://www.gs1.org/standards/barcodes/application-identifiers) (A.I.) gồm 2-4 chữ số. Tiền tố bắt buộc này cho biết loại thông tin mà mã vạch chứa đựng. Odoo tuân thủ các quy tắc GS1 để nhận diện thông tin, như được mô tả chi tiết trong [danh sách quy tắc GS1 mặc định](#barcode-operations-default-gs1-nomenclature-list). Việc bao gồm  phù hợp từ danh sách cho phép Odoo diễn giải chính xác các mã vạch GS1. Trong khi hầu hết các mẫu mã vạch yêu cầu độ dài cố định, thì một số loại như số lô và số sê-ri có độ dài linh hoạt.

Refer to the [GS1 nomenclature list](#barcode-operations-default-gs1-nomenclature-list) to see
a comprehensive list of all barcode patterns and rules to follow. Otherwise, refer to [this
GS1 usage doc](gs1_usage.md#barcode-operations-gs1-usage) for specific examples of combining  to product
information and configuring the workflow.

#### SEE ALSO
- [Lots workflow](gs1_usage.md#barcode-operations-gs1-lots)
- [Non-unit quantities workflow](gs1_usage.md#barcode-operations-quantity-ex)

<a id="barcode-operations-create-new-rules"></a>

### Tạo quy tắc

GS1 rules are a specific format of information contained in the barcode, beginning with an  and
containing a defined length of characters. Scanning GS1 barcodes from the [default GS1 list](#barcode-operations-default-gs1-nomenclature-list) auto-fills corresponding data in the Odoo
database.

Adding GS1 barcode rules in Odoo ensures accurate interpretation of unique, non-standard GS1
formats.

To do so, begin by turning on [developer mode](../../../general/developer_mode.md#developer-mode) and navigating to the
Barcode Nomenclatures list in Inventory app ‣ Configuration ‣
Barcode Nomenclatures. Then, select the Default GS1 Nomenclature list item.

Trên trang Phép đặt tên GS1 mặc định, chọn Thêm một dòng ở cuối bảng, sau đó một cửa sổ để tạo quy tắc mới sẽ mở ra. Trường Tên quy tắc được sử dụng nội bộ để xác định xem mã vạch biểu thị nội dung gì. Loại mã vạch là các phân loại thông tin khác nhau mà hệ thống có thể hiểu được (VD: sản phẩm, số lượng, sử dụng tốt nhất trước ngày, kiện hàng, phiếu giảm giá). Trình tự biểu thị mức độ ưu tiên của quy tắc, nghĩa là giá trị càng nhỏ thì quy tắc xuất hiện càng cao trên bảng. Odoo tuân theo thứ tự tuần tự của bảng này và sẽ sử dụng quy tắc so khớp đầu tiên dựa trên trình tự. Mẫu mã vạch là cách hệ thống nhận dạng trình tự các chữ cái hoặc số để đưa thông tin về sản phẩm vào.

After filling in the information, click the Save & New button to make another rule or
click Save & Close to save and return to the table of rules.

<a id="barcode-operations-troubleshooting"></a>

## Khắc phục sự cố mã vạch

Since GS1 barcodes are challenging to work with, here are some checks to try when the barcodes are
not working as expected:

1. Ensure that the Barcode Nomenclature setting is set as Default GS1
   Nomenclature. Jump to the [nomenclature setup section](#barcode-operations-set-up-barcode-nomenclature) for more details.
2. Ensure that the fields scanned in the barcode are enabled in Odoo. For example, to scan a barcode
   containing lots and serial numbers, make sure the Lots & Serial Numbers feature is
   enabled in [Odoo's settings](gs1_usage.md#barcode-operations-lot-setup) and [on the product](gs1_usage.md#barcode-operations-lot-setup-on-product).
3. Omit punctuation such as parentheses `()` or brackets `[]` between the  and the barcode sequence. These are typically used in examples for ease of reading
   and should **not** be included in the final barcode. For more details on building GS1 barcodes,
   go to [this section](#barcode-operations-create-gs1-barcode).
4. When a single barcode contains multiple encoded fields, Odoo requires all rules to be listed in
   the barcode nomenclature for Odoo to read the barcode. [This section](#barcode-operations-create-new-rules) details how to add new rules in the barcode nomenclature.
5. Test barcodes containing multiple encoded fields, piece by piece, to figure out which field is
   causing the issue.
6. After diagnosing the encoded field is unknown, [add new rules](#barcode-operations-create-new-rules) to Odoo's default list to recognize GS1 barcodes with
   unique specifications.

   #### IMPORTANT
   While the new field will be read, the information won't link to an existing field in Odoo
   without developer customizations. However, adding new rules is necessary to ensure the rest of
   the fields in the barcode are interpreted correctly.

<a id="barcode-operations-default-gs1-nomenclature-list"></a>

## GS1 nomenclature list

The table below contains Odoo's default list of GS1 rules. Barcode patterns are written in regular
expressions. Only the first three rules require a [check digit](https://www.gs1.org/services/check-digit-calculator) as the final character.

| Tên quy tắc                              | Loại                        | Mẫu mã vạch                           | Loại nội dung GS1   | Trường Odoo                             |
|------------------------------------------|-----------------------------|---------------------------------------|---------------------|-----------------------------------------|
| Serial Shipping Container Code           | Kiện hàng                   | (00)(\\d{18})                         | Mã dạng số          | Tên hiện hàng                           |
| Global Trade Item Number (GTIN)          | Đơn vị sản phẩm             | (01)(\\d{14})                         | Mã dạng số          | Barcode<br/>field on product form       |
| GTIN of contained trade items            | Đơn vị sản phẩm             | (02)(\\d{14})                         | Mã dạng số          | Gói hàng                                |
| Ship to / Deliver to global<br/>location | Vị trí đích                 | (410)(\\d{13})                        | Mã dạng số          | Vị trí đích                             |
| Ship / Deliver for forward               | Vị trí đích                 | (413)(\\d{13})                        | Mã dạng số          | Vị trí nguồn                            |
| I.D. of a physical location              | Vị trí                      | (414)(\\d{13})                        | Mã dạng số          | Vị trí                                  |
| Batch or lot number                      | Lô                          | (10)<br/>([!"%-/0-9:-?A-Z_a-z]{0,20}) | Tên bằng chữ và số  | Lô                                      |
| Số sê-ri                                 | Lô                          | (21)<br/>([!"%-/0-9:-?A-Z_a-z]{0,20}) | Tên bằng chữ và số  | Số sê-ri                                |
| Ngày đóng gói (YYMMDD)                   | Ngày đóng gói               | (13)(\\d{6})                          | Ngày                | Ngày đóng gói                           |
| Best before date (YYMMDD)                | Sử dụng tốt nhất trước ngày | (15)(\\d{6})                          | Ngày                | Sử dụng tốt nhất trước ngày             |
| Ngày hết hạn (YYMMDD)                    | Ngày hết hạn                | (17)(\\d{6})                          | Ngày                | Ngày hết hạn                            |
| Variable count of items                  | Số lượng                    | (30)(\\d{0,8})                        | Số đo               | ĐVT: Đơn vị                             |
| Count of trade items                     | Số lượng                    | (37)(\\d{0,8})                        | Số đo               | Qty in units for<br/>containers (AI 02) |
| Net weight: kilograms (kg)               | Số lượng                    | (310[0-5])(\\d{6})                    | Số đo               | SL theo kg                              |
| Length in meters (m)                     | Số lượng                    | (311[0-5])(\\d{6})                    | Số đo               | SL theo m                               |
| Net volume: liters (L)                   | Số lượng                    | (315[0-5])(\\d{6})                    | Số đo               | SL theo L                               |
| Net volume: cubic meters (m<sub>3</sub>) | Số lượng                    | (316[0-5])(\\d{6})                    | Số đo               | Qty in m<sub>3</sub>                    |
| Length in inches (in)                    | Số lượng                    | (321[0-5])(\\d{6})                    | Số đo               | SL theo inch                            |
| Net weight/volume: ounces (oz)           | Số lượng                    | (357[0-5])(\\d{6})                    | Số đo               | SL theo oz                              |
| Net volume: cubic feet (ft<sub>3</sub>)  | Số lượng                    | (365[0-5])(\\d{6})                    | Số đo               | Qty in ft<sub>3</sub>                   |
| Kiểu đóng gói                            | Kiểu đóng gói               | (91)<br/>([!"%-/0-9:-?A-Z_a-z]{0,90}) | Tên bằng chữ và số  | Loại kiện hàng                          |
