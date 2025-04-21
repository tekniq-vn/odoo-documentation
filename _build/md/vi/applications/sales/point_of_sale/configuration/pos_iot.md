# IoT system connection

To connect the POS with an [IoT system](../../../general/iot.md):

1. Make sure both the Point of Sale and Internet of Things (IoT) apps are installed on your
   database.
2. Set up the [Hộp IoT](../../../general/iot/iot_box.md) or
   [Windows virtual IoT](../../../general/iot/windows_iot.md).
3. Connect the peripheral devices to the IoT system:

   | Thiết bị                | Hướng dẫn                                                                                                                                                                                                |
   |-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | Máy in                  | Connect a supported receipt printer to a  port or<br/>to the network, and power it on. Refer to [Orders printing](../restaurant/kitchen_printing.md).                                                    |
   | Cash drawer             | The cash drawer should be connected to the printer with an RJ25 cable.                                                                                                                                   |
   | Barcode scanner         | The barcode scanner must end barcodes with an `ENTER` character (keycode 28) in order for<br/>the barcode scanner to be compatible. This is most likely the barcode scanner's default<br/>configuration. |
   | Cân                     | Connect the scale and power it on. Refer to [Connect a scale](../../../general/iot/devices/scale.md).                                                                                                    |
   | Màn hình cho khách hàng | Connect a screen to the  box to display the  order. Refer to [Connect a screen](../../../general/iot/devices/screen.md).                                                                                 |
   | Payment terminal        | The connection process depends on the terminal. Refer to the [payment terminals<br/>documentation](../payment_methods.md).                                                                               |
4. [Connect the IoT system to your Odoo database](../../../general/iot/connect.md).
5. [Access the POS settings](../configuration.md#configuration-settings) and select your POS, or click the
   vertical ellipsis button (⋮) on a POS card and click Edit. Scroll down
   to the Connected Devices section, enable IoT Box, then select the devices
   to be used for the POS. Click Save.

#### SEE ALSO
- [List of supported hardware](https://www.odoo.com/page/point-of-sale-hardware).
- [IoT documentation](../../../general/iot.md)

<a id="pos-pos-iot-connect-schema"></a>

## Setup example

![A suggested configuration for a point of sale system.](applications/sales/point_of_sale/configuration/pos_iot/pos-connections.png)
