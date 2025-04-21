# Quality checks

Quality checks are manual inspections conducted by employees, and are used to ensure the quality of
products. In Odoo, a quality check can be conducted for a single product, or multiple products
within the same inventory operation or manufacturing order.

Khi sử dụng Điểm kiểm soát chất lượng (QCP), bạn có thể tạo các kiểm tra chất lượng tự động theo các khoảng thời gian định kỳ. Khi các kiểm tra chất lượng được tạo bởi một , chúng sẽ xuất hiện trên lệnh sản xuất hoặc phiếu kho, nơi nhân viên xử lý đơn hàng sẽ được yêu cầu hoàn thành chúng. Để tìm hiểu chi tiết về cách tạo và cấu hình một , hãy tham khảo tài liệu về [điểm kiểm soát chất lượng](quality_control_points.md#quality-quality-management-quality-control-points).

While quality checks are most commonly created automatically by a , it is also possible to
manually create a single quality check. Creating a check manually is useful when an employee wants
to schedule a quality check that will only occur once, or register a quality check that they conduct
unprompted.

## Manual quality check

To manually create a single quality check, navigate to Quality ‣ Quality Control
‣ Quality Checks, and click New. On the quality check form, begin by selecting an
option from the Control per drop-down menu:

- Operation requests a check for an entire operation (ex. delivery order) and all
  products within it.
- Product requests a check for every unit of a product that is part of an operation (ex.
  every unit of a product within a delivery order).
- Số lượng yêu cầu kiểm tra cho mỗi lượng sản phẩm thuộc một hoạt động (VD: một lần kiểm tra cho năm đơn vị sản phẩm trong lệnh giao hàng). Việc chọn Số lượng cũng làm xuất hiện trường thả xuống Số lô/sê-ri, từ đó có thể chọn lô hoặc số sê-ri cụ thể cần kiểm tra chất lượng.

Next, select an inventory operation from the Picking drop-down menu or a manufacturing
order from the Production Order drop-down menu. This is necessary because Odoo needs to
know for which operation the quality check is being conducted.

If the quality check should be assigned to a specific , select it from the Control
Point drop-down menu. This is useful if the quality check is being created manually, but should
still be recognized as belonging to a specific .

Select a quality check type from the Type drop-down field:

- Instructions provides specific instructions for how to conduct the quality check.
- Take a Picture requires a picture to be attached to the check before the check can be
  completed.
- Pass - Fail is used when the product being checked must meet a certain criteria to
  pass the check.
- Selecting Measure causes a Measure input field to appear, in which a
  measurement must be entered before the check can be completed.
- Selecting Worksheet causes a Quality Template drop-down field to appear.
  Use it to select a quality worksheet that must be filled out to complete the check.

In the Team field, select the quality team that is responsible for the quality check. In
the Company field, select the company that owns the product being inspected.

On the Notes tab at the bottom of the form, enter any relevant instructions in the
Instructions text entry box (ex. 'Attach a picture of the product'). In the
Notes text entry box, enter any relevant information about the quality check (who
created it, why it was created, etc.).

Finally, if the check is being processed immediately, click the Pass button at the top
left of the screen if the check passes, or the Fail button if the check fails.

![A quality check form filled out for a Pass - Fail check.](applications/inventory_and_mrp/quality/quality_management/quality_checks/quality-check-form.png)

## Process quality check

Quality checks can be processed directly on the quality check's page, or from a manufacturing or
inventory order for which a check is required. Alternatively, if a quality check is created for a
specific work order operation, the check is processed in the *Shop Floor* module.

#### NOTE
Không thể tạo thủ công một kiểm tra chất lượng đơn lẻ được gán cho một công đoạn sản xuất cụ thể. Các kiểm tra chất lượng cho công đoạn chỉ có thể được tạo tự động thông qua . Tham khảo tài liệu về [Điểm kiểm soát chất lượng](quality_control_points.md#quality-quality-management-quality-control-points) để biết cách cấu hình  nhằm tạo kiểm tra chất lượng cho từng công đoạn cụ thể.

### Quality check page

To process a quality check from the check's page, begin by navigating to Quality ‣
Quality Control ‣ Quality Checks, then select the check to process. Follow the instructions for
how to complete the check, listed in the Instructions field of the Notes tab
at the bottom of the page.

If the quality check passes, click the Pass button at the top of the page. If the check
fails, click the Fail button, instead.

### Quality check on order

Để thực hiện kiểm tra chất lượng trên một đơn hàng, hãy chọn một lệnh sản xuất hoặc phiếu kho (nhập kho, giao hàng, trả hàng,...) cần được kiểm tra. Các lệnh sản xuất có thể được chọn bằng cách đi đến Sản xuất ‣ Hoạt động ‣ Lệnh sản xuất và nhấp vào một lệnh. Các phiếu kho có thể được chọn bằng cách đi đến Tồn kho, nhấp vào nút # Cần xử lý trên thẻ hoạt động và chọn một phiếu.

On the selected inventory or manufacturing order, a purple Quality Checks button appears
at the top of the order. Click the button to open the Quality Check pop-up window, which
shows all of the quality checks required for that order.

Follow the instructions that appear on the Quality Check pop-up window. If a Pass - Fail
check is being processed, complete the check by clicking Pass or Fail at the
bottom of the pop-up window. For all other quality check types, a Validate button
appears instead. Click it to complete the check.

![The "Quality Check" pop-up window on a manufacturing order.](applications/inventory_and_mrp/quality/quality_management/quality_checks/quality-check-pop-up.png)

### Quality check on work order

To process a quality check for a work order, begin by navigating to Manufacturing
‣ Operations ‣ Manufacturing Orders. Select an  that includes a work order for which a
quality check is required.

On the , select the Work Orders tab, and then click the Open Work Order
(external link icon) button on the line of the work order to be processed. On the resulting
Work Orders pop-up window, click the Open Shop Floor button to open the
*Shop Floor* module.

#### SEE ALSO
For a full guide to the Shop Floor module, see the [Shop Floor overview](../../manufacturing/shop_floor/shop_floor_overview.md) documentation.

When accessed from a specific work order, the *Shop Floor* module opens to the page for the work
center where the order is configured to be processed, and isolates the work order's card so that no
other cards are shown.

Process the work order's steps until the quality check step is reached. Click on the step to open a
pop-up window that details how the check should be completed. After following the instructions,
click Validate to complete the check. Alternatively, if a *Pass - Fail* check is being
processed, click either the Pass or Fail button.

It is also possible to complete a quality check by clicking the checkbox on the right side of the
step. Doing so automatically marks the check as *Passed*.

#### NOTE
The specific steps for processing a quality check depend upon the type of check being conducted.
For information about processing each type of quality check, see the associated documentation:

- [Instructions quality check](../quality_check_types/instructions_check.md)
- [Pass - Fail quality check](../quality_check_types/pass_fail_check.md)
- [Measure quality check](../quality_check_types/measure_check.md)
- [Take a Picture quality check](../quality_check_types/picture_check.md)
