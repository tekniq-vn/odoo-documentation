# Hóa đơn bán hàng

A customer invoice is a document issued by a company for products and/or services sold to a
customer. It records receivables as they are sent to customers. Customer invoices can include
amounts due for the goods and/or services provided, applicable sales taxes, shipping and handling
fees, and other charges.
Odoo supports multiple invoicing and payment workflows.

#### SEE ALSO
[Invoicing processes](overview.md)

From draft invoice to profit and loss report, the process involves several steps once the goods (or
services) have been ordered/shipped (or rendered) to a customer, depending on the invoicing policy:

- [Tạo hoá đơn](#accounting-invoice-creation)
- [Xác nhận hoá đơn](#accounting-invoice-confirmation)
- [Gửi hoá đơn](#accounting-invoice-sending)
- [Payment and reconciliation](#accounting-invoice-paymentandreconciliation)
- [Follow-up thanh toán](#accounting-invoice-followup)
- [Báo cáo](#accounting-invoice-reporting)

<a id="accounting-invoice-creation"></a>

## Tạo hoá đơn

Draft invoices can be created directly from documents like sales orders or purchase orders or
manually from the Customer Invoices journal in the Accounting Dashboard.

An invoice must include the required information to enable the customer to pay promptly for their
goods and services. Make sure the following fields are appropriately completed:

- Khách hàng: Khi một khách hàng được chọn, Odoo sẽ tự động đưa thông tin từ hồ sơ khách hàng bao gồm địa chỉ hóa đơn, [điều khoản thanh toán ưu tiên](payment_terms.md), [vị trí tài chính](../taxes/fiscal_positions.md), tài khoản phải thu và các thông tin khác vào hóa đơn. Để thay đổi các giá trị này cho một hóa đơn cụ thể, hãy chỉnh sửa trực tiếp trên hóa đơn. Để thay đổi cho các hóa đơn trong tương lai, hãy thay đổi các giá trị trong hồ sơ liên hệ.
- Invoice Date: If not set manually, this field is automatically set as the current date
  upon confirmation.
- Due Date or [payment terms](payment_terms.md): To specify when
  the customer has to pay the invoice.
- Journal: Is automatically set and can be changed if needed.
- [Tiền tệ](../get_started/multi_currency.md)
- Product: Click Add a line to add a product.
- Số lượng
- Giá
- [Taxes](../taxes/) (if applicable)

The Journal Items tab displays the accounting entries created.
Additional invoice information such as the Customer Reference, [Fiscal Positions](../taxes/fiscal_positions.md), [Incoterms](incoterms.md), and more can be added or
modified in the Other Info tab.

#### NOTE
Odoo initially creates invoices in Draft status. Draft invoices have no accounting
impact until they are [confirmed](#accounting-invoice-confirmation).

#### SEE ALSO
[Hóa đơn chiếu lệ](../../../sales/sales/invoicing/proforma.md)

<a id="accounting-invoice-confirmation"></a>

## Xác nhận hoá đơn

Click Confirm when the document is completed. The document's status changes to
Posted, and a journal entry is generated based on the invoice configuration. On
confirmation, Odoo assigns each invoice a unique number from a defined
[sequence](sequence.md).

#### NOTE
- Once confirmed, an invoice can no longer be updated. Click Reset to draft if
  changes are needed.
- If required, invoices and other journal entries can be locked once posted
  using the [Lock posted entries with hash](../reporting/data_inalterability.md#data-inalterability-lock) feature.

<a id="accounting-invoice-sending"></a>

## Gửi hoá đơn

To send the invoice to the customer, click Send & Print. A Configure your
document layout pop-up window will appear if a [default invoice layout](../../../studio/pdf_reports.md#studio-pdf-reports-default-layout) hasn't been customized. Then, select how to send this invoice
to the customer in the Send window.

To send and print multiple invoices, go to Accounting ‣ Customers ‣ Invoices
and select them. Then click the <i class="fa fa-cog"></i> Actions menu and select
Send & Print. A banner will appear on the selected invoices to indicate they are part of
an ongoing send and print batch. This helps prevent the process from being triggered manually again,
as it may take some time to complete for exceptionally large batches.

<a id="accounting-invoice-paymentandreconciliation"></a>

## Payment and reconciliation

In Odoo, an invoice is considered Paid when the associated accounting entry has been
reconciled with a corresponding bank transaction.

#### SEE ALSO
- thanh toán
- [Đối chiếu ngân hàng](../bank/reconciliation.md)

<a id="accounting-invoice-followup"></a>

## Follow-up thanh toán

Các [tác vụ follow-up](../payments/follow_up.md) của Odoo giúp các công ty theo dõi hóa đơn khách hàng. Có thể thiết lập những tác vụ khác nhau để nhắc nhở khách hàng thanh toán các hóa đơn chưa thanh toán, tùy thuộc vào mức độ chậm trễ của khách hàng. Những tác vụ này được nhóm thành các cấp độ nhắc nhở và sẽ kích hoạt khi một hóa đơn quá hạn một số ngày nhất định. Nếu có nhiều hóa đơn quá hạn cho cùng một khách hàng, các tác vụ sẽ được thực hiện trên hóa đơn quá hạn lâu nhất.

<a id="accounting-invoice-reporting"></a>

## Báo cáo

<a id="accounting-invoice-partner-reports"></a>

### Partner reports

<a id="accounting-invoices-partner-ledger"></a>

#### Sổ cái đối tác

The Partner Ledger report shows the balance of customers and suppliers. To access it,
go to Accounting ‣ Reporting ‣ Partner Ledger.

<a id="accounting-invoices-aging-report"></a>

#### Tuổi nợ phải thu

To review outstanding customer invoices and their related due dates, use the
[Aged Receivable](../reporting/#accounting-reporting-aged-receivable) report. To access it, go to
Accounting ‣ Reporting ‣ Aged Receivable.

<a id="accounting-invoices-aged-payable"></a>

#### Tuổi nợ phải trả

To review outstanding vendor bills and their related due dates, use the
[Aged Payable](../reporting/#accounting-reporting-aged-payable) report. To access it, go to
Accounting ‣ Reporting ‣ Aged Payable.

<a id="accounting-invoices-profit-and-loss"></a>

### Lãi và lỗ

The [Profit and Loss](../reporting/#accounting-reporting-profit-and-loss) statement shows details of income
and expenses.

<a id="accounting-invoices-balance-sheet"></a>

### Bảng cân đối kế toán

The [Balance Sheet](../reporting/#accounting-reporting-balance-sheet) summarizes the company's assets,
liabilities, and equity at a specific time.

* [Invoicing processes](overview.md)
* [Delivery and invoice addresses](customer_addresses.md)
* [Payment terms and installment plans](payment_terms.md)
* [Default terms and conditions (T&C)](terms_conditions.md)
* [Cash discounts and tax reduction](cash_discounts.md)
* [Credit notes and refunds](credit_notes.md)
* [Làm tròn tiền](cash_rounding.md)
* [Doanh thu chưa thực hiện](deferred_revenues.md)
* [Electronic invoicing ()](electronic_invoicing.md)
* [Invoice sequence](sequence.md)
* [Snailmail](snailmail.md)
* [EPC QR codes](epc_qr_code.md)
* [Incoterm](incoterms.md)
