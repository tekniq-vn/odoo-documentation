# Inventory management

In the Odoo *Inventory* app, [warehouses](inventory_management/warehouses.md) handle the broader
organization and distribution of stock across different physical sites, while [locations](inventory_management/use_locations.md) provide a more detailed breakdown within each warehouse for
efficient item management.

This document serves as an introduction to the terminology and concepts necessary to master
*Inventory*. For specific instructions and examples of how things work, refer to individual
documentation pages.

#### SEE ALSO
[Odoo Tutorials: Warehouses & Locations](https://www.youtube.com/watch?v=zMvudZVLuUo)

## Kho hàng

[Warehouses](inventory_management/warehouses.md) represent a physical place, with a physical
address, where a company's items are stored.

Configure [routes](../shipping_receiving/daily_operations/use_routes.md) in a warehouse to
control how products move to customers, from vendors, within the warehouse, or [between
warehouses](replenishment/resupply_warehouses.md).

## Vị trí

[Locations](inventory_management/use_locations.md) refer to specific areas within a warehouse,
such as shelves, floors, or aisles. These are sub-divisions within a warehouse, and are unique to
that warehouse. Users can create and manage numerous locations within a single warehouse to organize
inventory more precisely.

#### SEE ALSO
- [Vị trí](inventory_management/use_locations.md)
- [Điều chỉnh tồn kho](inventory_management/count_products.md)
- [Đếm theo chu kỳ](inventory_management/cycle_counts.md)
- [Scrap inventory](inventory_management/scrap_inventory.md)

<a id="inventory-warehouses-storage-location-type"></a>

### Location types

*Location types* in Odoo help categorize and manage where products are, and what actions need to be
taken with them. By default, on the Inventory app ‣ Configuration ‣ Locations
page, only internal locations are displayed.

To view the seven location types in Odoo, select any location, and in the Location Type
field, there are:

- Vendor Location: defines an area where products purchased from vendors originate.
  Items here are **not** in stock.
- View: used to organize and structure the warehouse hierarchy. For example, the view
  location `WH` (short for warehouse) groups all internal locations, such as `Stock`, receiving
  docks, quality checkpoints, and packing areas to show they all belong to the same warehouse.

  #### IMPORTANT
  View locations should **not** contain products, but it is possible to move them there.
- Internal Location: storage locations within the warehouse. Items stored in these
  locations are accounted for in [inventory valuation](../product_management/inventory_valuation/using_inventory_valuation.md).
- Customer Location: where sold products are tracked; items here are no longer in stock.
- Inventory Loss: counterpart location to consume missing items or create stock,
  accounting for discrepancies.

  In Odoo, examples of inventory loss locations are *Inventory Adjustment*, used to account for
  discrepancies during an inventory count, and *Scrap*, which is where damaged goods are sent to
  account for inventory losses.
- Production: where raw materials are consumed, and [manufactured products](../../manufacturing.md) are created.
- Transit Location: used for inter-company or inter-warehouse operations to track
  products shipped between different addresses, such as [Physical Locations/Inter-warehouse
  transit](#inventory-warehouses-storage-interwarehouse-transit).

![List of locations in Odoo.](../../../../.gitbook/assets/locations2.png)

#### NOTE
In Odoo, location types are color-coded:
: - **Red**: internal locations
  - **Blue**: view locations
  - **Black**: external locations (including inventory loss, vendor, and customer locations).

### View locations in Odoo

Odoo databases include pre-configured view locations to organize the hierarchy of locations. These
provide helpful context, and distinguish between internal and external locations.

- *Physical locations* serve as an umbrella for external locations, without changing a product's
  inventory value. (Inventory valuation changes occur when products move from internal to external
  locations).

<a id="inventory-warehouses-storage-interwarehouse-transit"></a>
- *Partner locations* group customer and vendor locations (external locations) together. Transfers
  to these locations affect inventory valuation.
- *Virtual locations* are locations that do **not** exist physically, but it is where items that are
  not in inventory can be placed. These can be items that are no longer in inventory due to loss, or
  other factors.

* [Kho hàng](inventory_management/warehouses.md)
* [Vị trí](inventory_management/use_locations.md)
* [Điều chỉnh tồn kho](inventory_management/count_products.md)
* [Đếm theo chu kỳ](inventory_management/cycle_counts.md)
* [Scrap inventory](inventory_management/scrap_inventory.md)
