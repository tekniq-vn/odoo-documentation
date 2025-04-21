# Quality alerts

In the Odoo *Quality* app, *quality alerts* are used to notify quality teams of product defects or
other issues. Quality alerts can be created from a manufacturing or inventory order, from a work
order in the *Shop Floor* module, or directly within the *Quality* app.

## Create quality alerts

There are multiple ways to create a new quality alert:

- **From the Quality app itself**, by to Quality ‣  Quality Control ‣ Quality
  Alerts, and then click New to open a quality alert form.
- Navigate to Manufacturing ‣ Operations ‣ Manufacturing Orders, and then
  select an . Click the Quality Alert button at the top of the  to open a
  quality alert form in a new page.

  #### IMPORTANT
  This method can only be used if a quality check has been requested for the . The
  Quality Alert button will not appear otherwise.
- Open the Inventory app, click the # To Process button on an inventory
  order type card (Receipts, Delivery Orders, etc.), and then select an order. Click the
  Quality Alert button at the top of the order to open a quality alert form in a new
  page.

  #### IMPORTANT
  Chỉ có thể sử dụng phương pháp này nếu kiểm tra chất lượng đã được yêu cầu cho phiếu kho. Nút Cảnh báo chất lượng sẽ không xuất hiện trong trường hợp khác. Nếu nút này không xuất hiện, bạn cũng có thể tạo cảnh báo chất lượng bằng cách nhấp vào biểu tượng ⚙️ (bánh răng) ở đầu trang và chọn tùy chọn Cảnh báo chất lượng từ menu hiện ra.
- Mở phân hệ Xưởng, sau đó chọn một khu vực sản xuất từ thanh điều hướng ở đầu trang. Tiếp theo, nhấp nút ⋮ (ba chấm dọc) ở góc dưới bên phải thẻ công đoạn để mở menu Bạn muốn làm gì?. Chọn tùy chọn Tạo cảnh báo chất lượng từ menu này để mở cảnh báo chất lượng trong cửa sổ bật lên.

#### NOTE
Depending on how a new quality alert form is opened, certain fields on the form may already be
filled in. For example, if a quality alert is created from a work order card in the *Shop Floor*
module, the Product and Work Center are pre-filled.

### Quality alerts form

After opening a new quality alert form, begin by giving it a short Title that summarizes
the issue with the product.

Then, if the quality alert is referencing:

- **A specific product or product variant**, select it from the Product or
  Product Variant drop-down menus.
- **A specific work center**, select it from the Work Center drop-down menu.
- **A specific picking order**, select it from the Picking drop-down menu.

Next in the Team field, select the quality team that is responsible for managing the
quality alert. If a specific employee should be responsible for the quality alert, select them from
the Responsible drop-down menu.

In the Tags field, select any tags relevant to the quality alert from the drop-down
menu.

Use the Root Cause field to select the cause of the quality issue, if known.

Lastly, choose a Priority level by selecting a ⭐ (star) number between one
and three. Quality alerts with higher priorities appear at the top of the Quality Alerts
Kanban board in the *Quality* app.

At the bottom of the quality alert form are four tabs which aid in adding supplemental information
or actions to be taken for the quality alert. They can be filled out as follows:

- In the Description tab, enter a description of the quality issue.
- Use the Corrective Actions tab to detail the steps that should be taken to fix the
  issue.
- Use the Preventive Actions tab to detail what should be done to prevent the issue from
  occurring in the future.
- In the Miscellaneous tab, select the Vendor of the product. If using an
  Odoo database which manages multiple companies, select the relevant company in the
  Company field. Finally, specify when the alert was assigned to a quality team in the
  Date Assigned field.

![A quality alert form that has been filled out.](applications/inventory_and_mrp/quality/quality_management/quality_alerts/alert-form.png)

## Manage quality alerts

To view all existing quality alerts, navigate to Quality ‣ Quality Control ‣
Quality Alerts. By default, alerts are displayed in a Kanban board view, which organizes them into
different stages based on where they are in the review process.

To move an alert to a different stage, simply drag and drop it on the desired stage. Alternatively,
select a quality alert to open it, and then click the desired stage above the top-right corner of
the quality alert form.

Để tạo cảnh báo mới trong một giai đoạn cụ thể, nhấp vào nút + (dấu cộng) bên phải tên giai đoạn. Trong thẻ cảnh báo mới xuất hiện bên dưới tiêu đề giai đoạn, nhập Tiêu đề cảnh báo, sau đó nhấp Thêm. Để cấu hình phần còn lại của cảnh báo, chọn thẻ cảnh báo để mở biểu mẫu của nó.

![The Quality Alerts page, displaying alerts in a Kanban view.](applications/inventory_and_mrp/quality/quality_management/quality_alerts/alert-kanban.png)
