# Jordan

<a id="localizations-jordan-configuration-modules"></a>

## Mô đun

The following modules are installed automatically with the Jordanian localization:

| Tên                 | Tên kỹ thuật   | Mô tả                                                                                                                                                                                         |
|---------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Jordan - Accounting | `l10n_jo`      | Jordanian [fiscal localization package](../fiscal_localizations.md#fiscal-localizations-packages), complete with<br/>the Jordanian chart of accounts, taxes, tax report, and fiscal positions |
| Jordan E-Invoicing  | `l10n_jo_edi`  | Integration module for JoFotara to support Jordanian e-invoicing requirements                                                                                                                 |

#### NOTE
In some cases, such as when upgrading to a version with additional modules, it is possible that
modules may not be installed automatically. Any missing modules can be manually [installed](../../general/apps_modules.md#general-install).

<a id="localizations-jordan-specifics"></a>

## Localization overview

The Jordanian localization package ensures compliance with Jordanian fiscal and accounting
regulations. It includes tools for managing taxes, fiscal positions, reporting, and a predefined
chart of accounts tailored to Jordan's standards.

The Jordanian localization package provides the following key features to ensure compliance with
local fiscal and accounting regulations:

- [Hệ thống tài khoản](../accounting/get_started/chart_of_accounts.md): a predefined structure tailored to Jordanian
  accounting standards
- [Thuế](#localizations-jordan-taxes): pre-configured tax rates, including standard VAT, zero-rated,
  and exempt options
- [Fiscal positions (tax and account mapping)](../accounting/taxes/fiscal_positions.md): automated tax adjustments based on customer or
  supplier registration status
- [Tax reporting](#localizations-jordan-tax-reporting): detailed overview of your net tax liability
- [E-invoicing (JoFotara)](#localizations-jordan-jofotara): integration for electronic invoicing
  in line with Jordanian government requirements

<a id="localizations-jordan-taxes"></a>

### Thuế

The following [taxes](../accounting/taxes.md) are available by default with the Jordanian
localization package:

- standard sales tax (16%): applied to most goods and services within Jordan.
- exempt transactions: for sales and services not subject to VAT, such as financial services or
  healthcare.
- export tax (0%): zero-rated tax applied to goods and services exported outside Jordan.

<a id="localizations-jordan-tax-reporting"></a>

### Tax reporting

The [VAT summary](../accounting/reporting/tax_returns.md) provides a detailed breakdown of
taxable, zero-rated, and exempt transactions. Like other [financial reports](../accounting/reporting.md), the VAT summary can be filtered by period, compared against other
periods, and exported in Excel and PDF formats, ensuring compliance with Jordanian tax laws.

<a id="localizations-jordan-jofotara"></a>

## E-invoicing with JoFotara

E-invoicing with JoFotara is integrated with Odoo, ensuring compliance with Jordanian government's
technical and legal requirements for electronic invoicing. The JoFotara integration in Odoo directly
connects with the Jordanian e-invoicing platform, allowing companies to:

- generate compliant electronic invoices
- submit invoices in real time for validation
- track invoice statuses directly within Odoo

The integration requires first creating an account with JoFotara, then generating API credentials,
and finally entering those credentials in your Odoo database to link the two.

[Government manuals](https://istd.gov.jo/EN/List/Electronic_billing_User_Manual) provide instructions for creating an account and generating the API
credentials.

<a id="localizations-jordan-jofotara-configuration"></a>

### Cấu hình

<a id="localizations-jordan-linking-jofotara"></a>

#### Link Odoo to JoFotara

1. If you don't already have an account, create one by going to the [government manuals](https://istd.gov.jo/EN/List/Electronic_billing_User_Manual)
   page and following the steps in the **Procedure Manual for Joining the Jordanian National
   Electronic Invoicing System**.
2. Generate API credentials (Activity Number, Secret Key, and Client ID) by going to the [government
   manuals](https://istd.gov.jo/EN/List/Electronic_billing_User_Manual) page and following the steps in **Procedure Manual for Linking to the
   Jordanian National Electronic Invoicing System**.
3. In your Odoo database, go to Accounting ‣ Configuration ‣ Settings. In the
   Electronic Invoicing (Jordan) section, enter the API credentials generated
   previously:
   - Activity Number (income source sequence)
   - JoFotara Secret Key
   - JoFotara Client ID
4. Enter the Taxpayer type:
   - Unregistered in the sales tax: for businesses not registered for sales tax. No tax
     on the invoice line is required.
   - Registered in the sales tax: for businesses registered under the standard sales tax
     system. One tax computed as a percentage is required per invoice line.
   - Registered in the special sales tax: for businesses subject to special sales tax
     regulations. One tax computed as a percentage and one fixed tax per invoice line are required
     per invoice.
5. Nhấp Lưu.

<a id="localizations-jordan-company-and-contacts"></a>

#### Company and customers

The JoFotara invoicing workflow requires address information related to the company that sends the
invoices and the customers who receive them:

1. Go to Settings ‣ Users & Companies ‣ Companies and select the company that
   will use JoFotara.
2. Fill in the Company Name, Tax ID (TIN), and Country. If
   desired, fill in additional optional fields such as Street, City,
   State, and ZIP.

   #### IMPORTANT
   - The Country must be set to Jordan.
   - The Company Name must match the name that is registered with the Income and
     Sales Tax Department (ISTD).
   - The company's Currency must be set to JOD.
3. Go to Accounting ‣ Customers ‣ Customers.
4. For each customer whose invoices will be sent to JoFotara, click on the customer to open the form
   view, and complete the Country and Tax ID. If desired, fill in additional
   optional fields such as Street, City, State, and
   ZIP.

<a id="localizations-jordan-sending-invoices"></a>

### Sending invoices to JoFotara via Odoo

Once the company has been [linked with JoFotara](#localizations-jordan-linking-jofotara) and
the [company and customers have been properly configured](#localizations-jordan-company-and-contacts), invoices can be sent to JoFotara via Odoo:

1. Go to Accounting ‣ Customers ‣ Invoices and open a confirmed (posted)
   invoice.
2. Click Send & Print.
3. In the Send window, select Send JoFotara e-invoice and click
   Send & Print.

When an invoice is sent to JoFotara, Odoo does the following:

- generates the invoice in the required format (UBL 1.2)
- submits the invoice to JoFotara for validation
- receives the QR code from JoFotara on the invoice's PDF

#### IMPORTANT
There is an inherent difference in how values are approximated in Odoo and ISTD due to the
differing system architectures. JOD values in Odoo are stored and approximated to three decimals,
whereas ISTD expects values to have nine decimals. As a result, an insignificant difference is
inevitable and arises between the values stores in Odoo and the values reported to ISTD, which
can have an error margin of <0.01.

<a id="localizations-jordan-jofotara-state"></a>

#### JoFotara State

The JoFotara State field in the Other Info tab of confirmed invoices
reflects the current state of the document in JoFotara. It can be changed manually to reflect the
actual state of the invoices in cases where a technical error or timeout prevents Odoo from updating
it automatically.

<a id="localizations-jordan-qr-codes"></a>

#### Validating QR codes (Sanad app)

To validate the QR code received from JoFotara on the invoice, follow these steps:

1. Install the [Sanad app](https://www.sanad.gov.jo/Default/en).
2. Navigate to More.
3. Click on Validate document and scan the QR code.
4. Review results.

<a id="localizations-jordan-debit-credit"></a>

#### Debit and credit notes

To send a debit or credit note to JoFotara, first create the [debit](../accounting/customer_invoices/credit_notes.md#accounting-credit-notes-issue-debit-note) or [credit note](../accounting/customer_invoices/credit_notes.md#accounting-credit-notes-issue-credit-note). In the Print and Send window, click
Send via JoFotara to submit it for real-time validation. Upon successful validation, the
QR code from JoFotara is embedded in the debit or credit note PDF.

#### NOTE
Ensure that the Reason for generating a debit/credit note aligns with ISTD
regulations.

<a id="localizations-jordan-discounts"></a>

#### Chiết khấu

JoFotara does not support negative quantities or negative prices on invoice lines. As a result,
global discount and fixed amount discount functionality are not supported.

Discounts must be applied **per invoice line as a percentage** instead of as a global discount or
fixed amount.

#### WARNING
Attempting to submit invoices to JoFotara with negative invoice lines will result in validation
errors.

#### SEE ALSO
[Discount types](../../sales/sales/products_prices/prices/pricing.md#sales-pricing-discount-button)
