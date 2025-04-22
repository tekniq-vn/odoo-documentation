# Secure connection (HTTPS)

If **Direct Devices** is enabled in a Point of Sale settings (for example, if you use an [ePos
printer](applications/sales/point_of_sale/configuration/epos_printers.md)), HTTP becomes the default protocol.

## Force your Point of Sale to use a secure connection (HTTPS)

Add a new **key** in the **System Parameters** to force your Point of Sale to use a secure
connection with the HTTPS protocol.

To do so, activate the [developer mode](applications/general/developer_mode.md#developer-mode), go to Settings ‣
Technical ‣ Parameters ‣ System Parameters, then create a new parameter, add the following
values and click on *Save*.

- **Khoá**: `point_of_sale.enforce_https`
- **Value**: `True`

#### SEE ALSO
- [Self-signed certificate for ePOS printers](applications/sales/point_of_sale/configuration/epos_ssc.md)
