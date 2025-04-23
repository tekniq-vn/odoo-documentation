# Cấu hình sản phẩm

A group of products in Odoo can be further defined using:

- [Units of measure (UoM)](configure/uom.md): a standard quantity for specifying product amounts
  (e.g., meters, yards, kilograms). Enables automatic conversion between measurement systems in
  Odoo, such as centimeters to feet.
  - *Ex: Purchasing fabric measured in meters but receiving it in yards from a vendor.*
- [Kiện hàng](configure/package.md): A physical container used to group products together, regardless of
  whether they are the same or different.
  - *Ex: A box containing assorted items for delivery, or a storage box of two hundred buttons on a
    shelf.*
- [Gói hàng](configure/packaging.md): groups the *same* products together to receive or sell them in
  specified quantities.
  * _Ex: Cans of soda sold in packs of six, twelve, or twenty-four._

## So sánh

This table provides a detailed comparison of units of measure, packages, and packaging to help\
businesses evaluate which best suits their requirements.

| Tính năng                 | Đơn vị tính                                                                                                         | Kiện hàng                                                                                                                                                                                                                                                                                                               | Gói hàng                                                                                            |
|---------------------------|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Mục đích                  | Standardized measurement for product units (e.g., cm, lb, L)                                                        | Tracks the specific physical container and its contents                                                                                                                                                                                                                                                                 | Groups a fixed number of items together for easier management (e.g., packs of 6, 12 or 24)          |
| Product uniformity        | Defined per product; saved as one  in the database                                                                  | Allows mixed products                                                                                                                                                                                                                                                                                                   | Same products only                                                                                  |
| Linh hoạt                 | Converts between vendor/customer  and database                                                                      | Items can be added or removed from the container                                                                                                                                                                                                                                                                        | Quantities are fixed (e.g., always packs of 6, 12 or 24)                                            |
| Complexity                | Simplest for unit conversions                                                                                       | More complex due to container-level inventory tracking                                                                                                                                                                                                                                                                  | Simpler; suitable for uniform product groupings                                                     |
| Inventory tracking        | Tracks product quantities within the warehouse in the specific  defined in the product<br/>form                     | Tracks package location and contents within the warehouse                                                                                                                                                                                                                                                               | Tracks grouped quantities but not individual items' locations                                       |
| Smooth barcode operations | Không khả dụng                                                                                                      | Requires scanning both the package and individual items for reception. (even if there are 30<br/>items in a package). Can enable the [Move Entire Packages](configure/package.md#inventory-product-management-move-entire-pack) feature to update the package's contained<br/>items' locations, when moving the package | Scanning a packaging barcode automatically records all included units. (e.g. 1 pack = 12<br/>units) |
| Product lookup            | Không khả dụng                                                                                                      | Scanning a product's barcode identifies its typical storage location in the Odoo database                                                                                                                                                                                                                               | Barcode identifies grouped quantity, not storage location                                           |
| Unique barcodes           | Không khả dụng                                                                                                      | Unique barcodes for individual packages (e.g. Pallet #12)                                                                                                                                                                                                                                                               | Barcodes set at the packaging type level (e.g. for a pack of 6)                                     |
| Reusability               | Not applicable                                                                                                      | Can be disposable or reusable, configured via the [Package Use](configure/package.md#inventory-warehouses-storage-cluster-pack) field                                                                                                                                                                                   | Disposable only                                                                                     |
| Container weight          | Not applicable                                                                                                      | Weight of the container itself is included in the *Shipping Weight* field of a package<br/>(Inventory app ‣ Products ‣ Packages)                                                                                                                                                                                        | Weight of the container is defined in the *Package Type* settings                                   |
| Theo dõi số lô/sê-ri      | Requires manual adjustments to track  via lots (See [use case](#inventory-product-management-lots-uom) for details) | Applies only to contained products                                                                                                                                                                                                                                                                                      | Applies to both contained products and the container                                                |
| Custom routes             | Cannot be set                                                                                                       | Cannot be set                                                                                                                                                                                                                                                                                                           | Routes can define specific warehouse paths for a particular packaging type                          |

## Trường hợp vận dụng

After comparing the various features, consider how these businesses, with various inventory\
management and logistics workflows, came to their decision.

### Pallets of items using packaging

Một nhà kho tiếp nhận các lô xà phòng được sắp xếp trên các pallet vật lý, mỗi pallet chứa 96 thanh. Các pallet này được sử dụng để chuyển hàng nội bộ và cũng được bán dưới dạng các đơn vị độc lập. Vì mục đích logistics, trọng lượng của pallet phải được bao gồm trong tổng trọng lượng vận chuyển cho những lần giao hàng nhất định. Ngoài ra, pallet cần có mã vạch để dễ theo dõi và số lượng từng thanh xà phòng phải được bao gồm trong số lượng hàng tồn kho khi pallet được nhận.

After evaluating various options, _product packaging_ was the most suitable solution. Packaging\
enables assigning a barcode to a pallet, identifying it as a "pallet type" containing 96 soap bars.\
This barcode streamlines operations by automatically registering the grouped quantity. Key\
distinctions include:

* **Warehouse tracking limitations**: Odoo tracks only the total quantity, not the number of\
  packagings. For instance, if a pallet with 12 and 24 quantities is received, Odoo records 36\
  quantities, not the pallet details.
* **Packaging barcodes are type-specific, not unique**: Barcodes represent packaging types (e.g.,\
  "pallet of 96 soap bars") but do not uniquely identify individual pallets, such as Pallet #1 or\
  Pallet #2.

### Capture product information using barcode

An Odoo user expects the **Barcode** app to display the typical storage location of a product by\
scanning a barcode for a container.

*Packages* was the most suitable. When the [appropriate setting is enabled](configure/package.md#inventory-warehouses-storage-enable-package), scanning a package barcode displays its contents in
the **Barcode** app.

Packages represent physical containers, enabling detailed tracking of the items they hold.\
Scanning a package provides visibility into its contents and facilitates operations, like inventory\
moves.

### Track different units of measure in storage

A fruit juice distributor tracks multiple for their operations:

* Fruits are purchased in tons.
* Juice is produced and stored in kilograms.
* Small samples are stored in grams for recipe testing.

_Unit of Measure_ was most suitable. Odoo automatically converts tons to kilograms during\
receipts. However, since Odoo tracks only one per product in the database, the company uses\
lot numbers to differentiate :

* LOT1: Grams (g)
* LOT2: Kilograms (kg)

Manual inventory adjustments are required to convert between lots, such as subtracting 1 kg from\
LOT2 to add 1,000 g to LOT1. While functional, this workaround can be time-consuming and prone to\
errors.

* [Loại sản phẩm](configure/type.md)
* [Đơn vị tính](configure/uom.md)
* [Kiện hàng](configure/package.md)
* [Gói hàng](configure/packaging.md)
