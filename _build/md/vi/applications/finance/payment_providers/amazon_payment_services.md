# Dịch vụ thanh toán Amazon

[Amazon Payment Services](https://paymentservices.amazon.com/) or APS is an online payment provider
established in Dubai offering several online payment options.

<a id="payment-providers-aps-configure-dashboard"></a>

## Configuration on APS Dashboard

1. Log into your [Amazon Payment Services Dashboard](https://fort.payfort.com/) and go to
   Integration Settings ‣ Security Settings. Generate the
   Access Code if none has been generated yet. Copy the values of the
   Merchant Identifier, Access Code, SHA Request Phrase and
   SHA Response Phrase fields, and save them for later.
2. Enter your Odoo database URL in the Origin URL, for example:
   `https://yourcompany.odoo.com/`. Then, click on Save Changes.
3. Navigate to Integration Settings ‣ Technical Settings and click on
   Redirection. Make sure Status is set to `Active` and select your
   preferred payment methods underneath in Payment Options.
4. Set Send Response Parameters to Yes and enter your database URL
   followed by `/payment/aps/return` in the Redirection URL.
   <br/>
   Ví dụ `https://yourcompany.odoo.com/payment/aps/return`.
   <br/>
   Enter your database URL followed by `/payment/aps/webhook` in the
   Direct Transaction Feedback and Notification URL fields.
   <br/>
   Ví dụ `https://yourcompany.odoo.com/payment/aps/webhook`.
   <br/>
   Click on Save Changes.
   <br/>
5. Under Integration Settings ‣ Payment Page Template you can customize the
   look and feel of the Amazon Payment Services payment page (where customers fill out their
   credit card details during payment).

<a id="payment-providers-aps-configure-odoo"></a>

## Configuration on Odoo

1. [Navigate to the payment provider Amazon Payment Services](../payment_providers.md#payment-providers-add-new),
   change its state to Enabled, and make sure it is Published.
2. In the Credentials tab, fill the Merchant Identifier,
   Access Code, SHA Request Phrase and SHA Response Phrase with
   the values you saved at the step [Configuration on APS Dashboard](#payment-providers-aps-configure-dashboard).
3. Configure the rest of the options to your liking.
