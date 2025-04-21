# Least packages removal

The *Least Packages* removal strategy fulfills an order by opening the fewest number of packages,
which is ideal for maintaining organized stock without needing to open multiple boxes.

#### SEE ALSO
- [About removal strategies](../removal_strategies.md)
- [Odoo Tutorials: Least Packages](https://www.odoo.com/slides/slide/5477/share)

To understand how the removal strategy works, consider the following example, featuring a warehouse
that stores packages of flour in bulk packages of `100 kg`.

To minimize moisture, and/or prevent pests from entering open packages, the least packages removal
strategy is used to pick from a single, opened package.

<a id="inventory-warehouses-storage-pkg-qty"></a>

## Quy trình

Using the least package removal strategy, the fewest number of packages is used to fulfill an order.

#### IMPORTANT
The [Packages feature](../removal_strategies.md#inventory-warehouses-storage-pack-setup) **must** be enabled to use
this strategy.

Consider the following example, featuring the product, `Flour`. The product's Units of
Measure field, located on the product form, is set to `kg`. The product is stored in packages of
`100 kg`, with one remaining package containing `54 kg`. The product category's Force
Removal Strategy is set to Least Packages.

#### SEE ALSO
- [Set removal strategy on product category](../removal_strategies.md#inventory-warehouses-storage-removal-config)

Create a [delivery order](../daily_operations/receipts_delivery_one_step.md#inventory-delivery-one-step) for eighty kilograms of flour by going
to the Sales app and creating a new quotation. After clicking Confirm,
the delivery order is created.

On the delivery order, the Quantity field displays the amount automatically picked,
according to the removal strategy.

For more details about *where* the units were picked, select the ⦙≣ (bulleted list)
icon, located on the far-right. Doing so opens the Open: Stock move pop-up window,
displaying how the reserved items were picked, according to the removal strategy.

In the Open: Stock move pop-up window, the Pick from field displays where
the quantities to fulfill the Demand are picked. Since the order demanded eighty
kilograms, which exceeds the quantity in the opened package of `54 kg`, an unopened package of `100
kg` is selected.

![Show which package was picked in the *Pick From* field.](applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies/least_packages/least-package.png)
