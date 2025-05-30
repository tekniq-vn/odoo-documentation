# VAT numbers verification (VIES)

[VAT Information Exchange System](https://ec.europa.eu/taxation_customs/vies/#/vat-validation), or
**VIES**, is a tool provided by the European Commission that allows you to check the validity of VAT
numbers for companies registered in the European Union.

Odoo's VAT Validation feature uses the VIES to verify your contacts' VAT numbers directly from
Odoo's interface.

#### NOTE
Regardless of whether or not the Verify VAT Numbers feature is enabled, Odoo checks the format of
a contact's VAT against the [expected format of VAT numbers](https://en.wikipedia.org/wiki/VAT_identification_number) from that country.

## VIES VAT number verification

To activate this feature, go to Accounting ‣ Configuration ‣ Settings. In the
Taxes section, enable the Verify VAT Numbers feature, and click on
Save.

Once the Verify VAT Numbers feature is enabled, if the contact's Tax ID
field is populated *and* its country is different from your company's country, Odoo displays an
Intra-Community Valid checkbox. Odoo tests the VAT number through the VIES and
automatically checks or unchecks the Intra-Community Valid checkbox depending on the
validity of the VAT number.

![Intra-community valid checkbox on the contact record](../../../../.gitbook/assets/intra-community-valid.png)

#### IMPORTANT
It is possible to manually override the Intra-Community Valid field on a contact in
case the automatic VIES check is incorrect (for example, if the company was recently created and
its VAT is not yet in the VIES). This change is logged in the chatter for transparency.

#### NOTE
Odoo can [automatically apply fiscal positions](fiscal_positions.md#fiscal-positions-automatic). If the Verify VAT
Numbers feature is enabled, any fiscal positions with VAT required enabled will require
Intra-Community valid VAT numbers to apply automatically.
