# Cash discounts and tax reduction

**Chiết khấu tiền mặt** là các khoản giảm giá cho số tiền mà khách hàng phải trả cho hàng hóa hoặc dịch vụ, và được coi như một động lực để khách hàng thanh toán hóa đơn đúng hạn. Những khoản chiết khấu này thường là một số phần trăm của tổng số tiền hóa đơn và được áp dụng nếu khách hàng thanh toán trong một khoảng thời gian xác định. Chiết khấu tiền mặt có thể giúp công ty duy trì dòng tiền ổn định.

A [tax reduction](#cash-discounts-tax-reductions) can also be applied depending on the country
or region.

#### SEE ALSO
- [Payment terms and installment plans](payment_terms.md)
- [Thanh toán](../payments.md)

<a id="cash-discounts-configuration"></a>

## Cấu hình

To grant cash discounts to customers, you must first verify the [gain and loss accounts](#cash-discounts-gain-loss-accounts). Then, configure [payment terms](#cash-discounts-payment-terms) and add a cash discount by checking the Early Discount
checkbox and filling in the discount percentage, discount days, and [tax
reduction](#cash-discounts-tax-reductions) fields.

<a id="cash-discounts-gain-loss-accounts"></a>

### Cash discount gain/loss accounts

With a cash discount, the amount you earn depends on whether the customer benefits from the cash
discount or not. This inevitably leads to gains and losses, which are recorded on default accounts.

To modify these accounts, go to Accounting ‣ Configuration ‣ Settings, and, in
the Default Accounts section, select the accounts you want to use for the
Cash Discount Gain account and Cash Discount Loss account.

<a id="cash-discounts-payment-terms"></a>

### Điều khoản thanh toán

Cash discounts are defined on [payment terms](payment_terms.md). Configure them to your liking by
going to Accounting ‣ Configuration ‣ Payment Terms, and make sure to fill out
the discount percentage, discount days, and [tax reduction](#cash-discounts-tax-reductions)
fields.

![Configuration of payment terms named "2/7 Net 30". The field "Description on Invoices"
reads: "Payment terms: 30 Days, 2% Early Payment Discount under 7 days".](../../../../.gitbook/assets/payment-terms.png)

<a id="cash-discounts-tax-reductions"></a>

### Miễn giảm thuế

Depending on the country or region, the base amount used to compute the tax can vary, which can lead
to a **tax reduction**. Since tax reductions are set on individual payment terms, each term can use
a specific tax reduction.

To configure how the tax reduction is applied, go to a payment term with the Early
Discount checkbox enabled, and select one of the three following options:

- Luôn luôn (khi xuất hóa đơn)
  : The tax is always reduced. The base amount used to compute the tax is the discounted amount,
    whether the customer benefits from the discount or not.
- Khi thanh toán sớm
  : The tax is reduced only if the customer pays early. The base amount used to compute the tax is the
    same as the sale: if the customer benefits from the reduction, then the tax is reduced. This means
    that, depending on the customer, the tax amount can vary after the invoice is issued.
- Không bao giờ
  : The tax is never reduced. The base amount used to compute the tax is the full amount, whether the
    customer benefits from the discount or not.

#### NOTE
- [Tax grids](../reporting/tax_returns.md#tax-returns-tax-grids), which are used for the tax report, are correctly
  computed according to the [type of tax reduction](#cash-discounts-tax-reductions) you
  configured.
- The **type of cash discount tax reduction** may be correctly pre-configured, depending on your
  [fiscal localization package](../../fiscal_localizations.md#fiscal-localizations-packages).

<a id="cash-discounts-customer-invoice"></a>

## Apply a cash discount to a customer invoice

On a customer invoice, apply a cash discount by selecting the [payment terms you created](#cash-discounts-payment-terms). Odoo automatically computes the correct amounts, tax amounts, due
dates, and accounting records.

Under the Journal Items tab, you can display the discount details by clicking on the
"toggle" button and adding the Discount Date and Discount Amount columns.

![An invoice of €100.00 with "2/7 Net 30" selected as payment terms. The "Journal Items" tab
is open, and the "Discount Date" and "Discount Amount" columns are displayed.](../../../../.gitbook/assets/invoice-journal-entry.png)

The discount amount and due date are also displayed on the generated invoice report sent to the
customer if the Show installment dates option is checked on the payment terms.

![An invoice of €100.00 with the following text added to the terms and conditions: "30
Days, 2% Early Payment Discount under 7 days. 118.58 € due if paid before 01/08/2023."](../../../../.gitbook/assets/invoice-print.png)

### Đối chiếu thanh toán

When you record a [payment](../payments.md) or [reconcile your bank transactions](../bank/reconciliation.md), Odoo takes the customer payment's date into account to determine if the
customer can benefit from the cash discount or not.

#### NOTE
If your customer pays the discount amount *after* the discount date, you can always decide to
mark the invoice as fully paid with a write-off or as partially paid.
