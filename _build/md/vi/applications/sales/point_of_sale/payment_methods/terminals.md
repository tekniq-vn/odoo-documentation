# Payment terminals

Connecting and integrating a payment terminal with your POS system allows you to accept multiple
payment options, including credit and debit cards, making the payment process more efficient.

<a id="terminals-configuration"></a>

## Cấu hình

Go to the [application settings](../configuration.md#configuration-settings), scroll down to the
Payment Terminals section, and tick your terminal's checkbox.

![checkbox in the settings to enable a payment terminal](applications/sales/point_of_sale/payment_methods/terminals/settings-pt.png)

Then, follow the corresponding documentation to configure your device:

- [Adyen configuration](terminals/adyen.md)
- [Ingenico configuration](terminals/ingenico.md)
- [Mercado Pago configuration](terminals/mercado_pago.md)
- [Razorpay configuration](terminals/razorpay.md)
- [SIX configuration](terminals/six.md)
- [Stripe configuration](terminals/stripe.md)
- [Vantiv configuration](terminals/vantiv.md)
- [Viva Wallet configuration](terminals/viva_wallet.md)
- [Worldline configuration](terminals/worldline.md)

Once the terminal is configured, you can [create the corresponding payment method and add it to
the POS](../payment_methods.md).

## Pay with a payment terminal

When processing a payment, select the terminal's payment method. Check the amount and
click on Send. Once the payment is successful, the status changes to Payment
Successful.

#### NOTE
- In case of connection issues between Odoo and the payment terminal, force the payment by
  clicking on Force Done, which allows you to validate the order.
  <br/>
  This option is only available after receiving an error message informing you that the
  connection failed.
  <br/>
- To cancel the payment request, click on Cancel.

* [Adyen](terminals/adyen.md)
* [Ingenico](terminals/ingenico.md)
* [Mercado Pago](terminals/mercado_pago.md)
* [Razorpay](terminals/razorpay.md)
* [SIX](terminals/six.md)
* [Stripe](terminals/stripe.md)
* [Vantiv](terminals/vantiv.md)
* [Viva Wallet](terminals/viva_wallet.md)
* [Worldline](terminals/worldline.md)
