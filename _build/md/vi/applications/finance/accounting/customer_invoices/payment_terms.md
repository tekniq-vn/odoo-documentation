# Payment terms and installment plans

**Payment terms** specify all the conditions of a sale's payment to help ensure customers pay their
invoices correctly and on time.

Payment terms are generally defined on documents such as sales orders, customer invoices, and
vendor bills. Payment terms cover:

- The due date(s)
- Early payment discounts
- Any other conditions on the payment

An **installment plan** allows the customers to pay an invoice in parts, with the amounts and
payment dates defined beforehand by the seller.

#### NOTE
- Payment terms are not to be confused with [down payment invoices](../../../sales/sales/invoicing/down_payment.md). If, for a specific order, you issue
  multiple invoices to your customer, that is neither a payment term nor an installment plan but
  an invoicing policy.
- This page is about the *payment terms* feature, not [terms & conditions](terms_conditions.md), which can be used to declare contractual obligations regarding content
  use, return policies, and other policies surrounding the sale of goods and services.

#### SEE ALSO
- [Odoo Tutorials: payment terms](https://www.odoo.com/slides/slide/payment-terms-1679)
- [Cash discounts and tax reduction](cash_discounts.md)

## Cấu hình

To create new payment terms, follow these steps:

1. Go to Accounting ‣ Configuration ‣ Payment Terms and click on
   New.
2. Enter a name in the Payment Terms field. This field is the name displayed both
   internally and on sales orders.
3. Tick the Early Discount checkbox and fill out the discount percentage, discount days,
   and [tax reduction](cash_discounts.md#cash-discounts-tax-reductions) fields to add a [cash discount](cash_discounts.md), if desired.
4. In the Due Terms section, add a set of rules (terms) to define what needs to be paid
   and by which due date(s). Defining terms automatically calculates the payments' due date(s). This
   is particularly helpful for managing **installment plans** ().

   To add a term, click on Add a line, define the discount's value and type in the
   Due fields, then fill out the After fields to determine the due date.
5. Enter the text to be displayed on the document (sales order, invoice, etc.) in the gray textbox
   in the Preview column.
6. Tick the Show installment dates checkbox to display a breakdown of each payment and
   its due date on the invoice report, if desired.

To test that your payment terms are configured correctly, enter an invoice date on the
Example line to generate the payments that would be due and their due dates
using these payment terms.

#### IMPORTANT
Terms are computed in the order of their due dates.

## Using payment terms

Payment terms can be defined using the Payment Terms field on:

- **Contacts:** To automatically set default payment terms on a contact's new sales orders,
  invoices, and bills. This can be modified in the contact form, under the Sales &
  Purchase tab.
- **Quotations/Sales Orders:** To set specific payment terms automatically on all invoices generated
  from a quotation or sales order.

Payment terms can be defined using the Due Date field, with the Terms
drop-down list on:

- **Customer invoices:** To set specific payment terms on an invoice.
- **Vendor bills:** To set specific payment terms on a bill.

## Bút toán

Invoices with specific payment terms generate different *journal entries*, with one *journal item*
for every computed *due date*.

This makes for easier [follow-ups](../payments/follow_up.md) and
[reconciliation](../bank/reconciliation.md) since Odoo takes each
due date into account, rather than just the balance due date. It also helps to get an accurate
[aged receivable report](./#accounting-invoices-aging-report).
