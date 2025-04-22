# SIPS

[SIPS](https://sips.worldline.com/) is an online payments solution from the multinational
Worldline.

## Cấu hình

#### SEE ALSO
- [Enabling a payment provider](applications/finance/payment_providers.md#payment-providers-add-new)

### Credentials tab

Odoo needs your **API Credentials** to connect with your SIPS account, which comprise:

- **Merchant ID**: The ID solely used to identify the merchant account with SIPS.
- **Secret Key**: The key to sign the merchant account with SIPS.
- **Secret Key Version**: The version of the key, pre-filled.
- **Interface Version**: Pre-filled, don't change it.

You can copy your credentials from your SIPS environment info documentation, in the section
**PROD**, and paste them in the related fields under the **Credentials** tab.

#### IMPORTANT
If you are trying SIPS as a test, with the *TEST* credentials, change the **State** to *Test
Mode*. We recommend doing this on a test Odoo database, rather than on your main database.

#### SEE ALSO
- [Thanh toán online](applications/finance/payment_providers.md)
