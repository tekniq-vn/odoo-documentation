# Project dashboard

Trang chủ dự án cho phép bạn có được cái nhìn tổng quan toàn diện về trạng thái của dự án. Nó hiển thị các thông tin như tổng số nhiệm vụ, bảng chấm công và giờ theo kế hoạch liên quan đến dự án, cũng như thông tin chi tiết về các mốc dự án, chi phí và doanh thu của dự án. Trong trang chủ dự án, bạn có thể tạo Cập nhật dự án, cho phép bạn nhanh chóng lưu lại trạng thái của dự án tại một thời điểm nhất định. Do đó, đây là một công cụ quan trọng để quản lý dự án hiệu quả và đảm bảo dự án của bạn đi đúng hướng.

## Using the project dashboard

To access the project dashboard, open the **Project** app and hover over the desired project’s
card. Then, click the <i class="fa fa-vertical-ellipsis"></i> (vertical ellipsis) icon and
select Dashboard.

The left side of the dashboard displays a list of existing [project updates](#project-project-dashboard-updates),
and the right side provides [detailed information about records linked to the project](#project-project-dashboard-smart-buttons), as well as [milestones](#project-project-dashboard-milestones),
[profitability](#project-project-dashboard-profitability), and [budgets](#project-project-dashboard-budgets).

#### NOTE
The information displayed on the project dashboard varies depending on the applications installed
on your database. For example, you will not see information about **Timesheets**, **Planning**,
or **Purchase Orders** if the corresponding applications are not installed.

<a id="project-project-dashboard-smart-buttons"></a>

### Totals smart buttons

The following smart buttons are displayed on the top left of the project dashboard:

> - Tasks: the number of completed (i.e., Done or Canceled
>   [tasks](applications/services/project/tasks/task_stages_statuses.md#project-tasks-task-stages-statuses-statuses)) and all tasks, in format
>   completed/all, as well as the entire project's completion percentage estimation.
> - Timesheets: the number of hours or days (depending on the **Timesheets** app
>   configuration) linked to the project. This includes all [timesheets](applications/services/timesheets.md),
>   whether or not they have been validated.
> - Planned: the number of hours that have been planned for shifts in the **Planning**
>   app. This includes all [planned shifts](applications/services/planning.md), including past shifts and shifts that
>   have not yet been published.
> - Documents: number of [documents](applications/productivity/documents.md) in the
>   project’s workspace.
> - Burndown Chart: click the smart button to access a [report](applications/essentials/reporting.md)
>   on the status of the project’s tasks over time.
> - Timesheets and Planning: click the smart button to access a [report](applications/essentials/reporting.md)
>   on the project’s timesheets and shifts.
> - **Additional fields**, such as Sales Orders, Sales Order Items,
>   Purchase Orders, and more, represent the number of records linked to the project.

<a id="project-project-dashboard-milestones"></a>

### Mốc thời gian

This section is only visible if [milestones](applications/sales/sales/invoicing/milestone.md)
have been created for this project. Click Add Milestone to create a new milestone.
Click a milestone in the checklist to edit it, enable its checkbox to mark it as completed, or
click the <i class="fa fa-trash"></i> (trash) icon to remove it.

<a id="project-project-dashboard-profitability"></a>

### Lợi nhuận

This section only applies to billable projects and provides a breakdown of project costs and
revenues.

<a id="project-project-dashboard-budgets"></a>

### Ngân sách

If a budget has been set for the project, its status and related details are displayed in this
section. Click Add Budget to create a new budget for the project.

#### NOTE
[Analytic accounting](applications/finance/accounting/reporting/analytic_accounting.md) must
be enabled in your database’s **Accounting** application in order for this section to be
displayed.

<a id="project-project-dashboard-updates"></a>

## Project updates

Project updates allow you to take a snapshot of the project’s overall status at a given point in
time, for example, during a periodic (weekly, bi-weekly, or monthly) review. This allows you to
compare specific data points, note any aspects of the project that need improvement, and estimate
if the project is on or off track.

To create a new project update, go to the project dashboard, click New, and fill in the
following fields:

> - Status: Choose between On Track, At Risk, Off
>   Track, On Hold, and Done. Once the status is set, a color-coded dot is
>   displayed on the project’s Kanban card, allowing the project manager to easily identify which
>   projects need attention.
> - Progress: Manually input the completion percentage based on the project's progress.
> - Date and Author: These fields are automatically filled in with
>   appropriate information based on the user who created the update and the current date.
> - Description: Use this rich-text field to gather notes. Depending on the project
>   configuration (e.g., if the project is billable), this field may be pre-filled with current
>   information on aspects such as profitability, budget, milestones, etc.
