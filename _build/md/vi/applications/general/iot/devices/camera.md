# Connect a camera

Bạn có thể kết nối camera với hộp  đã tích hợp với cơ sở dữ liệu Odoo chỉ trong vài bước. Sau khi camera được kết nối với hộp , nó có thể được sử dụng trong quy trình sản xuất hoặc có thể được liên kết với điểm kiểm soát chất lượng/kiểm tra chất lượng. Điều này cho phép chụp ảnh khi đạt đến điểm kiểm soát/kiểm tra chất lượng đã chọn hoặc khi nhấn một phím cụ thể trong quá trình sản xuất.

## Kết nối

To connect a camera to an  box, simply connect the two via cable.
This is usually done with a  cable of some sort.

If the camera is [supported](https://www.odoo.com/page/iot-hardware), there is no need to set up
anything, as it'll be detected as soon as it's connected.

![Camera recognized on the IoT box.](applications/general/iot/devices/camera/camera-dropdown.png)

## Link camera to quality control point in manufacturing process

In the Quality app, a device can be set up on a Quality Control Point.
To do that, navigate to the Quality app ‣ Quality Control ‣ Control Points and
open the desired Control Point that'll be linked to the camera.

On the control point form, edit the control point by selecting the Type field, and
clicking on Take a Picture from the drop-down menu. Doing so reveals a field called
Device, wherein the attached *device* can be selected. Save the changes, if
required.

![Setting up the device on the quality control point.](applications/general/iot/devices/camera/control-point-device.png)

The camera is now useable with the selected quality control point. When the quality control point
is reached during the manufacturing process, the database prompts the operator to take a picture.

![Graphic user interface of the device on the quality control point.](applications/general/iot/devices/camera/serial-number-picture.png)

#### NOTE
Quality control points can also be accessed by navigating to IoT App ‣
Devices. From here, select the device. There is a Quality Control Points tab, where
they can be added with the device.

#### SEE ALSO
- [Quality control points](../../../inventory_and_mrp/quality/quality_management/quality_control_points.md)
- [Quality alerts](../../../inventory_and_mrp/quality/quality_management/quality_alerts.md)

## Link camera to a work center in the Manufacturing app

Để liên kết camera với một tác vụ, trước tiên cần cấu hình trên khu vực sản xuất. Đi đến Ứng dụng Sản xuất ‣ Cấu hình ‣ Khu vực sản xuất. Sau đó, chọn Khu vực sản xuất mong muốn, nơi camera sẽ được sử dụng để hiển thị biểu mẫu chi tiết của khu vực đó. Tại đây, thêm thiết bị trong tab Bộ kích hoạt IoT, cột Thiết bị, bằng cách nhấp Thêm mộ dòng.

Now, the camera device can be linked to the Action column drop-down option labeled
Take a Picture. A key can also be added to trigger the action.

#### IMPORTANT
The first trigger listed is chosen first. The order of triggers matters, and they can be dragged
into any desired order.

#### NOTE
On the Work Order screen, a status graphic indicates whether the database is
correctly connected to the camera.

#### SEE ALSO
[Tích hợp với thiết bị IoT](../../../inventory_and_mrp/manufacturing/advanced_configuration/using_work_centers.md#workcenter-iot)
