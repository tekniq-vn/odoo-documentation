# Hạng mục phụ thuộc của công đoạn

Khi sản xuất một số sản phẩm nhất định, các hoạt động cụ thể có thể cần phải hoàn tất trước khi hoạt động khác bắt đầu. Để đảm bảo hoạt động sản xuất diễn ra theo đúng thứ tự, Odoo *Sản xuất* có tính năng *hạng mục phụ thuộc của công đoạn*. Tính năng này cho phép *chặn* các hoạt động trên danh mục vật tư (BoM) bằng những hoạt động khác cần diễn ra trước.

## Cấu hình

Tính năng *hạng mục phụ thuộc của công đoạn* sẽ không được bật theo mặc định. Để bật tính năng này, hãy bắt đầu bằng cách đi đến Sản xuất ‣ Cấu hình ‣ Cài đặt. Sau đó, bật tính năng Công đoạn, nếu nó chưa được kích hoạt.

Sau khi bật Công đoạn, tính năng Hạng mục phụ thuộc của công đoạn sẽ xuất hiện bên dưới. Bật Hạng mục phụ thuộc của công đoạn, sau đó nhấp vào Lưu để xác nhận thay đổi.

## Thêm hạng mục phụ thuộc vào BoM

Hạng mục phụ thuộc của công đoạn được cấu hình trên  của sản phẩm. Để thực hiện, hãy đi đến Sản xuất ‣ Sản phẩm ‣ Danh mục vật tư, sau đó chọn một  hoặc tạo một BOM mới bằng cách nhấp vào Mới.

Trên , nhấp vào tab Thông tin khác, sau đó bật hộp kiểm Hạng mục phụ thuộc của công đoạn. Thao tác này tạo tùy chọn Bị chặn bởi mới trong phần cài đặt của tab Hoạt động.

![Hộp kiểm Hạng mục phụ thuộc của hoạt động trên tab Thông tin khác của BoM.](applications/inventory_and_mrp/manufacturing/advanced_configuration/work_order_dependencies/operation-dependencies.png)

Tiếp theo, nhấp vào tab Hoạt động. Ở góc trên bên phải của tab này, nhấp vào nút cài đặt của tab, sau đó bật hộp kiểm Bị chặn bởi. Thao tác này sẽ tạo ra trường Bị chặn bởi cho mỗi hoạt động trên tab Hoạt động.

![Thiết lập cho tab Hoạt động trên BoM.](applications/inventory_and_mrp/manufacturing/advanced_configuration/work_order_dependencies/operations-settings.png)

Trong dòng hoạt động cần bị chặn, hãy nhấp vào trường Bị chặn bởi, và cửa sổ bật lên Mở: Hoạt động sẽ xuất hiện. Trong trường thả xuống Bị chặn bởi trên cửa sổ bật lên này, hãy chọn hoạt động chặn cần phải hoàn thành *trước* hoạt động bị chặn.

![Trường thả xuống Bị chặn bởi cho một hoạt động trên BoM.](applications/inventory_and_mrp/manufacturing/advanced_configuration/work_order_dependencies/blocked-by.png)

Cuối cùng, lưu  bằng cách nhấp vào Lưu.

## Lên kế hoạch công đoạn bằng cách sử dụng hạng mục phụ thuộc

Sau khi các hạng mục phụ thuộc của công đoạn đã được cấu hình trên , Odoo *Sản xuất* có thể lập kế hoạch thời điểm công đoạn diễn ra, dựa trên các hạng mục phụ thuộc của chúng. Để lập kế hoạch cho các công đoạn của một lệnh sản xuất, hãy bắt đầu bằng cách đi đến Sản xuất ‣ Hoạt động ‣ Lệnh sản xuất.

Tiếp theo, chọn lệnh sản xuất cho sản phẩm có  chứa hạng mục phụ thuộc của công đoạn hoặc tạo lệnh sản xuất mới bằng cách nhấp vào Mới. Nếu lệnh sản xuất mới được tạo, hãy chọn  có hạng mục phụ thuộc của công đoạn từ ​​trường thả xuống Danh mục vật tư, sau đó nhấp vào Xác nhận.

Sau khi xác nhận lệnh sản xuất, hãy chọn tab Công đoạn để xem các công đoạn cần thiết để hoàn thành lệnh sản xuất đó. Những công đoạn *không* bị công đoạn khác chặn sẽ hiển thị thẻ `Sẵn sàng` trong phần Trạng thái.

Các công đoạn bị chặn bởi một hoặc nhiều công đoạn sẽ hiển thị thẻ `Đang chờ công đoạn khác`. Khi (các) công đoạn chặn hoàn tất, thẻ này sẽ được cập nhật thành `Sẵn sàng`.

![Thẻ trạng thái cho công đoạn trong lệnh sản xuất.](applications/inventory_and_mrp/manufacturing/advanced_configuration/work_order_dependencies/work-order-status.png)

Để lên lịch cho các công đoạn của lệnh sản xuất, hãy nhấp vào nút Kế hoạch ở đầu trang. Sau đó, ngày và giờ bắt đầu theo lịch trình sẽ tự động được điền vào trường Ngày bắt đầu đã lên lịch cho mỗi công đoạn trên tab Công đoạn. Công đoạn bị chặn sẽ được lên lịch vào cuối khoảng thời gian đã xác định trong trường Thời lượng dự kiến của công đoạn trước đó.

![Trường Ngày bắt đầu đã lên lịch cho các công đoạn trong lệnh sản xuất.](applications/inventory_and_mrp/manufacturing/advanced_configuration/work_order_dependencies/scheduled-start-date.png)

### Lập kế hoạch theo khu vực sản xuất

Để xem nội dung trực quan về cách lập kế hoạch cho công đoạn, hãy đi đến trang Lập kế hoạch công đoạn bằng cách vào Sản xuất ‣ Kế hoạch ‣ Lập kế hoạch theo khu vực sản xuất. Trang này hiển thị dòng thời gian của tất cả công đoạn đã lên lịch cho từng hoạt động.

Nếu một công đoạn bị chặn do cần hoàn thành công đoạn khác trước, thì công đoạn bị chặn sẽ được hiển thị là đã lên lịch bắt đầu sau công đoạn chặn nó. Ngoài ra, một mũi tên sẽ kết nối hai công đoạn, dẫn từ hoạt động chặn đến hoạt động bị chặn.

![Mũi tên kết nối công đoạn bị chặn với công đoạn đang chặn công đoạn đó.](applications/inventory_and_mrp/manufacturing/advanced_configuration/work_order_dependencies/planning-arrow.png)
