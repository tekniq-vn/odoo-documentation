# Kho hàng

In the Odoo *Inventory* app, a *warehouse* is a physical space with an address for storing items,
such as a storage facility, distribution center, or physical store.

Each database has a pre-configured warehouse with the company's address. Users can set up multiple
warehouses, and [create stock moves](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/use_routes.md)
between them.

## Cấu hình

To create or manage warehouses, go to Inventory app ‣ Configuration ‣
Warehouses.

Then, select an existing warehouse, or create a new one by clicking New. Doing so opens
the warehouse form, which contains the following fields:

- Warehouse (*required field*): the full name of the warehouse.
- Short Name (*required field*): the abbreviated code for the warehouse (maximum five
  characters). The short name for the default warehouse in Odoo is `WH`.

  #### IMPORTANT
  The Short Name appears on warehouse documents, so it is recommended to use an
  memorable one, like "WH[first letters of location]" (e.g. `WHA`, `WHB`, etc.).
- Address (*required field*): the address of the warehouse. To change the warehouse
  address when creating two or more warehouses, hover over the field, and click the
  <i class="fa fa-arrow-right"></i> (right arrow).
- Company (*required field*): the company that owns the warehouse; this can be set as
  the company that owns the Odoo database, or the company of a customer or vendor.
- Intrastat region: [region name](applications/finance/accounting/reporting/intrastat.md) required for companies in the European
  Union.

#### IMPORTANT
The options below are available **only** when the *Multi-Step Routes* feature is enabled in
Inventory app ‣ Configuration ‣ Settings.

- Incoming Shipments: select the option to receive products from the warehouse in
  [one](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.md), [two](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps.md), or [three](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_three_steps.md) steps.
- Outgoing Shipments: select the option to deliver products from the warehouse in
  [one](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_one_step.md), [two](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/receipts_delivery_two_steps.md), or [three](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/delivery_three_steps.md) steps.
- Dropship Subcontractors: available with the *Subcontracting* feature enabled in
  Manufacturing app ‣ Configuration ‣ Settings. Tick this checkbox to purchase
  components from vendors, and dropship them to subcontractors.
- Resupply Subcontractors: available with the *Subcontracting* feature, tick this
  checkbox to supply subcontractors with raw materials stored in *this* specific warehouse.
- Manufacture to Resupply: tick this checkbox to allow for items to be manufactured in
  this warehouse.
- Manufacture: choose whether to manufacture products in [one](applications/inventory_and_mrp/manufacturing/basic_setup/one_step_manufacturing.md), [two](applications/inventory_and_mrp/manufacturing/basic_setup/two_step_manufacturing.md), or [three steps](applications/inventory_and_mrp/manufacturing/basic_setup/three_step_manufacturing.md).
- Buy to Resupply: tick this checkbox to allow for purchased products to be delivered to
  the warehouse.
- Resupply From: available with multiple warehouses in the database, select warehouses
  to pull stock *from* to fulfill orders.

#### SEE ALSO
[Use inventory adjustments to add stock to new warehouses](applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products.md)

![Example warehouse form.](../../../../../.gitbook/assets/warehouse-form.png)
