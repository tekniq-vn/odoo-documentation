# Accounting and Invoicing

**Odoo Invoicing** is a standalone invoicing app to create invoices, send them to your customers,
and manage payments.

**Odoo Accounting** is a full featured accounting app. Accountant productivity is at the core of its
development with features such as AI-powered invoice recognition, synchronization with your bank
accounts, smart matching suggestions, etc.

#### SEE ALSO
[Odoo Tutorials: Accounting](https://www.odoo.com/slides/accounting-19)

## Double-entry bookkeeping

Odoo automatically creates all the underlying journal entries for all accounting transactions (e.g.,
customer invoices, vendor bills, point-of-sales orders, expenses, inventory valuations, etc.).

Odoo uses the double-entry bookkeeping system, whereby every entry needs a corresponding and
opposite counterpart in a different account, with one account debited and the other credited.
It ensures that all transactions are recorded accurately and consistently and that the accounts
always balance.

#### SEE ALSO
[Accounting Cheat Sheet](applications/finance/accounting/get_started/cheat_sheet.md)

## Accrual and cash basis

Both accrual and cash basis accounting are supported in Odoo. This allows reporting income and
expense either when the transaction occurs (accrual basis) or when the payment is made or received
(cash basis).

#### SEE ALSO
[Cash basis](applications/finance/accounting/taxes/cash_basis.md)

<a id="accounting-multi-company"></a>

## Đa công ty

Several companies can be managed within the same database. Each company has its [chart of
accounts](applications/finance/accounting/get_started/chart_of_accounts.md), which is also useful to generate consolidation
reports. Users can access several companies but can only work on a single company's accounting at a
time.

## Môi trường đa tiền tệ

Odoo có một môi trường [đa tiền tệ](applications/finance/accounting/get_started/multi_currency.md) với tỷ giá hối đoái tự động để dễ dàng thực hiện giao dịch quốc tế. Mỗi giao dịch được ghi nhận bằng đồng tiền mặc định của công ty; đối với các giao dịch được thực hiện bằng đồng tiền khác, Odoo lưu trữ cả giá trị bằng đồng tiền của công ty và giá trị của giao dịch bằng đồng tiền của giao dịch đó. Odoo tạo ra các khoản lãi và lỗ tỷ giá sau khi đối chiếu các hạng mục bút toán.

#### SEE ALSO
[Manage a bank in a foreign currency](applications/finance/accounting/bank/foreign_currency.md)

## Branch management

Multiple branches can be managed thanks to multi-company hierarchies. This allows to post journal
entries on each branch as well as setting up a common lock date managed by the main company.

## Chuẩn mực quốc tế

Odoo Accounting supports more than 70 countries. It provides the central standards and mechanisms
common to all nations, and thanks to country-specific modules, local requirements are fulfilled.
Fiscal positions exist to address regional specificities like the chart of accounts, taxes, or any
other requirements.

#### SEE ALSO
[Fiscal localization packages](applications/finance/fiscal_localizations.md)

## Accounts receivable and payable

By default, there is a single account for the account receivable entries and one for the account
payable entries. As transactions are linked to your **contacts**, you can run a report per customer,
vendor, or supplier.

The **Partner Ledger** report displays the balance of your customers and suppliers. It is available
by going to Accounting ‣ Reporting ‣ Partner Ledger.

## Báo cáo

The following financial [reports](applications/finance/accounting/reporting.md) are available and updated in
real-time:

|                                  | Báo cáo tài chính    |
|----------------------------------|----------------------|
| Sao kê                           | Bảng cân đối kế toán |
| Profit and loss                  |                      |
| Cash flow statement              |                      |
| Báo cáo thuế                     |                      |
| ES sales list                    |                      |
| Kiểm toán                        | Sổ cái chung         |
| Cân đối thử                      |                      |
| Báo cáo nhật ký                  |                      |
| Báo cáo Intrastat                |                      |
| Check register                   |                      |
| Đối tác                          | Sổ cái đối tác       |
| Tuổi nợ phải thu                 |                      |
| Tuổi nợ phải trả                 |                      |
| Quản lý                          | Phân tích hoá đơn    |
| Unrealized currency gains/losses |                      |
| Kế hoạch khấu hao                |                      |
| Chi phí không được phép          |                      |
| Phân tích ngân sách              |                      |
| Biên lợi nhuận sản phẩm          |                      |
| Báo cáo 1099                     |                      |

### Báo cáo thuế

Odoo computes all accounting transactions for the specific tax period and uses these totals to
calculate the tax obligation.

#### IMPORTANT
Once the tax report has been generated for a period, Odoo locks it and prevents the creation of
new journal entries involving VAT. Any correction to customer invoices or vendor bills has to
be recorded in the next period.

#### NOTE
Depending on the country's localization, an XML version of the tax report can be generated to be
uploaded to the VAT platform of the relevant taxation authority.

## Đồng bộ hoá ngân hàng

The bank synchronization system directly connects with your bank institution to automatically
import all transactions into your database. It gives an overview of your cash flow without logging
into an online banking system or waiting for paper bank statements.

#### SEE ALSO
[Đồng bộ ngân hàng](applications/finance/accounting/bank/bank_synchronization.md)

## Định giá tồn kho

Both periodic (manual) and perpetual (automated) inventory valuations are supported in Odoo. The
available methods are standard price, average price,  and

#### SEE ALSO
[Định giá tồn kho tự động](applications/inventory_and_mrp/inventory/product_management/inventory_valuation/inventory_valuation_config.md)

## Lợi nhuận giữ lại

Retained earnings are the portion of income retained by a business. Odoo calculates current year
earnings in real-time, so no year-end journal or rollover is required. The profit
and loss balance is automatically reported on the balance sheet report.

#### SEE ALSO
[Accounting Cheat Sheet](applications/finance/accounting/get_started/cheat_sheet.md)

<a id="fiduciaries"></a>

## Đơn vị được ủy thác

The Accounting Firms mode can be activated by going to Accounting ‣
Configuration ‣ Settings ‣ Accounting Firms mode. When enabled:

- The document's sequence becomes editable on all documents;
- The Total (tax incl.) field appears to speed up and control the encoding by automating
  line creation with the right account and tax;
- Invoice Date and Bill Date are pre-filled when encoding a transaction.
- A Quick encoding option is available for customer invoices and vendor bills.

* [Bắt đầu](applications/finance/accounting/get_started.md)
  * [Accounting cheat sheet](applications/finance/accounting/get_started/cheat_sheet.md)
  * [Hệ thống tài khoản](applications/finance/accounting/get_started/chart_of_accounts.md)
  * [Hệ thống đa tiền tệ](applications/finance/accounting/get_started/multi_currency.md)
  * [Average price on returned goods](applications/finance/accounting/get_started/avg_price_valuation.md)
  * [Tax units](applications/finance/accounting/get_started/tax_units.md)
* [Thuế](applications/finance/accounting/taxes.md)
  * [Cash basis taxes](applications/finance/accounting/taxes/cash_basis.md)
  * [Withholding taxes](applications/finance/accounting/taxes/retention.md)
  * [VAT numbers verification (VIES)](applications/finance/accounting/taxes/vat_verification.md)
  * [Fiscal positions (tax and account mapping)](applications/finance/accounting/taxes/fiscal_positions.md)
  * [AvaTax integration](applications/finance/accounting/taxes/avatax.md)
    * [AvaTax use](applications/finance/accounting/taxes/avatax/avatax_use.md)
    * [Cổng thông tin Avalara (Avatax)](applications/finance/accounting/taxes/avatax/avalara_portal.md)
  * [TaxCloud integration](applications/finance/accounting/taxes/taxcloud.md)
  * [EU intra-community distance selling](applications/finance/accounting/taxes/eu_distance_selling.md)
  * [B2B (tax excluded) and B2C (tax included) pricing](applications/finance/accounting/taxes/B2B_B2C.md)
* [Hóa đơn bán hàng](applications/finance/accounting/customer_invoices.md)
  * [Invoicing processes](applications/finance/accounting/customer_invoices/overview.md)
  * [Delivery and invoice addresses](applications/finance/accounting/customer_invoices/customer_addresses.md)
  * [Payment terms and installment plans](applications/finance/accounting/customer_invoices/payment_terms.md)
  * [Default terms and conditions (T&C)](applications/finance/accounting/customer_invoices/terms_conditions.md)
  * [Cash discounts and tax reduction](applications/finance/accounting/customer_invoices/cash_discounts.md)
  * [Credit notes and refunds](applications/finance/accounting/customer_invoices/credit_notes.md)
  * [Làm tròn tiền](applications/finance/accounting/customer_invoices/cash_rounding.md)
  * [Doanh thu chưa thực hiện](applications/finance/accounting/customer_invoices/deferred_revenues.md)
  * [Electronic invoicing ()](applications/finance/accounting/customer_invoices/electronic_invoicing.md)
  * [Invoice sequence](applications/finance/accounting/customer_invoices/sequence.md)
  * [Snailmail](applications/finance/accounting/customer_invoices/snailmail.md)
  * [EPC QR codes](applications/finance/accounting/customer_invoices/epc_qr_code.md)
  * [Incoterm](applications/finance/accounting/customer_invoices/incoterms.md)
* [Vendor bills](applications/finance/accounting/vendor_bills.md)
  * [AI-powered document digitization](applications/finance/accounting/vendor_bills/invoice_digitization.md)
  * [Non-current assets and fixed assets](applications/finance/accounting/vendor_bills/assets.md)
  * [Deferred expenses](applications/finance/accounting/vendor_bills/deferred_expenses.md)
  * [Vendor bill sequence](applications/finance/accounting/vendor_bills/sequence.md)
* [Thanh toán](applications/finance/accounting/payments.md)
  * [Thanh toán online](applications/finance/accounting/payments/online.md)
    * [Install the patch to disable online invoice payment](applications/finance/accounting/payments/online/install_portal_patch.md)
  * [Séc](applications/finance/accounting/payments/checks.md)
  * [Batch payments by bank deposit](applications/finance/accounting/payments/batch.md)
  * [Batch payments: SEPA Direct Debit (SDD)](applications/finance/accounting/payments/batch_sdd.md)
  * [Follow up hoá đơn](applications/finance/accounting/payments/follow_up.md)
  * [Internal transfers](applications/finance/accounting/payments/internal_transfers.md)
  * [Thanh toán bằng SEPA](applications/finance/accounting/payments/pay_sepa.md)
  * [Pay by checks](applications/finance/accounting/payments/pay_checks.md)
  * [Forecast future bills to pay](applications/finance/accounting/payments/forecast.md)
  * [Trusted accounts (send money)](applications/finance/accounting/payments/trusted_accounts.md)
* [Bank and cash accounts](applications/finance/accounting/bank.md)
  * [Đồng bộ hoá ngân hàng](applications/finance/accounting/bank/bank_synchronization.md)
    * [Salt Edge](applications/finance/accounting/bank/bank_synchronization/saltedge.md)
    * [Ponto](applications/finance/accounting/bank/bank_synchronization/ponto.md)
    * [Enable Banking](applications/finance/accounting/bank/bank_synchronization/enablebanking.md)
  * [Giao dịch](applications/finance/accounting/bank/transactions.md)
  * [Đối chiếu ngân hàng](applications/finance/accounting/bank/reconciliation.md)
  * [Reconciliation models](applications/finance/accounting/bank/reconciliation_models.md)
  * [Manage a bank account in a foreign currency](applications/finance/accounting/bank/foreign_currency.md)
* [Báo cáo](applications/finance/accounting/reporting.md)
  * [Tax return (VAT declaration)](applications/finance/accounting/reporting/tax_returns.md)
  * [Tax carryover](applications/finance/accounting/reporting/tax_carryover.md)
  * [Analytic accounting](applications/finance/accounting/reporting/analytic_accounting.md)
  * [Analytic budgets](applications/finance/accounting/reporting/budget.md)
  * [Intrastat](applications/finance/accounting/reporting/intrastat.md)
  * [Data inalterability check report](applications/finance/accounting/reporting/data_inalterability.md)
  * [Tích hợp Silverfin](applications/finance/accounting/reporting/silverfin.md)
  * [Custom reports](applications/finance/accounting/reporting/customize.md)
  * [Year-end closing](applications/finance/accounting/reporting/year_end.md)
