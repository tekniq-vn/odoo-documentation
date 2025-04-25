# Thanh toán online

* [Install the patch to disable online invoice payment](install_portal_patch.md)
  * [Update Odoo to the latest release](install_portal_patch.md#update-odoo-to-the-latest-release)
  * [Update the list of available modules](install_portal_patch.md#update-the-list-of-available-modules)
  * [Install the module Invoice Online Payment Patch](install_portal_patch.md#install-the-module-invoice-online-payment-patch)

To make it more convenient for your customers to pay the invoices you issue, you can activate the
**Invoice Online Payment** feature, which adds a *Pay Now* button on their **Customer Portal**. This
allows your customers to see their invoices online and pay directly with their favorite payment
method, making the payment process much easier.

![Payment provider choice after having clicked on "Pay Now"](../../../../../.gitbook/assets/online-payment-providers.png)

## Cấu hình

Make sure your [payment providers are correctly configured](../../../payment_providers/).

#### NOTE
By default, "[Wire Transfer](../../../payment_providers/wire_transfer.md)" is the
only payment provider activated, but you still have to fill out the payment details.

To activate the Invoice Online Payment, go to Accounting ‣ Configuration ‣
Settings ‣ Customer Payments, enable **Invoice Online Payment**, and click on *Save*.

## Cổng thông tin Khách hàng

After issuing the invoice, click on *Send & Print* and send the invoice by email to the customer.
They will receive an email with a link that redirects them to the invoice on their **Customer
Portal**.

![Email with a link to view the invoice online on the Customer Portal.](../../../../../.gitbook/assets/view-invoice.png)

They can choose which Payment Provider to use by clicking on *Pay Now*.

!["Pay now" button on an invoice in the Customer Portal.](../../../../../.gitbook/assets/pay-now.png)

#### SEE ALSO
- [Thanh toán online](../../../payment_providers/)
