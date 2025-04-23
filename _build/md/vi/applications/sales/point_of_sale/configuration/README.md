# Cấu hình

<a id="configuration-settings"></a>

## Access the POS settings

To access the general POS settings, go to Point of Sale ‣ Configuration ‣
Settings. Then, open the dropdown menu in the Point of Sale field and select the POS to
configure.

![Dropdown menu to select the POS in the app settings](../../../.gitbook/assets/select-pos-dropdown.png)

#### NOTE
These settings are available to users with the [access rights](../../general/users.md)
Administration set as Settings.

You can also configure some settings from the dashboard by clicking the vertical ellipsis button
(⋮) on a POS card. Doing so opens a popup window, from which you can:

- [Enable multiple employees to log in.](employee_login.md)
- [Connect and set up an IoT sytem.](configuration/pos_iot.md)
- [Connect and set up an ePOS printer.](configuration/epos_ssc.md)

![popup window to access quick settings in POS](../../../.gitbook/assets/toggle-settings.png)

#### NOTE
These settings are available to users with the [access rights](../../general/users.md)
Point of Sale set as Administrator.

## Make products available

To make products available for sale, go to Point of Sale ‣ Products ‣ Products,
and select a product to open the product form. In the Sales tab, enable
Available in POS.

![Making a product available in your POS.](../../../.gitbook/assets/pos-available.png)

## PoS product categories

### Cấu hình

POS product categories allow users to categorize products and get a more structured and clean
POS interface.

To manage PoS categories, go to Point of Sale ‣ Configuration ‣ PoS Product
Categories. To add a new category, click Create. Then, name it in the
Category Name field.

To associate a category with a parent category, fill in the Parent Category field. A
parent category groups one or more child categories.

### Assign PoS product categories

Go to Point of Sale ‣ Products ‣ Products and open a product form. Then, go to
the Sales tab and fill in the Category field under the Point of
Sale section.

![Sales tab of a product form to add a PoS product category](../../../.gitbook/assets/form-pos-category.png)

### Adapt the POS interface

#### Start category

You can select one product category to display when [opening a POS session](../point_of_sale.md#pos-session-start). To configure it, go to your [POS settings](#configuration-settings) and
select a PoS category from the dropdown menu of the Start Category field within the
PoS Interface section.

![Setting to set up the start category feature](../../../.gitbook/assets/start-category.png)

#### Restrict categories

You can also limit the categories displayed on your POS interface. To achieve this, go to your
[POS settings](#configuration-settings) and choose the specific categories to display in the
Restrict Categories field within the PoS Interface section.

![Setting to set up the restrict category feature](../../../.gitbook/assets/restrict-category.png)

* [IoT system connection](configuration/pos_iot.md)
* [Máy in ePOS](configuration/epos_printers.md)
* [Secure connection (HTTPS)](configuration/https.md)
* [Self-signed certificate for ePOS printers](configuration/epos_ssc.md)
