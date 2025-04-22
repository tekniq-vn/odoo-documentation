# Đếm theo chu kỳ

For most companies, warehouse stock only needs to be counted once a year. This is why, by default,
after making an *inventory adjustment* in Odoo, the scheduled date for the next inventory count is
set for the 31st of December of the current year.

However, for some businesses, it's crucial to have an accurate inventory count at all times. These
companies use *cycle counts* to keep critical stock levels accurate. Cycle counting is a method by
which companies count their inventory more often in certain *locations*, to ensure that their
physical inventory counts match their inventory records.

## Cấu hình

In Odoo, cycle counts are performed by location. Therefore, the *Storage Locations* feature needs to
be enabled before performing a cycle count.

To enable this feature, navigate to Inventory app ‣ Configuration ‣ Settings,
and scroll down to the Warehouse section. Then, tick the checkbox next to
Storage Locations, and click Save.

![Enabled Storage Locations setting in inventory settings.](../../../../../.gitbook/assets/cycle-counts-enabled-setting.png)

## Change inventory count frequency by location

Once the *Storage Locations* feature is enabled, and there are multiple locations created in the
warehouse, the inventory count frequency can be changed for specific locations.

To view and edit locations, navigate to Inventory app ‣ Configuration ‣
Locations. This reveals a Locations page containing every location currently created
and listed in the warehouse.

From this page, click into a location to reveal the settings and configuration page for that
location.

Under the Cyclic Counting section, locate the Inventory Frequency (Days)
field, which should be set to `0` by default (if this location has not been edited previously). In
this field, change the value to any number of days desired for the frequency of counts.

![Location frequency setting on location.](../../../../../.gitbook/assets/cycle-counts-frequency-value.png)

Now, once an inventory adjustment is applied to this location, the next scheduled count date is
automatically set, based on the value entered into the Inventory Frequency (Days) field.

## Count inventory by location

To perform a cycle count for a specific location in the warehouse, navigate to
Inventory app ‣ Operations ‣ Physical Inventory. This reveals an
Inventory Adjustments page containing all products currently in-stock, with each product
listed on its own line.

From this page, the Filters and Group By options (accessible by clicking the
⬇️ (down arrow) icon, to the right of the Search... bar), can be used to
select specific locations and perform inventory counts.

To select a specific location, and view all products within that location, click the ⬇️
(down arrow) icon, to the right of the Search... bar. Then, in the Group By
column, click Add Custom Group to reveal a new drop-down menu.

![Filters and Group By menu on Inventory Adjustments page.](../../../../../.gitbook/assets/cycle-counts-filter-menu.png)

Click Location from the drop-down menu. Doing so sorts products into their storage
locations on the Inventory Adjustments page, and a cycle count can be performed for all
products in that location.

## Change full inventory count frequency

While cycle counts are typically performed per location, the scheduled date for full inventory
counts of all in-stock products in the warehouse can also be manually changed, to push the date up
sooner than the date listed.

To modify the default scheduled date, go to Inventory app ‣ Configuration ‣
Settings. Then, in the Operations section, locate the Annual Inventory Day
and Month setting field, which includes a drop-down field that is set to `31` December,
by default.

![Frequency field in inventory app settings.](../../../../../.gitbook/assets/cycle-counts-frequency-calendar.png)

To change the day, click the `31`, and change it to a day within the range `1-31`, depending on the
desired month of the year.

Then, to change the month, click December to reveal the drop-down menu, and select the
desired month.

Once all necessary changes have been made, click Save.

#### SEE ALSO
- [Điều chỉnh tồn kho](applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products.md)
- [Vị trí](applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_locations.md)
