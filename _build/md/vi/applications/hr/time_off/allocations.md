# Phân bổ

Once [time off types](../time_off.md#time-off-time-off-types) and [accrual plans](../time_off.md#time-off-accrual-plans) have been configured, the next step is to *allocate*, or give, time off to
employees.

The *Allocations* page of the **Time Off** app is **only** visible to users who have either *Time
Off Officer* or *Administrator* access rights for the **Time Off** application. For more information
on access rights, refer to the [access rights](../../general/users/access_rights.md)
documentation.

## Allocate time off

To create a new allocation, navigate to Time Off app ‣ Management ‣
Allocations.

This presents a list of all current allocations, including their respective statuses.

Click New to allocate time off, and a blank allocation form appears.

After entering a name for the allocation on the first blank field of the form, enter the following
information:

- Time Off Type: Using the drop-down menu, select the type of time off that is being
  allocated to the employees.
- Allocation Type: Select either Regular Allocation or Accrual
  Allocation. If the allocation is **not** based on an [accrual plan](../time_off.md#time-off-accrual-plans), select Regular Allocation.
- Accrual Plan: If Accrual Allocation is selected for the
  Allocation Type, the Accrual Plan field appears. Using the drop-down menu,
  select the accrual plan with which the allocation is associated. An accrual plan **must** be
  selected for an Accrual Allocation.
- Validity Period/Start Date: If Regular Allocation is selected for the
  Allocation Type, this field is labeled Validity Period. If
  Accrual Allocation is selected for the Allocation Type, this field is
  labeled Start Date.

  The current date populates the first date field, by default. To select another date, click on the
  pre-populated date to reveal a popover calendar window. Navigate to the desired start date for the
  allocation, and click on the date to select it.

  If the allocation expires, select the expiration date in the next date field. If the time off does
  *not* expire, leave the second date field blank. No Limit appears in the field if no
  date is selected.

  If Accrual Allocation is selected for the Allocation Type, this second
  field is labeled Run until.

  #### IMPORTANT
  Nếu Ngày bắt đầu nhập vào nằm giữa một khoảng thời gian, ví dụ giữa tháng, Odoo sẽ áp dụng phân bổ vào đầu hoặc cuối giai đoạn đó, tùy thuộc vào *Thời gian ghi nhận tích lũy* được nhập trong [kế hoạch tích lũy](../time_off.md#time-off-accrual-plans) (*Vào đầu giai đoạn tích lũy* hoặc *Vào cuối giai đoạn tích lũy*) thay vì ngày cụ thể đã nhập.

  For example, an allocation is created, and references an accrual plan that grants time *At the
  start of the accrual period*, monthly, on the first of the month.

  On the allocation form, the Allocation Type is set to Accrual
  Allocation, and the Start Date entered is `06/16/24`.

  Odoo's **Time Off** app retroactively applies the allocation to the beginning of the time
  period entered in the Start Date.

  Therefore, this allocation accrues time from `06/01/24`, rather than `06/16/24`.

  Additionally, if on the accrual form, the allocation references an accrual plan that grants
  time  *\`At the end of the accrual period*, the allocation accrues time from `7/01/24` rather
  than `6/18/24`.
- Allocation: Enter the amount of time that is being allocated to the employees. This
  field displays the time in either Hours or Days, depending on how the
  selected [Time Off Type](../time_off.md#time-off-time-off-types) is configured.
- Mode: Using the drop-down menu, select how the allocation is assigned. This selection
  determines who receives the time off allocation. The options are By Employee,
  By Company, By Department, or By Employee Tag.

  Depending on what is selected for the Mode, the field beneath Mode is
  labeled either: Employees, Company, Department, or
  Employee Tag.

  Using the drop-down menu, indicate the specific employees, company, department, or employee tags
  receiving this time off.

  Multiple selections can be made for either Employees or Employee Tag.

  Only one selection can be made for the Company or Department.
- Add a reason...: If any description or note is necessary to explain the time off
  allocation, enter it in this field at the bottom of the form.

![A new allocation form with all the fields filled out for the annual two week vacation
granted to all employees.](allocations/new-allocation.png)

<a id="time-off-request-allocation"></a>

## Request allocation

If an employee has used all their time off, or will run out of time off, they can request an
allocation for additional time. Allocations can be requested in one of two ways, either from the
[Dashboard](my_time.md#time-off-dashboard) or the [My Allocations](my_time.md#time-off-my-allocations) view.

To create a new allocation request, click either the New Allocation Request button on
the main **Time Off** dashboard, or the New button in the My Allocations
list view. Both buttons open a new allocation request form.

#### NOTE
Both options open a new allocation request form, but when requested from the
Dashboard, the form appears in a pop-up window, and the *Validity Period* field does
**not** appear. When requested from the My Allocations list view, the screen
navigates to a new allocation request page, instead of presenting a pop-up window.

Enter the following information on the new allocation request form:

- Time Off Type: Select the type of time off being requested for the allocation from the
  drop-down menu. After a selection is made, the title updates with the time off type.
- Validity Period: By default, the current date populates this field, and it is **not**
  able to be modified. This field **only** appears when requesting an allocatoin from the
  My Allocations view (Time Off ‣ My Time ‣ My Allocations).
- Allocation: Enter the amount of time being requested in this field. The format is
  presented in either Days or Hours, depending on how the Time
  Off Type is configured. Once this field is populated, the name of the allocation request is
  updated to include the amount of time being requested.
- Add a reason...: Enter a description for the allocation request in this field. This
  should include any details that approvers may need to approve the request.

If the request was created from the Dashboard, click the Save & Close button
on the New Allocation pop-up window to save the information and submit the request.

If the form was completed from the My Allocations list view, the information is
automatically saved as it is entered. However, the form can be saved manually at any time by
clicking the <i class="fa fa-cloud-upload"></i> (cloud upload) icon.

![An allocation request form filled out for an employee requesting an additional week of
sick time.](allocations/allocation-request.png)
