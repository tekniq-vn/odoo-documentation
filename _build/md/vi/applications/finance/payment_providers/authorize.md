# Authorize.Net

[Authorize.Net](https://www.authorize.net) is a United States-based online payment solution
provider, allowing businesses to accept **credit cards**.

## Cấu hình

#### SEE ALSO
- [Enabling a payment provider](applications/finance/payment_providers.md#payment-providers-add-new)

### Credentials tab

Odoo needs your **API Credentials & Keys** to connect with your Authorize.Net account, which
comprise:

- **API Login ID**: The ID solely used to identify the account with Authorize.Net.
- **Khóa giao dịch API**
- **Khóa chữ ký API**
- **Khóa khách hàng API**

To retrieve them, log into your Authorize.Net account, go to Account ‣ Settings
‣ Security Settings ‣ API Credentials & Keys, generate your **Transaction Key** and
**Signature Key**, and paste them on the related fields in Odoo. Then, click on **Generate Client
Key**.

#### IMPORTANT
To test Authorize.Net with a *sandbox* account, change the State to Test
Mode. We recommend doing this on a test Odoo database, rather than on your main database.

If you use the Test Mode with a regular account, it results in the following error:
*The merchant login ID or password is invalid or the account is inactive*.

### Tab cấu hình

#### Place a hold on a card

With Authorize.Net, you can enable the [manual capture](applications/finance/payment_providers.md#payment-providers-manual-capture). If enabled, the funds are reserved for 30 days on the
customer's card, but not charged yet.

#### WARNING
After **30 days**, the transaction is **voided automatically** by Authorize.Net.

#### SEE ALSO
- [Thanh toán online](applications/finance/payment_providers.md)

<a id="authorize-ach-payments"></a>

## ACH payments (USA only)

 is an electronic funds transfer system used between bank
accounts in the United States.

### Cấu hình

Để cho phép khách hàng thanh toán qua ACH, [đăng ký dịch vụ Authorize.Net eCheck](https://www.authorize.net/payments/echeck.html). Sau khi kích hoạt eCheck, nhân bản cổng thanh toán Authorize.Net đã cấu hình trước đó trên Odoo bằng cách vào Kế toán ‣ Cấu hình ‣ Nhà cung cấp dịch vụ thanh toán ‣ Authorize.net. Sau đó, nhấp vào biểu tượng bánh răng (⛭) và chọn Nhân bản. Đổi tên nhà cung cấp để phân biệt hai phiên bản (VD: `Authorize.net - Ngân hàng`).

When ready, change the provider's State to Enabled for a regular account or
Test Mode for a sandbox account.

## Import an Authorize.Net statement

<a id="authorize-import-template"></a>

### Xuất từ Authorize.Net

- Log in to Authorize.Net.
- Go to Account ‣ Statements ‣ eCheck.Net Settlement Statement.
- Define an export range using an *opening* and *closing* batch settlement. All transactions within
  the two batch settlements will be exported to Odoo.
- Select all transactions within the desired range, copy them, and paste them into the
  Report 1 Download sheet of the [Excel import template](#authorize-import-template).

![Selecting Authorize.Net transactions to import](../../../.gitbook/assets/authorize-report1.png)

Once the data is in the Report 1 Download sheet:

- Go to the Transaction Search tab on Authorize.Net.
- Under the Settlement Date section, select the previously used range of batch
  settlement dates in the From: and To: fields and click Search.
- When the list has been generated, click Download to File.
- In the pop-up window, select Expanded Fields with CAVV Response/Comma Separated,
  enable Include Column Headings, and click Submit.
- Open the text file, select All, copy the data, and paste it into the Report
  2 Download sheet of the [Excel import template](#authorize-import-template).
- Các dòng chuyển tiếp tự động được điền và cập nhật trong các trang tính chuyển tiếp cho báo cáo 1 và chuyển tiếp cho báo cáo 2 của [mẫu nhập Excel](#authorize-import-template). Hãy chắc chắn rằng tất cả các mục đã có mặt, và **nếu không**, hãy sao chép công thức từ những dòng đã được điền trước đó của các bảng tính trang tính chuyển tiếp cho báo cáo 1 hoặc 2 và dán vào các dòng trống.

#### IMPORTANT
To get the correct closing balance, **do not remove** any line from the Excel sheets.

### Nhập vào Odoo

To import the data into Odoo:

- Open the [Excel import template](#authorize-import-template).
- Copy the data from the transit for report 2 sheet and use *paste special* to only
  paste the values in the Odoo Import to CSV sheet.
- Look for *blue* cells in the Odoo Import to CSV sheet. These are chargeback entries
  without any reference number. As they cannot be imported as such, go to
  Authorize.Net ‣ Account ‣ Statements ‣ eCheck.Net Settlement Statement.
- Look for Charge Transaction/Chargeback, and click it.
- Copy the invoice description, paste it into the Label cell of the Odoo
  Import to CSV sheet, and add `Chargeback /` before the description.
- If there are multiple invoices, add a line into the [Excel import template](#authorize-import-template) for each invoice and copy/paste the description into each respective
  Label line.

#### NOTE
For **combined chargeback/returns** in the payouts, create a new line in the [Excel import
template](#authorize-import-template) for each invoice.

- Next, delete *zero transaction* and *void transaction* line items, and change the format
  of the Amount column in the Odoo Import to CSV sheet to *Number*.
- Go back to eCheck.Net Settlement Statement ‣ Search for a Transaction and
  search again for the previously used batch settlements dates.
- Verify that the batch settlement dates on eCheck.Net match the related payments' dates found in
  the Date column of the Odoo Import to CSV.
- If it does not match, replace the date with the one from eCheck.Net. Sort the column by *date*,
  and make sure the format is `MM/DD/YYYY`.
- Copy the data - column headings included - from the Odoo Import to CSV sheet, paste
  it into a new Excel file, and save it using the CSV format.
- Open the Accounting app, go to Configuration ‣ Journals, tick the
  Authorize.Net box, and click Favorites ‣ Import records ‣ Load
  file. Select the CSV file and upload it into Odoo.
