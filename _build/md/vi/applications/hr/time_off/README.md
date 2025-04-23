# Nghỉ phép

Odoo's **Time Off** application serves as a centralized hub for all time-off-related information.\
This application manages requests, balances, allocations, approvals, and reports.

Users can [request time off](applications/hr/time_off/request_time_off.md), and see an overview of their\
requests and time off balances. Managers can [allocate time off](applications/hr/time_off/allocations.md) to\
individuals, teams, or the whole company, and [approve time off requests](applications/hr/time_off/management.md#time-off-manage-time-off).

Detailed [reports](./#time-off-reporting) can be run to see how much time off (and what kinds of\
time off) are being used, [accrual plans](./#time-off-accrual-plans) can be created, and[public holidays](./#time-off-public-holidays) can be set.

#### NOTE

Be advised, only users with specific access rights can see all aspects of the **Time Off** app.

All users can access the _My Time Off_ and _Overview_ sections of the **Time Off** app. All other\
sections require specific access rights.

To better understand how access rights affect the **Time Off** app, refer to the[Nhân viên mới](applications/hr/employees/new_employee.md) document, specifically the section about configuring the work\
information tab.

## Cấu hình

In order to allocate time off to employees, and for employees to request and use their time off, the\
various time off types must be configured first, then allocated to employees (if allocation is\
required).

### Time off types

To view the currently configured time off types, navigate to Time Off app ‣\
Configuration ‣ Time Off Types. The time off types are presented in a list view.

The **Time Off** app comes with four preconfigured time off types: Paid Time Off,\
Sick Time Off, Unpaid, and Compensatory Days. These can be\
modified to suit business needs, or used as-is.

#### Create time off type

To create a new time off type, navigate to Time Off app ‣ Configuration ‣ Time\
Off Types. From here, click the New button to reveal a blank time off type form.

Enter the name for the particular type of time off in the blank line at the top of the form, such as`Sick Time` or `Vacation`. Then, enter the following information on the form.

#### NOTE

The only **required** fields on the time off type form are the name of the Time Off\
Type, the Take Time Off In, and the Kind of Time Off. In addition, the\
Time Off Requests and Allocation Requests sections **must** be\
configured.

**Time Off Requests section**

* Approval: select what specific kind of approval is required for the time off type. The\
  options are:
  * No Validation: No approvals are required when requesting this type of time off. The\
    time off request is automatically approved.
  * By Time Off Officer: Only the specified [Time Off Officer](./#time-off-time-off-officer), set on this form in the Notified Time Off Officer\
    field, is required to approve the time off request. This option is selected, by default.
  * By Employee's Approver: Only the employee's specified approver for time off, which\
    is set on the _Work Information_ tab on the [employee's form](applications/hr/employees/new_employee.md#employees-work-info-tab), is\
    required to approve the time off request.
  * By Employee's Approver and Time Off Officer: Both the employee's [specified\
    time off approver](applications/hr/employees/new_employee.md#employees-work-info-tab) and the [Time Off Officer](./#time-off-time-off-officer) are required to approve the time off request.

**Allocation Requests section**

* Requires allocation: If the time off must be allocated to employees, select\
  Yes. If the time off can be requested without time off being previously allocated,\
  select No Limit. If No Limit is selected, the following options do not\
  appear on the form.
*   Employee Requests: Select Extra Days Requests Allowed if the employee is\
    able to request more time off than was allocated.

    If employees should **not** be able to make requests for more time off than what was allocated,\
    select the Not Allowed option.

    **IMPORTANT**

    It is important to note that requesting additional time off does **not** guarantee that time\
    off is granted.
* Approval: Select the type of approvals required for the allocation of this particular\
  time off type.
  * Approved by Time Off Officer indicates the [Time Off Officer](./#time-off-time-off-officer) set on this form must approve the allocation.
  * No validation needed indicates that no approvals are required.

**Configuration section**

>

* Notified Time Off Officer: Select the person who is notified and responsible for\
  approving requests and allocations for this specific type of time off.
*   Take Time Off in: Select the format the time off is requested in from the drop-down\
    menu.

    The options are:

    * Day: if time off can only be requested in full day increments (8 hours).
    * Half Day: if time off can only be requested in half day increments (4 hours).
    * Hours: if the time off can be taken in hourly increments.
* Deduct Extra Hours: Enable this option if the time off request should factor in any\
  extra time accrued by the employee.
* Allow To Attach Supporting Document: Enable this option to allow the employee to\
  attach documents to the time off request. This is useful in situations where documentation is\
  required, such as long-term medical leave.
* Kind of Time Off: From the drop-down menu, select the type of time off, either\
  Worked Time or Absence. Worked Time indicates the time off\
  taken counts toward worked time for any type of accrual the employee is working towards, whereas\
  Absence does not count toward any type of accrual.
* Company: If multiple companies are created in the database, and this time off type\
  only applies to one company, select the company from the drop-down menu. If this field is left\
  blank, the time off type applies to all companies in the database. This field **only** appears in\
  a multi-company database.

**Negative Cap section**

Enable the Allow Negative Cap option if employees are able to request more time off than\
they currently have, allowing a negative balance. If enabled, an Amount in Negative\
field appears. In this field, enter the maximum amount of negative time allowed, in days.

![The top half of the time off type form, with all the information filled out for sick time
off.](../../.gitbook/assets/time-off-type-form-top.png)

**Payroll section**

If the time off type should create [Work entries](applications/hr/payroll/work_entries.md) in the **Payroll** app, select\
the Work Entry Type from the drop-down list.

**Timesheets section**

#### NOTE

The Timesheets section only appears if the user is in developer mode. Refer to the[Chế độ lập trình viên (chế độ gỡ lỗi)](applications/general/developer_mode.md#developer-mode) document for details on how to access the developer mode.

When an employee takes time off, and is also using timesheets, Odoo creates entries in the**Timesheets** app for the time off. This section defines how they are entered.

* Project: Select the project the time off type entries appear in.
* Task: Select the task that appears in the timesheet for this time off type. The\
  default options are: Time Off, Meeting, or Training.

**Display Option section**

* Color: Select a color to be used in the **Time Off** app dashboard.
* Cover Image: Select an icon to be used in the **Time Off** app dashboard.

![The lower half of the time off type form, with all the information filled out for sick time
off.](../../.gitbook/assets/time-off-type-form-bottom.png)

### Accrual plans

Some time off is earned through an accrual plan, meaning that for every specified amount of time an\
employee works (hour, day, week, etc), they earn or _accrue_ a specified amount of time off.

#### Create accrual plan

To create a new accrual plan, navigate to Time Off app ‣ Configuration ‣ Accrual\
Plans. Then, click the New button, which reveals a blank accrual plan form.

Nhập thông tin sau đây trên biểu mẫu:

* Name: Enter the accrual plan name.
* Accrued Gain Time: Select when the employee begins to accrue time off, either\
  At the start of the accrual period or At the end of the accrual period.
* Carry-Over Time: Select when the employee received previously earned time. The options\
  are:
  * At the start of the year: Select this if the accrual rolls over on January 1 of the\
    upcoming year.
  * At the allocation date: Select this if the accrual rolls over as soon as time is\
    allocated to the employee.
  * Other: Select this option if neither of the other two options are applicable. When\
    selected, a Carry-Over Date field appears. Select the date using the two drop-down\
    menus, one for the day and one for the month.
* Based on worked time: Enable this option if time off accrual is determined by the\
  employee's worked hours. Days **not** considered as worked time do **not** contribute to the\
  accrual plan in Odoo.
* Chuyển mốc: Trường này **chỉ** hiển thị khi đã cấu hình tối thiểu hai [quy tắc](./#time-off-rules) trong kế hoạch tích lũy. Tùy chọn này xác định thời điểm nhân viên được chuyển lên mốc mới. Nếu nhân viên đủ điều kiện để thay đổi mốc trong giữa kỳ trả lương, bạn cần quyết định xem họ sẽ chuyển mốc Ngay lập tức hay Sau kỳ tích lũy này (tức là sau khi kỳ trả lương hiện tại kết thúc).
* Company: This field **only** appears in a multi-company database. Using the drop-down\
  menu, select the company the accrual plan applies to. If left blank, the accrual plan can be used\
  for all companies.

![An accrual plan form with all the entries filled out.](../../.gitbook/assets/accrual-plan-form.png)

**Quy tắc**

Rules must be created in order for employees to accrue time off from the accrual plan.

To create a new rule, click the New Milestone button in the gray Rules\
section, and a Create Milestone modal form appears.

Fill out the following fields on the form:

*   Employee accrue: Select the parameters for earned time off in this section.

    First, select either Days or Hours for the increment of accrued time using\
    the drop-down menu.

    Next, enter the numerical amount of the selected parameter that is accrued. The numerical format\
    is `X.XXXX`, so that partial days or hours can also be configured.

    Last, select how often the time is accrued using the drop-down menu. The default options are\
    Hourly, Daily, Weekly, Twice a month,\
    Monthly, Twice a year, and Yearly.

    Depending on which option is selected, additional fields may appear. For example, if\
    Twice a month is selected, two additional fields appear, to specify the two days of\
    each month the milestone occurs.
*   Cap accrued time: If there is a maximum amount of days the employee can accrue with\
    this plan, enable this option.

    When enabled, two additional fields appear beneath it. Select the type of time period from the\
    drop-down menu, either Days or Hours.

    Then, enter a numerical value in the field to specify the maximum amount of time that can be\
    accrued.
*   Milestone reached: Enter the number and value of the time period that must pass before\
    the employee starts to accumulate time off. The first value is numerical; enter a number in the\
    first field.

    Then, select the type of time period using the drop-down menu in the second field. The options\
    are: Days, Months, or Years.
* Carry over: select how any unused time off is handled. The options are either:
  * None. Accrued time reset to 0: Any unused time off is gone.
  * All accrued time carried over: All unused time off is rolled over to the next\
    calendar year.
  * Carry over with a maximum: Unused time off is rolled over to the next calendar year,\
    but there is a cap. An Up to field appears if this is selected. Enter the maximum\
    number of Days that can roll over to the following year. Any time off beyond this\
    parameter is lost.

#### IMPORTANT

If the Carry over field is set to None. Accrued time reset to 0, that\
rule _overrides_ the Carry-Over Time set on the accrual plan.

If a company creates an accrual plan, granting employees time off At the start of the\
accrual period (i.e., the beginning of the year), and sets the Carry-Over Time on\
the _accrual plan_ to At the start of the year, it allows unused vacation time to\
rollover to the following year.

Then, the company adds rules to the accrual plan, allocating five days of vacation, annually, on\
the first of the year (one week of vacation allocated on January 1st).

If the Carry over field is set to None. Accrual time reset to 0 on the\
Create Milestone pop-up for, any unused vacation time _does not_ carry over, even\
though on the Accrual Plan form, the Carry-Over Time is set to\
At the start of the year.

The carry over set on the _rule_ takes precedence over the carry over set on the _accrual plan_\
_form_.

Once the form is completed, click Save & Close to save the Create Milestone\
form, and close the modal, or click Save & New to save the form and create another\
milestone. Add as many milestones as desired.

![A milestone form with all the entries filled out.](../../.gitbook/assets/milestone.png)

### Public holidays

To observe public or national holidays, and provide extra days off as holidays to employees,\
configure the observed _public holidays_ in Odoo.

It is important to configure these days in Odoo, so employees are aware of the days they have off,\
and do not request time off on days that are already set as a public holiday (non-working days).

Additionally, all public holidays configured in the **Time Off** app are also reflected in any app\
that uses working schedules, such as **Calendar**, **Planning**, **Manufacturing**, and more.

Due to Odoo's integration with other apps that use working schedules, it is considered best practice\
to ensure _all_ public holidays are configured.

#### Create public holiday

To create a public holiday, navigate to Time Off app ‣ Configuration ‣ Public\
Holidays.

All currently configured public holidays appear in a list view.

Click the New button, and a new line appears at the bottom of the list.

Enter the following information on that new line:

* Name: Enter the name of the holiday.
*   Company: If in a multi-company database, the current company populates this field by\
    default. It is **not** possible to edit this field.

    **NOTE**

    The Company field is hidden, by default. To view this field, click the(additional options) icon in the top-right corner of the\
    list, to the far-right of the column titles, and activate the Company selection\
    from the drop-down menu that appears.
* Ngày bắt đầu: Sử dụng bộ chọn ngày và giờ, chọn ngày và giờ bắt đầu kỳ nghỉ, sau đó nhấp Áp dụng. Theo mặc định, trường này được cấu hình cho ngày hiện tại. Thời gian bắt đầu được đặt theo giờ làm việc của công ty (theo [lịch làm việc](applications/hr/payroll.md#payroll-working-times)). Nếu máy tính của người dùng được đặt ở múi giờ khác, thời gian bắt đầu sẽ được điều chỉnh tương ứng so với múi giờ của công ty.
* Ngày kết thúc: Sử dụng bộ chọn ngày và giờ, chọn ngày và giờ kết thúc kỳ nghỉ, sau đó nhấp Áp dụng. Theo mặc định, trường này được cấu hình cho ngày hiện tại và thời gian được đặt theo giờ kết thúc của công ty (theo [lịch làm việc](applications/hr/payroll.md#payroll-working-times)). Nếu máy tính của người dùng được đặt ở múi giờ khác, thời gian bắt đầu sẽ được điều chỉnh tương ứng so với múi giờ của công ty.
* Working Hours: If the holiday should only apply to employees who have a specific set\
  of working hours, select the working hours from the drop-down menu. If left blank, the holiday\
  applies to all employees.
* Work Entry Type: If using the **Payroll** app, this field defines how the [work\
  entries](applications/hr/payroll.md#payroll-work-entries) for the holiday appear. Select the work entry type from the\
  drop-down menu.

![The list of public holidays in the configuration menu.](../../.gitbook/assets/holidays.png)

### Mandatory days

Some companies have special days where specific departments, or the entire staff, is required to be\
present, and time off is not allowed on those specific days.

These types of days are called _mandatory days_ in Odoo. These can be configured to be company-wide,\
or department specific. When configured, employees in the specified department or company are unable\
to submit time off requests for these mandatory days.

#### Create mandatory days

No mandatory days are configured in Odoo by default. To create a mandatory day, navigate to\
Time Off app ‣ Configuration ‣ Mandatory Days.

Click the New button in the top-left corner, and a blank line appears in the list.

Enter the following information on that new line:

* Name: Enter the name of the mandatory day.
* Company: If in a multi-company database, this field is visible, and the current\
  company populates this field, by default. Using the drop-down menu, select the company the\
  mandatory day is for.
*   Departments: This column is hidden by default. First, click the(additional options) icon in the top-right corner, next to\
    Color, and then tick the checkbox next to Departments to reveal that\
    column.

    Next, select the desired departments from the drop-down menu. Multiple departments can be\
    selected, and there is no limit to the amount of departments that can be added.

    If this field is left blank, the mandatory day applies to the entire company.
* Start Date: Using the calendar picker, select the date the mandatory day starts.
* End Date: Using the calendar picker, select the date the mandatory day ends. If\
  creating a single mandatory day, the end date should be the same as the start date.
* Color: If desired, select a color from the available presented options. If no color is\
  desired, select the `No color` option, represented by a white box with a red line diagonally\
  across it. The selected color appears on the main **Time Off** app dashboard, in both the calendar\
  and in the legend.

![The Mandatory Days section with three configured days.](../../.gitbook/assets/mandatory.png)

## Tổng quan

To view a color-coded schedule of the user's time off, and/or of the team managed by them, navigate\
to Time Off app ‣ Overview. This presents a calendar with the default filter of`My Team`, in a month view.

To change the time period displayed, click on the Month button to reveal a drop-down\
menu. Then, select either Day, Week, or Year to present the\
calendar in that corresponding view.

To navigate forward or backward in time, in the selected increment (Month,\
Week, etc.), click the ← (left arrow) or → (right arrow) to move\
either forward or backward in that specified amount of time.

For example, if Month is selected, the arrows adjust the view by one month.

To return to a view containing the current day, click the Today button at any time.

Team members are listed alphabetically on individual lines, and their requested time off,\
regardless of the status (_validated_ or _to approve_), is visible on the calendar.

Each employee is color-coded. The employee's color is selected at random, and does _not_ correspond\
to the type of time off they requested.

The status of the time off is represented by the color detail of the request, either appearing solid\
(_validated_) or striped (_to approve_).

The number of days or hours requested is written on the request (if there is enough space).

At the bottom of the calendar, in the Total line, a bar graph shows how many people are\
projected to be out on any given day. The number on each individual bar represents the number of\
employees out for those highlighted days.

Click on a time off entry to view the details for the specific time off entry. The total number of\
hours or days are listed, along with the start and end time of the time off. To view the details of\
the time off request in a modal, click the View button.

![Overview of the user's team, with time off requests shown.](../../.gitbook/assets/overview1.png)

## Báo cáo

The reporting feature allows users to view time off for their team, either by employee or type of\
time off. This allows users to see which employees are taking time off, how much time off they are\
taking, and what time off types are being used.

Any report can be added to a spreadsheet, when in either the (Graph) or (Pivot) view, through the _Insert in_\
_Spreadsheet_ button that appears in the top-left of the report.

#### NOTE

If the **Documents** app is installed, an option to add the report to a spreadsheet appears. If\
not, the report can be added to a _Dashboard_.

### By employee

To view a report of employee time off requests, navigate to Time Off app ‣\
Reporting ‣ by Employee.

The default report presents the current year's data in a list view, displaying all the employees in\
alphabetical order. Each employee's line is collapsed by default. To expand a line, click anywhere\
on the line.

The view expands, and has the time off requests organized by time off type. Click anywhere on a time\
off type line to expand it, and view all the individual time off requests that fall under that type.

The information shown in the list includes: the Employee name, Number of\
Days off requested, the Start Date, End Date, Status, and\
Description.

![Report of time off, shown by each employee in a list view.](../../.gitbook/assets/employee-report1.png)

The report can be displayed in other ways, as well. Click the corresponding button option in the\
top-right corner of the page to view the data in that specific way. The various options are a(List), or default view, (Graph),(Pivot) table, or (Calendar) view.

When a selection has been made, additional options appear for that particular selection. For more\
detailed information on the reports and their various options, refer to the [reporting](applications/essentials/reporting.md) documentation.

### By type

To view a list of all time off, organized by time off type, navigate to Time Off app\
‣ Reporting ‣ by Type. This shows all time off requests in a default bar chart.

Hover over a bar to view the Duration (Days) of that specific time off type.

![The various time off types, and how many days requested, in a bar chart. Details are
highlighted in a red box.](../../.gitbook/assets/bar-chart3.png)

Click on a bar to go to a detailed list view of all the time off requests for that time off type.

Each request is listed, with the following information displayed: the Employee,\
Number of Days, Request Type, Start Date, End Date,\
Status, and the Description.

The report can be displayed in other ways, as well. Click the corresponding button option in the\
top-right corner of the page to view the data in that way. The various options are a(Graph) (the default view), (List), or (Pivot) table.

When a selection has been made, additional options appear for that particular selection. For more\
detailed information on the reports, and their various options, refer to the [reporting](applications/essentials/reporting.md) documentation.

#### SEE ALSO

* [Phân bổ](applications/hr/time_off/allocations.md)
* [Request time off](applications/hr/time_off/request_time_off.md)
* [My time](applications/hr/time_off/my_time.md)
* [Quản lý](applications/hr/time_off/management.md)
* [Phân bổ](applications/hr/time_off/allocations.md)
* [Request time off](applications/hr/time_off/request_time_off.md)
* [My time](applications/hr/time_off/my_time.md)
* [Quản lý](applications/hr/time_off/management.md)
