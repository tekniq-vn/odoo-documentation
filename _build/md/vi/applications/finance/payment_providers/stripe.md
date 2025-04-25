# Stripe

[Stripe](https://stripe.com/) is a United States-based online payment solution provider allowing
businesses to accept **credit cards** and other payment methods.

#### SEE ALSO
- [List of countries supported by Stripe](https://stripe.com/global)
- [List of payment methods supported by Stripe](https://stripe.com/payments/payment-methods)

## Create your Stripe account with Odoo

The method to acquire your credentials depends on your hosting type:

Odoo Online

1. [Navigate to the payment provider Stripe](./#payment-providers-supported-providers) and
   click Connect Stripe.
2. Go through the setup process and confirm your email address when Stripe sends you a
   confirmation email.
3. At the end of the process, click Agree and submit. If all requested information
   has been submitted, you are then redirected to Odoo, and your payment provider is enabled.

Odoo.sh hoặc On-premise

1. [Navigate to the payment provider Stripe](./#payment-providers-supported-providers) and
   click Connect Stripe.
2. Go through the setup process and confirm your email address when Stripe sends you a
   confirmation email.
3. At the end of the process, click Agree and submit; you are then redirected to
   the payment provider **Stripe** in Odoo.
4. [Fill in your credentials](#stripe-api-keys).
5. [Generate a webhook](#stripe-webhook).
6. Set the State field to Enabled.

<a id="stripe-api-keys"></a>

### Fill in your credentials

If your **API credentials** are required to connect with your Stripe account, proceed as follows:

1. Go to [the API keys page on Stripe](https://dashboard.stripe.com/account/apikeys), or log into
   your Stripe dashboard and go to Developers ‣ API Keys.
2. In the Standard keys section, copy the Publishable key and the
   Secret key and save them for later.
3. In Odoo, [navigate to the payment provider Stripe](./#payment-providers-supported-providers).
4. In the Credentials tab, fill in the Publishable Key and
   Secret Key fields with the values you previously saved.

<a id="stripe-webhook"></a>

### Tạo webhook

If your **Webhook Signing Secret** is required to connect with your Stripe account, you can create a
webhook automatically or manually.

Create the webhook automatically

Make sure your [Publishable and Secret keys](#stripe-api-keys) are filled in, then click
Generate your webhook.

Create the webhook manually

1. Go to the [Webhooks page on Stripe](https://dashboard.stripe.com/webhooks), or log into
   your Stripe dashboard and go to Developers ‣ Webhooks.
2. In the Hosted endpoints section, click Add endpoint. Then, in the
   Endpoint URL field, enter your Odoo database's URL, followed by
   `/payment/stripe/webhook`, e.g., `https://yourcompany.odoo.com/payment/stripe/webhook`.
3. Click Select events at the bottom of the form, then select the following
   events:
   - in the Charge section: charge.refunded and
     charge.refund.updated;
   - in the Payment intent section:
     payment_intent.amount_capturable_updated,
     payment_intent.payment_failed, payment_intent.processing, and
     payment_intent.succeeded;
   - in the Setup intent section: setup_intent.succeeded.
4. Nhấp Thêm sự kiện.
5. Click Add endpoint, then click Reveal and save your
   Signing secret for later.
6. In Odoo, [navigate to the payment provider Stripe](./#payment-providers-supported-providers).
7. In the Credentials tab, fill the Webhook Signing Secret field with
   the value you previously saved.

#### NOTE
You can select other events, but they are currently not processed by Odoo.

## Bật Apple Pay

To allow customers to use the Apple Pay button to pay their eCommerce orders, go to the
Configuration tab, enable Allow Express Checkout, and click
Enable Apple Pay.

#### SEE ALSO
- [Express checkout and Google Pay](./#payment-providers-express-checkout)
- [Thanh toán online](./)
- [Use Stripe as a payment terminal in Point of Sale](../../sales/point_of_sale/payment_methods/terminals/stripe.md)
