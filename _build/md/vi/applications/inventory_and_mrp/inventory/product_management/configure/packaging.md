# Gói hàng

Trong Odoo *Tồn kho*, *gói hàng* đề cập đến bao bì dùng một lần chứa nhiều đơn vị của một sản phẩm cụ thể.

Ví dụ, các gói hàng khác nhau dùng cho lon nước ngọt, chẳng hạn như lốc 6 lon, lốc 12 lon hoặc thùng 36 lon, **phải** được cấu hình trên biểu mẫu sản phẩm riêng. Điều này là do gói hàng được áp dụng theo sản phẩm, không phải dùng chung.

## Cấu hình

Để sử dụng gói hàng, điều hướng đến Ứng dụng Tồn kho ‣ Cấu hình ‣ Cài đặt. Sau đó, dưới tiêu đề Sản phẩm, bật tính năng Gói hàng và nhấp vào Lưu.

![Bật gói hàng bằng cách chọn "Gói hàng".](applications/inventory_and_mrp/inventory/product_management/configure/packaging/enable-packagings.png)

<a id="inventory-product-management-packaging-setup"></a>

## Tạo gói hàng

Có thể tạo gói hàng ngay trên biểu mẫu sản phẩm hoặc từ trang `Gói hàng`.

### Từ biểu mẫu sản phẩm

Tạo gói hàng trên biểu mẫu sản phẩm bằng cách vào Ứng dụng Tồn kho ‣ Sản phẩm ‣ Sản phẩm và chọn sản phẩm mong muốn.

Trong tab Tồn kho, cuộn xuống phần Gói hàng và nhấp vào Thêm một dòng. Điền vào các trường sau trong bảng:

- Gói hàng (bắt buộc): tên gói hàng xuất hiện trên đơn mua/bán hàng như một lựa chọn đóng gói sản phẩm.
- Số lượng sản phẩm (bắt buộc): số lượng sản phẩm có trong gói hàng.
- Đơn vị tính (bắt buộc): đơn vị tính để định lượng sản phẩm.
- Bán hàng: chọn tùy chọn này cho các gói hàng dự định sử dụng cho đơn bán hàng.
- Mua hàng: chọn tùy chọn này cho các gói hàng dự định sử dụng cho đơn mua hàng.

#### NOTE
Truy cập các trường bổ sung trong bảng Gói hàng dưới đây bằng cách nhấp vào biểu tượng <i class="oi oi-settings-adjust"></i> (additional options) ở phía bên phải của tiêu đề cột trong phần Gói hàng và chọn tùy chọn mong muốn từ menu thả xuống.

- Mã vạch: mã số dùng để theo dõi gói hàng trong quá trình dịch chuyển tồn kho hoặc lấy hàng, sử dụng [Ứng dụng Mã vạch](../../../barcode/operations/receipts_deliveries.md#barcode-operations-intro). Để trống nếu không sử dụng.
- Công ty: cho biết gói hàng chỉ có tại công ty đã chọn. Để trống để gói hàng khả dụng cho tất cả công ty.

### Từ trang Gói hàng

Để xem tất cả gói hàng đã tạo, vào Ứng dụng Tồn kho ‣ Cấu hình ‣ Gói hàng. Sau đó, trang Gói hàng sẽ hiển thị với danh sách toàn bộ gói hàng đã tạo cho tất cả sản phẩm. Tạo gói hàng mới bằng cách nhấp vào Mới.

### Dự trữ một phần

Sau khi [hoàn tất thiết lập gói hàng](#inventory-product-management-packaging-setup), bạn có thể dự trữ toàn bộ hoặc một phần gói hàng cho các lô hàng xuất đi. Tính linh hoạt của đóng gói một phần đẩy nhanh việc thực hiện đơn hàng bằng cách cho phép giao ngay các mặt hàng có sẵn, trong khi chờ số hàng còn lại.

Để cấu hình phương pháp dự trữ gói hàng, hãy vào Ứng dụng Tồn kho ‣ Cấu hình ‣ Danh mục sản phẩm. Sau đó, nhấp vào Mới hoặc chọn danh mục sản phẩm mong muốn.

Trên biểu mẫu danh mục sản phẩm, trong phần Logistics, Dự trữ gói hàng có thể được đặt thành Chỉ dự trữ toàn bộ gói hàng hoặc Dự trữ một phần gói hàng.

#### IMPORTANT
**Phải** bật tính năng Gói hàng để có thể xem trường Dự trữ gói hàng. Để bật tính năng này, hãy vào Ứng dụng Tồn kho ‣ Cấu hình ‣ Cài đặt, cuộn đến phần Sản phẩm, đánh dấu vào ô Gói hàng và nhấp vào Lưu.

![Hiển thị trường Dự trữ gói hàng trên trang danh mục sản phẩm.](applications/inventory_and_mrp/inventory/product_management/configure/packaging/reserve-packaging.png)

## Sử dụng gói hàng

Khi tạo đơn bán hàng trong ứng dụng Bán hàng, xác định các gói hàng cần sử dụng cho sản phẩm. Gói hàng đã chọn sẽ được hiển thị trên  trong trường Gói hàng.

<a id="inventory-product-management-packaging-route"></a>

## Tuyến cung ứng dành cho gói hàng

Khi nhận các gói hàng, theo mặc định, chúng sẽ tuân theo [tuyến nhập kho đã cấu hình](../../shipping_receiving/daily_operations.md) của kho hàng. Để **tùy chọn** thiết lập một tuyến cung ứng riêng theo gói hàng, đi đến Ứng dụng Tồn kho ‣ Cấu hình ‣ Tuyến cung ứng.

#### IMPORTANT
Các tính năng *Gói hàng*, *Vị trí lưu kho* và *Tuyến cung ứng nhiều bước* (truy cập bằng cách vào Ứng dụng Tồn kho ‣ Cấu hình ‣ Cài đặt) **phải** được kích hoạt và lưu lại.

#### SEE ALSO
[Routes and push/pull rules](../../shipping_receiving/daily_operations/use_routes.md)

### Tạo tuyến cung ứng

Trên trang Tuyến cung ứng, nhấp vào Mới hoặc chọn một tuyến cung ứng **không** dành cho kho hàng. Tiếp theo, trong phần Áp dụng cho, chọn ô Gói hàng.

![Tạo tuyến cung ứng dành cho gói hàng.](applications/inventory_and_mrp/inventory/product_management/configure/packaging/route.png)

<a id="inventory-product-management-route-on-packaging"></a>

### Áp dụng tuyến cung ứng cho gói hàng

Sau đó, để áp dụng tuyến cung ứng, truy cập Ứng dụng Tồn kho ‣ Sản phẩm ‣ Sản phẩm và chọn sản phẩm sử dụng gói hàng.

Trong biểu mẫu sản phẩm, chuyển sang tab Tồn kho. Trong phần Gói hàng chứa [gói hàng đã cấu hình](#inventory-product-management-packaging-setup), nhấp vào biểu tượng <i class="oi oi-settings-adjust"></i> (additional options). Chọn ô Tuyến cung ứng để cột này hiển thị trong bảng Gói hàng.

Trong trường Tuyến cung ứng, chọn tuyến đường riêng theo gói hàng. Lặp lại các bước này cho tất cả gói hàng dự định sử dụng tuyến đường đó.

![Thiết lập tuyến cung ứng dành cho gói hàng.](applications/inventory_and_mrp/inventory/product_management/configure/packaging/apply-route.png)
