# Việt Nam

<a id="localizations-vietnam-modules"></a>

## Mô đun

The following modules are installed automatically with the Vietnamese localization:

| Tên                   | Tên kỹ thuật          | Mô tả                                                                                                        |
|-----------------------|-----------------------|--------------------------------------------------------------------------------------------------------------|
| Vietnam - Accounting  | `l10n_vn`             | This module includes the default<br/>[fiscal localization package](./#fiscal-localizations-packages).        |
| Vietnam - E-invoicing | `l10n_vn_edi_viettel` | This module includes the features required for integration with [SInvoice](#localizations-vietnam-sinvoice). |

#### NOTE
In some cases, such as when upgrading to a version with additional modules, it is possible that
modules may not be installed automatically. Any missing modules can be manually [installed](../../general/apps_modules.md#general-install).

<a id="localizations-vietnam-company"></a>

## Công ty

To use all the features of this fiscal localization, the following fields are required on the
[company record](../../general/companies/):

- Tên
- Address, including the City, State, Zip Code,
  and Country.
  > - In the Street field, enter the street name, number, and any additional address
  >   information.
  > - In the Street 2 field, enter the neighborhood.
- Tax ID: tax identification number.

<a id="localizations-vietnam-sinvoice"></a>

## E-invoicing with SInvoice

[SInvoice](https://www.sinvoice.vn/) is an e-invoice service platform provided by Viettel, one of the biggest e-invoice service
providers in Vietnam. Odoo supports integration with SInvoice to submit invoices generated in Odoo.

### Cấu hình

#### Nền tảng SInvoice

To send electronic invoices to SInvoice, the following must be created on [SInvoice](https://www.sinvoice.vn/):

- [SInvoice account](#localizations-vietname-sinvoice-registration)
- [Invoice template](#localizations-vietname-sinvoice-template)
- [Invoice symbol](#localizations-vietname-sinvoice-symbol)
- [Invoice issuance notice](#localizations-vietname-sinvoice-notice)

<a id="localizations-vietname-sinvoice-registration"></a>

##### Đăng ký SInvoice

To create an account, go to [SInvoice](https://www.sinvoice.vn/) and register for the desired plan. Fill in the form that
opens to be contacted by [SInvoice](https://www.sinvoice.vn/) to create an account.

Once you have an account, log into [SInvoice](https://www.sinvoice.vn/) using your Username and
Password.

<a id="localizations-vietname-sinvoice-template"></a>

##### Invoice template creation

1. On the left side of the overview page, in the Release management menu, click
   Create business information.
2. In the Update key information step, fill in the following fields and other optional
   information if needed: Unit name, Address, Contact person,
   Type of representative documents.
3. Click Update.
4. In the Look up digital certificate step, click Add new to add a digital
   certificate.
5. Select the Branch/Enterprise and the Type of digital certificate, then
   fill in the required fields for each type:
   > - Nhà cung cấp: CloudCA
   > - Signer ID: CloudCA
   > - Digital Certificate: CloudCA
   > - How to download file: HSM
   > - File Upload: HSM, USB-TOKEN
6. Click Generate key pair to generate encryption keys for authentication, and
   Save.
7. In the Manage invoice templates step, add a new Invoice template.
8. Select the Invoice type and fill in the Invoice template code,
   Invoice template name, and other optional information if needed.
9. Click Update.

#### SEE ALSO
[SInvoice documentation on electronic invoice template creation](https://www.sinvoice.vn/2021/02/hdsd-tai-lieu-nghiep-vu-tao-mau-hoa-don-dien-tu.html?debug=1)

<a id="localizations-vietname-sinvoice-symbol"></a>

##### Invoice symbol creation

On the left side of the main screen, in the Release management menu, click
Invoice symbol and follow these steps:

1. Click Add new and select the Invoice template.
2. Set the Status to Active to activate the symbol and fill in the
   Invoice symbol.
3. Enable Stop automatic sending to tax authorities and Default for built-in
   API based on preference.
4. Nhấp Lưu.

<a id="localizations-vietname-sinvoice-notice"></a>

##### Invoice issuance notice

On the left side of the main screen, in the Release management menu, click
Create issuance notice and follow these steps:

1. Click Add new, select the Name of the business unit to issue an e-invoice
   and the Tax agency name. Based on the business unit and tax agency selected, the
   Tax code, Address, Phone number, and Separator
   used are automatically filled and uneditable.
2. Click Select the invoice type for issuance, and then select and fill in the
   following information :
   - Invoice type: The invoice type on which to declare an issuance notice.
   - Invoice template: Select from the list of templates available based on the invoice
     type.
   - Symbol: Select from the list of symbols available based on the invoice type.
   - Quantity: Total number of invoices to issue for the selected type. Based on the
     type and template selected, this field is filled in automatically. It can be changed if needed.
   - Start date of use: The date from which the invoice template, range, and quantity
     are used for the issuance notice.
3. Click Save and select more invoice types if necessary by repeating the steps above.
   Click Save to finish drafting the notice.
4. Click Send to tax authorities for approval. Once approved, the notice's
   Status is changed to Active.

<a id="localizations-vietnam-sinvoice-odoo"></a>

#### Cơ sở dữ liệu Odoo

##### Link Odoo to SInvoice

To connect Odoo with SInvoice, go to Accounting ‣ Configuration ‣ Settings.
In the Vietnamese Integration section, fill in your SInvoice Username and
Password. Add a Default symbol to generate a prefix for the invoice number
managed in SInvoice if needed.

##### Mẫu hóa đơn

Để tạo mẫu SInvoice, đi tới Kế toán ‣ Cấu hình ‣ Mẫu. Nhấp vào Mới và thêm Mã mẫu cùng Loại hóa đơn mẫu. Mã mẫu là dãy số đầu tiên trong tên được SInvoice gán. Ví dụ, nếu mẫu hóa đơn là `1/001 - Hóa đơn GTGT - ND123`, thì Mã mẫu là `1/001`. Các mẫu SInvoice trong Odoo phải khớp với các mẫu trong SInvoice.

To add Invoice Symbols, click Add a new line.

### Sending invoices to SInvoice

Invoices can be sent to SInvoice once they have been confirmed. To do so, follow the
[invoice sending](../accounting/customer_invoices/#accounting-invoice-sending) steps. In the Send popup, enable
Send to SInvoice and click Send & Print.

Once the invoice has been successfully submitted to SInvoice, the SInvoice Status field
in the SInvoice tab of the invoice is updated to Sent. The
SInvoice Number, Issue Date, Secret Code and eInvoice
Number fields are also updated. The same information is available on SInvoice.

#### Replacement or adjustment invoices

A replacement invoice is issued to correct an invoice that has **yet to be tax declared**, whereas
an adjustment invoice is issued to correct one that has **already been tax declared**. Follow these
steps to issue a replacement or adjustment invoice:

1. Open the invoice and click Credit Note.
2. In the Credit Note popup, fill in the following fields:
   - Reason displayed on Credit Note
   - Adjustment type
   - Agreement Name
   - Agreement Date
   - Sổ nhật ký
   - Reversal date
3. Click Reverse and Create Invoice to issue a replacement invoice, or
   Reverse to issue an adjustment invoice.

The SInvoice Status in the SInvoice invoice tab is updated to
Replaced for a replacement invoice or Adjusted for an adjustment invoice.

#### Huỷ hoá đơn

If an invoice needs to be canceled, open the invoice and click Request Cancel. In the
Invoice Cancellation popup, enter the cancellation Reason,
Agreement Name, and Agreement Date, and click Request
Cancellation.

The SInvoice Status in the SInvoice invoice tab is updated to
Canceled.

<a id="localizations-vietnam-qrcode"></a>

## QR banking codes

Vietnamese QR banking is a payment service platform that allows customers to make instant domestic
payments to individuals and merchants in Vietnamese dong via online and mobile banking.

### Cấu hình

To activate QR banking codes, go to Accounting ‣ Configuration ‣ Settings and
enable QR Codes in the Customer Payments section.

#### Tài khoản Ngân hàng

To activate QR banking for a bank account, go to Contacts ‣ Configuration ‣
Bank Accounts and select the bank account. Fill in the Bank Identifier Code,
Proxy Type (based on the information used to identify the Merchant Account,
such as the card number and bank account numbers), and Proxy Value fields.

Enable Include Reference to include the invoice number in the QR code.

#### IMPORTANT
- The account holder's country must be set to `Vietnam`, and their city must be specified on the
  contact form.
- The [account number](../accounting/bank/#accounting-bank-account-number) and bank must be set on the
  Bank journal.

#### SEE ALSO
[Bank and cash accounts](../accounting/bank/)

### Generating QR codes on invoices

When creating a new invoice, open the Other Info tab and select EMV
Merchant-Presented QR-code in the Payment QR-code field.

#### NOTE
Ensure the Recipient Bank is configured, as Odoo uses this field to generate QR
codes.
