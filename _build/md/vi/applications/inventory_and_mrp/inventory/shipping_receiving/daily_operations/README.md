# Inbound and outbound flows

Configuring inbound and outbound flows in Odoo is key to optimizing efficiency, traceability, and
cost. Warehouse managers must balance speed and control, choosing between a streamlined process or
added checkpoints.

Odoo offers one-step, two-step, and three-step flows, with more steps providing greater control but
increasing operations. The best setup depends on quality checks, packaging, and warehouse size.

This guide helps businesses determine the most suitable configuration.

## Quy trình một bước

The *one-step inventory flow* is the simplest option, with minimal handling steps and the least
traceability. In this setup, products move directly from vendors to stock or from stock to
customers, with Odoo only tracking when items enter or leave the warehouse. This makes it ideal for
businesses with high-volume, low-risk products or fast-moving operations where additional validation
steps aren’t necessary.

- **Receiving**: Products go directly into stock.
- **Shipping**: Products ship directly from stock.
- **Best for**: Small warehouses, low stock levels, and non-perishable items, where minimal
  processing is needed before products are stored or shipped.

#### SEE ALSO
[One-step receipt and delivery](receipts_delivery_one_step.md)

## Quy trình hai bước

A *two-step flow* adds an input or output area for processing products before storage or shipment.
Incoming goods can be unboxed and inspected before shelving, while outgoing shipments are sorted and
consolidated before dispatch. This setup improves efficiency by assigning storage teams to picking
and stocking, while dedicated teams handle unboxing, (possibly) packing, and final verification to
reduce order fulfillment errors.

- **Receiving**: Products move to an *input* area before being transferred into stock.
  - Until transferred, received products are not automatically reserved for manufacturing, shipping,
    or other operations.
- **Shipping**: Products move to an *output* before shipping to allow for [sorting or
  consolidation](../picking_methods/).
- **Best for**: Large warehouses, high stock levels, bulky items, and workflows that separate
  receiving from storage to improve organization and efficiency.

#### SEE ALSO
[Two-step receipt and delivery](receipts_delivery_two_steps.md)

## Quy trình ba bước

A three-step flow builds on the two-step process by adding a quality check and packing area,
enforcing stricter processes and improving oversight.

#### IMPORTANT
While this setup enhances process control, separating picking and packing requires validation at
each step. If the same person handles both, it may cause redundancy and slow operations.

Quality checks and packing do not require a three-step flow. Enable [quality control points](../../../quality/quality_management/quality_control_points.md) separately or activate the
[Packages feature](../../product_management/configure/package.md#inventory-warehouses-storage-enable-package) in Odoo to incorporate
these processes without adding extra transfer steps.

- **Receiving**: Products follow a structured process: *input area* → *quality control* → *stock*.
- **Shipping**: Products are *picked*, *packed*, and then *shipped*, ensuring proper handling and
  organization.
- **Best for**: Very large warehouses with strict quality control requirements, dedicated picking
  and packing workflows, and a need for clear traceability across multiple handling stages. Suitable
  when multiple teams manage different steps before products are stocked or shipped.

#### SEE ALSO
- [Three-step receipt](receipts_three_steps.md)
- [Three-step delivery](delivery_three_steps.md)

## Add-ons

To optimize each flow, Odoo provides additional features that can enhance the process.

### Storage

To organize and store products efficiently, use:

### Delivery

Tailor the outgoing shipment process to fit the business needs. Picking methods and removal
strategies control how products are reserved for orders, while cross-docking and dropshipping
determine how they move. Configuring these options in Odoo ensures visibility into product movement
and confirms that items reach customers efficiently.

### Customization

Odoo's flexible framework enables businesses to tailor workflows to match specific operational
needs.

* [Routes and push/pull rules](use_routes.md)
* [One-step receipt and delivery](receipts_delivery_one_step.md)
* [Two-step receipt and delivery](receipts_delivery_two_steps.md)
* [Three-step receipt](receipts_three_steps.md)
* [Three-step delivery](delivery_three_steps.md)
* [Quy tắc lưu kho](putaway.md)
* [Storage categories](storage_category.md)
* [Organize a cross-dock in a warehouse](cross_dock.md)
* [Sell stock from multiple warehouses using virtual locations](stock_warehouses.md)
* [Consignment: buy and sell stock without owning it](owned_stock.md)
* [Dropship](dropshipping.md)
