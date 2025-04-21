# Ecuador

## Đầu trang

With the Ecuadorian localization you can generate electronic documents with its XML, Fiscal folio,
with electronic signature and direct connection to tax authority SRI.

The supported documents are Invoices, Credit Notes, Debit Notes, Purchase Liquidations and
Withholds.

The localization also Includes automations to easily predict the withholding tax to be applied to
each purchase invoice.

#### SEE ALSO
- [App Tour - Localización de Ecuador](https://www.youtube.com/watch?v=BQOXVSDeeK8)
- [Smart Tutorial - Localización de Ecuador](https://www.odoo.com/slides/smart-tutorial-localizacion-de-ecuador-170)

### Bảng thuật ngữ

Here are some terms that are essential on the Ecuadorian localization:

- **SRI**: meaning *Servicio de Rentas Internas*, the government organization that enforces pay of
  taxes in Ecuador.
- **EDI**: stands for *Electronic Data Interchange*, which refers to the sending of Electronics
  Documents.
- **RIMPE**: stands for *Regimen Simplificado para Emprendedores y Negocios*, the type of taxpayer
  qualified for SRI.

## Cấu hình

<a id="l10n-ec-module-installation"></a>

### Modules installation

[Install](../../general/apps_modules.md#general-install) the following modules to get all the features of the Ecuadorian
localization:

| Tên                         | Tên kỹ thuật           | Mô tả                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ecuador - Kế toán           | `l10n_ec`              | [Gói bản địa hóa tài chính](../fiscal_localizations.md) mặc định bổ sung đặc điểm kế toán cho bản địa hoá Ecuador, đại diện cho cấu hình tối thiểu cần thiết để doanh nghiệp hoạt động tại Ecuador theo hướng dẫn của . Khi cài đặt, phân hệ sẽ tự động tải: Hệ thống tài khoản, thuế, loại chứng từ, loại hỗ trợ thuế. Đồng thời, hệ thống tự động tạo biểu mẫu 103 và 104. |
| EDI kế toán của Ecuador     | `l10n_ec_edi`          | Includes all the technical and functional requirements to generate and validate<br/>[Electronics Documents](../accounting/customer_invoices/electronic_invoicing.md), based on the Technical<br/>documentation published by the SRI. The authorized documents are: Invoices, Credit Notes,<br/>Debit Notes, Withholdings and Purchase liquidations.                          |
| Báo cáo kế toán của Ecuador | `l10n_ec_reports`      | Includes all the technical and functional requirements to generate forms 103 and 104.                                                                                                                                                                                                                                                                                        |
| Ecuador - ATS Report        | `l10n_ec_reports_ats`  | Includes all the technical and functional requirements to generate the ATS report XML file<br/>ready to be uploaded to the *DIMM Formularios*.                                                                                                                                                                                                                               |
| Trang web tiếng Ecuado      | `l10n_ec_website_sale` | Includes all the technical and functional requirements to generate automatic electronic<br/>invoices from a Website sale.                                                                                                                                                                                                                                                    |
| Ecuadorian Point of Sale    | `l10n_ec_edi_pos`      | Includes all the technical and functional requirements to generate automatic electronic<br/>invoices from a POS sale.                                                                                                                                                                                                                                                        |

#### NOTE
When you install a database from scratch selecting `Ecuador` as the country, Odoo automatically
installs the base module Ecuadorian - Accounting.

<a id="l10n-ec-configure-your-company"></a>

### Cấu hình công ty của bạn

To configure your company information, go to the Contacts app and search the name given
to your company or activate [developer mode](../../general/developer_mode.md#developer-mode) and go to Company
‣ Contact and then edit the contact to configure the following information:

1. Check the Company option on top
   - Tên
   - Địa chỉ
   - Identification Number
   - Taxpayer Type
   - Điện thoại
   - Email
2. Upload company logo and save

![Populate company data for Ecuador in Odoo Contacts.](applications/finance/fiscal_localizations/ecuador/ecuador-company.png)

### Chứng từ điện tử

To upload your information for electronic documents go to Accounting ‣
Configuration ‣ Settings and search for **Ecuadorian Localization**.

Configure the next information:

- Tên pháp lý của công ty
- Use production servers: check the checkbox if your company is going to do electronic
  documents in the production environment. If you want to use the testing environment for electronic
  documents then keep the checkbox unchecked.
- Regime: select if your company is in General Regular or is qualified as RIMPE.
- Forced to keep accounting books: check the checkbox if your company has this
  condition.
- Default taxes for withholdings
- Issue withholds: check the checkbox if your company is going to do electronic
  withholds.
- Withhold consumibles: put the code of the withholding for when you buy goods.
- Withhold services: put the code of the withholding for when you buy services.
- Withhold credit card: put the code of the withholding for when you buy with credit
  card
- Withhold agent number: put the company withholding agent resolution number, if
  applicable for your company.
- Electronic Certificate File: upload electronic certificate and password, then save it.
- Special tax contributor number: if your company is qualified as a special taxpayer,
  fill out this field with it's corresponding tax contributor number.

![Electronic signature for Ecuador.](applications/finance/fiscal_localizations/ecuador/electronic-signature.png)

#### NOTE
When configuring the withholdings in the configuration menu, these suggested withholdings are
only for domestic suppliers when no withholdings are setup on their *Taxpayer Type*. Moreover,
the Credit Card withholding set up is always used when a Credit or Debit Card SRI Payment Metho
is used.

### VAT withholding

This configuration only applies if you are qualified as a *Withholding Agent* by the SRI, otherwise
skip this step. To configure your VAT withholding, go to Accounting ‣ Accounting
‣ Configuration ‣ Ecuadorian SRI: Taxpayer Type SRI.

You must configure the withholding percentage that applies for each type of taxpayer, specify the
Goods VAT Withholding and the Services VAT Withholding.

![Taxpayer Type configuration for Ecuador.](applications/finance/fiscal_localizations/ecuador/contributor-type.png)

### Printer points

To configure your printer points, go to Accounting ‣ Configuration ‣ Accounting:
Journals.

Printer points need to be configured for each type of electronic document that you need. For
example: Customer Invoice, Credit Notes, and Debit Notes

For each printer point, you need to configure the following information:

- Journal Name: in this format `[Emission Entity]-[Emission Point] [Document Type]`, for
  example: `001-001 Sales Documents`.
- Type: refers to the type of journal, select `Sales`.
- Use Documents?: this checkbox is automatically checked, leave it checked.
- Emission Entity: configure the establishment number.
- Emission Point: configure the printer point.
- Emission address: configure the address of the establishment.
- Default income account: configure the default income account.
- Dedicated Credit Note Sequence: check the checkbox if *Credit Notes* are to be
  generated from this printer point - journal.
- Short Code: This is the unique code for the sequence of accounting entries, enter a
  unique 5-digit code, for example: `VT001`

Customer Invoice, Credit Notes and Debit Notes need to use the same journal as the
Emission Point, and the Entity Point should be unique per journal.

![Configuring a printer point for Ecuador electronic document type of Customer Invoices.](applications/finance/fiscal_localizations/ecuador/printer-point.png)

#### NOTE
In the Advanced Settings tab, check the Electronic Invoicing checkbox to
enable it for Ecuador.

#### SEE ALSO
[Electronic invoicing (EDI)](../accounting/customer_invoices/electronic_invoicing.md)

### Withholding

A Withholding Journal must be defined, go to go to Accounting ‣ Configuration ‣
Accounting:  Journals where you need to configure the following information:

- Journal Name: in this format `[Emission Entity]-[Emission Point] [Document Type]`, for
  example: `001-001 Withholding`.
- Type: refers to the type of journal, select `Miscellaneous`.
- Withhold Type: Configure Purchase Withholding.
- Use Documents?: this checkbox is automatically checked, leave it checked.
- Emission Entity: configure the establishment number.
- Emission Point: configure the printer point.
- Emission address: configure the address of the establishment.
- Default account: configure the default income account.
- Short Code: This is the unique code for the sequence of accounting entries, enter a
  unique 5-digit code, for example: `RT001`

![Configuring withholding for Ecuador electronic document type of Withholding.](applications/finance/fiscal_localizations/ecuador/withhold.png)

#### NOTE
In the Advanced Settings tab, check the Electronic Invoicing checkbox to
enable the sending of electronic invoicing for the withholding.

### Purchase Liquidations

When using Purchase Liquidations, a specific journal must be created, go to
Accounting ‣ Configuration ‣ Accounting:  Journals and configure the following
information:

- Journal Name: in this format `[Emission Entity]-[Emission Point] [Document Type]`, for
  example: `001-001 Withhold`.
- Type: refers to the type of journal, select `Miscellaneous`.
- Purchase Liquidations: check the checkbox to enable purchase liquidations.
- Use Documents?: this checkbox is automatically checked, leave it checked.
- Emission Entity: configure the establishment number.
- Emission Point: configure the printer point.
- Emission address: configure the address of the establishment.
- Short Code: This is the unique code for the sequence of accounting entries, enter a
  unique 5-digit code, for example: `RT001`

![Configuring purchase liquidations for Ecuador electronic document type of Withholding.](applications/finance/fiscal_localizations/ecuador/purchase-liqudations.png)

#### NOTE
In the Advanced Settings tab, check the Electronic Invoicing checkbox to
enable the sending of electronic invoicing for the withholding.

### Configure master data

#### Hệ thống tài khoản

The [chart of accounts](../accounting/get_started/chart_of_accounts.md)
is installed by default as part of the set of data included in the localization module, the accounts
are mapped automatically in Taxes, Default Account Payable, Default Account Receivable.

The chart of accounts for Ecuador is based on the most updated version of Superintendency of
Companies, which is grouped in several categories and is compatible with NIIF accounting.

You can add or delete accounts according to the company's needs.

#### Sản phẩm

In addition to the basic information in your products, you must add the configuration of the
withholding code (tax) that applies.

Go to Accounting ‣ Vendors:  Products under the tab "Purchase"

![Sản phẩm dành cho Ecuador.](applications/finance/fiscal_localizations/ecuador/products.png)

#### Liên hệ

Configure the next information when you create a contact:

- Check the Company option on top if it is a contact with RUC, or check
  Individual if it is a contact with cedula or passport.
- Tên
- Address: Street is a required field to confirm the Electronic Invoice.
- Identification Number: select an identification type `RUC`, `Cedula`, or `Passport`.
- Taxpayer Type: select the contact's SRI Taxpayer Type.
- Điện thoại
- Email

![Liên hệ dành cho Ecuador.](applications/finance/fiscal_localizations/ecuador/contacts.png)

#### NOTE
The SRI Taxpayer Type has inside the configuration of which VAT and Profit
withholding will apply when you use this contact on Vendor Bill, and then create a withholding
from there.

#### Xem lại thuế của bạn

As part of the localization module, taxes are automatically created with its configuration and
related financial accounts.

![Thuế dành cho Ecuador.](applications/finance/fiscal_localizations/ecuador/taxes.png)

The following options have been automatically configured:

- Tax Support: to be configured only in the IVA tax, this option is useful when you
  register purchase withholdings.
- Code ATS: to be configured only for income tax withholding codes, it is important when
  you register the withholding.
- Tax Grids: configure the codes of 104 form if it is a IVA tax and configure the codes
  of 103 form if it is a  income tax withholding code.
- Tên thuế:
  - For IVA tax, format the name as: `IVA [percent] (104, [form code] [tax support code] [tax
    support short name])`
  - For income tax withholding code, format the name as: `Code ATS [Percent of withhold] [withhold
    name]`

Once the Ecuador module is installed, the most common taxes are automatically configured. If you
need to create an additional one, you can do so, for which you must base yourself on the
configuration of the existing taxes.

![Taxes with tax support for Ecuador.](applications/finance/fiscal_localizations/ecuador/taxes-with-tax-support.png)

#### Review your Document Types

Some accounting transactions like *Customer Invoices* and *Vendor Bills* are classified by document
types. These are defined by the government fiscal authorities, in this case by the SRI.

Each document type can have a unique sequence per journal where it is assigned. As part of the
localization, the document type includes the country on which the document is applicable; also the
data is created automatically when the localization module is installed.

The information required for the document types is included by default so the user does not need to
fill anything there.

![Document types for Ecuador.](applications/finance/fiscal_localizations/ecuador/document-types.png)

## Quy trình

Once you have configured your database, you can register your documents.

### Sales documents

#### Hóa đơn bán hàng

Customer invoices are electronic documents that, when validated, are sent to SRI. These
documents can be created from your sales order or manually. They must contain the following data:

- Customer: type the customer's information.
- Journal: select the option that matches the printer point for the customer invoice.
- Document Type: type document type in this format `(01) Invoice`.
- Payment Method (SRI): select how the invoice is going to be paid.
- Products: specify the product with the correct taxes.

![Customer invoice for Ecuador.](applications/finance/fiscal_localizations/ecuador/customer-invoice.png)

#### Giấy báo có khách hàng

The [Customer credit note](../accounting/customer_invoices/credit_notes.md) is an
electronic document that, when validated, is sent to SRI. It is necessary to have a validated
(posted) invoice in order to register a credit note. On the invoice there is a button named
Credit note, click on this button to be directed to the Create credit note
form, then complete the following information:

- Credit Method: select the type of credit method.
  - Partial Refund: use this option when you need to type the first number of documents
    and if it is a partial credit note.
  - Full Refund: use this option if the credit note is for the total invoice and you
    need the credit note to be auto-validated and reconciled with the invoice.
  - Full refund and new draft invoice: use this option if the credit note is for the
    total invoice and you need the credit note to be auto-validated and reconciled with the invoice,
    and auto-create a new draft invoice.
- Reason: type the reason for the credit note.
- Rollback Date: select the specific options.
- Reversal Date: type the date.
- Use Specific Journal: select the printer point for your credit note, or leave it empty
  if you want to use the same journal as the original invoice.

Once reviewed, you can click on the Reverse button.

![Add Customer Credit Note for Ecuador.](applications/finance/fiscal_localizations/ecuador/add-customer-credit-note.png)

When the Partial Refund option is used, you can change the amount of the credit note and
then validate it. Before validating the credit note, review the following information:

- Customer: type the customer's information.
- Journal: select the printer point for the customer Credit Note.
- Document Type: this is the document type `(04) Credit Note`.
- Products: It must specify the product with the correct taxes.

![Customer Credit Note for Ecuador.](applications/finance/fiscal_localizations/ecuador/customer-credit-note.png)

#### Giấy báo nợ khách hàng

The Customer debit note is an electronic document that, when validated, is sent to SRI.
It is necessary to have a validated (posted) invoice in order to register a debit note. On the
invoice there is a button named Debit Note, click on this button to be directed to the
Create debit note form, then complete the following information:

- Reason: type the reason for the debit note.
- Debit note date: select the specific options.
- Copy lines: select this option if you need to register a debit note with the same
  lines of invoice.
- Use Specific Journal: select the printer point for your credit note, or leave it empty
  if you want to use the same journal as the original invoice.

Once reviewed you can click on the Create Debit Note button.

![Add Customer Debit Note for Ecuador.](applications/finance/fiscal_localizations/ecuador/add-customer-debit-note.png)

You can change the debit note amount, and then validate it. Before validating the debit note, review
the following information:

- Customer: type the customer's information.
- Journal: select the printer point for the customer Credit Note.
- Document Type: this is the document type `(05) Debit Note`.
- Products: It must specify the product with the correct taxes.

![Customer Debit Note for Ecuador.](applications/finance/fiscal_localizations/ecuador/customer-debit-note.png)

#### Customer withholding

The Customer withholding is a non-electronic document for your company, this document is
issued by the client in order to apply a withholding to the sale.

It is necessary to have a validated (posted) invoice in order to register a customer withholding. On
the invoice there is a button named Add Withhold,  click on this button to be directed
to the Customer withholding form, then complete the following information:

- Document Number: type the withholding number.
- Withhold Lines: select the taxes that the customer is withholding.

Before validating the withholding, review that the amounts for each tax are the same as the original
document.

![Customer withhold for Ecuador.](applications/finance/fiscal_localizations/ecuador/customer-withhold.png)

### Purchase Documents

#### Hóa đơn mua hàng

The Vendor bill is a non-electronic document for your company, this document is issued
by your vendor when your company generates a purchase.

The bills can be created from the purchase order or manually, it must contain the following
information:

- Vendor: type the vendor's information.
- Bill Date: select the date of invoice.
- Journal: it is the journal for vendor bills.
- Document Type: this is the document type `(01) Invoice`
- Document number: type the document number.
- Payment Method (SRI): select how the invoice is going to be paid.
- Products: specify the product with the correct taxes.

![Mua hàng dành cho Ecuador.](applications/finance/fiscal_localizations/ecuador/purchase-invoice.png)

#### IMPORTANT
When creating the purchase withholding, verify that the bases (base amounts) are correct. If you
need to edit the amount of the tax in the Vendor bill, click the Edit
button. Otherwise, from the Journal Items tab click the Edit button and
set the adjustment to go where you want.

#### Purchase liquidation

The Purchase liquidation is an electronic document that, when validated, is sent to SRI.

Companies issue this type of electronic document when they purchase, and the vendor does not issue
an invoice due to one or more of the following cases:

- Services were provided by non-residents of Ecuador.
- Services provided by foreign companies without residency or establishment in Ecuador.
- Purchase of goods or services from natural persons not registered with a RUC, who due to their
  cultural level or hardiness are not able to issue sales receipts or customer invoices.
- Reimbursement for the purchase of goods or services to employees in a dependency relationship
  (full-time employee).
- Services provided by members of collegiate bodies for the exercise of their function.

These types of electronic documents can be created from the Purchase Order or manually
from the Vendor Bills form view. It must contain the following data:

- Vendor: type the vendor's information.
- Journal: select the journal for the Purchase Liquidation with the correct
  printer point.
- Document Type: this is the document type `(03) Purchase Liquidation`
- Document number: type the document number (sequence), you will only have to do this
  once, then the sequence will be automatically assigned for the next documents.
- Payment Method (SRI): select how the invoice is going to be paid.
- Products: specify the product with the correct taxes.

Once you review the information you can validate the Purchase Liquidation.

![Purchase liquidation for Ecuador.](applications/finance/fiscal_localizations/ecuador/purchase-liquidation.png)

#### Purchase withholding

The Purchase withholding is an electronic document that, when validated, is sent to SRI.

It is necessary to have an invoice in a validated state in order to register a Purchase
withholding. On the invoice, there is a button named Add Withhold, click on this button
to be directed to the Withholding form, then complete the following information:

- Document number: type the document number (sequence), you will only have to do this
  once, then the sequence will be automatically assigned for the next documents.
- Withhold lines: The taxes appear automatically according to the configuration of
  products and vendors, you should review if the taxes and tax support are correct, and, if it is
  not correct, you can edit and select the correct taxes and tax support.

Once you review the information you can validate the Withholding.

![Purchase withhold for Ecuador.](applications/finance/fiscal_localizations/ecuador/purchase-withhold.png)

#### NOTE
You can't change the tax support for one that was not included in the configuration of the taxes
used on the Vendor Bill. To do so, go to the tax applied on the Vendor
Bill and change the Tax Support there.

A withholding tax can be divided into two or more lines, this will depend on whether two or more
withholdings percentages apply.

### thương mại điện tử

The [ATS Report module](#ecuador-ats) enables the following:

- Choose the SRI Payment Method in each payment method's configuration.
- Customers can manually input their identification type and identification number during the
  eCommerce checkout process.
- Automatically generate a valid electronic invoice for Ecuador at the end of the checkout process.

#### Cấu hình

##### Trang web

To generate an invoice after the checkout process, navigate to Website ‣
Configuration ‣ Settings and activate the Automatic Invoice option found under the
Invoicing section.

#### IMPORTANT
The sales journal used for invoicing is the first in the sequence of priority in the
Journal menu.

##### Nhà cung cấp dịch vụ thanh toán

To activate the payment providers that should be used to capture eCommerce payments, navigate to
Website ‣ Configuration ‣ Payment Providers section and then click on the
View other providers button under the Activate Payments heading. From here,
each payment provider can be configured by selecting a provider record. Refer to the [payment
provider](../payment_providers.md) documentation for more information.

###### Phương thức thanh toán

To activate one or more payment methods for a payment provider, click → Enable Payment
Methods within the Configuration tab of each provider.

When configuring the payment method, it is **mandatory** to set the SRI Payment Method
for each method. This field appears after you create and save the payment method for the first
time.

#### NOTE
Adding the SRI Payment Method is necessary to generate correctly the electronic
invoice from an eCommerce sale. Select a **payment method** to access its configuration menu and
the field.

#### SEE ALSO
[Nhà cung cấp dịch vụ thanh toán](../payment_providers.md)

![l10n_ec SRI Payment Method.](applications/finance/fiscal_localizations/ecuador/l10n-ec-sri-payment-method.png)

#### eCommerce workflow

##### Identification type and number

The client who is making a purchase will have the option to indicate their identification type and
number during the checkout process. This information is required to correctly generate the
electronic invoice after the checkout is completed.

![Biểu mẫu thanh toán trên trang web.](applications/finance/fiscal_localizations/ecuador/website-checkout-form.png)

#### NOTE
Verification is done to ensure the Identification Number field is completed and has
the correct number of digits. For RUC identification, 13 digits are required. For Cédula,
9 digits are required.

After finishing the checkout process, a confirmed invoice is generated, ready to be sent manually or
asynchronously to the SRI.

### Point of Sale electronic invoicing

Make sure the *Ecuadorian module for Point of Sale* (`l10n_ec_edi_pos`) is [installed](#l10n-ec-module-installation) to enable the following features and configurations:

- Choose the SRI payment method in each payment method configuration.
- Manually input the customer's identification type and identification number when creating a
  new contact on *POS*.
- Automatically generate a valid electronic invoice for Ecuador at the end of the checkout process.

#### Cấu hình phương thức thanh toán

To [create a payment method for a point of sale](../../sales/point_of_sale/payment_methods.md),
go to Point of Sale ‣ Configuration ‣ Payment Methods. Then, set the
SRI Payment Method in the payment method form.

#### Chu trình lập hóa đơn

##### Identification type and number

The POS cashier can [create a new contact for a customer](../../sales/point_of_sale.md#pos-customers) who requests an
invoice from an open POS session.

The *Ecuadorian Module for Point of Sale* adds two new fields to the contact creation form:
Identification Type and Tax ID.

#### NOTE
As the identification number length differs depending on the identification type, Odoo
automatically checks the Tax ID field upon saving the contact form. To manually
ensure the length is correct, know that the RUC and Citizenship types
require 13 and 10 digits, respectively.

##### Electronic invoice: anonymous end consumer

When clients do not request an electronic invoice for their purchase, Odoo automatically sets the
customer as Consumidor Final and generates an electronic invoice anyway.

#### NOTE
If the client requests a credit note due to a return of this type of purchase, the credit note
should be made using the client's real contact information. Credit notes cannot be created to
*Consumidor Final* and can be managed [directly from the POS session](../../sales/point_of_sale.md#pos-refund).

##### Electronic invoice: specific customer

If a customer requests an invoice for their purchase, it is possible to select or create a contact
with their fiscal information. This ensures the invoice is generated with accurate customer details.

#### NOTE
If the client requests a credit note due to a return of this type of purchase, the credit note
and return process can be managed [directly from the POS session](../../sales/point_of_sale.md#pos-refund).

## Báo cáo tài chính

In Ecuador, there are fiscal reports that the company presents to SRI. Odoo supports two of the main
financial reports used by companies: **reports 103** and **104**.

To get these reports, go to the **Accounting** app and select Reporting ‣
Statements Reports ‣ Tax Report and then filter by `Tax Report 103` or `Tax Report 104`.

### Báo cáo 103

This report contains information of income tax withholdings in a given period, this can be reported
monthly or semi-annually.

You can see the information needed to report, which includes base and tax amounts, but also includes
the tax code within the parenthesis in order to report it to the SRI.

![Report 103 form for Ecuador.](applications/finance/fiscal_localizations/ecuador/103-form.png)

### Báo cáo 104

This report contains information on VAT tax and VAT withholding for a given period, this can be
monthly or semi-annually.

You can see the information needed to report, which includes base and tax amounts, but also includes
the tax code within the parenthesis to report it to the SRI.

![Report 104 form for Ecuador.](applications/finance/fiscal_localizations/ecuador/104-form.png)

<a id="ecuador-ats"></a>

### Báo cáo ATS

[Install](../../general/apps_modules.md#general-install) the *ATS Report* (`l10n_ec_reports_ats`) module to enable
downloading the ATS report in XML format.

#### NOTE
The Ecuadorian *ATS Report* module depends on the previous installation of the *Accounting* app
and the *Ecuadorian EDI module*.

#### Cấu hình

To issue electronic documents, ensure your company is configured as explained in the
[electronic invoice](#l10n-ec-configure-your-company) section.

In the , every document generated in Odoo (invoices,
vendor bills, sales and purchases withholdings, credit notes, and debit notes) will be included.

##### Vendor bills

When generating a vendor bill, it is necessary to register the authorization number from the
invoice that the vendor generated for the purchase. To do so, go to Accounting
‣ Vendors ‣ Bills and select the bill. Then, enter the number from the vendor's invoice in the
Authorization Number field.

##### Credit and debit notes

When generating a credit note or debit note manually or through importation, it is necessary to link
this note to the sales invoice that is being modified by it.

#### NOTE
Remember to add all required information to the documents before downloading the  file. For example, add the *Authorization Number* and the
*SRI Payment Method* on documents, when needed.

#### Tạo XML

To generate the  report, go to
Accounting ‣ Reports ‣ Tax Report and choose a time period for the desired
 report, then click ATS.

The downloaded XML file is ready to be uploaded to *DIMM Formularios*.

![ATS report download for Ecuador in Odoo Accounting.](applications/finance/fiscal_localizations/ecuador/ats-report.png)

#### NOTE
When downloading the  report, Odoo generates a
warning pop-up alerting the user if a document(s) has missing or incorrect data. Nevertheless,
the user can still download the XML file.
