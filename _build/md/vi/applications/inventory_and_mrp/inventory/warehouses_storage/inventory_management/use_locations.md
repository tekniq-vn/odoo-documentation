# Vị trí

A *location* is a specific space within a warehouse. This can be a shelf, room, aisle, etc.

## Cấu hình

To create specific storage locations, enable the *Storage Locations* feature by going to
Inventory app ‣ Configuration ‣ Settings. In the Warehouses
section, tick the Storage Locations checkbox. Then, click Save.

#### NOTE
Typically, the Storage Locations feature is used with [Multi-Step Routes](../../shipping_receiving/daily_operations/use_routes.md), which controls how products move between
locations.

![Show Storage Locations feature.](applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations/enable-location.png)

## Create new location

After enabling *Storage Locations*, go to Inventory app ‣ Configuration ‣
Locations.

![List of internal locations.](applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations/locations.png)

On this page, click New. The new location form can then be configured as follows:

- Location Name: recognizable name of the location.
- Parent Location: the location within which the new location exists. After the location
  is created, it is listed on the Locations page using a *location hierarchy*, to
  describe how a specific location fits within larger areas of the warehouse.

### Additional Information section

In addition to the required fields above, configure the following location fields to ensure the
location serves its intended purpose in the database:

- Location Type: from the drop-down menu, choose Vendor Location,
  View, Internal Location, Customer Location,
  Inventory Loss, Production, or Transit Location to categorize
  the location. For details on each location type, refer to the [Location Types section](../inventory_management.md#inventory-warehouses-storage-location-type).
- Storage Category: only available with the [Storage Categories](../../shipping_receiving/daily_operations/storage_category.md) feature enabled in
  Inventory app ‣ Configuration ‣ Settings.
- Company: the company the location belongs to.
- Is a Scrap Location?: tick this checkbox to allow for scrapped/damaged goods to be
  stored in this location.
- Is a Return Location?: tick this checkbox to allow products to be returned to this
  location.
- Barcode: used with the *Barcode* app, enter the barcode to [identify actions](../../../barcode/setup/software.md#barcode-setup-location) at this location when scanned.
- Replenish Location: used for [configuring routes](../../shipping_receiving/daily_operations/use_routes.md), tick this checkbox to set the location as
  a destination for receiving products from *Buy*, *Manufacture*, or other procurement routes,
  ensuring products are correctly supplied to the warehouse.

![Additional Information section of new location creation form.](applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations/new-location.png)

Configure the remaining fields in the Additional Information section as follows:

- Company: the company whose warehouse the location is inside of. Leave this field blank
  if this location is shared between companies.
- Is a Scrap Location?: tick this checkbox to allow for scrapped/damaged goods to be
  stored in this location.
- Is a Return Location?: tick this checkbox to allow products to be returned to this
  location.
- Barcode: the barcode assigned to the location.
- Replenish Location: tick this checkbox to get all quantities to replenish at this
  location.

In the Cyclic Counting section, change the value in the Inventory Frequency
(Days) field from the default `0`, if necessary.

![Cyclic Counting section of new location creation form.](applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations/use-locations-cyclic-counting.png)

When different than `0`, the inventory count dates for products stored at this location are
automatically set at the defined frequency.

In the Logistics section, in the Removal Strategy field, click the drop-down
menu and select the [removal strategy](../../shipping_receiving/removal_strategies.md) for how
items should be removed from this location.

<a id="inventory-location-hierarchy"></a>

### Cyclic Counting section

To schedule regular inventory counts at this location, set the Inventory Frequency
(Days) field to the desired interval. By default, it is set to `0` (no scheduled counts).

For example, setting this field to `30`, schedules a count every thirty days. For more specifics on
setting up and using this feature, refer to the [Cycle Counts documentation](cycle_counts.md).

The Last Effective Inventory field displays the date the last inventory count at this
location occurred. When scheduled inventory counts are enabled, the Next Expected
Inventory field displays the date of the next inventory count.

### Logistics section

In the Logistics section of the locations form, optionally select a Removal
Strategy to determine the order and priority of how products are picked from inventory. The options
are: First In First Out (FIFO), Last In First Out (LIFO), Closest
Location, and First Expiry First Out (FEFO).

#### SEE ALSO
[Removal strategies](../../shipping_receiving/removal_strategies.md)

## Current stock at location

To view the current stock at a single location, go to Inventory app ‣
Configuration ‣ Locations, and select the desired location.

Next, click the Current Stock smart button to get a list of all products at the
location.
