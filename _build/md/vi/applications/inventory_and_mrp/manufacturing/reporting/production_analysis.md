# Production analysis

The *Production Analysis* report provides statistics about products manufactured using Odoo's
*Manufacturing* app. The report is useful when trying to understand production costs, manufacturing
durations, and other important statistics about manufactured products.

To open the Production Analysis report, navigate to Manufacturing app ‣ Reporting
‣ Production Analysis.

#### IMPORTANT
The Production Analysis report is one of many reports available across the Odoo app
suite. This documentation only covers the measures specific to the Production
Analysis report, along with a few use case examples.

For a full overview of the basic features available in most Odoo reports, see the documentation
on [reporting essentials](applications/essentials/reporting.md).

## Đơn vị tính

*Measures* are the datasets that can be selected in the Production Analysis report. Each
dataset represents a specific statistic about  in the database. Choose a measure by clicking
the Measures <i class="fa fa-caret-down"></i> button, and selecting one of the options from the
drop-down menu:

The options displayed in the Measures <i class="fa fa-caret-down"></i> drop-down menu, and the
order they appear in, differ depending on the filters, groupings, and comparisons enabled in the
Search... bar. By default, the available measures appear as follows:

- Average Employee Cost/Unit: the average cost paid to employees to produce one unit of
  the product.
- By-Products Total Cost: the total value of all by-products created by manufacturing
  the product.
- Component Cost/Unit: the average cost of the components required to produce one unit
  of the product.
- Cost/Unit: the average cost of producing one unit of the product, including component,
  employee, operation, and subcontracting costs.
- Duration of Operations/Unit: the average total duration of operations required to
  produce one unit of the product.
- Quantity Demanded: the total number of units of the product included in .
- Quantity Produced: the total number of units of the product that have actually been
  produced.
- Total Component Cost: the total amount spent on the product's components, across every
   for the product.
- Total Cost: the total amount spent manufacturing every unit of the product produced so
  far.
- Total Duration of Operations: the cumulative duration of every operation completed
  while manufacturing the product.
- Total Employee Cost: the cumulative amount paid to employees to manufacture the
  product.
- Total Operation Cost: the cumulative amount spent on operations required to produce
  the product.
- Total Operation Cost/Unit: the average cost of the operations required to produce one
  unit of the product.
- Total Subcontracting Cost: the cumulative amount paid to subcontractors to produce the
  product.
- Total Subcontracting Cost/Unit: the average cost of engaging a subcontractor to
  produce one unit of the product.
- Yield Percentage (%): the total quantity of the product produced versus the total
  quantity demanded, represented as a percentage.
- Count: the total count of  created for the product.

## Use case: compare products

One of the best uses for the Production Analysis report is comparing statistics about
two or more products. This is accomplished by entering the products into the Search...
bar, then selecting the necessary measure, filter, and grouping, to see the desired data.

## Use case: compare time periods

The Production Analysis report can also be used to compare data for two different time
periods. This is accomplished using the options in the Comparison section of the
Search... bar.
