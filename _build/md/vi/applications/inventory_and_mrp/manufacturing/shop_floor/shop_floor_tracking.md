# Shop Floor time tracking

By signing in to the Odoo *Shop Floor* module as *operators*, employees are able to track the amount
of time they spend working on each work order.

Odoo tracks the time it takes to complete each work order, as well as the time each operator spends
on each work order.

## Operator sign in

To sign in to the *Shop Floor* module as an operator, sign in to the Odoo database, and open the
Shop Floor module. The employee profile that is signed in to the database is
automatically signed in as an operator.

All active operators are listed in the operator panel on the left side of the module. The panel can
be opened or collapsed by clicking the show/hide panel (white square with black column on
left side) button, located in the top-left corner of the module.

![The operator panel in the Shop Floor module, with the show/hide panel button above it.](applications/inventory_and_mrp/manufacturing/shop_floor/shop_floor_tracking/operator-panel.png)

To sign in to *Shop Floor* as a different employee, click the + Add Operator button at
the bottom of the panel. Doing so opens the Select Employee pop-up window, which lists
every employee that is able to sign in to the module.

Click on a specific employee to sign in using their profile. If no PIN code is required to sign in
as that employee, the profile will be signed in automatically.

If a PIN code is required, a Password? pop-up window appears, showing a number pad, from
which the code can be entered. Enter the code using the number pad, and click Confirm to
sign in to the *Shop Floor* module.

![The "Password?" pop-up window, which is used to enter an operator PIN code.](applications/inventory_and_mrp/manufacturing/shop_floor/shop_floor_tracking/pin-code.png)

#### NOTE
A PIN code can be set for each employee, which must be entered each time they sign in to the
*Shop Floor* module, check in or out in the *Kiosk Mode* of the *Attendances* application, or
sign in as a cashier in the *Point of Sale* application.

To set an employee PIN, navigate to the Employees app, and select a specific
employee. At the bottom of the employee's form, click on the HR Settings tab, and
enter a numerical code in the PIN Code field.

Once an employee is signed in to the module, their name appears in the operator panel, along with
every other employee that has signed in. While the panel can list multiple employees, only one
employee can be active at any given time, on a single instance of the *Shop Floor* module.

Click on an employee's name to make their profile active. The active employee appears highlighted
in blue, while employees that are signed in, but not active, have their names faded out.

To sign out a specific employee from the module, click the X (remove) button next to
their name, in the operator panel.

## Track work order duration

To track time spent working on a work order, begin by selecting the employee working on it from the
operator panel.

Tiếp theo, đi đến trang của khu vực sản xuất nơi công đoạn được lên lịch xử lý. Việc này có thể được thực hiện bằng cách chọn khu vực sản xuất từ thanh điều hướng phía trên trong phân hệ *Xưởng*, hoặc bằng cách nhấp vào tên của khu vực sản xuất trên thẻ của lệnh sản xuất (MO) chứa công đoạn này.

Trên trang của khu vực sản xuất, tìm thẻ cho công đoạn. Khi công việc bắt đầu, hãy nhấp vào header của thẻ công đoạn để bắt đầu tính thời gian hoàn thành. Thời lượng này được hiển thị bằng một bộ đếm giờ trên header của thẻ công đoạn, theo dõi tổng thời gian làm việc trên công đoạn đó theo tất cả nhân viên.

![A work order card with an active timer.](applications/inventory_and_mrp/manufacturing/shop_floor/shop_floor_tracking/work-order-timer.png)

Ngoài ra, số tham chiếu của công đoạn sẽ hiển thị trong bảng điều khiển của nhân viên vận hành, ngay bên dưới tên của nhân viên đang thực hiện công đoạn đó, cùng với một đồng hồ tính giờ thứ hai — dùng để theo dõi thời gian mà nhân viên đã dành riêng cho công đoạn này. Đồng hồ tính giờ này chỉ phản ánh thời gian làm việc trong phiên hiện tại, ngay cả khi nhân viên đó đã từng làm việc trên công đoạn này trước đó.

Employees are able to work on multiple work orders simultaneously, and track their time for each.
The reference number for each work order being worked on appears below the employee's name, along
with a timer.

![An employee card in the operator panel, showing two work order timers.](applications/inventory_and_mrp/manufacturing/shop_floor/shop_floor_tracking/employee-timer.png)

To pause the timer on the work order card, and remove the work order from below the employee's name
on the operator panel, click the header a second time.

Once the work order is completed, click the Mark as Done button at the bottom of the
work order card, which causes the card to fade away. If the timer is still active, it stops once the
card disappears completely.

## View work order duration

To view the duration of a work order, navigate to Manufacturing app ‣ Operations
‣ Manufacturing Orders, and select an .

To view and select  that have been completed and marked as *Done*, remove the To Do
filter from the Search... bar, by clicking on the X (close) button on the
right side of the filter.

On the page for the , click on the Work Orders tab to see a list of all work orders
included in the . The time it took to complete each work order is displayed in the
Real Duration column of the tab.

The *Real Duration* represents the total time spent working on the work order by all workers who
worked on it. It includes time tracked in the *Shop Floor* module, as well as time tracked on the
Work Orders tab of the  itself.
