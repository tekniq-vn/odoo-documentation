# Take a Picture quality check

In Odoo *Quality*, a *Take a Picture* check is one of the quality check types that can be selected
when creating a new quality check or quality control point (QCP). *Take a Picture* checks require a
picture to be attached to the check, which can then be reviewed by a quality team.

## Create a Take a Picture quality check

There are two distinct ways that *Take a Picture* quality checks can be created. A single check can
be manually created. Alternatively, a  can be configured that automatically creates checks at a
predetermined interval.

This documentation only details the configuration options that are unique to *Take a Picture*
quality checks and . For a full overview of all the configuration options available when
creating a single check or a , see the documentation on [quality checks](../quality_management/quality_checks.md#quality-quality-management-quality-checks) and [quality control points](../quality_management/quality_control_points.md#quality-quality-management-quality-control-points).

### Quality check

To create a single *Take a Picture* quality check, navigate to Quality ‣ Quality
Control ‣ Quality Checks, and click New. Fill out the new quality check form as
follows:

- In the Type drop-down field, select the Take a Picture quality check type.
- In the Team drop-down field, select the quality team responsible for managing the
  check.
- In the Instructions text field of the Notes tab, enter instructions for
  how the picture should be taken.

![A quality check form configured for a Take a Picture quality check.](applications/inventory_and_mrp/quality/quality_check_types/picture_check/picture-check-form.png)

### Quality control point

To create a  that generates *Take a Picture* quality checks automatically, navigate to
Quality ‣ Quality Control ‣ Control Points, and click New. Fill out
the new  form as follows:

- In the Type drop-down field, select the Take a Picture quality check type.
- If the *Maintenance* app is installed, a Device field appears after selecting the
  *Take a Picture* check type. Use this field to specify a device that should be used to take
  quality check pictures. For information about managing devices in the *Maintenance* app, see the
  documentation on [adding new equipment](../../maintenance/add_new_equipment.md#maintenance-equipment-management-add-new-equipment).
- In the Team drop-down field, select the quality team responsible for managing the
  checks created by the .
- In the Instructions text field, enter instructions for how the picture should be
  taken.

![A Quality Control Point (QCP) form configured to create a Take a Picture quality check.](applications/inventory_and_mrp/quality/quality_check_types/picture_check/picture-qcp-form.png)

## Process a Take a Picture quality check

Once created, there are multiple ways that *Take a Picture* quality checks can be processed. If a
quality check is assigned to a specific inventory, manufacturing, or work order, the check can be
processed on the order itself. Alternatively, a check can be processed from the check's page.

### From the check's page

To process a *Take a Picture* quality check from the check's page, begin by navigating to
Quality ‣ Quality Control ‣ Quality Checks, and then select a quality check.
Follow the Instructions for how to take the picture.

After taking the picture, make sure it is stored on the device being used to process the quality
check (computer, tablet, etc.). Then, click the ✏️ (pencil) button in the
Picture section to open the device's file manager. In the file manager, navigate to the
picture, select it, and click Open to attach it.

![The edit button (pencil) on a Take a Picture quality check.](applications/inventory_and_mrp/quality/quality_check_types/picture_check/picture-edit-button.png)

### On an order

Để thực hiện kiểm tra chất lượng *Chụp ảnh* trên một đơn hàng, hãy chọn một lệnh sản xuất hoặc phiếu kho (nhập kho, giao hàng, trả hàng,...) cần được kiểm tra. Các lệnh sản xuất có thể được chọn bằng cách đi đến Sản xuất ‣ Hoạt động ‣ Lệnh sản xuất và nhấp vào một lệnh. Các phiếu kho có thể được chọn bằng cách đi đến Tồn kho, nhấp vào nút # Cần xử lý trên thẻ hoạt động và chọn một phiếu.

On the selected manufacturing or inventory order, a purple Quality Checks button appears
at the top of the page. Click the button to open the Quality Check pop-up window, which
shows all of the quality checks required for that order.

Follow the instructions detailing how to take the picture, which are shown on the Quality
Check pop-up window. After taking the picture, make sure it is stored on the device being used to
process the quality check (computer, tablet, etc.).

Then, click the Take a Picture button in the Picture section to open the
device's file manager. In the file manager, navigate to the picture, select it, and click
Open to attach it. Finally, click Validate on the Quality Check
pop-up window to complete the quality check.

![A Take a Picture quality check pop-up window on a manufacturing or inventory order.](applications/inventory_and_mrp/quality/quality_check_types/picture_check/picture-check-pop-up.png)

Nếu cần tạo cảnh báo chất lượng, hãy nhấp vào nút Cảnh báo chất lượng xuất hiện ở đầu lệnh sản xuất hoặc phiếu kho sau khi kiểm tra được xác nhận. Việc nhấp vào Cảnh báo chất lượng sẽ mở biểu mẫu cảnh báo chất lượng trên trang mới. Để xem hướng dẫn đầy đủ về cách điền biểu mẫu cảnh báo chất lượng, tham khảo tài liệu về [cảnh báo chất lượng](../quality_management/quality_alerts.md#quality-quality-management-quality-alerts).

### On a work order

When configuring a  that is triggered during manufacturing, a specific work order can also be
specified in the Work Order Operation field on the  form. If a work order is
specified, a *Take a Picture* quality check is created for that specific work order, rather than the
manufacturing order as a whole.

*Take a Picture* quality checks configured for work orders **must** be completed from the *Shop
Floor* module. To do so, begin by navigating to Manufacturing ‣ Operations ‣
Manufacturing Orders. Then, select an  that includes a work order for which a *Take a Picture*
quality check is required.

On the , select the Work Orders tab, and then click the Open Work Order
(external link icon) button on the line of the work order to be processed. On the resulting
Work Orders pop-up window, click the Open Shop Floor button to open the
*Shop Floor* module.

When accessed from a specific work order, the *Shop Floor* module opens to the page for the work
center where the order is configured to be processed, and isolates the work order's card, so no
other cards are shown.

Process the work order's steps until the *Take a Picture* quality check step is reached. Click on
the step to open a pop-up window that includes instructions for how the picture should be taken.
After taking the picture, make sure it is stored on the device being used to process the quality
check (computer, tablet, etc.).

Then, click the Take a Picture button on the pop-up window to open the device's file
manager. In the file manager, navigate to the picture, select it, and click Open to
attach it.

Finally, click Validate at the bottom of the pop-up window to complete the quality
check. The pop-up window then moves on to the next step of the work order.

![A Take a Picture check in the Shop Floor module.](applications/inventory_and_mrp/quality/quality_check_types/picture_check/picture-check-shop-floor.png)

If a quality alert must be created, exit the pop-up window by clicking the X (close)
button in the top-right corner.

Then, click the ⋮ (three vertical dots) button on the bottom-right corner of the work
order card to open the What do you want to do? pop-up window.

On the What do you want to do? pop-up window, select the Create a Quality
Alert button. Doing so opens a blank quality alert form in a new Quality Alerts pop-up
window.

#### SEE ALSO
For a complete guide on how to fill out quality alert forms, view the documentation on
[quality alerts](../quality_management/quality_alerts.md).

## Review picture attached to quality check

After a picture has been attached to a check, it can then be reviewed by quality team members or
other users. To do so, navigate to Quality ‣ Quality Control ‣ Quality Checks,
and select a quality check to review.

The attached picture appears in the Picture section of the quality check form. After
reviewing the picture, click the Pass button if the check passes, or the
Fail button if the check fails.

![A Take a Picture check with a picture attached.](applications/inventory_and_mrp/quality/quality_check_types/picture_check/review-picture-check.png)
