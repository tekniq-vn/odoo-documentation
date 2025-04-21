# Màn hình cho khách hàng

The **customer display** feature provides customers with real-time checkout updates on a secondary
display.

![màn hình khách hàng](applications/sales/point_of_sale/shop/customer_display/display.png)

## Cấu hình

Depending on your POS setup, the feature can be displayed [locally on a secondary screen](#customer-display-local) or on [another monitor connected to an IoT Box](#customer-display-iot).

To activate the feature, go to the POS settings, scroll down to the Connected Devices
section, and tick the Customer Display checkbox.

![customer display setting checkbox](applications/sales/point_of_sale/shop/customer_display/feature-setting.png)

<a id="customer-display-local"></a>

### Local

Connect a second screen to your POS and [open a POS session](../../point_of_sale.md#pos-session-start). Then, click
Customer Screen to open a new window to drag and drop onto the second screen.

<a id="customer-display-iot"></a>

### IoT system

Connect an IoT box to your database and the second screen to the IoT box. Then, go to
Point of Sale ‣ Configuration ‣ Settings, scroll down to the
Connected Devices section, tick the IoT Box checkbox, and select the second
monitor in the Customer Display field.

![iot setting to connect a customer display](applications/sales/point_of_sale/shop/customer_display/iot-setting.png)

#### NOTE
Both devices need to be connected to the same local network.

#### SEE ALSO
[IoT system connection](../configuration/pos_iot.md)
