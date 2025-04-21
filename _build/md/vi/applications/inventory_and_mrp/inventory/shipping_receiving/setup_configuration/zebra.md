# Zebra label configuration

In Odoo, labels printed in the Zebra Programming Language (ZPL) file format are designed to fit a
four-by-six inch label. To resize (or reformat) text to fit a variety of  label sizes,
[navigate to the ZPL label view](#inventory-shipping-receiving-zpl-view), and alter the 
code.

#### WARNING
When customizing code in Odoo, please note that upgrading the database to newer versions may
break custom  code. **Customers are responsible for maintaining their custom code**.

Refer to the following sections for explanations, and example code, for frequently requested Zebra
label customizations.

- [Adjust margins](#inventory-shipping-receiving-margin)
- [Enlarge/minimize barcodes](#inventory-shipping-receiving-resize)
- [Rotate elements](#inventory-shipping-receiving-rotate)

<a id="inventory-shipping-receiving-zpl-view"></a>

## Navigate to ZPL label view

To begin customizing a Zebra label in Odoo, turn on [developer mode](../../../../general/developer_mode.md#developer-mode), and on
the main Odoo dashboard, type `Reports`. From the search results that appear in the resulting pop-up
window, choose Settings / Technical / Reporting / Reports to open the
Reports page.

#### NOTE
To manually navigate to the Reports page, go to Settings app ‣
Technical ‣ Reporting: Reports.

![Show global search result for "Reports".](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/search.png)

On the Reports page, in the Search... bar, type `ZPL`, and hit `Enter`.
Upon doing so, Odoo presents a list of available Zebra labels in Odoo. Select the desired Zebra
label from the list to modify it on a separate page.

#### NOTE
Printable ZPL labels in Odoo:

- [số lô/sê-ri](print_on_validation.md#inventory-shipping-receiving-lot-sn-labels)
- loại hoạt động
- package barcode
- [nhãn sản phẩm](print_on_validation.md#inventory-shipping-receiving-product-labels)
- product packaging
- finished product (Odoo *Manufacturing* app required)

Next, click the <i class="fa fa-code"></i> Qweb Views smart button, and choose the desired label
[view](../../../../../developer/reference/user_interface/view_records.md).

![Show Qweb smart button on the Lot and Serial Number (ZPL) report.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/qweb-views.png)

On the resulting view form, go to the Architecture tab to view the  code.

#### IMPORTANT
Để đảm bảo tùy chỉnh **không** bị ghi đè khi cập nhật, hãy nhấp vào biểu tượng <i class="fa fa-bug"></i> (bọ) trên trang chế độ xem. Sau đó, chọn tùy chọn Xem siêu dữ liệu từ menu thả xuống để mở cửa sổ bật lên Xem siêu dữ liệu. Tiếp theo, đảm bảo trường Không cập nhật được đặt thành đúng (thay đổi). Nhấp Đồng ý để thoát khỏi cửa sổ bật lên Xem siêu dữ liệu.

![Architecture tab in the view.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/architecture.png)

<a id="inventory-shipping-receiving-margin"></a>

## Adjust margin

Text gets cut off from standard  labels printed in Odoo when the line exceeds fifty-five
characters. To fit long product names, or lot numbers, on a single line, adjust the margin.

Để bắt đầu, đi đến mã [ZPL của nhãn](#inventory-shipping-receiving-zpl-view) trong tab Kiến trúc. Trong mã  của nhãn sản phẩm, tìm lệnh `^FT`, xác định vị trí bắt đầu để đặt văn bản hoặc yếu tố đồ họa trên nhãn. Hai số ngay sau lệnh `^FT` xác định tọa độ x và y tính bằng điểm () từ các lề trái và trên.

#### IMPORTANT
When customizing lot/serial number labels, look for the `^FO` command, instead of `^FT`.

Mặc định

![Example barcode label with the product name cut off.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/default-margin.png)

**Mã**:

```xml
^XA^CI28
^FT100,80^A0N,40,30^FD[E-COM11] Cabinet with Doors (wood: Cherry, handles: brass)^FS
...
^XZ
```

Modified

![Example barcode label with the product name margin adjusted to the left.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/fixed-margin.png)

**Mã**:

```xml
^XA^CI28
^FT0,80^A0N,40,30^FD[E-COM11] Cabinet with Doors (wood: Cherry, handles: brass)^FS
...
^XZ
```

<a id="inventory-shipping-receiving-resize"></a>

## Resize barcode

To adjust the size of the barcode to scale, begin by navigating to the [ZPL code of the label](#inventory-shipping-receiving-zpl-view) in the Architecture tab. Look for the `^FO`
command (typically in the third line), which is the starting point of the margin for the barcode.

The `^BY` command configures barcode size, and takes three numbers: bar width, width of wide bars
relative to narrow bars, and bar height. By default,  code in Odoo uses `^BY3`, setting the bar
width to three dots, a typical size that is easy for barcode scanners to read.

Mặc định

![Ví dụ nhãn mã vạch.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/normal-barcode.png)

**Mã**:

```xml
^XA^CI28
...
^FO100,160^BY3
...
^XZ
```

Modified

![Example barcode label with the barcode size reduced.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/shrink-barcode.png)

**Mã**:

```xml
^XA^CI28
...
^FO100,160^BY2
...
^XZ
```

<a id="inventory-shipping-receiving-rotate"></a>

## Rotate elements

To rotate elements in , begin by navigating to the [ZPL code of the label](#inventory-shipping-receiving-zpl-view) in the Architecture tab.

The `^BC` command's first parameter ()
defines the rotation of an item, which can be:

- `N`: display normally
- `R`: rotate 90 degrees
- `I`: rotate 180 degrees
- `B`: rotate 270 degrees

Mặc định

![Ví dụ nhãn mã vạch.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/lot.png)

**Mã**:

```xml
^XA^CI28
...
^BCN,100,Y,N,N
...
^XZ
```

Modified

![Example barcode label with the barcode rotated.](applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/zebra/rotate.png)

**Mã**:

```xml
^XA^CI28
...
^BCB,100,Y,N,N
...
^XZ
```
