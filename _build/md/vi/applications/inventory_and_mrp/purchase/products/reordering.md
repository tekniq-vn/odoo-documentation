# Configure reordering rules

For certain products, it is necessary to ensure that there is always a minimum amount available on
hand at any given time. By adding a reordering rule to a product, it is possible to automate the
reordering process so that a purchase order is automatically created whenever the amount on hand
falls below a set threshold.

#### IMPORTANT
The *Inventory* module must be installed to use reordering rules.

## Configure products for reordering

Products must be configured in a specific way before a reordering rule can be added to them.

Starting from the Inventory, Manufacturing,
Purchase, or Sales module, navigate to Products
‣ Products and then click Create to make a new product. Alternatively, find a product
that already exists in the database and click into it's product form.

Next, on the product form, enable reordering by checking the Can be Purchased option
underneathe the Product Name field. Finally, set the Product Type to
`Storable Product` under the General Information tab.

![Configure a product for reordering in Odoo.](../../../../.gitbook/assets/product-configured-for-reordering.png)

## Add a reordering rule to a product

After properly configuring a product, a reordering rule can be added to it by selecting the now
visible Reordering Rules tab at the top of that product's form, and then clicking
Create on the Reordering Rules dashboard.

![Access reordering rules for a product from the product page in Odoo.](../../../../.gitbook/assets/reordering-rules-tab.png)

Once created, the reordering rule can be configured to generate purchase orders automatically by
defining the following fields:

- Location specifies where the ordered quantities should be stored once they are
  received and entered into stock.
- Min Quantity sets the lower threshold for the reordering rule while Max
  Quantity sets the upper threshold. If the stock on hand falls below the minimum quantity, a new
  purchase order will be created to replenish it up to the maximum quantity.
- Multiple Quantity can be configured so that products are only ordered in batches of a
  certain quantity. Depending on the number entered, this can result in the creation of a purchase
  order that would put the resulting stock on hand above what is specified in the Max
  Quantity field.
- UoM specifies the unit of measurement by which the quantity will be ordered. For
  discrete products, this should be set to `Units`. However, it can also be set to units of
  measurement like `Volume` or `Weight` for non-discrete products like water or bricks.

![Configure the reordering rule in Odoo.](../../../../.gitbook/assets/reordering-rule-configuration.png)

## Manually trigger reordering rules using the scheduler

Reordering rules will be automatically triggered by the scheduler, which runs once a day by
default. To trigger reordering rules manually, navigate to Inventory ‣ Operations
‣ Run Scheduler. On the pop-up window, confirm the manual action by clicking Run
Scheduler.

#### NOTE
Manually triggering reordering rules will also trigger any other scheduled actions.

## Manage reordering rules

To manage the reordering rules for a single product, navigate to that product page's form and select
the Reordering Rules tab at the top of the form.

To manage all reordering rules for every product, go to Inventory ‣ Configuration
‣ Reordering Rules. From this dashboard, typical bulk actions in Odoo can be performed such as
exporting data or archiving rules that are no longer needed. As well, the Filters,
Group By or triple-dotted menu on the form are available to search for and/or organize
the reordering rules as desired.
