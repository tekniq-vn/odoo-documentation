# Tăng cường lead

*Lead enrichment* is a service that provides business information for a contact attached to a lead.
Lead enrichment is an In-App Purchase (IAP) that requires credits to use, and is available for
existing leads in an Odoo database.

The information provided by lead enrichment can include general information about the business
(including full business name and logo), social media accounts, Company type,
Founded information, Sectors information, the number of
Employees, Estimated revenue, Phone number,
Timezone, and Technologies Used.

#### NOTE
Enterprise Odoo users with a valid subscription get free credits to test  features before deciding to purchase more credits for the database. This includes
demo/training databases, educational databases, and one-app-free databases.

#### IMPORTANT
The *leads* feature **must** be activated in the *CRM* settings page in order to use lead
enrichment. To access the *CRM* settings, navigate to CRM app ‣ Configuration
‣ Settings. Under the CRM section activate the Leads option and click
Save.

## Lead enrichment set up

To set up lead enrichment in the *CRM* application, navigate to CRM app ‣
Configuration ‣ Settings. Then, under the Lead Generation section, tick the checkbox
next to Lead Enrichment, and select either Enrich leads on demand only or
Enrich all leads automatically. Click the Save button to activate the
changes.

![CRM lead generation settings page, with lead enrichment activation highlighted, and enrich
leads on demand only chosen.](applications/sales/crm/optimize/lead_enrichment/lead-enrichment-activate.png)

## Tăng cường lead

Enrichment of leads is based on the domain of the email address of the customer set on the lead.
There are two different ways that a lead can be enriched: *automatically* or *manually*.

### Automatically enrich leads

During set up, if Enrich all leads automatically was selected on the *CRM*
Settings page, then no action needs to be taken by the user to enrich the lead. A
scheduled action runs automatically, every sixty minutes, and enrichment occurs on leads, after a
remote database is contacted.

### Manually enrich leads

If the Enrich leads on demand only option was selected on the *CRM* Settings
page, when activating Lead Enrichment, each lead that a user wishes to enrich **must**
be manually enriched. This is achieved by clicking the Enrich button in the top menu of
the lead.

The same information will be retrieved at the same  credit cost (one per
enrichment). This method of enrichment is useful when every lead does not need to be enriched, or
cost is an issue.

![Manual enrich button feature highlighted on the CRM lead.](applications/sales/crm/optimize/lead_enrichment/manual-enrichment.png)

## Định giá

Lead enrichment is an In-App Purchase (IAP) feature, and each enriched lead costs one credit.

#### NOTE
See here for full pricing information: [Lead Generation by Odoo IAP](https://iap.odoo.com/iap/in-app-services/273).

To buy credits, navigate to CRM app ‣ Configuration ‣ Settings. In the
Lead Generation section, under the Lead Enrichment feature, click on
Buy Credits.

![Buy credits from the lead enrichment settings.](applications/sales/crm/optimize/lead_enrichment/buy-lead-enrichment-credits-setting.png)

Credits and balances may also be purchased by navigating to the Settings app. In
the Contacts section, under the Odoo IAP feature, click on View
My Services.

![Buy credits in the Odoo IAP settings.](applications/sales/crm/optimize/lead_enrichment/view-my-services-setting.png)

#### SEE ALSO
[Mua hàng trong ứng dụng (IAP)](../../../essentials/in_app_purchase.md)

#### IMPORTANT
When collecting a company's contact information, make sure to be aware of the latest EU
regulations. For more information about General Data Protection Regulation, refer to: [Odoo GDPR](http://odoo.com/gdpr).
