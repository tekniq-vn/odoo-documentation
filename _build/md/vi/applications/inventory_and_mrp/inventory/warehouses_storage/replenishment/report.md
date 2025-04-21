# Replenishment report

The *replenishment report* is an interactive dashboard that uses [manual reordering rules](reordering_rules.md), lead times, and upcoming demands to forecast quantities of products that need
restocking.

Reordering rules used on this dashboard are normal reordering rules, but the user benefits from a
monitoring menu with extra options to manage suggestions for replenishment.

This enables users to anticipate future needs, keep less products on hand without the risk of
running out, plan and consolidate orders.

To access the replenishment report, go to Inventory app ‣ Operations ‣
Replenishment.

The fields and features unique to the replenishment dashboard are displayed below. For definitions
of the other fields, go to the [Create reordering rules section](reordering_rules.md#inventory-warehouses-storage-rr-fields).

By default, the quantity in the To Order field is the quantity required to reach the set
Max Quantity. However, the To Order quantity can be adjusted by clicking on
the field and changing the value. To replenish a product manually, click <i class="fa fa-truck"></i>
Order Once.

Clicking <i class="fa fa-bell-slash"></i> Snooze temporarily deactivates the reordering rule for
the set period, hiding the entry from the replenishment dashboard, when it is supposed to appear.

![Replenishment report that displays recommended quantities to order.](applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/report/replenishment-dashboard.png)

#### NOTE
Automatic reordering rules appear on this menu, too but are hidden by default.

## Replenishment information

In each line of the replenishment report, clicking the <i class="fa fa-info-circle"></i> (info)
icon opens the Replenishment Information pop-up window, which displays the *lead times*
and *forecasted date*.

For detailed information on how to use this feature for replenishment, go to the [Just in time
logic](reordering_rules.md#inventory-warehouses-storage-just-in-time) section.
