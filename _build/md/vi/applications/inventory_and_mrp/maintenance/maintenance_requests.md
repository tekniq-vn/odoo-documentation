# Maintenance requests

In order to keep equipment and work centers functioning properly, it is often necessary to perform
maintenance on them. This can include preventive maintenance, intended to prevent equipment from
breaking down, or corrective maintenance, which is used to fix equipment that is broken or otherwise
unusable.

In Odoo *Maintenance*, users can create *maintenance requests* to schedule and track the progress of
equipment and work center maintenance.

## Create maintenance request

To create a new maintenance request, navigate to Maintenance app ‣ Maintenance ‣
Maintenance Requests, and click New.

Begin filling out the form by entering a descriptive title in the Request field (e.g.,
`Drill not working`).

The Created By field auto-populates with the user creating the request, but a different
user can be selected by clicking on the drop-down menu.

In the For drop-down menu, select Equipment if the maintenance request is
being created for a piece of equipment, or Work Center if it is being created for a work
center.

Depending on the option selected in the For field, the next field is titled either
Equipment or Work Center. Using the drop-down menu for either field, select
a piece of equipment or a work center.

If the *Custom Maintenance Worksheets* setting is enabled in the *Maintenance* app's settings, a
Worksheet Template field appears below the Equipment or Work
Center field. If necessary, use this field to select a worksheet to be filled out by the employee
performing the maintenance.

The next field is titled Request Date, and is set by default to the date on which the
maintenance request is created. This date cannot be changed by the user.

In the Maintenance Type field, select the Corrective option if the request
is intended to fix an existing issue, or the Preventive option if the request is
intended to prevent issues from occurring in the future.

If the request is being created to address an issue that arose during a specific manufacturing order
(MO), select it in the Manufacturing Order field.

If an  was selected in the Manufacturing Order field, a Work Order field
appears below it. If the issue arose during a specific work order, specify it in this field.

In the Team field, select the maintenance team that is responsible for managing the
request. If a specific team member is responsible, select them in the Responsible field.

Trường Ngày đã lên lịch dùng để chỉ định ngày bảo trì sẽ diễn ra và thời gian bắt đầu. Chọn ngày bằng cách nhấp vào trường để mở lịch trong cửa sổ bật lên, sau đó chọn ngày trên lịch. Nhập giờ và phút vào hai trường dưới lịch, rồi nhấp Áp dụng để lưu ngày và giờ.

The Duration field is used to specify the time it takes to complete the maintenance
request. Use the text-entry field to enter the time in a `00:00` format.

If Work Center was selected in the For field, a Block Workcenter
checkbox appears below the Duration field. Enable the checkbox to prevent work orders or
other maintenance from being scheduled at the specified work center while the maintenance request is
being processed.

Trường Mức độ ưu tiên được sử dụng để thể hiện mức độ quan trọng (hoặc khẩn cấp) của yêu cầu bảo trì. Gán mức ưu tiên từ 0 đến 3 ⭐⭐⭐ (sao) bằng cách nhấp vào số sao mong muốn. Các yêu cầu có mức ưu tiên cao hơn sẽ hiển thị phía trên những yêu cầu có mức ưu tiên thấp hơn trên bảng Kanban dùng để theo dõi tiến trình xử lý yêu cầu bảo trì.

In the Notes tab at the bottom of the form, enter any relevant details about the
maintenance request (why the maintenance issue arose, when it occurred, etc.).

The Instructions tab is used to include instructions for how maintenance should be
performed. Select one of the three options, and then include the instructions as detailed below:

- PDF: click the Upload your file button to open the device's file manager,
  and then select a file to upload.
- Google Slide: enter a Google Slide link in the text-entry field that
  appears after the option is selected.
- Text: enter the instructions in the text-entry field that appears after the option is
  selected.

![A maintenance request form filled out for a piece of equipment.](../../../_images/request-form.png)

## Process maintenance request

Once a maintenance request has been created, it appears in the *New Request* stage of the
*Maintenance Requests* page, which can be accessed by navigating to Maintenance app
‣ Maintenance ‣ Maintenance Requests.

Maintenance requests can be moved to different stages by dragging and dropping them. They can also
be moved by clicking on a request to open it in a new page, and then selecting the desired stage
from the stage indicator bar, located above the top-right corner of the request's form.

Successful maintenance requests should be moved to the Repaired stage, indicating that
the specified piece of equipment or work center is repaired.

Failed maintenance requests should be moved to the Scrap stage, indicating the specified
piece of equipment, or work center, could not be repaired, and must instead be scrapped.
