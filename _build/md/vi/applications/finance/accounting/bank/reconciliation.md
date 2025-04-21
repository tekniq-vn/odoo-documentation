# Đối chiếu ngân hàng

**Đối chiếu ngân hàng** là quy trình khớp các [giao dịch ngân hàng](transactions.md) của bạn với hồ sơ kinh doanh như [hóa đơn bán hàng](../customer_invoices.md), [hóa đơn mua hàng](../vendor_bills.md) và [thanh toán](../payments.md). Quy trình này không chỉ bắt buộc với hầu hết doanh nghiệp mà còn mang lại nhiều lợi ích như: giảm thiểu rủi ro sai sót trong báo cáo tài chính, phát hiện hoạt động gian lận và quản lý dòng tiền hiệu quả hơn.

Thanks to the bank [reconciliation models](reconciliation_models.md), Odoo pre-selects the
matching entries automatically.

#### SEE ALSO
- [Odoo Tutorials: Bank reconciliation](https://www.odoo.com/slides/slide/bank-reconciliation-2724)
- [Đồng bộ hoá ngân hàng](bank_synchronization.md)
- [Giao dịch](transactions.md)

## Bank reconciliation view

To access a bank journal's **reconciliation view**, go to your Accounting Dashboard and
either:

- click the journal name (e.g., Bank) to display all transactions, including those
  previously reconciled or
- click the Reconcile items button to display all transactions Odoo pre-selected for
  reconciliation. You can remove the Not Matched filter from the search bar to include
  previously reconciled transactions.

![Reaching the bank reconciliation tool from your accounting dashboard](applications/finance/accounting/bank/reconciliation/bank-card.png)

The bank reconciliation view is structured into three distinct sections: transactions, counterpart
entries, and resulting entry.

![The user interface of the reconciliation view of a bank journal.](applications/finance/accounting/bank/reconciliation/user-interface.png)

Giao dịch
: The transactions section on the left shows all bank transactions, with the newest displayed
  first. Click a transaction to select it.

Bút toán đối ứng
: The counterpart entries section on the bottom right displays the options to match the selected
  bank transaction. Multiple tabs are available, including
  [Match existing entries](#reconciliation-existing-entries), [Thanh toán theo lô](#reconciliation-batch-payments),
  [Hoạt động thủ công](#reconciliation-manual-operations), and Discuss, which contains the chatter for
  the selected bank transaction.

Bút toán kết quả
: The resulting entry section on the top right displays the selected bank transaction matched with
  the counterpart entries and includes any remaining debits or credits. In this section, you can
  validate the reconciliation or mark it as To Check. Any [reconciliation model
  buttons](#reconciliation-button) are also available in the resulting entry section.

## Đối chiếu giao dịch

Transactions can be matched automatically with the use of [reconciliation models](reconciliation_models.md), or they can be matched with [existing entries](#reconciliation-existing-entries), [batch payments](#reconciliation-batch-payments),
[manual operations](#reconciliation-manual-operations), and [reconciliation model buttons](#reconciliation-button).

1. Select a transaction among unmatched bank transactions.
2. Define the counterpart. There are several options for defining a counterpart, including
   [matching existing entries](#reconciliation-existing-entries), [manual operations](#reconciliation-manual-operations), [batch payments](#reconciliation-batch-payments), and
   [reconciliation model buttons](#reconciliation-button).
3. If the resulting entry is not fully balanced, balance it by adding another existing counterpart
   entry or writing it off with a [manual operation](#reconciliation-manual-operations).
4. Click the Validate button to confirm the reconciliation and move to the next
   transaction.

#### NOTE
Bank transactions are posted on the **journal's suspense account** until reconciliation. At this
point, reconciliation modifies the transaction journal entry by replacing the bank suspense
account with the corresponding receivable, payable, or outstanding account.

<a id="reconciliation-existing-entries"></a>

### Match existing entries

This tab contains matching entries Odoo automatically pre-selects according to the reconciliation
models. The entry order is based on [reconciliation models](reconciliation_models.md), with
suggested entries appearing first.

<a id="reconciliation-batch-payments"></a>

### Thanh toán theo lô

[Batch payments](payments/batch-payments) allow you to group different payments to ease
reconciliation. Use the Batch Payments tab to find batch payments for customers and
vendors. Similarly to the Match Existing Entries tab, the Batch Payments tab
has a search bar that allows you to search for specific batch payments.

<a id="reconciliation-manual-operations"></a>

### Hoạt động thủ công

If there is not an existing entry to match the selected transaction, you may instead wish to
reconcile the transaction manually by choosing the correct account and amount. Then, complete any
of the relevant optional fields.

#### NOTE
Lines are silently reconciled unless a write-off entry is required, which launches a
reconciliation wizard.

![Click on fully paid to manually set an invoice as entirely paid.](applications/finance/accounting/bank/reconciliation/fully-paid.png)

<a id="reconciliation-button"></a>

### Reconciliation model buttons

Use a [reconciliation model](reconciliation_models.md) button for manual operations that are
frequently used. These custom buttons allow you to quickly reconcile bank transactions manually and
can also be used in combination with existing entries.
