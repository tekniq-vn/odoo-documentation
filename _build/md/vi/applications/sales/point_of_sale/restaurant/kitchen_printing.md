# Orders printing

Integrating printers in a restaurant or bar's workflow can enhance communication and collaboration
between the front-of-house and back-of-house teams, leading to a more streamlined and efficient
service.

## Cấu hình

<a id="kitchen-printing-enable"></a>

### Enable and create printers

To enable sending orders to a kitchen or bar printer, go to Point of Sale ‣
Configuration ‣ Settings, scroll down to the Restaurant & Bar section, and enable
Kitchen Printers. Type in a name for the printer in the Printers field and
click Create and edit... to open a setup form.

To get a list of all the printers already created or to modify an already created printer, click
--> Printers and select the desired printer to open the setup form.

![settings to enable the kitchen printers](../../../../.gitbook/assets/printers-settings.png)

<a id="kitchen-printing-setup-form"></a>

### Setup form

From the [setup form](#kitchen-printing-enable), select the Printer Type according
to your installation:

- If your printer is connected to an IoT system, select Use a printer connected to the
  IoT Box and select the device in the IoT Device field.
- If you use an Epson printer that does not require an IoT system, select Use an Epson
  printer and enter the printer's IP address in the Epson Printer IP Address field.

#### SEE ALSO
- [IoT system connection to Odoo](../../../general/iot/connect.md)
- [Connect a printer](../../../general/iot/devices/printer.md)
- [Self-signed certificate for ePOS printers](../configuration/epos_ssc.md)

Set your printer to print specific products based on their POS category. To do so, click
Add a line in the Printed Product Categories field. If you leave this field
empty, all products are sent to the printer regardless of their POS category.

![setup form to configure a kitchen printer](../../../../.gitbook/assets/printer-setup.png)

## In đơn hàng

From an open session, start taking an order and click Order to send it to the bar or the
kitchen.

![order button from the POS UI to send orders to a kitchen or a bar](../../../../.gitbook/assets/order-button.png)

#### NOTE
When products can be printed, they appear in green in the cart, and the order button turns green.
