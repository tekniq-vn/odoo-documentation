# Enrich contacts with partner autocomplete

*Partner autocomplete* enriches the contacts database with corporate data. In any module, enter the
new company name into the Customer field (`partner_id` technical field), and select one
of the companies suggested in the drop-down menu. Instantly get valuable company information full of
hard-to-find data for a desired company.

#### IMPORTANT
A company **cannot** already be manually entered in the *Contacts* application prior to enriching
it with data.

The information provided by partner autocomplete can include general information about the business
(including full business name and logo), social media accounts, Company type,
Founded information, Sectors information, the number of
Employees, Estimated revenue, Phone number,
Timezone, and Technologies Used.

#### IMPORTANT
When getting a company's contact information make sure to be aware of the latest EU regulations.
For more information about General Data Protection Regulation refer to: [Odoo GDPR](http://odoo.com/gdpr). In Odoo, individual contact information cannot be searched for with
the partner autocomplete feature.

## Cấu hình

Go to Settings app ‣ Contacts section. Then, activate the Partner
Autocomplete feature, by ticking the checkbox beside it, and clicking Save.

![View of settings page and the activations of the feature in Odoo.](applications/sales/crm/optimize/partner_autocomplete/settings-partner-autocomplete.png)

## Enrich contacts with corporate data

From any module, as the user is typing in the name of a new company contact, Odoo reveals a large
drop-down menu of potential match suggestions. If any are selected, the contact is then populated
with corporate data related to that specific selection.

For example, after typing `Odoo`, the following information populates:

![Creating a new contact in Odoo](applications/sales/crm/optimize/partner_autocomplete/odoo-autocomplete.png)

In the chatter, the following information populates about the company, after clicking on the desired
pre-populated contact:

![View of the information being shown about odoo with the autocomplete option in Odoo](applications/sales/crm/optimize/partner_autocomplete/odoo-info-autocomplete.png)

## Định giá

*Partner Autocomplete* is an *In-App Purchase (IAP)* service, which requires prepaid credits to be
used. Each request consumes one credit.

To buy credits, go to Settings app ‣ Contacts section. Then, locate either the
Partner Autocomplete feature and click Buy credits, or locate the
Odoo IAP feature and click View My Services. From the resulting page, select
a desired package.

#### NOTE
If the database runs out of credits, the only information populated when clicking on the
suggested company will be the website link and the logo.

Learn about our [Privacy Policy](https://iap.odoo.com/privacy).

#### NOTE
Enterprise Odoo users with a valid subscription get free credits to test  features before deciding to purchase more credits for the database. This includes
demo/training databases, educational databases, and one-app-free databases.

#### SEE ALSO
[Mua hàng trong ứng dụng (IAP)](../../../essentials/in_app_purchase.md)
