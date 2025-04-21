# Deferred expenses

**Deferred expenses** and **prepayments** (also known as **prepaid expenses**) are both costs that
have already occurred for products or services yet to be received.

Such costs are **assets** for the company that pays them since it already paid for products and
services but has either not yet received them or not yet used them. The company cannot report them
on the current **profit and loss statement**, or *income statement*, since the payments will be
effectively expensed in the future.

These future expenses must be deferred on the company's balance sheet until the moment in time they
can be **recognized**, at once or over a defined period, on the profit and loss statement.

Ví dụ, giả sử chúng ta trả trước 1.200 USD cho một năm bảo hiểm. Chúng ta đã thanh toán toàn bộ chi phí ngay bây giờ nhưng vẫn chưa sử dụng dịch vụ. Do đó, chúng ta hạch toán khoản chi phí mới này vào một *tài khoản trả trước* và quyết định ghi nhận chi phí theo tháng. Trong vòng 12 tháng tiếp theo, 100 USD sẽ được ghi nhận là chi phí mỗi tháng.

Odoo Accounting handles deferred expenses by spreading them across multiple entries that are
posted periodically.

#### NOTE
The server checks once a day if an entry must be posted. It might then take up to 24 hours before
you see a change from Draft to Posted.

## Cấu hình

Make sure the default settings are correctly configured for your business. To do so, go to
Accounting ‣ Configuration ‣ Settings. The following options are available:

Sổ nhật ký
: The deferral entries are posted in this journal.

Tài khoản chi phí trả trước
: Expenses are deferred on this Current Asset account until they are recognized.

Tài khoản doanh thu hoãn lại
: Revenues are deferred on this Current Liability account until they are recognized.

Tạo bút toán
: By default, Odoo [automatically generates](#vendor-bills-deferred-generate-on-validation)
  the deferral entries when you post a vendor bill. However, you can also choose to
  [generate them manually](#vendor-bills-deferred-generate-manually) by selecting the
  Manually & Grouped option instead.

Tính toán số tiền
: Suppose a bill of $1200 must be deferred over 12 months.
  <br/>
  - The Months option accounts for $100 each month prorated to the number of days in
    that month (e.g., $50 for the first month if the Start Date is set to the 15th of
    the month).
  - Tùy chọn Tháng đầy đủ coi mỗi tháng bắt đầu là tháng đầy đủ, (VD: $100 cho tháng đầu tiên ngay cả khi Ngày bắt đầu được đặt vào ngày 15 của tháng.) Điều này có nghĩa là với tùy chọn Tháng đầy đủ, toàn bộ $100 được ghi nhận trong tháng đầu tiên dù chỉ là một phần tháng, loại bỏ nhu cầu tháng thứ 13 để ghi nhận phần còn lại như khi sử dụng tùy chọn Tháng.
  - The Days option accounts for different amounts depending on the number of days in
    each month (e.g., ~$102 for January and ~$92 for February).

<a id="vendor-bills-deferred-generate-on-validation"></a>

## Generate deferral entries on validation

For each line of the bill that should be deferred, specify the start and end dates of the deferral
period.

If the Generate Entries field is set to On invoice/bill validation, Odoo
automatically generates the deferral entries when the bill is validated. Click on the
Deferred Entries smart button to see them.

One entry, dated on the same day as the bill's accounting date, moves the bill amounts from the
expense account to the deferred account. The other entries are deferral entries which will, month
after month, move the bill amounts from the deferred account to the expense account to recognize
the expense.

## Báo cáo

The deferred expense report computes an overview of the necessary deferral entries for each account.
To access it, go to Accounting ‣ Reporting ‣ Deferred Expense.

To view the journal items of each account, click on the account name and then Journal
Items.

![Deferred expense report](deferred_expenses/deferred_expense_report.png)

#### NOTE
Only bills whose accounting date is before the end of the period of the report
are taken into account.

<a id="vendor-bills-deferred-generate-manually"></a>

## Generate grouped deferral entries manually

If you have a lot of deferred revenues and wish to reduce the number of journal entries created, you
can generate deferral entries manually. To do so, set the Generate Entries field in the
**Settings** to Manually & Grouped. Odoo then aggregates the deferred amounts in a
single entry.

At the end of each month, go to the Deferred Expenses report and click the
Generate Entries button. This generates two deferral entries:

- One dated at the end of the month which aggregates, for each account, all the deferred amounts
  of that month. This means that at the end of that period, a part of the deferred expense is
  recognized.
- The reversal of this created entry, dated on the following day (i.e., the first day of the
  next month) to cancel the previous entry.
