# Year-end closing

Year-end closing is vital for maintaining financial accuracy, complying with regulations, making
informed decisions, and ensuring transparency in reporting.

<a id="year-end-fiscal-years"></a>

## Fiscal years

By default, the fiscal year is set to last 12 months and end on December 31st. However, its duration
and end date can vary due to cultural, administrative, and economic considerations.

To modify these values, go to Accounting ‣ Configuration ‣ Settings. Under the
Fiscal Periods section, change the Last Day field if necessary.

If the period lasts *more* than or *less* than 12 months, enable Fiscal Years and
Save. Go back to the Fiscal Periods section and click ➜ Fiscal
Years. From there, click Create, give it a Name, and both a
Start Date and End Date.

#### NOTE
Once the set fiscal period is over, Odoo automatically reverts to the default periodicity, taking
into account the value specified in the Last Day field.

<a id="year-end-checklist"></a>

## Year-end checklist

### Before closure

Before closing a fiscal year, ensure first everything is accurate and up-to-date:

- Make sure all bank accounts are fully [reconciled](../bank/reconciliation.md) up to year-end,
  and confirm that the ending book balances match the bank statement balances.
- Verify that all [customer invoices](../customer_invoices/) have been entered and
  approved and that there are no draft invoices.
- Confirm that all [vendor bills](../vendor_bills/) have been entered and agreed upon.
- Validate all [expenses](../../expenses/), ensuring their accuracy.
- Corroborate that all [received payments](../payments/) have been encoded and recorded
  accurately.
- Close all [suspense accounts](../bank/#bank-accounts-suspense).
- Book all [depreciation](../vendor_bills/assets.md) and [deferred revenue](../customer_invoices/deferred_revenues.md) entries.

### Closing a fiscal year

Then, to close the fiscal year:

- Run a [tax report](./#accounting-reporting-tax-report), and verify that all tax information is
  correct.
- Reconcile all accounts on the [balance sheet](./#accounting-reporting-balance-sheet):
  - Update the bank balances in Odoo according to the actual balances found on the bank statements.
  - Reconcile all transactions in the cash and bank accounts by running the [aged receivables](./#accounting-reporting-aged-receivable) and [aged payables](./#accounting-reporting-aged-payable) reports.
  - Audit all accounts, being sure to fully understand all transactions and their nature, making
    sure to include loans and fixed assets.
  - Optionally, [match payments](../payments/#accounting-payments-auto-reconcile-tool) to validate any open
    vendor bills and customer invoices with their payments. While this step is optional, it could
    assist the year-end closing process if all outstanding payments and invoices are reconciled,
    potentially finding errors or mistakes in the system.

Next, the accountant likely verifies balance sheet items and book entries for:

> - year-end manual adjustments,
> - work in progress,
> - depreciation journal entries,
> - loans,
> - tax adjustments,
> - ...

If the accountant is going through the year-end audit, they may want to have paper copies of all
balance sheet items (such as loans, bank accounts, prepayments, sales tax statements, etc.) to
compare these with the balances in Odoo.

#### Current year's earnings

Odoo uses a unique account type called **current year's earnings** to display the amount difference
between the **income** and **expenses** accounts.

#### NOTE
The chart of accounts can only contain one account of this type. By default, it is a 999999
account named Undistributed Profits/Losses.

Để phân bổ lợi nhuận năm hiện tại, tạo một bút toán hỗn hợp để hạch toán vào bất kỳ tài khoản vốn chủ sở hữu nào. Sau khi hoàn tất, kiểm tra xem lợi nhuận năm hiện tại trên **bảng cân đối kế toán** có hiển thị số dư bằng 0 chính xác hay không. Nếu đúng như vậy, thiết lập Ngày khóa sổ cho mọi người dùng vào ngày cuối cùng của năm tài chính bằng cách vào Kế toán ‣ Kế toán ‣ Ngày khóa sổ.

#### NOTE
Một bút toán khoá sổ cuối năm cụ thể là **tùy chọn** để đóng **báo cáo kết quả hoạt động kinh doanh**. Các báo cáo được tạo theo thời gian thực, có nghĩa là báo cáo kết quả hoạt động kinh doanh sẽ phản ánh chính xác ngày kết thúc năm tài chính được chỉ định trong Odoo. Do đó, bất cứ khi nào **báo cáo kết quả hoạt động kinh doanh** được tạo, ngày bắt đầu sẽ tương ứng với ngày đầu của **năm tài chính**, và số dư của tất cả các tài khoản nên bằng không.
