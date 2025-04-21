# Connect a scale

#### IMPORTANT
- In EU member states, [certification is legally required](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.096.01.0107.01.ENG)
  to use a scale as an integrated device.
- Odoo is not certified in several countries, including France, Germany, and Switzerland. If you
  reside in one of these countries, you can still use a scale but without integration into your
  Odoo database. Alternatively, you can acquire a *non-integrated* certified scale that prints
  certified labels, which can then be scanned into your Odoo database.

Để kết nối cân với hệ thống IoT, sử dụng cáp USB. Trong một số trường hợp, có thể cần bộ chuyển đổi từ cổng nối tiếp sang USB để hoàn tất kết nối. Nếu cân tương thích với hệ thống IoT <[https://www.odoo.com/page/iot-hardware](https://www.odoo.com/page/iot-hardware)>_, không cần thiết lập bổ sung; cân sẽ tự động được nhận diện ngay khi kết nối. Nếu cân không được nhận diện, hãy khởi động lại hộp IoT hoặc [khởi động lại dịch vụ IoT ảo trên Windows](../windows_iot.md#iot-windows-iot-restart) và [cập nhật driver của cân](../iot_advanced/updating_iot.md#iot-updating-iot-handlers).

#### NOTE
If the scale still does not function after updating the drivers, it might not be [compatible with
the Odoo IoT system](https://www.odoo.com/page/iot-hardware). In such cases, a different scale
must be used.

Once the scale is connected to the IoT system, follow these steps to configure it in the POS
settings:

1. [Access the POS settings](../../../sales/point_of_sale/configuration.md#configuration-settings) and select your POS, or click the
   vertical ellipsis button (⋮) on a POS card and click Edit.
2. Scroll down to the Connected Devices section and enable IoT Box.
3. Select the scale in the Electronic Scale field.
4. Nhấp Lưu.

#### SEE ALSO
[Connect an IoT system to a POS](../../../sales/point_of_sale/configuration/pos_iot.md)

The scale is then available in all the [POS's sessions](../../../sales/point_of_sale.md).
If a product is configured with a price per weight, selecting it on the PoS screen opens
the scale popup. The cashier can then weigh the product to automatically add the correct price to
the cart.

![Electronic Scale dashboard view when no items are being weighed.](scale/scale-view.png)

## Ariva S scales

For Ariva S series scales (manufactured by Mettler-Toledo, LLC.) to function with IoT systems, a
specific setting must be modified, and a dedicated Mettler USB-to-proprietary RJ45 cable is required.

#### IMPORTANT
The official Mettler USB-to-RJ45 cable (Mettler part number 72256236) must be used. Contact
Mettler or a partner to purchase an authentic cable. **No other** cable works for this
configuration.

To configure the Ariva S scale for IoT system recognition, refer to page 17 of [Mettler's Setup
Guide for Ariva S series scales](https://www.mt.com/dam/RET_DOCS/Ariv.pdf) and follow these steps:

1. Hold the **>T<** button for eight seconds, or until CONF appears.
2. Press **>T<** until GRP 3 appears, then press **>0<** to confirm.
3. At step 3.1, make sure the value is set to 1 (USB Virtual COM ports) by
   pressing **>T<** to cycle through the options.
4. Press **>0<** until 3.6 (if available, otherwise skip the next step).
5. At step 3.6, make sure the value is set to 3 (8217 Mettler-Toledo (WO))
   by pressing **>T<** to cycle through the options.
6. Press **>0<** (multiple times if necessary) until GRP 4 appears.
7. Press **>T<** until EXIT appears.

   #### IMPORTANT
   Do **not** make any other changes unless otherwise needed.
8. Press **>0<**.
9. Press **>0<** again to SAVE; the scale restarts.
10. Reboot the IoT box or [restart the Windows virtual IoT service](../windows_iot.md#iot-windows-iot-restart).
    The scale should then appear as `Toledo 8217`, as opposed to the previous display, where it
    appeared as `Adam Equipment Serial`.
