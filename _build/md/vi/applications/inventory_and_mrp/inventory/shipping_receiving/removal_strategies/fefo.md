# FEFO removal

The *First Expired, First Out* (FEFO) removal strategy targets products for removal based on their
assigned removal dates.

#### SEE ALSO
[About removal strategies](../removal_strategies.md)

<a id="inventory-warehouses-storage-removal-date"></a>

## Removal date

Products **must** be removed from inventory before their *removal date*, which is set as a certain
number of days before the product's *expiration date*.

The user sets this number of days by navigating to the product form's Inventory tab.
Under the Traceability section, ensure the Tracking field is set to either
By Lots or By Unique Serial Number.

Next, select the Expiration Date option, which makes the Removal Date field
(and other date fields) appear.

#### IMPORTANT
The Lots and Serial Numbers and Expiration Dates features **must** be
enabled in Inventory app ‣ Configuration ‣ Settings to track expiration
dates.

The expiration date of a product is determined by adding the date the product was received to the
number of days specified in the Expiration Date field of the product form.

The removal date takes this expiration date, and subtracts the number of days specified in the
Removal Date field of the product form.

#### SEE ALSO
[Ngày hết hạn](../../product_management/product_tracking/expiration_dates.md)

<a id="inventory-warehouses-storage-exp-date"></a>

To view the expiration dates of items in stock, navigate to the product form, and click the
On Hand smart button.

Next, click the additional options icon, located on the far-right, and select the columns:
Expiration Date and Removal Date.

![Show expiration dates from the inventory adjustments model accessed from the *On Hand*
smart button from the product form.](../../../../../.gitbook/assets/removal-date.png)

## Quy trình

Using the  removal strategy ensures that products with the
nearest removal date are picked first.

To understand how this removal strategy works, consider the following example below about the
product, `Carton of eggs`, which is a box containing twelve eggs.

The product is tracked By Lots, and the product category's Force Removal
Strategy is set to First Expired, First Out (FEFO).

#### SEE ALSO
- [Set up force removal strategy](../removal_strategies.md#inventory-warehouses-storage-removal-config)
- [Enable lots tracking](../removal_strategies.md#inventory-warehouses-storage-lots-setup)
- [Odoo Tutorials: Perishable Products](https://www.odoo.com/slides/slide/5324/share)

|                                                        | LOT1      | LOT2      | LOT3      |
|--------------------------------------------------------|-----------|-----------|-----------|
| On-hand stock                                          | 5         | 2         | 1         |
| Ngày hết hạn                                           | Ngày 4/4  | Ngày 10/4 | Ngày 15/4 |
| [Removal date](#inventory-warehouses-storage-exp-date) | Ngày 26/2 | Ngày 4/3  | Ngày 9/3  |

To see the removal strategy in action, go to the Sales app and create a new
quotation.

Clicking Confirm creates a delivery order for today, December 29th, and the lot numbers
with the soonest expiration dates are reserved, using the 
removal strategy.

To view the detailed pickings, click the ⦙≣ (bulleted list) icon, located on the
far-right of the Carton of egg's product line, in the Operations tab of the delivery
order. Doing so opens the Open: Stock move pop-up window.

In the Open: Stock move pop-up window, the Pick from field displays where
the quantities to fulfill the Demand are picked from.

Since the order demanded six Cartons of eggs, using the 
removal strategy, all five Cartons from `LOT1`, with the removal date of February 26th, are picked.
The remaining Carton is selected from `LOT2`, which has a removal date of March 4th.

![The stock moves window that shows the lots to be removed using FEFO.](../../../../../.gitbook/assets/eggs-picking.png)
