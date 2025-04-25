# Buckaroo

[Buckaroo](https://www.buckaroo.eu/) is a Dutch-based company that offers several online payment
possibilities.

<a id="payment-providers-buckaroo-configure-dashboard"></a>

## Configuration on Buckaroo Plaza

1. Log into [Buckaroo Plaza](https://plaza.buckaroo.nl), go to My Buckaroo ‣
   Websites and select the Push settings tab.
2. Tick the Enable Push Response check box in the Delayed and Push responses
   section.
3. Enter the URL of your Odoo database, followed by `/payment/buckaroo/webhook` in both the
   Push URI Success/Pending and Push URI Failure text fields. For example:
   `https://yourcompany.odoo.com/payment/buckaroo/webhook`.
4. Leave the other fields as they are and click Save.
5. In the General tab, copy the website Key (i.e., the key used to uniquely
   identify your website with Buckaroo) and save it for later.
6. Go to Configuration ‣ Security ‣ Secret key, enter or Generate a
   Secret key and click Save. Save the key for later.

## Configuration on Odoo

1. [Navigate to the payment provider Buckaroo](./#payment-providers-add-new) and change its state
   to Enabled.
2. In the Credentials tab, fill the Website Key and Secret Key
   fields with the values you saved at the step
   [Configuration on Buckaroo Plaza](#payment-providers-buckaroo-configure-dashboard).
3. Configure the options in the other tabs to your liking.

#### SEE ALSO
[Thanh toán online](./)
