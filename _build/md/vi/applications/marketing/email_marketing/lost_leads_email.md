# Lost leads reactivation email

In Odoo, lost leads are removed from the active *CRM* pipeline, but can still be targeted with the
*Email Marketing* application for strategic campaign purposes, such as lost leads reactivation.

A lost leads reactivation email looks at the leads that were lost during a specific period of time,
and uses custom filters and lost reasons to exclude undesirable leads from the mailing list.

Once a lost leads reactivation email is complete, it can be sent as is, modified and sent to
different groups for A/B testing, or saved as a template for later.

## Minimum requirements

In order to create and deliver a lost leads reactivation email campaign, the *CRM* and *Email
Marketing* applications **must** be [installed](../../general/apps_modules.md#general-install) and configured.

Here are the minimum necessary filters that pertain to a lost leads reactivation mailing campaign:

- The [Recipients](#email-marketing-recipients-field) field **must** be set to the
  *Lead/Opportunity* model.
- A [Blacklist](#email-marketing-blacklist-filter) filter to exclude unsubscribed recipients.
- A [Created on](#email-marketing-created-on-filter) to target leads that were lost during a
  specific period of time.
- [Stage](#email-marketing-stage-filter) filter(s) to exclude leads that were already won, or
  are still active in new stages of the sales pipeline (i.e. *New*, *Qualified*, etc.). These values
  will be different per organization; however, it's minimally viable to exclude all the leads in the
  *Won* stage.
- One or more [Lost Reason](#email-marketing-lost-reason-filter) filters to exclude undesired
  leads, such as duplicate, spam, or irrelevant records.
- A pair of [Active](#email-marketing-active-filter) filters to target *both* active and
  inactive leads.

## Add the necessary filters

First, navigate to the Email Marketing app, and on the Mailings page,
click the New button in the top-left corner.

<a id="email-marketing-recipients-field"></a>

On the new Mailings form, enter an appropriate Subject line for the email in
the corresponding field. Then, in the Recipients field, choose the
Lead/Opportunity model from the drop-down menu.

<a id="email-marketing-blacklist-filter"></a>

In the rules section, located beneath the Recipients field, click the modify filter
(▶ (triangle pointing right)) icon to expand the filter rules. Leave the default
Blacklist rule in place.

<a id="email-marketing-created-on-filter"></a>

### Được tạo vào

Bắt đầu bằng cách nhấp vào Quy tắc mới bên dưới quy tắc mặc định Danh sách hạn chế. Sau đó, nhấp vào trường đầu tiên của quy tắc mới xuất hiện và chọn tham số Được tạo vào từ menu thả xuống. Với thiết lập này, bạn có thể chỉ định khoảng thời gian cụ thể khi lead mục tiêu bị mất (VD: 30 ngày trước, 90 ngày trước, năm trước,...).

Then, in the second field, select <= (less than or equal to), >= (greater
than or equal to), or is between as a date operator, in order to frame the time
selection chosen in the third field.

In the third field, use the calendar popover window to select dates, and click Apply to
lock in the time range.

![A custom filter rule setting the time period to be anything before today's date.](applications/marketing/email_marketing/lost_leads_email/created-on.png)

#### IMPORTANT
When there is more than one rule applied, make sure the statement at the top of the
Recipients filter list reads: Match all of the following rules. If it
does not, click on the statement, and select all from the drop-down menu (as opposed
to any).

![The statement at the top of the filters list, with the drop-down menu open.](applications/marketing/email_marketing/lost_leads_email/match-all.png)

<a id="email-marketing-stage-filter"></a>

### Giai đoạn

Now, add the Stage filter to exclude leads that are in the *New*, *Qualified*, and *Won*
stages of the sales pipeline.

#### NOTE
This step assumes that the *New*, *Qualified*, and *Won* stages exist in the CRM pipeline;
however, stage names may differ from business to business. Refer to the database's actual stage
names in the *CRM* app's pipeline to complete this step, accordingly.

Begin again by clicking New Rule and select Stage from the first field's
drop-down menu. In the second field, select the is not in operator, and in the third
field, select the New, Qualified and Won stages to define the
rule's parameters.

When the rule is added in this way, the logic in the third field renders as `OR` (`|`)
statements.

![Include multiple Stages in the filtering rule, using the "is in" operator.](applications/marketing/email_marketing/lost_leads_email/stage-is-in.png)

<a id="email-marketing-lost-reason-filter"></a>

### Lý do mất

Next, add one or more Lost Reason rules to exclude leads that should **not** be targeted
for specific [lost reasons](../../sales/crm/pipeline/lost_opportunities.md).

Để làm điều đó, hãy tạo một Quy tắc mới khác, một lần nữa. Sau đó, trong trường đầu tiên của quy tắc, chọn Lý do mất từ menu thả xuống. Đối với toán tử, chọn không trong hoặc không chứa từ menu thả xuống. Với bất kỳ lựa chọn nào, hãy sử dụng trường thứ ba để nhập một lý do mất (hoặc nhiều lý do, tùy theo lựa chọn toán tử) để đưa vào quy tắc.

If choosing the does not contain operator, then repeat the preceding steps to add more
lost reasons, as needed, where each lost reason occupies one rule row at a time.

For more information, refer to the section below outlining how to [select appropriate lost
reasons](#email-marketing-select-lost-reasons).

![A list of filter rules that exclude all lost reasons other than the desired reason.](applications/marketing/email_marketing/lost_leads_email/reasons.png)

<a id="email-marketing-active-filter"></a>

### Đang hoạt động

Finally, add a pair of Active filters to include both active and inactive leads for the
campaign.

#### IMPORTANT
Adding both active *and* inactive lead records is necessary to capture the full scope of lost
leads in the database. Doing one without the other greatly impacts the number of targetable
records for the email campaign, and does **not** include a complete or accurate lost leads
audience.

Đầu tiên, nhấp vào biểu tượng (Thêm nhánh) trên quy tắc được tạo gần đây nhất (VD: Lý do mất), nằm ở giữa ba biểu tượng bên phải hàng quy tắc. Thao tác này sẽ thêm một cặp quy tắc bất kỳ. Sau đó, trong trường đầu tiên của quy tắc trên cùng trong nhánh mới tạo, chọn tham số Hoạt động từ menu thả xuống. Quy tắc sẽ tự động điền thành: Hoạt động *là* `đã đặt`.

For the first field of the bottom rule of the branch, select Active from the drop-down
menu again. However, this time, select is not from the operator drop-down menu in the
second field. The rule should then read: Active *is not* `set`.

![A pair of Match Any Of filter rules that include both active and inactive leads.](applications/marketing/email_marketing/lost_leads_email/active.png)

## Add body content

Now, with the domain section of the email campaign complete, create the body content of the email
using any of the premade stylized templates, or choose between the Plain Text or
Start From Scratch options for more granular control. For more information, refer to the
*Email Marketing* [documentation on how to create an email](../email_marketing.md#email-marketing-create-email).

## Send or schedule

Once all the components of the email campaign are complete, either:

- click the purple Send button at the top-left of the form to immediately send the
  email; or
- click the gray Schedule button, located to the right of the Send button,
  to send the email at a future date and time.

<a id="email-marketing-select-lost-reasons"></a>

## Select appropriate lost reasons

When a lead is marked as lost, Odoo recommends selecting a *Lost Reason* to indicate why the
opportunity did not result in a sale. Doing so keeps the pipeline organized and reporting data
accurate, and generates potential to follow up with the lead in the future.

If an existing *Lost Reason* is not applicable, users with the necessary permissions can create new
ones, which means the lost reasons in a database can vary from organization to organization, and
from pipeline to pipeline.

For more information on *Lost Reasons*, including the creation of them, refer to
[Manage lost opportunities](../../sales/crm/pipeline/lost_opportunities.md).

By default, Odoo includes a few common *Lost Reasons*, such as:

- *Quá đắt*
- *We don't have people/skills*
- *Not enough stock*

When determining which reasons to include in a lost leads reactivation email, consider what the
email is advertising, in order pinpoint one or more relevant lost reasons. Then, add a rule stating,
Lost Reason *does not contain* `_____` for every reason in the database, **except** for
the relevant one(s).

## Analyze the results

After sending a lost leads reactivation email, marketing teams can use the smart buttons along the
top of the email to analyze the results, and determine follow-up actions.

Clicking on any of the smart buttons opens a list of records matching that button's specific
criteria.

![The Mailing page of a sent email showing the smart buttons along the top of the page.](applications/marketing/email_marketing/lost_leads_email/smart-buttons.png)

The smart buttons include:

- Sent: total number of emails sent.
- Opened: percentage of recipients that opened the email.
- Replied: percentage of recipients that replied to the email.
- Clicked: click-through rate (%) of recipients that clicked on a link in the email.
- Leads/Opportunities: number of leads (or opportunities) that have been created in the
  *CRM* pipeline, as a result of the email campaign.
- Quotations: number of quotations that have been created in the *Sales* application, as
  a result of the email.
- Invoiced: total revenues generated, as a result of the email campaign, via invoices
  sent to, and paid by, customers. These values are recorded in either the *Invoicing* or
  *Accounting* application, depending on which app is installed in the database.
- Received: percentage of recipients that received the email.
- Bounced: percentage of emails that bounced ().
- Ignored: the number of recipients that received the email, but have not interacted
  with it in a meaningful way (i.e. opened, clicked, etc.).

## Email nurturing

*Email nurturing* (sometimes referred to as *lead nurturing*) is the process of sending a series of
timely and relevant "nudge" emails to connect with a lead, build a deeper relationship, and
ultimately convert the lead into a sale.

The point of nurturing is to keep the email campaign "visible" or at the top of a lead's inbox,
until they are ready to buy.

There are many approaches to effective lead nurturing, but they often involve:

- Sending an initial email (such as, a lost leads reactivation email).
- Sending a follow-up email each week (or according to specific triggers) for the duration of the
  campaign.
- Continuously analyzing results to learn what approaches have resulted in sales.
- Continuously adjusting the approach to remain "visible" at the top of the lead's inbox, and
  hopefully, get a meaningful response from the lead.

As a campaign progresses, a marketing team may send different follow-up emails depending on how a
lead responded the previous week.

#### SEE ALSO
- [Email Marketing](../email_marketing.md)
- [Manage unsubscriptions (blacklist)](unsubscriptions.md)
- [Tự động hóa marketing](../marketing_automation.md)
