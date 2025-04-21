# Vantiv

Connecting a Vantiv payment terminal allows you to offer a fluid payment flow to your customers and
ease the work of your cashiers.

#### NOTE
Please note MercuryPay only operates with US and Canadian banks, making this procedure only
suitable for North American businesses.

#### WARNING
Vantiv card readers should be purchased exclusively from Vantiv, as certain Vantiv terminals
bought on Amazon do not include the correct encryption needed to be used with an Odoo database.

## Cấu hình

### Configure the payment method

Enable the payment terminal in the Payment Terminals section [of the application
settings](../../configuration.md#configuration-settings).

Then, go to Point of Sale ‣ Configuration ‣ Payment Methods, and [create
the related payment method](../../payment_methods.md). Set the journal type as Bank and
select Vantiv in the Use a Payment Terminal field.

Type the name you want to give to your Vantiv Credentials and click Create
and edit. Enter your Merchant ID and Merchant Password, then click
Save & Close.

![Vantiv payment method](applications/sales/point_of_sale/payment_methods/terminals/vantiv/vantiv-method.png)

Once the payment method is created, you can select it in your POS settings. To do so, go to the
[POS' settings](../../configuration.md#configuration-settings) and add the payment method under the
Payment section.
