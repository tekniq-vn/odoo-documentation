# Closest location removal

For the *Closest Location* removal strategy, products are picked based on the alphanumeric order of
storage location titles.

The goal of this strategy is to save the warehouse worker from taking a long journey to a farther
shelf when the product is also available at a closer location.

#### SEE ALSO
[About removal strategies](./)

<a id="inventory-warehouses-storage-sequence"></a>

To understand *location sequence* in the closest removal strategy, consider the following example:

#### IMPORTANT
To use this removal strategy, the Storage Locations and Multi-Step Routes
settings **must** be enabled in Inventory app ‣ Configuration ‣ Settings.

#### SEE ALSO
[Set up removal strategy](./#inventory-warehouses-storage-removal-config)

<a id="inventory-warehouses-storage-location-name"></a>

## Location names

To configure location names, begin by navigating to Inventory app ‣ Configuration
‣ Locations. Then, select an existing location, or click New to create a new one, and
then enter the desired name in the Location Name field.

Once the locations are named in alphabetical order, based on their proximity to the output or
packing location, set the removal strategy on the [parent location](../../warehouses_storage/inventory_management/use_locations.md#inventory-location-hierarchy).

To do that, in the Locations list, select the parent location of the alphabetically
named storage locations.

Doing so opens the form for the parent location. In the Removal Strategy field, select
Closest Location.

## Quy trình

To see how the closest location removal strategy works, consider the following example, featuring
the popular product, `iPhone charger`, which is stored in `WH/Stock/Shelf 1`, `WH/Stock/Shelf 2`,
and `WH/Stock/Shelf 3`.

Fifteen, five, and thirty units are in stock at each respective location.

Create a [delivery order](../daily_operations/receipts_delivery_one_step.md#inventory-delivery-one-step) for eighteen units of the `iPhone
charger` by navigating to the Sales app and creating a new quotation.

After adding the products, clicking Confirm creates a delivery order that reserves items
stored at the closest location, using the removal strategy.

For more details about *where* the units were picked, select the ⦙≣ (bulleted list)
icon, located on the far-right. Doing so opens the Open: Stock move pop-up window that
displays how the reserved items were picked, according to the removal strategy.

In the Open: Stock move pop-up window, the Pick from field displays where
the quantities to fulfill the Demand are picked. All fifteen of the units stored at the
closest location, `WH/Stock/Shelf 1`, are picked first. The remaining three units are then selected
from the second closest location, `WH/Stock/Shelf 2`.

![Display *Pick From* quantities for the order for iPhone chargers.](../../../../../.gitbook/assets/stock-move-window.png)
