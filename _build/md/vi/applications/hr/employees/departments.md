# Phòng ban

All employees in the *Employees* app fall under specific departments within a company.

## Create new departments

To make a new department, navigate to Employees app ‣ Departments, then click
New in the top-left to reveal a blank department form. Fill out the following
information on the department form:

![The department for with all fields filled out.](applications/hr/employees/departments/department-form.png)
- Department Name: enter a name for the department.
- Manager: using the drop-down menu, select the department manager.
- Parent Department: if the new department is housed within another department (has a
  parent department), select the parent department using the drop-down menu.
- Custom Appraisal Templates: if employees in this department require a specific
  appraisal form that is different from the default appraisal form, tick the checkbox. If this
  option is activated, an Appraisal Templates tab appears below the form. This field
  **only** appears if the *Appraisals* app is installed.
- Company: using the drop-down menu, select the company the department is part of.
- Appraisal Survey: using the drop-down menu, select the default survey to use for the
  department when requesting feedback from employees. This field **only** appears if the
  *Appraisals* app is installed, **and** the *360 Feedback* option is enabled in the settings.
- Color: select a color for the department. Click the default white color box to display
  all the color options. Click on a color to select it.
- Appraisal Templates tab: this tab **only** appears if the Custom Appraisal
  Templates options is activated on the form. Make any desired edits to the appraisal form. The
  appraisal form is used for appraisals for all employees within this department.

After the form is completed, click the <i class="fa fa-cloud-upload"></i> (cloud upload) icon to
manually save the changes. When saved, a Department Organization chart appears in the
top-right of the department card.

#### NOTE
The form auto-saves while data is entered, however the Department Organization chart
does **not** appear until the form is manually saved. If the form is not saved, the
Department Organization chart is visible upon opening the department card from the
Departments dashboard.

#### SEE ALSO
Refer to the [Đánh giá](../appraisals.md) documentation for more information.

## Departments dashboard

To view the currently configured departments, navigate to Employees app ‣
Departments. All departments appear in a Kanban view, by default, and are listed in alphabetical
order.

![The departments dashboard view with all the department cards in a Kanban view.](applications/hr/employees/departments/departments.png)

### Chế độ xem kanban

Each department has its own Kanban card on the main Departments <i class="oi oi-view-kanban"></i>
(Kanban) dashboard view, that can display the following information:

- Department name: the name of the department.
- Company: the company the department is part of.
- Employees: the number of employees within the department.
- Appraisals: the number of appraisals scheduled for employees in the department.
- Time Off Requests: the number of unapproved time off requests for employees in the
  department [awaiting approval](../time_off/management.md#time-off-manage-time-off) . This **only** appears if there
  are requests to approve.
- Allocation Requests: the number of unapproved allocation requests for employees in the
  department [awaiting approval](../time_off/management.md#time-off-manage-allocations). This **only** appears if there
  are requests to approve.
- New Applicants: the number of [new applicants](../recruitment/recruitment-flow.md#recruitment-new) for a position
  in this department. This **only** appears if there are new applicants.
- Expense Reports: the number of employees in the department with [open expense
  reports to approve](../../finance/expenses/approve_expenses.md). This **only** appears if there are
  any expense reports waiting for approval.
- Absence: the number of absences for the current day.
- Color bar: the selected color for the department appears as a vertical bar on the left side of the
  department card.

#### NOTE
Click on an alert in a department card, such as Time Off Requests, to reveal a list
view of the requests to approve. This list includes **all** open requests to approve, not just
from the specific department.

The default view for the Departments dashboard is a Kanban view. It is possible to view
the departments in two other forms: a list view and a hierarchy view.

### Xem danh sách

To view the departments in a list view, click the <i class="fa fa-align-justify"></i> (list) icon
in the top-right corner. The departments appear in a list view, which displays the
Department Name, Company, Manager, Employees,
Parent Department, and Color for each department.

The departments are sorted alphabetically by Department Name, by default.

![The departments presented in a list view.](applications/hr/employees/departments/list.png)

### Hierarchy view

To view the departments in a hierarchy view, click the <i class="fa fa-share-alt fa-rotate-90"></i>
(hierarchy) icon in the top-right corner. The departments appear in an organizational
chart format, with the highest-level department at the top (typically Management), and
all other departments beneath it. All child departments of the first-level child departments are
folded.

Each department card displays the Department Name, the Manager (and their
profile image), the Number of Employees in the department, and the ability to expand the
department (Unfold) if there are child departments beneath it.

Click the Unfold button on a department card to expand it. Once expanded, the
Unfold button changes to a Fold button. To collapse the department, click
the Fold button. Only **one** department *per row* can be unfolded at a time.

Click anywhere on a department card to open the department form. Click the (#) Employees
smart button to view a list of all the employees in that department, including all employees in the
child departments beneath it, organized by individual department.
