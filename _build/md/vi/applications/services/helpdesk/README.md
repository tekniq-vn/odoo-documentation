# Hỗ trợ

Odoo *Helpdesk* is a ticketing-based customer support application. Multiple teams can be configured
and managed in one dashboard, each with their own pipeline for tickets submitted by customers.
Pipelines are organized in customizable stages that enable teams to track, prioritize, and solve
customer issues quickly and efficiently.

## Create a Helpdesk team

To view or modify *Helpdesk* teams, go to Helpdesk app ‣ Configuration ‣
Helpdesk Teams. To create a new team, click the New button in the top-left of the
dashboard.

![View of the Helpdesk teams page in Odoo Helpdesk.](../../.gitbook/assets/helpdesk-teams-list.png)

On the blank Helpdesk team form, enter a Name for the new team. Then, enter a
description of the team in the field below the team name, if desired. To change the company this
team is assigned to, select it from the Company drop-down menu.

#### IMPORTANT
The team description is published on the public facing [website form](helpdesk/overview/receiving_tickets.md), where customers and portal users submit tickets. The
description included in this field should **not** include any information that is for internal
use only.

![View of a Helpdesk team's website form displaying the team description.](../../.gitbook/assets/team-description-webform.png)

### Visibility & Assignment

The *Visibility* settings alter which internal users and portal users have access to this team and
its tickets. The *Assignment* settings alter how users are assigned to handle each ticket.

#### Determine team visibility

Under the Visibility section, select one of the following options to determine who can
view this team and its tickets:

- Invited internal users (private): internal users can access the team and the tickets
  they are following. This access can be modified on each ticket individually by adding or removing
  the user as a follower. Internal users are considered *invited* once they are added as followers
  to an individual ticket, or [to the team itself](#helpdesk-follow).
- All internal users (company): all internal users can access the team and all of its
  tickets.
- Invited portal users and all internal users (public): all internal users can access
  the team and all of its tickets. Portal users can only access the tickets they are following.

#### WARNING
A team's visibility can be altered after the initial configuration. However, if the team changes
from public access to either private or company-only access, portal users are removed as
followers from both the team, and from individual tickets.

<a id="helpdesk-follow"></a>

#### Follow all team's tickets

If a user should be notified about any updates regarding tickets for this team, select their name
from the Followers drop-down menu, located in the Follow All Team's Tickets
field. Multiple users can be selected to follow a single team.

#### IMPORTANT
External contacts can be selected in the Followers field. If the team's visibility is
set to Invited internal users (private), followers are notified about updates to the
team's tickets, but are **not** able to view them in the portal.

#### Automatically assign new tickets

When tickets are received, they need to be assigned to a member of the team. This is done either
manually on each ticket individually, or through Automatic Assignment. Check the
Automatic Assignment checkbox to enable this feature for the team.

![View of a Helpdesk team settings page emphasizing the automatic assignment features in Odoo
Helpdesk.](../../.gitbook/assets/helpdesk-visibility-assignment.png)

As soon as Automatic Assignment has been enabled, additional fields appear.

Select one of the following assignment methods, based on how the workload should be allocated across
the team:

- Each user is assigned an equal number of tickets: tickets are assigned to team members
  based on total ticket count, regardless of the number of open or closed tickets they are
  currently assigned.
- Each user has an equal number of open tickets: tickets are assigned to team members
  based on how many open tickets they are currently assigned.

#### NOTE
When Each user is assigned an equal number of tickets is selected, the overall number
of tickets assigned to team members is the same, but it does **not** consider the current
workload.

When Each user has an equal number of open tickets is selected, it ensures a balanced
workload among team members, as it takes the current number of active tickets into account.

Finally, add the Team Members who are to be assigned tickets for this team. Leave the
field empty to include all employees who have the proper assignments and access rights configured in
their user account settings.

#### IMPORTANT
If an employee has time off scheduled in the *Time Off* application, they are **not** assigned
tickets during that time. If no employees are available, the system looks ahead until there is a
match.

#### SEE ALSO
- [Manage users](../general/users.md#users-add-individual)
- [Access rights](../general/users/access_rights.md)

## Create or modify stages

*Stages* are used to organize the *Helpdesk* pipeline and track the progress of tickets. Stages are
customizable, and can be renamed to fit the needs of each team.

#### IMPORTANT
[Developer mode](../general/developer_mode.md#developer-mode) **must** be activated to access the stages menu. To
activate developer mode, go to Settings app ‣ General Settings ‣ Developer
Tools, and click Activate the developer mode.

To view or modify *Helpdesk* stages, go to Helpdesk app ‣ Configuration ‣
Stages.

The default list view on the Stages page displays the stages currently available in
*Helpdesk*. They are listed in the order they appear in the pipeline.

To change the order of the stages, click the <i class="oi oi-draggable"></i> (drag) icon, to the
left of the stage name, and drag it to the desired place on the list.

![View of the stage list page emphasizing the buttons used to change the order the stages
appear in the list.](../../.gitbook/assets/stages-list-buttons.png)

To create a new stage, click the New button at the top-left of the stage list. Doing so
reveals a blank stage form.

Choose a Name for the new stage, and add a description, if desired. Then, proceed to
fill out the remaining fields following the steps below.

![View of a stage's settings page in Odoo Helpdesk.](../../.gitbook/assets/new-stage-details.png)

### Add email and SMS templates to stages

When an Email Template is added to a stage, an email is automatically sent to the
customer when a ticket reaches that specific stage in the pipeline. Likewise, adding an
SMS Template triggers an SMS text message to send to the customer.

#### IMPORTANT
SMS Text Messaging is an [In-App Purchase (IAP)](../essentials/in_app_purchase.md)
service that requires prepaid credits to work. Refer to [SMS Pricing FAQ](https://iap-services.odoo.com/iap/sms/pricing) for additional information.

To select an existing email template, select it from the Email Template field. Click on
the <i class="oi oi-arrow-right"></i> (right arrow) icon to the right of the field to edit the
chosen template.

To create a new template, click the field, and enter a title for the new template. Then, select
Create and edit from the drop-down menu that appears, and complete the form details.

Follow the same steps to select, edit, or create an SMS Template.

![View of an SMS template setup page in Odoo Helpdesk](../../.gitbook/assets/sms-template1.png)

#### SEE ALSO
[Mẫu Email](../general/companies/email_template.md)

### Assign stages to a team

Make a selection in the Helpdesk Teams field on the Stages form. More than
one team may be selected, since the same stage can be assigned to multiple teams.

### Fold a stage

By default, stages are unfolded in the Kanban view of either tickets dashboard: My
Tickets (Helpdesk app ‣ Tickets ‣ My Tickets) or All Tickets
(Helpdesk app ‣ Tickets ‣ All Tickets).

Tickets in an unfolded stage are visible in the pipeline under the stage name, and are considered
*open*.

Stages can be configured to be folded in the Kanban view of a tickets page (My Tickets
or All Tickets).

The name of the folded stages are still visible, though the tickets in the stage are no longer
immediately visible.

To fold a stage, check the Folded in Kanban box on the Stages form.

#### WARNING
Tickets that reach a *folded* stage are considered *closed*. Closing a ticket before the work is
completed can result in reporting and communication issues. This setting should **only** be
enabled for stages that are considered *closing* stages.

Stages can be temporarily folded in the Kanban view of the tickets pipeline, as well.

View a specific team's pipeline by navigating to Helpdesk app, and clicking the
team's Kanban card.

Select a stage to fold temporarily, then click the <i class="fa fa-gear"></i> (gear) icon, and
select Fold from the drop-down menu.

![Kanban view of a Helpdesk stage, with the temporary fold option emphasized.](../../.gitbook/assets/fold-stage-kanban.png)

#### IMPORTANT
Manually folding a stage from the Kanban view is temporary and does **not** close the tickets in
the stage.

## Gộp phiếu hỗ trợ

If duplicate tickets are found in *Helpdesk*, they can be combined into a single ticket using the
*merge* feature.

#### IMPORTANT
The *merge* feature is **only** accessible if the [Data Cleaning](../productivity/data_cleaning.md) application is installed on the database.

Để gộp hai hoặc nhiều phiếu hỗ trợ, đi đến Ứng dụng Hỗ trợ ‣ Phiếu hỗ trợ ‣ Tất cả phiếu hỗ trợ. Xác định các phiếu hỗ trợ cần gộp và đánh dấu vào hộp kiểm ở góc bên trái của mỗi phiếu hỗ trợ để chọn chúng. Sau đó, nhấp vào biểu tượng <i class="fa fa-cog"></i> Tác vụ và chọn Gộp từ menu thả xuống. Thao tác này sẽ mở một trang mới, trong đó các phiếu hỗ trợ đã chọn được liệt kê với xếp hạng Tính tương đồng của chúng. Từ đây, nhấp vào [Gộp](../productivity/data_cleaning.md#data-cleaning-merge-records) để gộp các phiếu hỗ trợ hoặc HUỶ BỎ.

#### SEE ALSO
- [Odoo Tutorials: Helpdesk](https://www.odoo.com/slides/helpdesk-51)

* [Tổng quan](helpdesk/overview.md)
  * [Receiving tickets](helpdesk/overview/receiving_tickets.md)
  * [Trung tâm hỗ trợ](helpdesk/overview/help_center.md)
  * [Service level agreements (SLA)](helpdesk/overview/sla.md)
  * [Báo cáo](helpdesk/overview/reports.md)
  * [Đánh giá của khách hàng](helpdesk/overview/ratings.md)
* [Nâng cao](helpdesk/advanced.md)
  * [Dịch vụ hậu mãi](helpdesk/advanced/after_sales.md)
  * [Close tickets](helpdesk/advanced/close_tickets.md)
  * [Track and bill time](helpdesk/advanced/track_and_bill.md)
