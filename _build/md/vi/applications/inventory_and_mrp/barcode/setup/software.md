# Activate the Barcodes in Odoo

<a id="inventory-barcode-software"></a>

The barcode scanning features can save you a lot of time usually lost
switching between the keyboard, the mouse and the scanner. Properly
attributing barcodes to products, pickings locations, etc. allows you to
work more efficiently by controlling the software almost exclusively
with the barcode scanner.

## Cấu hình

To use this feature, you first need to activate the *Barcode*
functionality via Inventory ‣ Settings ‣ Barcode Scanner. Once you
have ticked the feature, you can hit save.

![image](applications/inventory_and_mrp/barcode/setup/software/software_01.png)

## Set Product Barcodes

You can easily assign barcodes to your different products via the
*Inventory* app. To do so, go to Settings ‣ Configure Products Barcodes.

![image](applications/inventory_and_mrp/barcode/setup/software/software_02.png)

Then, you have the possibility to assign barcodes to your products
directly at creation on the product form.

![image](applications/inventory_and_mrp/barcode/setup/software/software_03.png)![image](applications/inventory_and_mrp/barcode/setup/software/software_04.png)

#### NOTE
Be careful to add barcodes directly on the product variants and not on
the template product. Otherwise, you won’t be able to differentiate
them.

<a id="barcode-setup-location"></a>

## Set Locations Barcodes

If you manage multiple locations, you will find useful to attribute a
barcode to each location and stick it on the location. You can configure
the locations barcodes in Inventory ‣ Configuration ‣ Locations.

![image](applications/inventory_and_mrp/barcode/setup/software/software_05.png)![image](applications/inventory_and_mrp/barcode/setup/software/software_06.png)

#### NOTE
You can easily print the barcode you allocate to the locations via the
*Print* menu.

## Định dạng mã vạch

Hầu hết các sản phẩm bán lẻ sử dụng mã vạch EAN-13, còn được gọi là GTIN (Số định danh thương mại toàn cầu). GTIN được các công ty sử dụng để định danh duy nhất cho sản phẩm và dịch vụ của mình. Mặc dù GTIN và UPC thường được dùng thay thế cho nhau, GTIN đề cập đến dãy số mà mã vạch biểu thị, trong khi UPC đề cập đến chính mã vạch đó. Thông tin thêm về GTIN có thể được tìm thấy trên trang web của GS1.

Để tạo GTIN cho các mặt hàng, một công ty phải có Tiền tố công ty GS1. Tiền tố này là số sẽ xuất hiện ở đầu mỗi GTIN và xác định công ty là chủ sở hữu của mã vạch cũng như các sản phẩm được gán mã đó. Để tìm hiểu thêm về Tiền tố công ty GS1 hoặc mua giấy phép cho một tiền tố, hãy truy cập trang Tiền tố công ty GS1.

Odoo users are able to use GTIN barcodes to identify their products. However, since Odoo supports
any numeric string as a barcode, it is also possible to define a custom barcode for internal use.
