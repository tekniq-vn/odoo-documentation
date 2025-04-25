# Vendor bills

Vendor bills can be registered either **manually** or **automatically** in Odoo. The
[Aged Payable report](#accounting-vendor-bills-age-payable-report) provides an overview of all
outstanding bills to help ensure timely payment of the correct amounts.

#### SEE ALSO
- Tutorial [Registering a vendor bill](https://www.odoo.com/slides/slide/register-a-vendor-bill-6582)
- [Manage vendor bills](../../../inventory_and_mrp/purchase/manage_deals/manage.md)

<a id="accounting-vendor-bills-creation"></a>

## Bill creation

<a id="accounting-vendor-bills-creation-manual"></a>

### Thủ công

To create a vendor bill manually, go to Accounting ‣ Vendors ‣ Bills and
click New.

<a id="accounting-vendor-bills-automatic"></a>

### Tự động

Vendor bills can be automatically created by **sending an email** to an [email alias](invoice_digitization.md#invoice-digitization-email-alias) associated with the purchase journal, or by **uploading a PDF**
in Accounting ‣ Vendors ‣ Bills and then clicking Upload.

#### NOTE
- Once the bill is uploaded, the PDF document appears on the right side of the screen, making it
  easy to fill in the bill information.
- Bills can be [digitized](invoice_digitization.md) for automatic completion.
- Services such as digitizing scanned or PDF vendor bills in Odoo require [In-App
  Purchase (IAP)](../../../essentials/in_app_purchase.md) credit or tokens.

<a id="accounting-vendor-bills-bill-completion"></a>

## Bill completion

Whether the bill is created manually or automatically, make sure the following fields are
appropriately completed:

- Vendor: Odoo automatically fills in some information based on the information on the
  vendor's contact record as well as previous purchase orders and bills.
- Bill Reference: Add the sales order reference provided by the vendor. This field is
  used to [match](../payments/#accounting-payments-payments-matching) the products when they are received.
- Auto-Complete: Select a past bill/purchase order to complete the document
  automatically. The Vendor field should be completed before completing this field.
- Bill Date: Select the document's issuance date.
- Accounting Date: Update the document's accounting registration date if needed.
- Payment Reference: The Memo field automatically includes the payment
  reference once the payment is registered.
- Recipient Bank: Indicates the account number to which the payment will be made. This
  field is required when paying via batch payment files (such as [NACHA](../../fiscal_localizations/united_states.md#l10n-us-ach-electronic-transfers) and [SEPA](../payments/pay_sepa.md)).
- Due Date or Payment Terms must be specified for the bill payment.
- Journal: Select which journal should record the bill and in which [currency](../get_started/multi_currency.md).

#### NOTE
Multiple bills for the same purchase order may be issued if the vendor is on back-order and sends
invoices as products are shipped or if the vendor sends partial bills or requests a deposit. In
this case, multiple bills may have the same Bill Reference.

<a id="accounting-vendor-bills-bill-confirmation"></a>

## Bill confirmation

Click Confirm when the document is completed. The status changes to Posted,
and a journal entry is generated based on the vendor bill information. On confirmation, Odoo assigns
each vendor bill a unique number from a defined [sequence](sequence.md).

#### NOTE
Once confirmed, a vendor bill can no longer be updated. Click Reset to draft if
changes are required.

<a id="accounting-vendor-bills-bill-payment"></a>

## Payment and reconciliation

To register a payment, click on Register Payment. In the Register Payment
window, select the Journal, the Payment Method, the Amount, and
the Currency.

When the Amount paid is less than the total remaining amount on the vendor bill, the
payment is [partial](../payments/#accounting-payments-partial-payment), and the Payment
Difference field displays the outstanding balance.

The Memo field is filled automatically if the Payment Reference has been set
correctly on the vendor bill. If the field is empty, select the vendor invoice number as a
reference.

Then click Create payment. An In Payment/Partial banner appears
on the bill until it is [reconciled](../bank/reconciliation.md) and its status updates to
Paid.

#### SEE ALSO
- thanh toán
- [Đối chiếu ngân hàng](../bank/reconciliation.md)

<a id="accounting-vendor-bills-age-payable-report"></a>

## Báo cáo tuổi nợ phải trả

To get an overview of the open vendor bills and their due dates, go to Accounting
‣ Reporting ‣ Aged payable.

Click the <i class="fa fa-caret-right"></i> (right arrow) icon next to a vendor to view the details
of all their outstanding bills, including the due dates and amounts.

#### NOTE
Click PDF or XLSX to generate a PDF or XLSX file, respectively.

* [AI-powered document digitization](invoice_digitization.md)
* [Non-current assets and fixed assets](assets.md)
* [Deferred expenses](deferred_expenses.md)
* [Vendor bill sequence](sequence.md)
