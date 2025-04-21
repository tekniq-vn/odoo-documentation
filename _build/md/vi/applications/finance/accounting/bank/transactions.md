# Giao dịch

Importing transactions from your bank statements allows keeping track of bank account transactions
and reconciling them with the ones recorded in your accounting.

[Bank synchronization](bank_synchronization.md) automates the process. However, if you do not
want to use it or if your bank is not yet supported, other options exist:

- [Import bank transactions](#transactions-import) delivered by your bank;
- [Register bank transactions](#transactions-register) manually.

#### NOTE
[Grouping transactions by statement](#transactions-statements) is optional.

<a id="transactions-import"></a>

## Nhập giao dịch

Odoo supports multiple file formats to import transactions:

- SEPA recommended Cash Management format (CAMT.053)
- Comma-separated values (CSV)
- Open Financial Exchange (OFX)
- Quicken Interchange Format (QIF)
- Belgium: Coded Statement of Account (CODA)

To import a file, go to the Accounting Dashboard, and in the Bank journal,
click on Import File.

Next, select the file and upload it.

After setting the necessary formatting options and mapping the file columns with their related Odoo
fields, you can run a Test and Import your bank transactions.

#### SEE ALSO
[Xuất và nhập dữ liệu](../../../essentials/export_import_data.md)

<a id="transactions-register"></a>

## Register bank transactions manually

You can also record your bank transactions manually. To do so, go to Accounting
Dashboard, click on the Bank journal, and then on New. Make sure to fill
out the Partner and Label fields to ease the reconciliation process.

<a id="transactions-statements"></a>

## Sao kê

A **bank statement** is a document provided by a bank or financial institution that lists the
transactions that have occurred in a particular bank account over a specified period of time.

In Odoo Accounting, it is optional to group transactions by their related statement, but depending
on your business flow, you may want to record them for control purposes.

#### IMPORTANT
If you want to compare the ending balances of your bank statements with the ending balances of
your financial records, *don't forget to create an opening transaction* to record the bank
account balance as of the date you begin synchronizing or importing transactions. This is
necessary to ensure the accuracy of your accounting.

To access a list of existing statements, go to the Accounting Dashboard, click the
<i class="fa fa-ellipsis-v"></i> (ellipsis) icon next to the bank or cash journal you want to
check, then click Statements.

<a id="transactions-statement-kanban"></a>

### Statement creation from the kanban view

Mở chế độ xem đối chiếu ngân hàng (kanban) từ Trang chủ Kế toán bằng cách nhấp vào tên sổ nhật ký ngân hàng và xác định giao dịch tương ứng với giao dịch cuối cùng (mới nhất) trên sao kê ngân hàng của bạn. Nhấp vào nút Sao kê khi di chuột qua đường phân cách phía trên để tạo sao kê từ giao dịch đó trở xuống đến giao dịch cũ nhất chưa thuộc bất kỳ sao kê nào.

![A "Statement" button is visible when hovering on the line separating two transactions.](transactions/statements-kanban.png)

In the Create Statement window, fill out the statement's Reference, verify
its Starting Balance and Ending Balance, and click Save.

<a id="transactions-statement-list"></a>

### Statement creation from the list view

Mở danh sách giao dịch bằng cách nhấp vào tên sổ nhật ký ngân hàng và chuyển sang chế độ xem danh sách. Chọn tất cả các giao dịch tương ứng với sao kê ngân hàng, sau đó, trong cột Sao kê, chọn một sao kê hiện có hoặc tạo mới bằng cách nhập tham chiếu của nó, nhấp vào Tạo và chỉnh sửa..., điền thông tin chi tiết sao kê và lưu lại.

<a id="transactions-view-edit-print"></a>

### Statement viewing, editing, and printing

To view an existing statement, click on the statement amount in the reconciliation (kanban) view or
click on the statement name in the bank transaction list view. From here, you can edit the
Reference, Starting Balance, or Ending Balance.

#### NOTE
Manually updating the Starting Balance automatically updates the Ending
Balance based on the new value of the Starting Balance and the value of the
statement's transactions.

#### WARNING
If the Starting Balance doesn't equal the previous statement's Ending
Balance, or if the Ending Balance doesn't equal the running balance
(Starting Balance plus the statement's transactions), a warning appears explaining
the issue. To maintain flexibility, it is still possible to save without first resolving the
issue.

To attach a digital copy (i.e., JPEG, PNG, or PDF) of the bank statement for enhanced recordkeeping,
click the <i class="fa fa-paperclip"></i> Attachments button and select the file to attach.

To generate and print a PDF of the bank statement, click the Print button (if accessed
via the reconciliation view) or click on the <i class="fa fa-cog"></i>(gear) icon and click
<i class="fa fa-print"></i>Statement (if accessed via the list view).

#### NOTE
When a bank statement is generated to be printed, it is automatically added to the
Attachments.
