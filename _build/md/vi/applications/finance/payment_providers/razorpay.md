# Razorpay

[Razorpay](https://razorpay.com/) is an online payments provider established in India and\
covering more than 100 payment methods.

## Configuration on Razorpay Dashboard

1. Log into [Razorpay Dashboard](https://dashboard.razorpay.com/) and go to\
   Settings ‣ API Keys. Generate the new keys and copy the values of the\
   Key Id and Secret Key fields and save them for later.
2. Go to Settings ‣ Webhooks, click on Create New Webhook,\
   and enter your Odoo database URL followed by `/payment/razorpay/webhook` in\
   the Webhook URL text field.\
   Ví dụ: `https://example.odoo.com/payment/razorpay/webhook`.\

3. Fill the Secret field with a password of your choice and save it for later.
4. Make sure the payment.authorized, payment.captured,\
   payment.failed, refund.failed and refund.processed\
   checkboxes are ticked.
5. Click on Create Webhook to finalize the configuration.

#### IMPORTANT

The Recurring payments feature must\
be activated if you want to make recurring payments.\
Send a request to the [Razorpay Support team](https://razorpay.com/support/#request) to\
enable recurring payments.

## Configuration on Odoo

1. [Navigate to the payment provider Razorpay](../payment_providers.md#payment-providers-add-new) and change its
   state to Enabled.
2. In the Credentials tab, fill the Key Id, Key Secret, and\
   Webhook Secret with the values you saved at the step[Configuration on Razorpay Dashboard](razorpay.md#payment-providers-razorpay-configure-dashboard).
3. Configure the rest of the options to your liking.

#### IMPORTANT

If you configure Odoo to capture amounts manually:

* Be aware that the **manual voiding** of a transaction is not supported by Razorpay.
* After **five days**, if the transaction hasn't been captured yet, it'll automatically be**voided**.

#### SEE ALSO
- [Thanh toán online](../payment_providers.md)
