# Xendit

[Xendit](https://www.xendit.co) is an Indonesian-based payment solution provider that covers
several Southeast Asian countries. It allows businesses to accept credit cards as well as several
local payment methods.

<a id="payment-providers-xendit-configure-dashboard"></a>

## Configuration on the Xendit Dashboard

1. Create a Xendit account if necessary and log in to the [Xendit Dashboard](https://dashboard.xendit.co).
2. Check your account mode in the top left corner of the page. Use the Test Mode to try
   the integration without charging your customers. Switch to Live Mode once you are
   ready to accept payments.
3. Navigate to Configuration: Settings in the left part of the application page.
   In the Developers section, click
   [API Keys](https://dashboard.xendit.co/settings/developers#api-keys).
4. Click Generate Secret Key. In the popup box, enter any API key name,
   select Write for the Money-in Products permission and None
   for all other permissions then click Generate key.
5. Confirm your password to display your API key. Copy or download the key and **save
   this information securely for later**. This is the only time the API key can be viewed or
   downloaded.
6. Once completed, scroll down the page to the
   [Webhooks](https://dashboard.xendit.co/settings/developers#webhooks) section to generate
   the webhook token.
7. Under Webhook verification token, click View Webhook Verification Token,
   then confirm your password to display the token. Save it for later.
8. In the Webhook URL section, enter your Odoo database's URL, followed by
   `/payment/xendit/webhook` (e.g., `https://example.odoo.com/payment/xendit/webhook`) in the field
   Invoices paid and click the Test and save button next to it.

## Configuration on Odoo

1. [Navigate to the payment provider Xendit](./#payment-providers-add-new) and change its state
   to Enabled.
2. Fill in the Secret Key and Webhook Token fields with the
   information saved at the step [Configuration on the Xendit Dashboard](#payment-providers-xendit-configure-dashboard).
3. Configure the rest of the options to your liking.

#### SEE ALSO
[Thanh toán online](./)
