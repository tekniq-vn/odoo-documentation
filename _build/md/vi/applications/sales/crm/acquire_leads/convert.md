# Convert leads into opportunities

*Leads* act as a qualifying step before an opportunity is created. This provides additional time to
review its potential, and gauge its viability, before the opportunity is assigned to a salesperson.

## Cấu hình

To activate the *Leads* setting, navigate to CRM app ‣ Configuration ‣ Settings
and check the box labeled, Leads. Then, click Save.

![Leads setting on CRM configuration page.](applications/sales/crm/acquire_leads/convert/convert-leads-leads-setting.png)

Activating this feature adds a new menu option, Leads, to the header bar, located along
the top of the screen.

![Leads menu on CRM application.](applications/sales/crm/acquire_leads/convert/convert-leads-leads-menu.png)

Sau khi cài đặt *Lead* được kích hoạt, nó sẽ áp dụng cho tất cả bộ phận sales theo mặc định. Để tắt tính năng lead cho một bộ phận cụ thể, hãy đi đến Ứng dụng CRM ‣ Cấu hình ‣ Bộ phận Sales. Sau đó, chọn một bộ phận từ danh sách để mở trang cấu hình của bộ phận đó. Bỏ chọn hộp kiểm Lead, nằm bên dưới trường Bộ phận sales, rồi nhấp Lưu.

![Leads menu on CRM application.](applications/sales/crm/acquire_leads/convert/convert-leads-leads-button.png)

## Convert a lead into an opportunity

To convert a lead into an *opportunity*, navigate to CRM app ‣ Leads, and click
on a lead from the list to open it.

#### WARNING
If a Similar Leads smart button appears at the top of the page for the lead, it
indicates a similar lead or opportunity already exists in the database. Before converting this
lead, click the smart button to confirm if the lead should be merged.

![Close up of a lead with emphasis on the Similar Leads smart button.](applications/sales/crm/acquire_leads/convert/similar-leads-smart-button.png)

Click the Convert to Opportunity button, located at the top-left of the page.

![Create opportunity button on a lead record.](applications/sales/crm/acquire_leads/convert/convert-leads-convert-opp-button.png)

This opens a Convert to opportunity pop-up modal. Here, in the Conversion
Action field, select the Convert to opportunity option.

#### NOTE
To merge this lead with an existing similar lead or opportunity, select Merge with
existing opportunities in the Conversion Action field. This generates a list of the
similar leads/opportunities to be merged.

When merging, Odoo gives priority to whichever lead/opportunity was created in the system first,
merging the information into the first created lead/opportunity. However, if a lead and an
opportunity are being merged, the resulting record is referred to as an opportunity, regardless
of which record was created first.

Then, select a Salesperson and a Sales Team to which the opportunity should
be assigned. Neither field is required, though if a selection is made in the Salesperson
field, the Sales Team field is populated automatically, based on the salesperson's team
assignments.

If the lead has already been assigned to a salesperson or a team, these fields automatically
populate with that information.

![Create opportunity pop-up.](applications/sales/crm/acquire_leads/convert/convert-leads-conversion-action.png)

Under the Customer heading, choose from the following options:

- Create a new customer: choose this option to use the information in the lead to create
  a new customer record.
- Link to an existing customer: choose this option, then select a customer from the
  resulting drop-down menu, to link this opportunity to an existing customer record.
- Do not link to a customer: choose this option to convert the lead, but not link it to
  a new or existing customer.

Lastly, when all configurations are complete, click Create Opportunity.

To view the newly created opportunity, navigate to CRM app ‣ My Pipeline.

#### NOTE
Some filters may need to be removed from the Search... bar on the top
Pipeline page to view all opportunities.
