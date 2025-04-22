# Ả Rập Xê Út

## Cấu hình

[Install](applications/general/apps_modules.md#general-install) the following modules to get all the features of the Saudi Arabian
localization:

| Tên                           | Tên kỹ thuật   | Mô tả                                                                                                             |
|-------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------|
| Ả Rập Xê Út - Kế toán         | `l10n_sa`      | Default [fiscal localization package](applications/finance/fiscal_localizations.md#fiscal-localizations-packages) |
| Ả Rập Xê Út - Hoá đơn điện tử | `l10n_sa_edi`  | Triển khai hóa đơn điện tử ZATCA                                                                                  |
| Ả Rập Xê Út - POS             | `l10n_sa_pos`  | Point of Sale compliance                                                                                          |

## ZATCA e-invoices

The ZATCA e-invoicing system is designed to streamline and digitize the invoicing process for
businesses operating in Saudi Arabia.

#### SEE ALSO
[ZATCA e-invoicing page](https://zatca.gov.sa/en/E-Invoicing/Pages/default.aspx)

### Thông tin công ty

Go to Settings ‣ General Settings ‣ Companies, click Update info,
and ensure the following company information is complete and up-to-date.

- The full Company Name.
- All relevant Address fields, including the Building Number and
  Plot Identification (four digits each).
- Select an enterprise Identification Scheme. It is recommended to use the
  Commercial Registration Number.
- Enter the Identification Number for the selected Identification Scheme.
- Mã số thuế GTGT.
- Ensure the Currency is set to SAR.

#### NOTE
It is also necessary to fill out similar information for partner companies.

### Simulation mode

#### IMPORTANT
It is strongly recommended to thoroughly test all invoicing workflows using the Fatoora
**simulation** portal first, as **any** invoice submitted to the regular Fatoora portal will be
accounted for, which could lead to fines and penalties.

#### Fatoora simulation portal

Log in on the [Fatoora portal](https://fatoora.zatca.gov.sa/) using the company's ZATCA
credentials. Then, click the Fatoora Simulation Portal button to switch to the
simulation portal.

#### SEE ALSO
[ZACTA Fatoora portal user manual version 3 (May 2023)](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf)

<a id="saudi-arabia-api-mode"></a>

#### Tích hợp API ZATCA

On Odoo, go to Accounting ‣ Configuration ‣ Settings. Under ZATCA
API Integration, select the Simulation (Pre-Production) API mode and click
Save.

<a id="saudi-arabia-journals"></a>

#### Sổ nhật ký bán hàng

Each sales journal on Odoo needs to be configured. To do so, go to Accounting ‣
Configuration ‣ Journals, open any sales journal (e.g., Customer Invoices), and go to the
ZATCA tab. Once there, enter any Serial Number to identify the journal.

#### NOTE
The same serial number can be used for all of the company's sales journals.

Tiếp theo, nhấp Onboard sổ nhật ký. Trong hộp thoại hiện ra, bạn cần nhập mã . Để lấy mã, mở [Cổng mô phỏng Fatoora](https://fatoora.zatca.gov.sa/), nhấp Onboard thiết bị/đơn vị giải pháp mới, chọn số lượng mã OTP cần tạo (mỗi mã dùng cho một sổ nhật ký cần cấu hình), rồi nhấp Tạo mã OTP. Sao chép một mã OTP, dán vào hộp thoại trên Odoo và nhấp Yêu cầu.

#### NOTE
OTP codes expire after one hour.

#### Kiểm tra

When confirming an invoice, there is now an option to process the invoice, sending it directly the
Fatoora simulation portal. Odoo displays the portal's response after each submission. Only rejected
invoices can be reset to draft and edited on Odoo. Furthermore, at the end of each day, Odoo sends
all unprocessed invoices to the portal.

#### Thuế

When using a **0% tax** in a customer invoice, it is necessary to specify the reason behind such a
rate. To configure taxes, go to Accounting ‣ Configuration ‣ Settings ‣
Taxes, and open the tax to edit. Under the Advanced Options, select an
Exemption Reason Code and click Save.

When using **retention** or **withholding an amount** in a customer invoice, the tax used to retain
the amount needs to be specified.

### Chế độ production

When ready for production, change the [API mode](#saudi-arabia-api-mode) to
Production and click Save.

#### WARNING
Setting the API mode to Production is **irreversible**.

The sales journals initially linked to the simulation portal now needs to be linked to the regular
portal. To do so, [onboard the journals](#saudi-arabia-journals) again, ensuring to use the
regular [Fatoora portal](https://fatoora.zatca.gov.sa/) this time.
