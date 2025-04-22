# PayPal

[Paypal](https://www.paypal.com/) is an American online payment provider available worldwide, and
one of the few that does not charge a subscription fee.

#### NOTE
While PayPal is available in [over 200 countries/regions](https://www.paypal.com/webapps/mpp/country-worldwide), only [a selection of currencies are
supported](https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies).

## Settings in PayPal

To access your PayPal account settings, log into PayPal, open the Account Settings, and
open the Website payments menu.

![PayPal account menu](../../../.gitbook/assets/paypal-account.png)

#### IMPORTANT
Note that for PayPal to work **in Odoo**, the options [Auto Return](#paypal-auto-return) and
[PDT](#paypal-pdt) **must** be enabled.

<a id="paypal-auto-return"></a>

### Auto Return

The **Auto Return** feature automatically redirects customers to Odoo once the payment is processed.

From Website payments, go to Website preferences ‣ Update ‣ Auto
return for website payments ‣ Auto return and select On. Enter the address of your
Odoo database (e.g., `https://yourcompany.odoo.com`) in the Return URL field, and
Save.

#### NOTE
Any URL does the job. Odoo only needs the setting to be enabled since it uses another URL.

<a id="paypal-pdt"></a>

### Payment Data Transfer (PDT)

 allows to receive payment confirmations, displays the payment
status to the customers, and verifies the authenticity of the payments. From Website
preferences ‣ Update, scroll down to Payment data transfer and select On.

### PayPal Account Optional

We advise not to prompt customers to log in with a PayPal account upon payment. It is better and
more accessible for customers to pay with a debit/credit card. To disable that prompt, go to
Account Settings ‣ Website payments ‣ Update and select On for
PayPal account optional.

### Payment Messages Format

If you use accented characters (or anything other than primary Latin characters) for customer names
or addresses, then you **must** configure the encoding format of the payment request sent by Odoo to
PayPal. If you do not, some transactions fail without notice.

To do so, go to [your production account](https://www.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding). Then, click More Options and set the two default
encoding formats as UTF-8.

## Cài đặt trong Odoo

#### SEE ALSO
[Enabling a payment provider](applications/finance/payment_providers.md#payment-providers-add-new)

Odoo needs your **API Credentials** to connect with your PayPal account. To do so, go to
Accounting ‣ Configuration ‣ Payment Providers and Activate PayPal.
Then, enter your PayPal account credentials in the Credentials tab:

- Email: the login email address in Paypal;
- PDT Identity Token: the key used to verify the authenticity of transactions.

<a id="paypal-testing"></a>

## Test environment

### Cấu hình

Thanks to PayPal sandbox accounts, you can test the entire payment flow in Odoo.

Log into the [Paypal Developer Site](https://developer.paypal.com/) using your PayPal credentials,
which creates two sandbox accounts:

- A business account (to use as merchants, e.g.,
  [pp.merch01-facilitator@example.com](mailto:pp.merch01-facilitator@example.com));
- A default personal account (to use as shoppers, e.g.,
  [pp.merch01-buyer@example.com](mailto:pp.merch01-buyer@example.com)).

Log into PayPal sandbox using the merchant account and follow the same configuration instructions.
Enter your sandbox credentials in Odoo (Accounting ‣ Configuration ‣ Payment
Providers ‣ PayPal in the Credentials tab, and make sure the status is set on
Test Mode.

Run a test transaction from Odoo using the sandbox personal account.

#### SEE ALSO
- [Thanh toán online](applications/finance/payment_providers.md)
