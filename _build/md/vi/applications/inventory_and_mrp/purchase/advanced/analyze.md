# Purchase Analysis report

The *Purchase Analysis* report provides statistics about products purchased using Odoo's
**Purchase** app. This data is useful for gaining a deeper understanding of key metrics related to
purchase orders (POs), including the quantity of products ordered and received, the amount of time
it takes to receive purchased products, and more.

To open the Purchase Analysis report, navigate to Purchase app ‣ Reporting ‣
Purchase.

#### IMPORTANT
The Purchase Analysis report is one of many reports available across the Odoo app
suite. This documentation only covers the measures specific to the Purchase Analysis
report, along with a few use case examples.

For a full overview of the basic features available in most Odoo reports, see the documentation
on [reporting essentials](../../../essentials/reporting.md).

## Đơn vị tính

*Measures* refer to the various datasets that can be displayed on the Purchase Analysis
report, with each dataset representing a key statistic about  or products. To choose a measure,
click the Measures <i class="fa fa-caret-down"></i> button, and select one of the options from the
drop-down menu:

- # of Lines: The number of  order lines, across all .
- Average Cost: The average cost of .
- Days to Confirm: The number of days it takes to confirm a .
- Days to Receive: The number of days it takes to receive the products in a .
- Gross Weight: The total weight of purchased products.
- Qty Billed: The quantity of a product (or products) for which the vendor has already
  been billed.
- Qty Ordered: The quantity of a product (or products) ordered.
- Qty Received: The quantity of an ordered product (or products) received.
- Qty to be Billed: The quantity of an ordered product (or products) for which the
  vendor has yet to be billed.
- Total: The total amount spent, including tax.
- Untaxed Total: The total amount spent, excluding tax. This measure is selected by
  default.
- Volume: The total volume of ordered products, for products which are measured by
  volume.
- Count: The total count of .

<a id="purchase-purchase-analysis-example"></a>

## Use case: determine days to receive products from each vendor

One possible use case for the Purchase Analysis report is determining how long each
vendor takes to deliver purchased items. This allows companies to make better informed decisions
about which vendors they want to purchase from.

## Use case: compare vendor POs for two time periods

Another use for the Purchase Analysis report is to compare key statistics about 
for two different time periods, for a specific vendor. By doing so, it is easy to understand how
purchases from the vendor have increased or decreased.
