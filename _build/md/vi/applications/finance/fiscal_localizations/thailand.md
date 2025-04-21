# Thái Lan

## Cấu hình

[Install](../../general/apps_modules.md#general-install) the 🇹🇭 Thailand localization package to get all the
features of the Thai localization:

| Tên                           | Tên kỹ thuật      | Mô tả                                                                                           |
|-------------------------------|-------------------|-------------------------------------------------------------------------------------------------|
| Thái Lan - Kế toán            | `l10n_th`         | Default [fiscal localization package](../fiscal_localizations.md#fiscal-localizations-packages) |
| Thailand - Accounting Reports | `l10n_th_reports` | Country-specific accounting reports                                                             |
![Thailand localization modules](applications/finance/fiscal_localizations/thailand/modules.png)

## Chart of accounts and taxes

Odoo's fiscal localization package for Thailand includes the following taxes:

- Thuế GTGT 7%
- miễn thuế GTGT
- Withholding tax
- Withholding income tax

## Báo cáo thuế

Odoo allows users to generate Excel files to submit their VAT to the **Revenue Department** of
Thailand.

### Sales and purchase tax report

To generate a sales and purchase tax report, go to Accounting ‣ Reporting ‣ Tax
Report. Select a specific time or time range on the tax report, and click
VAT-202-01 (xlsx) for purchase tax and VAT-202-02 (xlsx) for sales tax.

![Thai purchase and sales taxes reports](applications/finance/fiscal_localizations/thailand/tax-report.png)

### Withholding PND tax report

PND report data displays the summarized amounts of the applicable **withholding corporate income
tax returns (domestic)** from vendor bills under the PND53 (TH) and
PND3 (TH) tax reports. It is installed by default with the Thai localization.

![PND tax reports](applications/finance/fiscal_localizations/thailand/pnd-report.png)

#### NOTE
Withholding corporate income tax returns (domestic) is the tax used in case the company has
withheld the tax from “**Personal (PND3)**” or “**Corporate (PND53)**” services provided such as
rental, hiring, transportation, insurance, management fee, consulting, etc.

The PND tax report allows users to generate a CSV file for bills to upload on the
[RDprep for Thailand e-Filling application](https://efiling.rd.go.th/rd-cms/).

To generate a PND CSV file, go to Accounting ‣ Reporting ‣ Tax Report, select a
specific time or time range on the tax report, and click PND3 or PND53.

This generates the `Tax Report PND3.csv` and `Tax Report PND53.csv` files that lists all
the vendor bill lines with the applicable withholding tax.

![PND3 and PND53 CSV files](applications/finance/fiscal_localizations/thailand/pnd3-pnd53.png)

#### WARNING
Odoo cannot generate the PND or PDF report or **withholding tax certificate** directly. The
generated `Tax Report PND3.csv` and `Tax Report PND53.csv` files must be exported
to an external tool to convert them into a **withholding PND** report or a **PDF** file.

## Tax invoice

Báo cáo **hóa đơn thuế PDF** có thể được tạo từ Odoo thông qua phân hệ **Hóa đơn**. Người dùng có tùy chọn in báo cáo PDF cho hóa đơn thông thường và hóa đơn thuế. Để in **hóa đơn thuế**, người dùng có thể nhấp vào In hóa đơn trong Odoo. Hóa đơn thông thường có thể được in dưới dạng **hóa đơn thương mại** bằng cách nhấp vào Nút bánh răng (⚙️) ‣ In ‣ Hóa đơn thương mại.

![Commercial invoice printing](applications/finance/fiscal_localizations/thailand/tax-invoice.png)

### Headquarter/Branch number settings

You can inform a company's **Headquarters** and **Branch number** in the **Contacts** app. Once
in the app, open the **contact form** of the company and under the Sales & Purchase tab:

- If the contact is identified as a branch, input the **Branch number** in the
  Company ID field.
- If the contact is a **Headquarters**, leave the Company ID field **blank**.

![Company Headquarter/Branch number](applications/finance/fiscal_localizations/thailand/contact.png)

## PromptPay QR code on invoices

The **PromptPay QR code** is a QR code that can be added to invoices to allow customers to pay their
bills using the PromptPay-supported bank mobile application. The QR code is generated based on the
**invoice amount** and one of the following **merchant information**:

- Ewallet ID
- Merchant Tax ID
- Mobile Number

### Kích hoạt mã QR

Go to Accounting ‣ Configuration ‣ Settings. Under the Customer
Payments section, activate the QR Codes feature.

### PromptPay QR bank account configuration

Go to Contacts ‣ Configuration ‣ Bank Accounts and select the bank account for
which you want to activate PromptPay QR. Set the Proxy Type and fill in the
Proxy Value field depending on the chosen type.

#### IMPORTANT
- The account holder's city is mandatory.
- The Include Reference checkbox doesn't work for PromptPay QR codes.

![PromptPay bank account configuration](applications/finance/fiscal_localizations/thailand/qr-promptpay-bank.png)

#### SEE ALSO
[Bank and cash accounts](../accounting/bank.md)

### Cấu hình sổ nhật ký ngân hàng

Go to Accounting ‣ Configuration ‣ Journals, open the bank journal, then fill
in the Account Number and Bank under the Journal Entries tab.

![Bank Account's journal configuration](applications/finance/fiscal_localizations/thailand/qr-bank-journal.png)

### Issue invoices with PromptPay QR code

When creating a new invoice, open the Other Info tab and set the Payment
QR-code option to EMV Merchant-Presented QR-code.

![Select EMV Merchant-Presented QR-code option](applications/finance/fiscal_localizations/thailand/qr-code-invoice-emv.png)

Ensure that the Recipient Bank is the one you configured, as Odoo uses this field to
generate the PromptPay QR code.
