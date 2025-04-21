# Quản lý BoM dùng cho biến thể sản phẩm

Odoo cho phép sử dụng một danh mục vật tư (BoM) cho nhiều biến thể của cùng một sản phẩm. Việc có một  chung cho mỗi sản phẩm có nhiều biến thể giúp tiết kiệm thời gian vì bạn không cần quản lý nhiều .

## Kích hoạt biến thể sản phẩm

Để kích hoạt tính năng biến thể sản phẩm, hãy đi đến Ứng dụng Tồn kho ‣ Cấu hình ‣ Cài đặt, và cuộn xuống phần Sản phẩm. Sau đó, nhấp vào hộp kiểm để bật tùy chọn Biến thể. Tiếp theo, nhấp vào Lưu để áp dụng cài đặt.

Để biết thêm thông tin về cách cấu hình các biến thể sản phẩm, hãy tham khảo tài liệu [biến thể sản phẩm](../../../sales/sales/products_prices/products/variants.md).

![Chọn "Biến thể" từ phần cài đặt ứng dụng Tồn kho.](applications/inventory_and_mrp/manufacturing/advanced_configuration/product_variants/product-variants-variants-settings.png)

## Tạo thuộc tính sản phẩm tùy chỉnh

Sau khi tính năng biến thể sản phẩm được kích hoạt, hãy tạo và chỉnh sửa thuộc tính sản phẩm trên trang Thuộc tính.

Có thể truy cập trang Thuộc tính bằng cách đi đến Ứng dụng Tồn kho ‣ Cấu hình ‣ Cài đặt rồi nhấp vào nút Thuộc tính hoặc đi đến Ứng dụng Tồn kho ‣ Cấu hình ‣ Thuộc tính.

Khi vào trang Thuộc tính, hãy nhấp vào một thuộc tính hiện có hoặc nhấp vào Tạo để tạo một thuộc tính mới. Sau khi bạn nhấp vào Tạo, một biểu mẫu trống mới sẽ hiển thị để tạo thuộc tính. Đối với thuộc tính hiện có, hãy nhấp vào Chỉnh sửa trên biểu mẫu của thuộc tính đó để thực hiện thay đổi.

Đặt Tên thuộc tính, và chọn một danh mục từ menu thả xuống của trường Danh mục. Sau đó, chọn những tùy chọn mong muốn cạnh các trường Loại hiển thị và Chế độ tạo biến thể. Sau khi chọn xong, hãy nhấp vào Thêm một dòng bên dưới tab Giá trị thuộc tính để thêm giá trị mới.

Sau khi đã thêm tất cả Giá trị mong muốn, hãy nhấp vào Lưu để lưu thuộc tính mới.

## Thêm các biến thể sản phẩm vào biểu mẫu sản phẩm

Thuộc tính đã tạo có thể được áp dụng cho các biến thể cụ thể của những sản phẩm cụ thể. Để thêm các biến thể vào một sản phẩm, hãy đi đến biểu mẫu sản phẩm bằng cách vào Ứng dụng Tồn kho ‣ Sản phẩm ‣ Sản phẩm. Để thực hiện thay đổi cho sản phẩm, hãy nhấp vào Chỉnh sửa. Sau đó, nhấp vào tab Biến thể.

Trong header Thuộc tính, nhấp vào Thêm một dòng để thêm thuộc tính mới và chọn một thuộc tính từ menu thả xuống để thêm vào.

Sau đó, bên dưới header Giá trị, nhấp vào menu thả xuống để chọn các giá trị hiện có từ danh sách. Nhấp vào từng giá trị mong muốn để thêm chúng và lặp lại quy trình này cho những thuộc tính khác cần thêm vào sản phẩm.

Khi hoàn thành, hãy nhấp vào Lưu để lưu thay đổi.

![Tab biến thể trên biểu mẫu sản phẩm có các giá trị và thuộc tính.](applications/inventory_and_mrp/manufacturing/advanced_configuration/product_variants/product-variants-product-form.png)

## Áp dụng các thành phần của BoM cho biến thể sản phẩm

Tiếp theo, tạo một  mới hoặc chỉnh sửa một BoM hiện có. Để tạo mới, đi đến Ứng dụng Sản xuất ‣ Sản phẩm ‣ Danh mục vật tư. Sau đó, nhấp vào Tạo để mở một biểu mẫu Danh mục vật tư mới và cấu hình từ đầu.

Thêm sản phẩm vào  bằng cách nhấp vào menu thả xuống trong trường Sản phẩm và chọn sản phẩm mong muốn.

Sau đó, thêm thành phần bằng cách nhấp vào Thêm một dòng trong phần Thành phần của tab Thành phần và chọn các thành phần mong muốn từ menu thả xuống.

Chọn giá trị mong muốn trong các cột Số lượng và Đơn vị tính sản phẩm. Sau đó, chọn giá trị mong muốn trong cột Áp dụng cho các biến thể.

#### NOTE
Tùy chọn Áp dụng cho các biến thể để chỉ định thành phần cho những biến thể sản phẩm cụ thể trên  sẽ khả dụng sau khi cài đặt Biến thể được kích hoạt từ ứng dụng Tồn kho. Nếu trường Áp dụng cho các biến thể không hiển thị ngay lập tức, hãy kích hoạt trường này từ menu tùy chọn bổ sung (biểu tượng dấu ba chấm, bên phải hàng header).

![Tùy chọn "Áp dụng cho các biến thể" trên menu tùy chọn bổ sung.](applications/inventory_and_mrp/manufacturing/advanced_configuration/product_variants/product-variants-apply-on-variants.png)

Mỗi thành phần có thể được chỉ định cho nhiều biến thể. Nếu không chỉ định biến thể cho thành phần, thì nó sẽ được sử dụng trong mọi biến thể của sản phẩm. Nguyên tắc tương tự được áp dụng khi cấu hình hoạt động và phụ phẩm.

Khi thiết lập  dành cho các biến thể bằng cách chỉ định thành phần, trường Biến thể sản phẩm trong phần chính của  phải được để trống. Trường này *chỉ* được sử dụng khi tạo  dành riêng cho một biến thể sản phẩm cụ thể.

Khi hoàn thành tất cả cấu hình mong muốn cho , hãy nhấp vào Lưu ở đầu biểu mẫu để lưu thay đổi.

## Bán và sản xuất các biến thể sản phẩm có BoM

Để bán và sản xuất các biến thể sản phẩm có  theo đơn đặt hàng, hãy đi đến Ứng dụng Bán hàng ‣ Tạo để tạo một báo giá mới.

### Bán biến thể sản phẩm có BoM

Trên biểu mẫu Báo giá trống, hãy nhấp vào menu thả xuống cạnh trường Khách hàng để thêm khách hàng.

Sau đó, trong tab Chi tiết đơn hàng, nhấp vào Thêm sản phẩm và chọn sản phẩm có  đã tạo trước đó với các biến thể từ menu thả xuống. Tiếp theo, cửa sổ bật lên Cấu hình sản phẩm sẽ hiển thị.

Từ cửa sổ bật lên, nhấp vào tùy chọn thuộc tính mong muốn để cấu hình đúng biến thể của sản phẩm cần sản xuất. Sau đó, nhấp vào biểu tượng + hoặc - màu xanh lá cây bên cạnh `1` để thay đổi số lượng bán và sản xuất, nếu muốn.

![Cửa sổ bật lên Cấu hình sản phẩm để chọn thuộc tính biến thể.](applications/inventory_and_mrp/manufacturing/advanced_configuration/product_variants/product-variants-variant-popup.png)

Sau khi đã chọn tất cả các thông số kỹ thuật, hãy nhấp vào Thêm. Thao tác này sẽ biến cửa sổ bật lên thành cửa sổ bật lên Cấu hình thứ hai, nơi các sản phẩm tùy chọn khả dụng sẽ xuất hiện, nếu chúng đã được tạo trước đó.

Khi đã sẵn sàng, hãy nhấp vào Xác nhận để đóng cửa sổ bật lên.

Sau đó, nhấp vào Lưu để lưu tất cả các thay đổi và nhấp vào Xác nhận ở đầu biểu mẫu Báo giá để tạo và xác nhận đơn bán hàng (SO) mới.

### Sản xuất biến thể sản phẩm có BoM

Sau khi  được xác nhận, nút Sản xuất sẽ xuất hiện ở đầu biểu mẫu . Nhấp vào nút Sản xuất này để mở biểu mẫu Lệnh sản xuất.

Trên biểu mẫu này, các thành phần phù hợp cho biến thể đã chọn được liệt kê trong tab Thành phần. Đồng thời, các thành phần khác nhau sẽ được liệt kê tùy vào biến thể. Để xem mọi bước Hoạt động bắt buộc hoặc tùy chọn, hãy nhấp vào tab Công đoạn.

Để vào màn hình công đoạn ở chế độ xem máy tính bảng, hãy nhấp vào biểu tượng máy tính bảng nằm ở bên phải trên dòng hoạt động cần được hoàn thành.

Từ chế độ xem máy tính bảng, nhấp vào Đánh dấu là hoàn tất khi hoạt động kết thúc để hoàn thành các hoạt động.

Ngoài ra, bạn có thể nhấp vào nút Đánh dấu là hoàn tất ở đầu biểu mẫu lệnh sản xuất để hoàn thành lệnh sản xuất đó.

![Lệnh sản xuất cho các biến thể của sản phẩm có BoM.](applications/inventory_and_mrp/manufacturing/advanced_configuration/product_variants/product-variants-manufacturing-order.png)

Sau đó, quay lại  thông qua breadcrumb ở đầu trang.

Bây giờ sản phẩm đã được sản xuất, hãy nhấp vào nút Giao hàng để giao sản phẩm cho khách hàng. Từ biểu mẫu Lệnh giao hàng, hãy nhấp vào Xác thực, sau đó nhấp vào Áp dụng để giao sản phẩm.

Để hoàn tất việc bán hàng, hãy nhấp vào  thông qua breadcrumb ở đầu trang một lần nữa. Sau đó, nhấp vào Tạo hoá đơn, tiếp theo là Tạo hoá đơn một lần nữa để lập hóa đơn đơn hàng cho khách hàng.
