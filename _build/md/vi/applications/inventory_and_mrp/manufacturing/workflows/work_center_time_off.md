# Khu vực sản xuất ngừng hoạt động

Trong Odoo, *khu vực sản xuất* được sử dụng để thực hiện các hoạt động sản xuất tại những địa điểm cụ thể. Tuy nhiên, nếu không thể sử dụng một khu vực sản xuất vì lý do nào đó, các công đoạn sẽ bắt đầu tồn đọng tại khu vực sản xuất cho đến khi nó hoạt động trở lại.

Trong trường hợp đó, cần phải làm cho khu vực sản xuất này không khả dụng trong Odoo để các công đoạn mới được chuyển đến những khu vực sản xuất dự trù đang hoạt động. Bằng cách sử dụng ứng dụng **Ngày nghỉ** của Odoo, bạn có thể khiến một khu vực sản xuất không khả dụng trong một khoảng thời gian nhất định. Điều này đảm bảo hoạt động sản xuất có thể tiếp diễn cho đến khi khu vực sản xuất bị ảnh hưởng khả dụng trở lại.

## Cấu hình

Trước khi một khu vực sản xuất có thể được đánh dấu là không khả dụng, nền tảng Odoo phải được cấu hình chính xác. Trước tiên, cần phải bật [chế độ lập trình viên](../../../general/developer_mode.md#developer-mode). Khi bật chế độ này, nút thông minh *Ngày nghỉ* sẽ xuất hiện trên trang *Giờ làm việc* của mỗi khu vực sản xuất.

Tiếp theo, hãy cài đặt ứng dụng **Ngày nghỉ**. Đây là ứng dụng được sử dụng để quản lý thời gian nghỉ của tất cả tài nguyên trong Odoo, bao gồm cả nhân viên và khu vực sản xuất.

Để thực hiện, hãy đi đến ứng dụng Ứng dụng, sau đó tìm kiếm `Ngày nghỉ` trong thanh tìm kiếm. Thẻ cho ứng dụng Ngày nghỉ phải là thẻ duy nhất xuất hiện trên trang. Nhấp vào nút Cài đặt trên thẻ để cài đặt ứng dụng.

Bước cuối cùng là cấu hình các khu vực sản xuất một cách chính xác. Đối với quy trình này, cần phải có ít nhất hai khu vực sản xuất: một khu vực không khả dụng và một khu vực tiếp nhận các công đoạn mà khu vực kia không thể xử lý. Nếu không cấu hình khu vực sản xuất thứ hai nào, thì Odoo không thể chuyển các công đoạn ra khỏi khu vực sản xuất không khả dụng và chúng sẽ tích tụ trong danh sách chờ của khu vực đó.

Để tạo một khu vực sản xuất, hãy đi đến Ứng dụng Sản xuất ‣ Cấu hình ‣ Khu vực sản xuất ‣ Mới.

#### SEE ALSO
Để biết hướng dẫn chi tiết về cách tạo khu vực sản xuất, hãy tham khảo tài liệu về [khu vực sản xuất](../advanced_configuration/using_work_centers.md).

Đảm bảo cả hai khu vực sản xuất đều có cùng thiết bị được liệt kê trong tab Thiết bị. Như vậy, các hoạt động được xử lý tại khu vực này cũng có thể được thực hiện tại khu vực kia.

Trên khu vực sản xuất không khả dụng, hãy chọn khu vực sản xuất thứ hai từ menu thả xuống Khu vực sản xuất dự trù. Giờ đây, Odoo sẽ chuyển công đoạn đến khu vực sản xuất thứ hai khi khu vực đầu tiên không khả dụng vì bất kỳ lý do gì.

![Biểu mẫu khu vực sản xuất được cấu hình với một trung tâm làm việc dự trù.](applications/inventory_and_mrp/manufacturing/workflows/work_center_time_off/alternative-work-center-selection.png)

## Thêm ngày ngừng hoạt động cho khu vực sản xuất

Sau khi cấu hình xong, bạn có thể chỉ định ngày ngừng hoạt động cho một khu vực sản xuất. Bắt đầu bằng cách đi đến Ứng dụng Sản xuất ‣ Cấu hình ‣ Khu vực sản xuất và chọn khu vực sản xuất bị ảnh hưởng. Nhấp vào nút <i class="oi oi-arrow-right"></i> (Liên kết nội bộ) ở phía bên phải của menu thả xuống Giờ làm việc để mở trang giờ làm việc của khu vực sản xuất.

![Nút "Liên kết ngoài" về Giờ làm việc trên biểu mẫu khu vực sản xuất.](applications/inventory_and_mrp/manufacturing/workflows/work_center_time_off/working-hours-button.png)

Trang giờ làm việc hiển thị giờ làm việc tiêu chuẩn cho khu vực sản xuất. Khi chế độ lập trình viên được kích hoạt, nút thông minh <i class="fa fa-plane"></i> Ngày nghỉ sẽ xuất hiện ở đầu trang. Nhấp vào nút đó để mở trang Ngày nghỉ của tài nguyên.

Trên trang này, nhấp vào Mới để cấu hình một bản ghi ngày nghỉ mới. Trên biểu mẫu ngày nghỉ, hãy ghi chú Lý do đóng khu vực sản xuất (VD: thiết bị hỏng, bảo trì,...), chọn khu vực sản xuất bị ảnh hưởng làm Tài nguyên và chọn Ngày bắt đầu và Ngày kết thúc để xác định khoảng thời gian mà khu vực sản xuất này không khả dụng.

![Biểu mẫu "Ngày nghỉ của tài nguyên".](applications/inventory_and_mrp/manufacturing/workflows/work_center_time_off/time-off-form.png)

## Lập kế hoạch khu vực sản xuất dự trù

Khi một khu vực sản xuất ngừng hoạt động trong khoảng thời gian đã xác định, các công đoạn được gửi đến khu vực đó có thể được tự động chuyển đến một khu vực sản xuất dự trù bằng cách sử dụng nút *Kế hoạch*.

Bắt đầu bằng cách tạo một lệnh sản xuất (MO) mới thông qua Ứng dụng Sản xuất ‣ Hoạt động ‣ Lệnh sản xuất ‣ Mới. Trên biểu mẫu , hãy chỉ định một Sản phẩm sử dụng khu vực sản xuất không khả dụng để xử lý một trong các hoạt động sản xuất sản phẩm đó. Nhấp vào Xác nhận để xác nhận .

Trên  đã xác nhận, hãy chọn tab Công đoạn. Theo mặc định, khu vực sản xuất không khả dụng được chỉ định trong cột Khu vực sản xuất. Ngoài ra còn có nút Kế hoạch ở phía trên bên trái của trang.

Sau khi nhấp vào Kế hoạch, khu vực sản xuất được liệt kê trong cột Khu vực sản xuất của tab Công đoạn sẽ tự động được thay đổi thành khu vực sản xuất dự trù.

![Trước khi nhấp vào "Kế hoạch", công đoạn sẽ được lên lịch tại "Dây chuyền lắp ráp chính".](applications/inventory_and_mrp/manufacturing/workflows/work_center_time_off/before-planning.png)![Sau khi nhấp vào "Kế hoạch", công đoạn sẽ được lên lịch lại tại "Dây chuyền lắp ráp dự trù".](applications/inventory_and_mrp/manufacturing/workflows/work_center_time_off/after-planning.png)

Khi thời gian ngừng hoạt động của khu vực sản xuất không khả dụng kết thúc, Odoo sẽ biết được khu vực sản xuất đó đã khả dụng trở lại. Tại thời điểm này, việc nhấp vào nút Kế hoạch sẽ không chuyển các công đoạn đến khu vực sản xuất dự trù, trừ khi khu vực kia quá tải.
