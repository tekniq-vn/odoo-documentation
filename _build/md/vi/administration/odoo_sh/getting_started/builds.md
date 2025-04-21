<a id="odoosh-gettingstarted-builds"></a>

# Bản dựng

## Tổng quan

Trong Odoo.sh, bản dựng là một cơ sở dữ liệu được tải bởi máy chủ Odoo ([odoo/odoo](https://github.com/odoo/odoo) & [odoo/enterprise](https://github.com/odoo/enterprise)) chạy trên một bản sửa đổi cụ thể của kho lưu trữ dự án của bạn trong môi trường được container hoá. Mục đích là kiểm thử hành vi khả quan của máy chủ, cơ sở dữ liệu và các tính năng với bản sửa đổi này.

![image](administration/odoo_sh/getting_started/builds/interface-builds.png)

Trong chế độ xem này, một hàng biểu thị một nhánh và mỗi ô trong hàng biểu thị một bản dựng của nhánh này.

Thông thường, bản dựng được tạo sau các lần push vào nhánh kho lưu trữ Github của bạn. Chúng cũng có thể được tạo khi bạn thực hiện các thao tác khác, chẳng hạn như nhập cơ sở dữ liệu trên Odoo.sh hoặc yêu cầu dựng lại một nhánh trong dự án của mình.

Một bản dựng được coi là thành công nếu không có lỗi hoặc cảnh báo nào xuất hiện trong quá trình tạo. Bản dựng thành công được đánh dấu màu xanh lục.

Một bản dựng được coi là thất bại nếu có lỗi xuất hiện trong quá trình tạo. Bản dựng thất bại được đánh dấu màu đỏ.

Nếu cảnh báo xuất hiện trong quá trình tạo nhưng không có lỗi, bản dựng được coi là gần như thành công. Bản dựng này sẽ được đánh dấu màu vàng để thông báo cho lập trình viên rằng cảnh báo đã được đưa ra.

Không phải lúc nào bản dựng cũng tạo cơ sở dữ liệu từ đầu. Ví dụ, khi push thay đổi lên nhánh production, bản dựng được tạo chỉ khởi động máy chủ với bản sửa đổi mới của bạn và cố gắng tải cơ sở dữ liệu production hiện tại lên đó. Nếu lỗi không xảy ra, bản dựng được coi là thành công và ngược lại là không thành công.

## Giai đoạn

### Hoạt động thực tế

Bản dựng đầu tiên của nhánh production sẽ tạo cơ sở dữ liệu từ đầu. Nếu bản dựng thành công, cơ sở dữ liệu này được coi là cơ sở dữ liệu production cho dự án của bạn.

Từ đó, các lần push vào nhánh sản xuất sẽ tạo ra các bản dựng mới nhằm tải cơ sở dữ liệu bằng máy chủ chạy phiên bản mới.

Nếu bản dựng thành công hoặc có cảnh báo nhưng không có lỗi, cơ sở dữ liệu production sẽ chạy với bản dựng này cùng với bản sửa đổi liên quan đến nó.

Nếu bản dựng không thể tải hoặc cập nhật cơ sở dữ liệu, thì bản dựng thành công trước đó sẽ được sử dụng lại để tải cơ sở dữ liệu. Do đó cơ sở dữ liệu sẽ chạy bằng máy chủ có bản sửa đổi thành công trước đó.

Bản dựng được sử dụng để chạy cơ sở dữ liệu production luôn là bản dựng đầu tiên trong danh sách bản dựng. Nếu một bản dựng thất bại, nó sẽ được đặt sau bản dựng hiện đang chạy cơ sở dữ liệu production.

### Staging

Bản dựng staging sẽ sao chép cơ sở dữ liệu production và thử tải bản sao này cùng với các bản sửa đổi của nhánh staging.

Mỗi lần bạn push một bản sửa đổi mới lên nhánh staging, bản dựng được tạo sẽ sử dụng một bản sao mới của cơ sở dữ liệu production. Các bản dựng của cùng một nhánh không sử dụng lại cơ sở dữ liệu. Điều này đảm bảo:

* bản dựng staging sử dụng cơ sở dữ liệu gần giống với production, do đó bạn không phải tiến hành kiểm thử bằng dữ liệu đã lỗi thời,
* bạn có thể tùy ý chỉnh sửa trong cùng một cơ sở dữ liệu staging và sau đó có thể yêu cầu dựng lại khi muốn khởi động lại với một bản sao production mới.

Tuy nhiên, điều này có nghĩa là nếu bạn thực hiện các thay đổi cấu hình trong cơ sở dữ liệu staging và không áp dụng chúng trong production, thì những thay đổi này sẽ không được chuyển sang bản dựng tiếp theo của cùng một nhánh staging.

### Phát triển

Bản dựng phát triển tạo cơ sở dữ liệu mới, tải dữ liệu demo và chạy các bản kiểm thử đơn vị.

Bản dựng sẽ được coi là thất bại và được đánh dấu màu đỏ nếu các bản kiểm thử thất bại trong quá trình cài đặt, vì chúng có tác dụng báo lỗi nếu có sự cố xảy ra.

Nếu tất cả các bản kiểm thử đều đạt và không có lỗi, bản dựng sẽ được coi là thành công.

Theo danh sách phân hệ cần cài đặt và kiểm thử, bản dựng phát triển có thể mất tới 1 giờ để sẵn sàng. Lý do là vì nhiều bản kiểm thử được thiết lập trong bộ phân hệ Odoo mặc định.

## Tính năng

Nhánh production sẽ luôn xuất hiện đầu tiên, sau đó các nhánh khác được sắp xếp theo thứ tự bản dựng được tạo gần nhất. Bạn có thể lọc các nhánh.

![image](administration/odoo_sh/getting_started/builds/interface-builds-branches.png)

Đối với mỗi nhánh, bạn có thể truy cập cơ sở dữ liệu của bản dựng cuối cùng bằng liên kết *Kết nối* và đi đến mã nhánh bằng liên kết *Github*. Đối với các nhánh khác không phải nhánh sản xuất, bạn có thể tạo bản dựng mới sẽ sử dụng bản sửa đổi mới nhất của nhánh bằng liên kết *dựng lại*. Liên kết cuối cùng này không khả dụng khi đã có bản dựng đang tiến hành cho nhánh.

![image](administration/odoo_sh/getting_started/builds/interface-builds-build.png)

Đối với mỗi bản dựng, bạn có thể truy cập các thay đổi trên bản sửa đổi bằng nút có biểu tượng Github. Bạn có thể truy cập cơ sở dữ liệu của bản dựng với tư cách là quản trị viên bằng nút *Kết nối*. Ngoài ra, bạn có thể truy cập cơ sở dữ liệu với tư cách người dùng khác bằng nút *Kết nối với tư cách* trong menu thả xuống của nút *Kết nối*.

<a id="odoosh-gettingstarted-builds-download-dump"></a>
![image](administration/odoo_sh/getting_started/builds/interface-builds-build-dropdown.png)

<a id="odoosh-gettingstarted-builds-dropdown-menu"></a>

Trong menu thả xuống của bản dựng, bạn có thể truy cập các tính năng tương tự như trong [chế độ xem nhánh](branches.md#odoosh-gettingstarted-branches-tabs): *Nhật ký*, *Web Shell*, *Trình soạn thảo*, *Email đi*. Bạn cũng có thể *Tải xuống bản kết xuất* cơ sở dữ liệu của bản dựng đó.
