# Linking existing listings

Once the eBay account is linked existing listings from within the eBay seller account need to be
added manually to the Odoo product listings.

The process will be as follows:
- Turn off eBay scheduled actions
- Add products and link listings
- Turn on eBay scheduled actions

#### SEE ALSO
To learn more about the eBay connector visit these pages as well:

- [eBay connector setup](applications/sales/sales/ebay_connector/setup.md)
- [How to list a product?](applications/sales/sales/ebay_connector/manage.md)
- [Troubleshooting eBay connector](applications/sales/sales/ebay_connector/troubleshooting.md)

## Turn off eBay scheduled actions

To start linking existing listings in eBay, first turn off the eBay notifications in the scheduled
actions in Odoo. The reason for this is so that no orders or eBay data syncs during this process.
The Scheduled Actions can be accessed by first activating
[developer mode](applications/general/developer_mode.md#developer-mode). After doing so, go to Settings ‣ Technical
‣ Automation ‣ Scheduled Actions.

#### WARNING
[Chế độ lập trình viên (chế độ gỡ lỗi)](applications/general/developer_mode.md) must be activated to ensure the technical menu appears for
the user.

Disabling scheduled actions enables users to sync and validate eBay data before receiving orders.
The following are descriptions of scheduled actions that need to be temporarily deactivated:

- eBay: get new orders: eBay pushes new orders not already in Odoo (based on
  client_order_reference, or sales order reference field). This command
  also updates existing orders, where changes we made in eBay. New and updated orders are then
  placed in draft mode. Customers will be created if they are not already in Odoo.
- eBay: synchronize stock: eBay displays Odoo's stock on hand.
- eBay: update categories: eBay will push updated monthly categories (only up to fourth
  layer; a manual update required for the rest).

To toggle off the eBay notification, select the entry from the Scheduled Actions list.
Then, on the page, click the Active toggle button to turn it off.

### Sync eBay categories

To ensure that Odoo's eBay products have all the categories available on eBay, the eBay categories
should be synced to Odoo next.

Navigate to Settings ‣ Technical ‣ Automation ‣ Scheduled Actions. Click into
the scheduled action labeled: Ebay: update categories and then click Run
Manually.

#### IMPORTANT
Odoo only recognizes eBay category paths up to four layers deep. If a product has a listing of
more than four, the category field will only populate up to the fourth layer.

If product categories beyond four paths are required, users need to manually add those paths.
This has historically been done by getting a list of all product categories beyond 4 paths,
manually importing them into the Product Category model in Odoo, then linking them individually
to the product.

Users can import the remaining product categories into the eBay product categories manually using
using the Action menu and Import feature.

## Link eBay listings

To add eBay listings in Odoo, either manually add products, using a listing ID, or establish an
automatic listing link between Odoo and eBay.

### Manual listing link

To add an eBay listing to products in Odoo, begin by going to Sales app ‣ Products
‣ Products and selecting the desired product. Click on Sell on eBay (either in the
eBay tab or under the Product name). Select Save if necessary.

Still the product form, click link to listing in the top menu and enter in listing ID
from eBay in the pop up (the listing ID is in the eBay product URL).

## Turn on eBay scheduled Actions

The next step is to turn on the eBay notifications in the scheduled actions in Odoo so that orders
and data are exchanged. The Scheduled Actions can be accessed by first activating
[developer mode](applications/general/developer_mode.md#developer-mode) and go to Settings ‣ Technical ‣
Automation ‣ Scheduled Actions.

Turning on the following scheduled actions allows users to sync and validate eBay data
automatically.

- eBay: get new orders: eBay will push all new orders not already in Odoo (based on
  client_order_reference, or sales order reference field), and will update orders if there has been
  a change from eBay. Orders will be put in draft mode. Customers will be created if they are not
  already in Odoo.
- eBay: synchronize stock: eBay will display the stock on hand in Odoo.
- eBay: update categories: eBay will push updated monthly categories (only up to fourth
  layer, will need to manually update the rest).

#### NOTE
If an order comes in and the listing from the order is not linked to a product, eBay will create
a consumable product.product in its place. These consumables should be altered on the
*Sales Order* while in draft state to represent a storable product, and then the user can link to
the listing as they come in.

#### SEE ALSO
- [How to list a product?](applications/sales/sales/ebay_connector/manage.md)
- [Troubleshooting eBay connector](applications/sales/sales/ebay_connector/troubleshooting.md)
- [eBay connector setup](applications/sales/sales/ebay_connector/setup.md)
