# AsiaPay

[AsiaPay](https://www.asiapay.com/) is an online payments provider established in Hong Kong and
covering several Asian countries and payment methods.

<a id="payment-providers-asiapay-configure-dashboard"></a>

## Configuration on AsiaPay Dashboard

1. Log into AsiaPay Dashboard according to the account provided by AsiaPay.
   - [PayDollar](https://www.paydollar.com/b2c2/eng/merchant/index.jsp): For markets in HK,
     CN, MO, TW, SG, MY, IN, VN, NZ and AU
   - [PesoPay](https://www.pesopay.com/b2c2/eng/merchant/index.jsp): For market in PH
   - [SiamPay](https://www.siampay.com/b2c2/eng/merchant/index.jsp): For market in TH
   - [BimoPay](https://www.bimopay.com/b2c2/eng/merchant/index.jsp): For market in ID
2. Go to Profile ‣ Account Information. Copy the values of the
   Currency and Secure Hash fields and save them for later.
3. Go to Profile ‣ Payment Account Settings and enable the option
   Return Value Link (Datefeed);
   <br/>
   Enter your Odoo database URL followed by `/payment/asiapay/webhook` in the
   Return Value Link (Datefeed) text field. For example:
   `https://yourcompany.odoo.com/payment/asiapay/webhook`;
   <br/>
   Click on Test to check if the webhook is working correctly.
   <br/>
4. Click on Update to finalize the configuration.

<a id="payment-providers-asiapay-configure-odoo"></a>

## Configuration on Odoo

1. [Navigate to the payment provider AsiaPay](applications/finance/payment_providers.md#payment-providers-add-new) and change its state
   to Enabled.
2. In the Credentials tab, choose the Brand of your Asiapay account. Then
   fill in the Merchant ID and Secure Hash Secret, and the
   Currency in the Configuration tab with the values you saved at the
   step [Configuration on AsiaPay Dashboard](#payment-providers-asiapay-configure-dashboard);
   <br/>
   By default, the payment provider AsiaPay is configured to verify the secret hash with the hash
   function `SHA1`. If a different function is [set on your account](#payment-providers-asiapay-configure-dashboard), activate the [developer mode](applications/general/developer_mode.md#developer-mode) and set the same value to the field Secure Hash Function in the
   Credentials tab.
   <br/>
3. Configure the rest of the options to your liking.

#### SEE ALSO
- [Thanh toán online](applications/finance/payment_providers.md)
