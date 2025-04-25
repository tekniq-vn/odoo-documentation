# IoT system connection to Odoo

## Khoá học tiên quyết

To connect the IoT system to an Odoo database, the following prerequisites must be met:

- The Internet of Things (IoT) app must be [installed](../apps_modules.md#general-install).
- The IoT system must be connected to the network.
- The computer connecting to Odoo must be on the same network as the IoT system.

#### NOTE
It is recommended to connect the IoT system to a **production** instance, as other types of
environments may cause issues (e.g., with [HTTPS certificate generation](iot_advanced/https_certificate_iot.md#iot-https-certificate-iot-iot-eligibility)).

#### SEE ALSO
- [Hộp IoT](iot_box.md)
- [Windows virtual IoT](windows_iot.md)

## Kết nối

The IoT system can be connected to the Odoo database using a [pairing code](#iot-connect-pairing-code) or a [connection token](#iot-connect-token).

<a id="iot-connect-pairing-code"></a>

### Connection using a pairing code

#### NOTE
- The pairing code is displayed for up to 5 minutes after the IoT system starts. If the code is
  no longer visible, reboot the IoT box or [restart the Windows virtual IoT service](windows_iot.md#iot-windows-iot-restart) to display the pairing code again. Alternatively, connect the IoT
  system to the database using a [connection token](#iot-connect-token).
- The pairing code is not displayed if the IoT system is already connected to a database (e.g.,
  a test database).

1. Retrieve the IoT's system pairing code:

   Hộp IoT

   Connect the IoT box to an external monitor or printer. If the IoT box was already plugged
   prior to this, reboot it by unplugging it for a few seconds and replugging it.
   - External monitor: The pairing code should be displayed on the screen a few minutes after
     rebooting the IoT box.
   - Printer: The pairing code should be printed automatically.

   Windows virtual IoT

   On the computer with the Windows virtual IoT installed, open the IoT system's homepage
   in a web browser by navigating to the URL `http://localhost:8069`. Then, scroll to the
   Pairing Code section.
2. In Odoo, open the IoT app and click Connect.
3. In the Connect an IoT Box popup that opens, enter the Pairing code.
4. Click Pair.

<a id="iot-connect-token"></a>

### Connection using a connection token

1. In Odoo, open the IoT app and click Connect.
2. In the Connect an IoT Box popup that opens, copy the Token.
3. Access the [IoT box's](iot_box.md#iot-iot-box-homepage) or [Windows virtual IoT's](windows_iot.md#iot-windows-iot-homepage) homepage.
4. In the Odoo database connected section, click Configure.
5. Paste the token into the Server Token field and click Connect.

<a id="iot-connect-iot-form"></a>

## IoT system form

Once the IoT system is connected to the Odoo database, it is displayed as a card in the IoT app.
Click the IP address on the card to access the [IoT box's](windows_iot.md#iot-windows-iot-homepage) or
[Windows virtual IoT's](iot_box.md#iot-iot-box-homepage) homepage. Click the card to access the
list of [devices](devices/) connected to the IoT system.

#### NOTE
By default, drivers are automatically [updated](iot_advanced/updating_iot.md#iot-updating-iot-handlers) every time the
IoT system is restarted. To disable automatic updates, uncheck the Automatic drivers
update option.

<a id="iot-connect-troubleshooting"></a>

## Khắc phục sự cố

### The pairing code does not appear or does not work

The [pairing code](#iot-connect-pairing-code) might not be displayed or printed under the
following circumstances:

- The IoT system is not connected to the Internet.
- The IoT system is already connected to an Odoo database.
- The [pairing code](#iot-connect-pairing-code) display time has expired. Reboot the IoT box
  or [restart the Windows virtual IoT service](windows_iot.md#iot-windows-iot-restart) to display the pairing
  code again.
- The IoT system's image version is too old and needs to be [updated](iot_advanced/updating_iot.md#iot-updating-iot-image-code).

### The IoT system is connected but does not appear in the database

The IoT system might take a few minutes to restart when it connects to a database. If it still does
not appear after a few minutes:

- Verify that the IoT system can reach the database and the server does not use a multi-database
  environment.
- Reboot the IoT box or [restart the Windows virtual IoT service](windows_iot.md#iot-windows-iot-restart).

### The IoT box is connected to the Odoo database but cannot be reached

Verify that the IoT system and the computer running the Odoo database are connected to the same
network.

### The Windows virtual IoT's homepage cannot be accessed from another device

Check the [Windows Firewall configuration](windows_iot.md#iot-windows-iot-firewall).

### The IoT system is disconnected from the database after an Odoo upgrade

[Update the IoT system's image](iot_advanced/updating_iot.md#iot-updating-iot-image-code) by flashing the IoT box's card or
[uninstalling the Windows virtual IoT program](windows_iot.md#iot-windows-iot-uninstall) and
[reinstalling](windows_iot.md#iot-windows-iot-installation) the latest package for Windows **matching your
database's version**.
