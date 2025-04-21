# Inter-warehouse replenishment

When a business operates multiple locations, such as warehouses, retail shops, or manufacturing
facilities, resupplying stock from a central warehouse is sometimes necessary. Odoo uses a *Route*
configuration that enables locations to replenish from a central distribution center, automatically
generating *inter-warehouse transfers*. Odoo Inventory manages these transfers to keep
stores in stock.

This guide explains how to conduct inter-warehouse transfers using two replenishment strategies:

1. [Make to order (MTO)](#inventory-warehouses-storage-mto)
2. [Reordering rule](#inventory-warehouses-storage-reordering-rule)

#### SEE ALSO
[Difference between MTO and reordering rules](../replenishment.md)

## Cấu hình

The initial configuration for both replenishment strategies is the same. First go to
Inventory app ‣ Configuration ‣ Settings. In the Warehouse section,
activate Storage Locations. Then, click Save to apply the setting.

![Enable Storage Locations in Inventory settings.](applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/resupply_warehouses/storage-locations.png)

### Kho hàng

Configure the settings for the central warehouse and connecting storage locations by going to
Inventory app ‣ Configuration ‣ Warehouses.

#### IMPORTANT
Each central warehouse and other locations *must* have its own warehouse. For example, each shop
is considered a local warehouse.

Select an existing warehouse, or create a new one to be resupplied from the central warehouse, by
clicking New. Then, give the warehouse a name and a Short Name, which will
appear on that warehouse's transfers.

In the Warehouse Configuration tab, locate the Resupply From field. Check
the box next to the central warehouse's name. If the warehouse can be resupplied by more than one
warehouse, make sure to check those warehouses' boxes too. Now, Odoo knows which warehouses can
resupply this warehouse.

#### SEE ALSO
[Kho hàng](../inventory_management/warehouses.md)

![Supply one warehouse with another in the Warehouse Configuration tab.](applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/resupply_warehouses/warehouse.png)

### Set route on a product

Products must also be configured properly in order for them to be transferred between warehouses.

Go to Inventory app ‣ Products ‣ Products and select the desired product.

In the Inventory tab, the new route appears as X: Supply Product from Y in
the Routes section, where 'X' is the store's warehouse that receives products, and 'Y'
is the warehouse that sends products.

Tick the X: Supply Product from Y checkbox, which is intended to be used with the 
route or a reordering rule to replenish stock by moving the product from one warehouse to another.
Proceed to the dedicated sections below to continue the process.

<a id="inventory-warehouses-storage-mto"></a>

#### MTO

To replenish products using the make-to-order method, go to the product form and ensure the
[MTO route is unarchived](mto.md#inventory-warehouses-storage-unarchive-mto), so it appears in the
Routes section of the Inventory tab.

With the resupply and  routes ticked, jump to the section titled: [Replenish from another
warehouse](#inventory-warehouses-storage-resupply-workflow).

<a id="inventory-warehouses-storage-reordering-rule"></a>

#### Reordering rule

To replenish products using reordering rules, first ensure the X: Supply Product from Y
route is selected in the Inventory tab of the product form.

Then, create a reordering rule to automate replenishment by clicking the Reordering
Rules smart button.

Click New, and set:

- Location: the stock location of the retail store. For example, `SHOP/Stock`.
- Route: X: Supply Product from Y.
- Min Quantity and Max Quantity to trigger automatic stock transfers when
  inventory falls below the set threshold.

#### SEE ALSO
[Quy tắc tái đặt hàng](reordering_rules.md)

<a id="inventory-warehouses-storage-resupply-workflow"></a>

## Replenish one warehouse from another

After completing the setup, trigger replenishment using one of several methods, such as:

- Navigate to the product form of the product that is resupplied from another warehouse.

  Click the Replenish button on the top-left of the product page. In the pop-up window,
  set the warehouse to the retail shop, (e.g. `Store`), and click Confirm.
  ![Replenish pop-up window on the product form.](applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/resupply_warehouses/replenish.png)
- Create a quotation, and in the Other Info tab, set the Warehouse to the
  retail shop (e.g. `Store`), when selling the product makes the on-hand quantity of the product go
  below the minimum set on the reordering rule.
  ![Create a quote at the store.](applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/resupply_warehouses/warehouse-field.png)

Once triggered, Odoo creates two transfers: One is a *delivery order* from the central, supplying
warehouse, which contains all the necessary products to the store, and the second is a *receipt* at
the shop, from the main warehouse.

While in transit, the product is located at `Physical Locations/Inter-warehouse transit`.
