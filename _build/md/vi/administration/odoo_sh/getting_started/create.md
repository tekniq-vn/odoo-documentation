<a id="odoosh-gettingstarted-create"></a>

# Tạo dự án của bạn

## Triển khai nền tảng của bạn

Đi đến [Odoo.sh](https://www.odoo.sh/) và bấm nút *Triển khai nền tảng của bạn*.

![image](administration/odoo_sh/getting_started/create/deploy.png)

## Đăng nhập bằng Github

Đăng nhập bằng tài khoản Github của bạn. Nếu bạn chưa có tài khoản, hãy nhấp vào liên kết *Tạo tài khoản*.

![image](administration/odoo_sh/getting_started/create/github-signin.png)

## Uỷ quyền cho Odoo.sh

Cấp cho Odoo.sh quyền truy cập cần thiết vào tài khoản của bạn bằng cách nhấp vào nút  *Ủy quyền*.

![image](administration/odoo_sh/getting_started/create/github-authorize.png)

Về cơ bản, Odoo.sh cần:

* biết thông tin đăng nhập và email Github của bạn,
* tạo một kho lưu trữ mới nếu bạn quyết định bắt đầu từ đầu,
* đọc các kho lưu trữ hiện có của bạn, bao gồm cả các kho lưu trữ trong tổ chức bạn, nếu bạn muốn bắt đầu từ kho lưu trữ hiện có,
* tạo webhook để nhận thông báo mỗi khi bạn thực hiện thay đổi,
* thực hiện các thay đổi nhằm giúp việc triển khai của bạn diễn ra dễ dàng hơn, chẳng hạn như hợp nhất các nhánh hoặc thêm [phân hệ phụ](https://git-scm.com/book/en/v2/Git-Tools-Submodules) mới.

## Gửi dự án của bạn

Chọn xem bạn muốn bắt đầu từ đầu bằng cách tạo kho lưu trữ mới hay bạn muốn sử dụng kho lưu trữ hiện có.

Sau đó, chọn tên hoặc chọn kho lưu trữ bạn muốn sử dụng.

Chọn phiên bản Odoo bạn muốn sử dụng. Nếu bạn dự định nhập cơ sở dữ liệu hiện có hoặc một bộ ứng dụng hiện có, bạn có thể cần chọn phiên bản tương ứng. Nếu bắt đầu từ đầu, hãy sử dụng phiên bản mới nhất.

Nhập *mã gói đăng ký* của bạn. Mã này còn được gọi là *mã giới thiệu đăng ký*, *số hợp đồng* hoặc *mã kích hoạt*.

Đó phải là mã gói đăng ký Enterprise của bạn bao gồm Odoo.sh.

Đối tác có thể sử dụng mã đối tác của họ để bắt đầu dùng thử. Nếu khách hàng của đối tác khởi động một dự án, họ phải có gói đăng ký Enterprise bao gồm Odoo.sh và sử dụng mã gói đăng ký đó. Đối tác sẽ nhận lại 50% số tiền dưới dạng hoa hồng. Vui lòng liên hệ với đại diện kinh doanh hoặc chuyên viên quản lý tài khoản để nhận khoản hoa hồng này.

Khi gửi biểu mẫu, nếu bạn được thông báo rằng gói đăng ký không hợp lệ, điều đó có nghĩa là:

* đó không phải là gói đăng ký đang tồn tại,
* đó không phải là gói đăng ký đối tác,
* đây là gói đăng ký Enterprise nhưng không bao gồm Odoo.sh,
* đó không phải là gói đăng ký đối tác hay đăng ký Enterprise (VD: đăng ký online).

Nếu chưa chắc chắn về gói đăng ký của bạn, vui lòng liên hệ với [bộ phận hỗ trợ Odoo](https://www.odoo.com/help).

![image](administration/odoo_sh/getting_started/create/deploy-form.png)

## Xong!

Bạn có thể bắt đầu sử dụng Odoo.sh và bản dựng đầu tiên của bạn sắp được tạo. Bạn sẽ sớm có thể kết nối với cơ sở dữ liệu đầu tiên của mình.

![image](administration/odoo_sh/getting_started/create/deploy-done.png)

<a id="odoo-sh-import-your-database"></a>

## Nhập cơ sở dữ liệu

Bạn có thể nhập cơ sở dữ liệu của mình vào dự án Odoo.sh nếu nó là [phiên bản được hỗ trợ](../../supported_versions.md) của Odoo.

### Đưa các phân hệ vào hoạt động thực tế

Nếu bạn sử dụng các phân hệ cộng đồng hoặc tùy chỉnh, hãy thêm chúng vào một nhánh trong kho lưu trữ Github của bạn. Cơ sở dữ liệu được lưu trữ trên nền tảng online Odoo.com không có bất kỳ phân hệ tùy chỉnh nào. Do đó, người dùng các cơ sở dữ liệu này có thể bỏ qua bước này.

Bạn có thể cơ cấu các phân hệ của mình theo ý muốn, Odoo.sh sẽ tự động phát hiện các thư mục chứa add-on của Odoo. Ví dụ: bạn có thể đặt tất cả thư mục phân hệ vào thư mục gốc của kho lưu trữ hoặc nhóm các phân hệ vào thư mục theo danh mục mà bạn xác định (kế toán, dự án,...).

Đối với các phân hệ Community có sẵn trong kho Git công khai, bạn cũng có thể cân nhắc thêm chúng bằng cách sử dụng [Phân hệ phụ](../advanced/submodules.md#odoosh-advanced-submodules).

Sau đó, [đặt nhánh này thành nhánh production](branches.md#odoosh-gettingstarted-branches-stages) hoặc [hợp nhất nó vào nhánh production của bạn](branches.md#odoosh-gettingstarted-branches-mergingbranches).

### Tải xuống bản sao lưu

#### Cơ sở dữ liệu on-premise

Truy cập URL `/web/database/manager` của cơ sở dữ liệu on-premise của bạn và tải xuống bản sao lưu.

#### WARNING
Nếu bạn không thể truy cập trình quản lý cơ sở dữ liệu thì có thể quản trị viên hệ thống đã vô hiệu hóa nó. Tham khảo [tài liệu bảo mật trình quản lý cơ sở dữ liệu](../../on_premise/deploy.md#db-manager-security).

Bạn sẽ cần mật khẩu chính của máy chủ cơ sở dữ liệu. Nếu không có, hãy liên hệ với quản trị viên hệ thống của bạn.

![image](administration/odoo_sh/getting_started/create/create-import-onpremise-backup.png)

Chọn zip bao gồm filestore làm định dạng sao lưu.

![image](administration/odoo_sh/getting_started/create/create-import-onpremise-backup-dialog.png)

#### Cơ sở dữ liệu Odoo Online

[Truy cập trình quản lý cơ sở dữ liệu của bạn](https://accounts.odoo.com/my/databases/manage) và tải xuống bản sao lưu cơ sở dữ liệu.

![image](administration/odoo_sh/getting_started/create/create-import-online-backup.png)

#### WARNING
Các phiên bản online (VD: *saas-\**) không được hỗ trợ trên Odoo.sh.

### Tải lên bản sao lưu

Sau đó, trong dự án Odoo.sh của bạn, hãy nhập bản sao lưu bạn vừa tải xuống vào tab sao lưu của nhánh production.

![image](administration/odoo_sh/getting_started/create/create-import-production.png)

Sau khi nhập bản sao lưu, bạn có thể truy cập cơ sở dữ liệu bằng nút *Kết nối* trong tab lịch sử của nhánh.

![image](administration/odoo_sh/getting_started/create/create-import-production-done.png)

### Kiểm tra máy chủ thư đi của bạn

Một máy chủ thư mặc định được cung cấp kèm Odoo.sh. Để sử dụng nó, không được bật máy chủ thư đi nào trong cơ sở dữ liệu của bạn tại Cài đặt ‣Kỹ thuật ‣ Máy chủ thư đi ([Chế độ lập trình viên](../../../applications/general/developer_mode.md#developer-mode) phải được kích hoạt).

Sau khi nhập cơ sở dữ liệu của bạn, tất cả máy chủ thư đi đều bị tắt nên bạn sử dụng máy chủ thư Odoo.sh được cung cấp theo mặc định.

#### WARNING
Cổng 25 đã (và sẽ luôn) bị đóng. Nếu bạn muốn kết nối với máy chủ SMTP bên ngoài, bạn nên sử dụng cổng 465 và 587.

### Kiểm tra các tác vụ đã lên lịch của bạn

Tất cả tác vụ đã lên lịch sẽ bị vô hiệu hóa sau khi nhập.

Điều này nhằm ngăn cơ sở dữ liệu mới nhập thực hiện các tác vụ có thể ảnh hưởng đến production đang diễn ra của bạn, chẳng hạn như gửi thư còn nằm trong danh sách chờ, xử lý thư hàng loạt hoặc đồng bộ hóa dịch vụ của bên thứ ba (Lịch, lưu trữ tệp,...).

Nếu bạn định dùng cơ sở dữ liệu đã nhập trong production, hãy bật lại các tác vụ đã lên lịch mà bạn cần. Bạn có thể kiểm tra những tác vụ được bật trong cơ sở dữ liệu gốc và bật lại tác vụ tương tự trong cơ sở dữ liệu đã nhập. Tác vụ đã lên lịch nằm trong Cài đặt ‣ Kỹ thuật ‣ Tự động hoá ‣ Tác vụ đã lên lịch.

### Nhập gói đăng ký của bạn

Gói đăng ký của bạn bị hủy liên kết sau khi nhập.

Theo mặc định, cơ sở dữ liệu đã nhập được coi là một bản sao và do đó gói đăng ký Enterprise sẽ bị xóa, vì mỗi gói đăng ký chỉ có thể được liên kết với một cơ sở dữ liệu.

Nếu bạn định dùng cơ sở dữ liệu mới được nhập trong production, hãy hủy liên kết cơ sở dữ liệu cũ khỏi gói đăng ký và đăng ký cơ sở dữ liệu mới. Đọc [tài liệu đăng ký cơ sở dữ liệu](../../on_premise.md) để xem hướng dẫn.
