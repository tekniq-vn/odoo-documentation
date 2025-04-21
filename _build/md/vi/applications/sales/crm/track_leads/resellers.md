# Đại lý

Within Odoo's *CRM* app, leads can be forwarded to resellers (or partners). Leads can be manually
assigned, or automatically assigned, based on the resellers' designated *level* and location.

## Cấu hình

To utilize the reseller features, the *Resellers* module first needs to be installed. Navigate to
the Apps application, and remove the Apps filter from the
Search... bar. Then, search for `Resellers`.

![The resellers module in Odoo.](applications/sales/crm/track_leads/resellers/resellers-module.png)

Click Activate on the Resellers module card that appears. Doing so installs
the module, and returns to the main Odoo dashboard.

After the module is installed, navigate to the CRM app. Under the
Configuration menu is a new section, titled Resellers, with three
options beneath it: Partner Levels, Partner Activations, and
Commission Plans.

<a id="crm-partner-levels"></a>

## Partner levels

Partner *levels* are used to differentiate between various resellers. To view the partner levels,
navigate to CRM app ‣ Configuration ‣ Resellers: Partner Levels.

On the Partner Levels page that appears, there are three default levels:

- Vàng
- Bạc
- Đồng

New levels can be added, as needed, by clicking New, and filling out the resulting level
form.

Existing levels can also be edited and renamed, if desired, as well. To modify a level, select it
from the list, and proceed to make any desired changes from the level form page that appears.

Level weight is used to decide the probability a partner to be assigned a lead or opportunity. On
the level form, assign a numerical value (greater than zero) to the Level Weight field.
If the weight is zero, no leads are assigned.

<a id="crm-partner-activations"></a>

## Partner activations

Partner *activations* are used to identify the status of a partner. Activations are assigned on an
individual contact record, and can be used to group or filter the *Partnership Analysis* report
(CRM app ‣ Reporting ‣ Partnerships).

To view the partner levels, navigate to CRM app ‣ Configuration ‣ Partner
Activations.

Three activation types are created by default in the *CRM* app:

- Fully Operational
- Ramp-up
- First Contact

New partner activations can be added, as needed, by clicking New, and entering a
Name on the new line that appears. Then, select the desired status in the
Active column.

Existing partner activations can also be edited and renamed, if desired. To rename a status, click
the Name field of a desired level, and enter a new name.

To change the active status of an activation, slide the toggle in the Active column of
the desired activation to the *inactive* position.

![The list of default partner activations in the CRM app.](applications/sales/crm/track_leads/resellers/activations-toggle.png)

## Partner assignments

After [partner levels](#crm-partner-levels) and [partner activations](#crm-partner-activations) configured.

To update an individual partner record, navigate to CRM app ‣ Sales ‣
Customers, and click the Kanban card for the desired partner to open the customer record.

On the customer record, click the Partner Assignment tab.

Click the Partner Level field, and select an option from the drop-down menu to assign a
level. Click the Activation field, and select a partner activation type from the
drop-down list, if desired. Then, click the Level Weight field to assign a different
level weight, if necessary.

## Publish partners

With the Odoo *Website* and *Resellers* apps installed, a new webpage (`/partners`) is created to
display a list of all active partners from the *CRM* app.

Next, return to CRM app ‣ Sales ‣ Customers, and click the Kanban card for a
partner. From that partner's contact form, click the Go to Website smart button at the
top of the page to open that partner's webpage.

Next, click Edit at the top-right of the partner's webpage, and use the [building
blocks](../../../websites/website/web_design/building_blocks.md) to add any additional design
elements, or information about the partner.

After making any necessary changes to the page, click Save. At the top of the page,
slide the Unpublished toggle to the active, Published position, if needed.

Repeat these steps for all partners.

![An example of the partners webpage, displaying available partners by level and location.](applications/sales/crm/track_leads/resellers/partners-webpage.png)
