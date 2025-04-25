# AvaTax integration

Avalara's *AvaTax* is a cloud-based tax software. Integrating *AvaTax* with Odoo provides real-time
and region-specific tax calculations when users sell, purchase, and invoice items in Odoo. *AvaTax*
tax calculation is supported with every United Nations charted country, including inter-border
transactions.

#### IMPORTANT
*AvaTax* is only available for integration with databases/companies that have locations in the
United States, Canada, and Brazil. This means the fiscal position/country of a database can only
be set to the United States, Canada, or Brazil. For more information, reference this
documentation: [Fiscal country](#avatax-fiscal-country).

*AvaTax* accounts for location-based tax rates for each state, county, and city. It improves
remittance accuracy by paying close attention to laws, rules, jurisdiction boundaries, and special
circumstances (like, tax holidays, and product exemptions). Companies who integrate with *AvaTax*
can maintain control of tax-calculations in-house with this simple  integration.

#### IMPORTANT
Some limitations exist in Odoo while using AvaTax for tax calculation:

- AvaTax is **not** supported in Odoo's **Point of Sale** app, because a dynamic tax
  calculation model is excessive for transactions within a single delivery address, such as
  stores or restaurants.
- AvaTax and Odoo use the company address, **not** the warehouse address.
- Excise tax is **not** supported. This includes tobacco/vape taxes, fuel taxes, and other
  specific industries.

#### SEE ALSO
Avalara's support documents: [About AvaTax](https://community.avalara.com/support/s/document-item?language=en_US)

## Set up on AvaTax

To use *AvaTax*, an account with Avalara is required for the setup. If one has not been set up yet,
connect with Avalara to purchase a license: [Avalara: Let's Talk](https://www.avalara.com/us/en/get-started.html).

Then, [create a basic company profile](https://www.odoo.com/r/2k0).

### Create basic company profile

Collect essential business details for the next step: locations where tax is collected,
products/services sold (and their sales locations), and customer tax exemptions, if applicable.
Follow the Avalara documentation for creating a basic company profile:

1. [Add company information](https://www.odoo.com/r/XZDW).
2. [Tell us where the company collects and pays tax](https://www.odoo.com/r/E6g).
3. [Verify jurisdictions and activate the company](https://www.odoo.com/r/NIy).
4. [Add other company locations for location-based filing](https://www.odoo.com/r/GF4).
5. [Add a marketplace to the company profile](https://www.odoo.com/r/QA5).

<a id="avatax-create-avalara-credentials"></a>

### Kết nối với AvaTax

After creating the basic company profile in Avalara, connect to *AvaTax*. This step links Odoo and
*AvaTax* bidirectionally.

Navigate to either Avalara's [sandbox](https://sandbox.admin.avalara.com/) or [production](https://admin.avalara.com/) environment. This will depend on which type of Avalara account the
company would like to integrate.

#### SEE ALSO
[Sandbox vs production environments in Avalara](https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-vs-production.html).

Log in to create the License Key. Go to Settings ‣ License and API
Keys. Click Generate License Key.

#### IMPORTANT
A warning appears stating: `If your business app is connected to Avalara solutions, the
connection will be broken until you update the app with the new license key. This action cannot
be undone.`

Generating a new license key breaks the connection with existing business apps using the *AvaTax*
integration. Make sure to update these apps with the new license key.

If this will be the first  integration being made
with *AvaTax* and Odoo, then click Generate license key.

If this is an additional license key, ensure the previous connection can be broken. There is
**only** one license key associated with each of the Avalara sandbox and production accounts.

#### WARNING
Copy this key to a safe place. It is strongly encouraged to back up the license key for
future reference. This key **cannot** be retrieved after leaving this screen.

## Cấu hình Odoo

Before using *AvaTax*, there are some additional configurations in Odoo to ensure tax calculations
are made accurately.

Verify that the Odoo database contains necessary data. The country initially set up in the database
determines the fiscal position, and aids *AvaTax* in calculating accurate tax rates.

<a id="avatax-fiscal-country"></a>

### Fiscal country

To set the Fiscal Country, navigate to Accounting app ‣ Configuration
‣ Settings.

#### SEE ALSO
[Fiscal localizations](../../fiscal_localizations.md)

Under the Taxes section, set the Fiscal Country feature to United
States, Canada, or Brazil. Then, click Save.

### Cài đặt công ty

All companies operating under the Odoo database should have a full and complete address listed in
the settings. Navigate to the Settings app, and under the Companies
section, ensure there is only one company operating the Odoo database. Click Update Info
to open a separate page to update company details.

If there are multiple companies operating in the database, click Manage Companies to
load a list of companies to select from. Update company information by clicking into the specific
company.

Database administrators should ensure that the Street..., Street2...,
City, State, ZIP, and Country are all updated for
the companies.

This ensures accurate tax calculations and smooth end-of-year accounting operations.

#### SEE ALSO
- [Công ty](../../../general/companies.md)
- [Bắt đầu](../get_started.md)

### Cài đặt phân hệ

Next, ensure that the Odoo *AvaTax* module is installed. To do so, navigate to the
Apps application. In the Search... bar, type in `avatax`, and press
`Enter`. The following results populate:

| Tên                               | Tên kỹ thuật                 | Mô tả                                                                                                                                                                    |
|-----------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avatax                            | `account_avatax`             | Default *AvaTax* module. This module adds the base *AvaTax* features for tax calculation.                                                                                |
| Avatax for geo localization       | `account_avatax_geolocalize` | This module includes the features required for integration of *AvaTax* into geo-localization<br/>in Odoo.                                                                |
| Avatax cho SO                     | `account_avatax_sale`        | Includes the information needed for tax calculation on sales orders in Odoo.                                                                                             |
| Avatax cho Tồn kho                | `account_avatax_stock`       | Includes tax calculation in Odoo Inventory.                                                                                                                              |
| Cầu nối Amazon/Avatax             | `sale_amazon_avatax`         | Includes tax calculation features between the *Amazon Connector* and Odoo.                                                                                               |
| Avatax Brazil                     | `l10n_br_avatax`             | Includes information for tax calculation in the Brazil localization.                                                                                                     |
| Avatax Brazil for Services        | `l10n_br_avatax_services`    | This module includes the required features for tax calculation for services in the Brazil<br/>localization.                                                              |
| Avatax Brazil Sale for Services   | `l10n_br_edi_sale_services`  | This module includes the required features for tax calculation for the sale of services in<br/>the Brazil localization. This includes electronic data interchange (EDI). |
| Test SOs for the Brazilian AvaTax | `l10n_br_test_avatax_sale`   | This module includes the required features for test sales orders in the Brazil localization.                                                                             |

Click the Install button on the module labeled, Avatax: `account_avatax`.
Doing so installs the following modules:

- Avatax: `account_avatax`
- Avatax for SO: `account_avatax_sale`
- Avatax for Inventory: `account_avatax_stock`

Should *AvaTax* be needed for geo-localization, or with the *Amazon Connector*, then install those
modules individually by clicking on Install on Avatax for geo localization
and Amazon/Avatax Bridge, respectively.

#### SEE ALSO
For localization specific *AvaTax* instructions, view the following [fiscal localization](../../fiscal_localizations.md) documentation:

- [Brazil](../../fiscal_localizations/brazil.md)
- [Hợp chủng quốc Hoa Kỳ](../../fiscal_localizations/united_states.md)

<a id="avatax-credentials"></a>

### Cài đặt Odoo AvaTax

To integrate the *AvaTax*  with Odoo, go to
Accounting app ‣ Configuration ‣ Settings section. The AvaTax
fields in the Taxes section is where the *AvaTax* configurations are made, and the
credentials are entered in.

First, tick the checkbox to the left of the AvaTax settings, to activate *AvaTax* on the
database. This is a quick, convenient way to activate and deactivate *AvaTax* tax calculation on the
Odoo database.

![Cấu hình cài đặt AvaTax](../../../../_images/avatax-configuration-settings.png)

#### Khoá học tiên quyết

First, select the Environment in which the company wishes to use *AvaTax* in. It can
either be Sandbox or Production.

#### SEE ALSO
For help determining which *AvaTax* environment to use (either Production or
Sandbox), visit: [Sandbox vs Production environments](https://knowledge.avalara.com/bundle/fzc1692293626742/page/sandbox-vs-production.html).

#### Thông tin đăng nhập

Now, the credentials can be entered in. The *AvaTax* Account ID should be entered in the
API ID field, and the License Key should be entered in the API
Key field.

#### IMPORTANT
The Account ID can be found by logging into the *AvaTax* portal ([sandbox](https://sandbox.admin.avalara.com/) or [production](https://admin.avalara.com/)). In the
upper-right corner, click on the initials of the user and Account. The
Account ID is listed first.

To access the License Key see this documentation:
[Kết nối với AvaTax](#avatax-create-avalara-credentials).

For the Company Code field, enter the Avalara company code for the company being
configured. Avalara interprets this as `DEFAULT`, if it is not set. The Company Code can
be accessed in the Avalara management portal.

First, log into the *AvaTax* portal ([sandbox](https://sandbox.admin.avalara.com/) or [production](https://admin.avalara.com/)). Then, navigate to Settings ‣ Manage Companies.
The Company Code value is located in the row of the Company in the
Company Code column.

![AvaTax company code highlighted on the company details page.](../../../../_images/company-code.png)

#### Transaction options

There are two transactional settings in the Odoo *AvaTax* settings that can be configured:
Use UPC and Commit Transactions.

If the checkbox next to Use UPC is ticked, the transactions will use Universal Product
Codes (UPC), instead of custom defined codes in Avalara. Consult a certified public accountant (CPA)
for specific guidance.

Should the Commit Transactions checkbox be ticked, then, the transactions in the Odoo
database will be committed for reporting in *AvaTax*.

#### Address validation

The *Address Validation* feature ensures that the most up-to-date address by postal standards is set
on a contact in Odoo. This is important to provide accurate tax calculations for customers.

#### IMPORTANT
The Address Validation feature only works with partners/customers in North America.

Additionally, tick the checkbox next to the Address validation field.

#### IMPORTANT
For accurate tax calculations, it is best practice to enter a complete address for the contacts
saved in the database. However, *AvaTax* can still function by implementing a best effort attempt
using only the Country, State, and Zip code. These are the
three minimum required fields.

Save the settings to implement the configuration.

#### WARNING
All previously-entered addresses for contacts in the Odoo database will need to be validated
using the manually validate process outlined above. Addresses are not automatically validated if
they were entered previously. This only occurs upon tax calculation.

#### Test connection

After entering all the above information into the *AvaTax* setup on Odoo, click Test
connection. This ensures the API ID and API KEY are correct, and a
connection is made between Odoo and the *AvaTax* application programming interface (API).

#### Sync parameters

Upon finishing the configuration and settings of the *AvaTax* section, click the Sync
Parameters button. This action synchronizes the exemption codes from *AvaTax*.

<a id="avatax-fiscal-positions"></a>

### Vị trí tài chính

Next, navigate to Accounting app ‣ Configuration ‣ Accounting: Fiscal
Positions. A Fiscal Position is listed named, Automatic Tax Mapping
(AvaTax). Click it to open *AvaTax's* fiscal position configuration page.

Here, ensure that the Use AvaTax API checkbox is ticked.

Optionally, tick the checkbox next to the field labeled: Detect Automatically. Should
this option be ticked, then, Odoo will automatically apply this Fiscal Position for
transactions in Odoo.

Enabling Detect Automatically also makes specific parameters, such as VAT
required, Foreign Tax ID, Country Group, Country,
Federal States, or Zip Range appear. Filling these parameters filters the
Fiscal Position usage. Leaving them blank ensures all calculations are made using this
Fiscal Position.

#### WARNING
Should the Detect Automatically checkbox not be ticked, each customer will need to
have the Fiscal Position set on their Sales and Purchase tab of the
contact record. To do so, navigate to Sales app ‣ Order ‣ Customers, or
Contacts app ‣ Contacts. Then, select a customer or contact to set the fiscal
position on.

Navigate to the Sales and Purchase tab, and down to the section labeled,
Fiscal Position. Set the Fiscal Position field to the fiscal position
for the customer.

#### SEE ALSO
[Fiscal positions (tax and account mapping)](fiscal_positions.md)

#### AvaTax accounts

Upon selecting the checkbox option for Use AvaTax API a new AvaTax tab
appears. Click into this tab to reveal two different settings.

The first setting is the AvaTax Invoice Account, while the second is, AvaTax
Refund Account. Ensure both accounts are set for smooth end-of-year record keeping. Consult a
certified public accountant (CPA) for specific guidance on setting both accounts.

Click Save to implement the changes.

### Tax mapping

The *AvaTax* integration is available on sale orders and invoices with the included *AvaTax* fiscal
position.

#### Product category mapping

Before using the integration, specify an Avatax Category on the product categories.
Navigate to Inventory app ‣ Configuration ‣ Product Categories. Select the
product category to add the AvaTax Category to. In the AvaTax Category
field, select a category from the drop-down menu, or Search More... to open the complete
list of options.

![Specify AvaTax Category on products.](../../../../_images/avatax-category.png)

#### Product mapping

Danh mục *AvaTax* cũng có thể được thiết lập cho từng sản phẩm riêng lẻ. Để cài đặt Danh mục Avatax, đi đến Ứng dụng Tồn kho ‣ Sản phẩm ‣ Sản phẩm. Chọn sản phẩm cần thêm Danh mục Avatax. Trong tab Thông tin chung, ở phía bên phải, có một trường chọn có nhãn: Danh mục Avatax. Cuối cùng, nhấp vào menu thả xuống và chọn danh mục, hoặc Tìm kiếm thêm... để tìm danh mục không có trong danh sách.

#### NOTE
If both the product, and its category, have an AvaTax Category set, the product's
AvaTax Category takes precedence.

![Override product categories as needed.](../../../../_images/override-avatax-product-category.png)

#### IMPORTANT
Mapping an AvaTax Category on either the *Product* or *Product Category* should be
completed for every *Product* or *Product Category*, depending on the route that is chosen.

#### SEE ALSO
- [Fiscal positions (tax and account mapping)](fiscal_positions.md)
- [AvaTax use](avatax/avatax_use.md)
- [Cổng thông tin Avalara (Avatax)](avatax/avalara_portal.md)
- [US Tax Compliance: Avatax elearning video](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)

* [AvaTax use](avatax/avatax_use.md)
* [Cổng thông tin Avalara (Avatax)](avatax/avalara_portal.md)
