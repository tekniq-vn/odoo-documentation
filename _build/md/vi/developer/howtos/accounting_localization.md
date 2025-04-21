# Accounting localization

#### WARNING
This tutorial requires knowledge about how to build a module in Odoo (see
[Server framework 101](../tutorials/server_framework_101.md)).

## Installation procedure

On installing the [account](https://github.com/odoo/odoo/blob/17.0/addons/account) module, the localization module corresponding to the country code of the company is installed automatically.
In case of no country code set or no localization module found, the [l10n_generic_coa](https://github.com/odoo/odoo/blob/17.0/addons/l10n_generic_coa) (US) localization module is installed by default.
Check [post init hook](https://github.com/odoo/odoo/blob/17.0/addons/account/__init__.py) for details.

For example, [l10n_ch](https://github.com/odoo/odoo/blob/17.0/addons/l10n_ch) will be installed if the company has `Switzerland` as country.

## Building a localization module

The structure of a basic `l10n_XX` module may be described with the following `__manifest__.py` file:

```python
{
    "name": "COUNTRY - Accounting",
    "version": "1.0.0",
    "category": "Accounting/Localizations/Account Charts",
    "license": "LGPL-3",
    "depends": [
        "account",
    ],
    "data": [
        "data/other_data.xml",
        "views/xxxmodel_views.xml",
    ],
    "demo": [
        "demo/demo_company.xml",
    ]
}
```

Your worktree should look like this

```bash
l10n_xx
├── data
│   ├── template
│   │   ├── account.account-xx.csv
│   │   ├── account.group-xx.csv
│   │   └── account.tax.group-xx.csv
│   └── other_data.xml
├── views
│   └── xxxmodel_views.xml
├── demo
│   └── demo_company.xml
├── models
│   ├── template_xx.py
│   └── __init__.py
├── __init__.py
└── __manifest__.py
```

In the first file `models/template_xx.py`, we set the name for the chart of accounts along with some basic fields.

#### SEE ALSO
[Chart Template References](../reference/standard_modules/account.md)

## Chart of Accounts

### Account tags

#### SEE ALSO
[Account Tag References](../reference/standard_modules/account/account_account_tag.md#reference-account-account-tag)

Tags are a way to sort accounts.
For example, imagine you want to create a financial report having multiple lines but you have no way to find a rule to dispatch the accounts according to their `code`.
The solution is the usage of tags, one for each report line, to filter accounts like you want.

Put the tags in the `data/account_account_tag_data.xml` file.

### Accounts

#### SEE ALSO
- [Account References](../reference/standard_modules/account/account_account.md#reference-account-account)
- [Hệ thống tài khoản](../../applications/finance/accounting/get_started/chart_of_accounts.md)

Obviously, Chart of Accounts cannot exist without Accounts. You need to specify them in `data/account.account.template.csv`.

#### WARNING
- Avoid the usage of `asset_cash` `account_type`!
  Indeed, the bank & cash accounts are created directly at the installation of the localization module and then, are linked to an `account.journal`.
- Only one account of type payable/receivable is enough for the generic case.  We need to define a PoS receivable account as well however. (linked in the CoA)
- Don't create too many accounts: 200-300 is enough. But mostly, we try to find a good balance where the CoA needs minimal adapting for most companies afterwards.

### Account groups

#### SEE ALSO
[Account Group References](../reference/standard_modules/account/account_group.md#reference-account-group)

Account groups allow describing the hierarchical structure of the chart of accounts. The filter needs to be activated in the report and then when you decollapse into journal entries it will show the parents of the account.

It works with the prefix *start*/*end*, so every account where the code starts with something between *start* and *end* will have this `account.group` as the parent group.  Furthermore, the account groups can have a parent account group as well to form the hierarchy.

### Taxes

#### SEE ALSO
- [Tax References](../reference/standard_modules/account/account_tax.md#reference-account-tax)
- [Thuế](../../applications/finance/accounting/taxes.md)

To add taxes you first need to specify tax groups. You normally need just one tax group for every tax rate, except for the 0% as you need to often distinguish between exempt, 0%, not subject, ... taxes.
This model only has two required fields: `name` and `country`. Create the file `data/template/account.tax.group-xx.csv` and list the groups.

Now you can add the taxes via `data/template/account.tax-xx.csv` file.  The first tax you define that is purchase/sale also becomes the default purchase/sale tax for your products.

### Tax Report

<div><span class="badge" style="background-color:#AD5E99">Enterprise feature</span><div>

The tax report is declared in the Invoicing (`account`) app, but the report is only accessible when Accounting (`account_accountant`) is installed.

#### SEE ALSO
- [Report Line](../reference/standard_modules/account/account_report_line.md)
- [Tax return (VAT declaration)](../../applications/finance/accounting/reporting/tax_returns.md)

In the previous section, you noticed the fields `invoice_repartition_line_ids` or `refund_repartition_line_ids` and probably understood nothing about them. Good news: you are not alone on this incomprehension. Bad news: you have to figure it out a bit. The topic is complicated. Indeed:

```default
accounting_localization/tax_report.dot
> Graph not rendered because `dot` is not installed
```

The simple version is that, in the tax template, you indicate in the invoice/refund repartition lines whether the base or a percentage of the tax needs to be reported in which report line (through the *minus/plus_report_line_ids* fields).
It becomes clear also when you check the tax configuration in the Odoo interface (or check the docs [Tax References](../reference/standard_modules/account/account_tax.md#reference-account-tax), [Tax Repartition References](../reference/standard_modules/account/account_tax_repartition.md#reference-account-tax-repartition)).

So, once you have properly configured taxes, you just need to add the `data/account_tax_report_data.xml` file with a record for your `account.report`. For it to be considered as a tax report, you need to provide it with the right `root_report_id`.

```xml
<odoo>
    <record id="tax_report" model="account.report">
        <field name="name">Tax Report</field>
        <field name="root_report_id" ref="account.generic_tax_report"/>
        <field name="country_id" ref="base.XX"/>
    </record>

    ...
</odoo>
```

... followed by the declaration of its lines, as `account.report.line` records.

### Fiscal positions

#### SEE ALSO
- [Fiscal Position References](../reference/standard_modules/account/account_fiscal_position.md#reference-account-fiscal-position)
- [Fiscal positions (tax and account mapping)](../../applications/finance/accounting/taxes/fiscal_positions.md)

Specify fiscal positions in the `data/template/account.fiscal.position-xx.csv` file.

## Final steps

Finally, you may add a demo company, so the localization can easily be tested in demo mode.

## Accounting reports

<div><span class="badge" style="background-color:#AD5E99">Enterprise feature</span><div>

#### SEE ALSO
[Báo cáo](../../applications/finance/accounting/reporting.md)

Accounting reports should be added via a separate module `l10n_XX_reports` that should go to the [enterprise repository](https://github.com/odoo/enterprise/blob/17.0).

Basic `__manifest__.py` file for such a module looks as following:

```python
{
    "name": "COUNTRY - Accounting Reports",
    "category": "Accounting/Localizations/Reporting",
    "version": "1.0.0",
    "license": "OEEL-1",
    "depends": [
        "l10n_XX", "account_reports"
    ],
    "data": [
        "data/balance_sheet.xml",
        "data/profit_and_loss.xml",
    ],
    "auto_install": True,
}
```

Functional overview of financial reports is here: [Báo cáo](../../applications/finance/accounting/reporting.md).

Some good examples:

* [l10n_ch_reports/data/account_financial_html_report_data.xml](https://github.com/odoo/enterprise/blob/17.0/l10n_ch_reports/data/account_financial_html_report_data.xml)
* [l10n_be_reports/data/account_financial_html_report_data.xml](https://github.com/odoo/enterprise/blob/17.0/l10n_be_reports/data/account_financial_html_report_data.xml)

You can check the meaning of the fields here:

* [Report](../reference/standard_modules/account/account_report.md)
* [Report Line](../reference/standard_modules/account/account_report_line.md)

If you gave a `root_report_id` to your report, it is now available in its variant selector. If not,
you still need to add a menu item for it. A default menu item can be created from the form view of
the report by clicking on Actions ‣ Create Menu Item. You will then need to
refresh the page to see it. Alternatively, to create a dedicated section for a totally new report in
the Reporting menu, you need to create a new `ir.ui.menu` record (usually in the main
`l10n_XX` module) and a new `ir.actions.client` (usually in the new report XML file) that calls the
`account.report` with  the new **report id**. Then, set the new menu as `parent_id` field in the
action model.
