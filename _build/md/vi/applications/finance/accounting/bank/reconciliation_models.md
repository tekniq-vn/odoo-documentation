# Reconciliation models

Reconciliation models are used to automate the [bank reconciliation](reconciliation.md) process,
which is especially handy when dealing with recurring entries like bank fees. Reconciliation models
can also be helpful in handling [cash discounts](../customer_invoices/cash_discounts.md).

Each model is created based on a [model type](#models-type) and bank transaction
conditions.

#### SEE ALSO
- [Đồng bộ hoá ngân hàng](bank_synchronization.md)
- [Odoo Tutorials: Reconciliation models](https://www.odoo.com/slides/slide/reconciliation-models-1841?fullscreen=1)

<a id="models-type"></a>

## Reconciliation model types

The reconciliation models are available by going to Accounting ‣ Configuration
‣ Banks: Reconciliation Models. For each reconciliation model, a Type must be set.
Three types of models exist:

- Nút để tạo bút toán đối ứng: một nút được tạo trong phần mục nhập kết quả của chế độ xem đối chiếu ngân hàng. Khi được nhấn, nút này tạo ra một bút toán đối ứng để đối chiếu với giao dịch đang hoạt động dựa trên các quy tắc được thiết lập trong mẫu. Các quy tắc được chỉ định trong mẫu xác định tài khoản đối ứng, số tiền, nhãn và phân phối phân tích của bút toán đối ứng.
- Rule to suggest counterpart entry: used for recurring transactions to match the
  transaction to a new entry based on conditions that must match the information on the transaction;
- Rule to match invoices/bills: used for recurring transactions to match the transaction
  to existing invoices, bills, or payments based on conditions that must match the information on
  the transaction.

## Default reconciliation models

In Odoo, different models are available by default depending on the company's fiscal localization.
These can be updated if needed. Users can also create their own reconciliation models by clicking
New.

#### IMPORTANT
If a record matches with several reconciliation models, the first one in the *sequence* of models
is applied. You can rearrange the order by dragging and dropping the handle next to the name.

![Rearrange the sequence of models in the list view.](applications/finance/accounting/bank/reconciliation_models/list-view.png)

### Invoices/Bills perfect match

This model should be at the top of the *sequence* of models, as it enables Odoo to suggest matching
existing invoices or bills with a bank transaction based on set conditions.

![Set rules to trigger the reconciliation.](applications/finance/accounting/bank/reconciliation_models/invoices-bills-perfect-match.png)

Odoo tự động đối chiếu thanh toán khi tùy chọn Tự động xác thực được chọn và các điều kiện của mô hình được đáp ứng hoàn hảo. Trong trường hợp này, hệ thống mong đợi tìm thấy tham chiếu hóa đơn/thanh toán (vì đã chọn Nhãn) và tên đối tác (vì đã chọn Đối tác đã được thiết lập) trên dòng sao kê ngân hàng để gợi ý bút toán đối ứng chính xác và tự động đối chiếu thanh toán.

### Invoices/Bills partial match if underpaid

This model suggests a customer invoice or vendor bill that partially matches the payment when the
amount received is slightly lower than the invoice amount, for example in the case of
**cash discounts**. The difference is reconciled with the account indicated in the
counterpart entries tab.

The reconciliation model Type is Rule to match invoices/bills, and the
Payment tolerance should be set.

![Set rules to trigger the reconciliation.](applications/finance/accounting/bank/reconciliation_models/partial-match.png)

#### NOTE
The Payment tolerance is only applicable to lower payments. It is disregarded when an
overpayment is received.

#### SEE ALSO
[Cash discounts and tax reduction](../customer_invoices/cash_discounts.md)

### Line with bank fees

This model suggests a counterpart entry according to the rules set in the model. In this case, the
reconciliation model Type is Rule to suggest counterpart entry, and the
Label can be used for example, to identify the information referring to the
Bank fees in the label of the transaction.

![Set rules to trigger the reconciliation.](applications/finance/accounting/bank/reconciliation_models/bank-fees.png)

#### NOTE
[Regular expressions](https://regexone.com/), often abbreviated as **Regex**, can be used in
Odoo in various ways to search, validate, and manipulate data within the system. Regex can be
powerful but also complex, so it's essential to use it judiciously and with a good understanding
of the patterns you're working with.

To use regular expressions in your reconciliation models, set the Transaction Type
to Match Regex and add your expression. Odoo automatically retrieves the
transactions that match your Regex expression and the conditions specified in your model.

![Using Regex in Odoo](applications/finance/accounting/bank/reconciliation_models/regex.png)

## Partner mapping

Việc map đối tác cho phép bạn thiết lập quy tắc tự động khớp các giao dịch với tài khoản đối tác phù hợp, giúp tiết kiệm thời gian và giảm rủi ro sai sót trong quá trình đối chiếu thủ công. Ví dụ, bạn có thể tạo quy tắc map đối tác cho các khoản thanh toán đến có số tham chiếu hoặc từ khóa cụ thể trong mô tả giao dịch. Khi một khoản thanh toán đến đáp ứng các tiêu chí này, Odoo sẽ tự động map với tài khoản khách hàng tương ứng.

To create a partner mapping rule, go to the Partner Mapping tab and enter the
Find Text in Label, Find Text in Notes, and Partner.

![defining partner mapping](applications/finance/accounting/bank/reconciliation_models/partner-mapping.png)
