# Lưu trữ

<a id="hosting-change-solution"></a>

## Thay đổi giải pháp lưu trữ

Hướng dẫn thay đổi loại hình lưu trữ cơ sở dữ liệu phụ thuộc vào giải pháp hiện đang được sử dụng và giải pháp sẽ được chuyển sang.

## Chuyển cơ sở dữ liệu on-premise

### Sang Odoo Online

#### IMPORTANT
- Odoo Online *không* tương thích với **ứng dụng ngoại chuẩn**.
- Phiên bản hiện tại của cơ sở dữ liệu phải [được hỗ trợ](supported_versions.md).

1. Tạo một [bản sao của cơ sở dữ liệu](on_premise.md#on-premise-duplicate).
2. Trong bản sao này, gỡ cài đặt tất cả **ứng dụng ngoại chuẩn**.
3. Sử dụng trình quản lý cơ sở dữ liệu để lấy *bản kết xuất với filestore*.
4. [Gửi một phiếu hỗ trợ](https://www.odoo.com/help) gồm thông tin sau:
   - **số gói đăng ký** của bạn,
   - **URL** bạn muốn sử dụng cho cơ sở dữ liệu (VD: `company.odoo.com`), và
   - **bản kết xuất** dưới dạng tệp đính kèm hoặc dưới dạng liên kết tới tệp (bắt buộc đối với tệp lớn hơn 60 MB).
5. Sau đó, Odoo sẽ đảm bảo cơ sở dữ liệu tương thích trước khi chuyển sang online. Trong trường hợp có vấn đề kỹ thuật trong quá trình này, Odoo có thể liên hệ với bạn.

#### NOTE
Nếu bạn gặp khó khăn về thời gian, [hãy gửi phiếu hỗ trợ](https://www.odoo.com/help) để lên lịch chuyển đổi càng sớm càng tốt.

### Sang Odoo.sh

Làm theo hướng dẫn trong [phần Nhập cơ sở dữ liệu của bạn](odoo_sh/getting_started/create.md#odoo-sh-import-your-database) của tài liệu Odoo.sh *Tạo dự án của bạn*.

## Chuyển cơ sở dữ liệu Odoo Online

#### IMPORTANT
[Phiên bản trung gian](supported_versions.md#supported-versions) của Odoo Online không được Odoo.sh hoặc on-premise hỗ trợ. Do đó, nếu cơ sở dữ liệu cần chuyển đang chạy phiên bản trung gian, trước tiên nó phải được nâng cấp lên [phiên bản chính](supported_versions.md#supported-versions) kế tiếp, hoặc chờ phát hành nếu cần.

#### WARNING
Nếu có gói đăng ký Odoo đang hoạt động liên kết với cơ sở dữ liệu đang được di chuyển, hãy liên hệ với Quản lý dịch vụ khách hàng hoặc [gửi phiếu hỗ trợ](https://www.odoo.com/help) để hoàn tất quá trình chuyển gói đăng ký.

### Sang on-premise

1. Đăng nhập vào [trình quản lý cơ sở dữ liệu Odoo Online](https://www.odoo.com/my/databases/) và nhấp vào biểu tượng bánh răng (⚙) bên cạnh tên cơ sở dữ liệu để Tải xuống một bản sao lưu. Nếu quá trình tải xuống không thành công do tệp quá lớn, [hãy liên hệ với bộ phận hỗ trợ của Odoo](https://www.odoo.com/help).
2. Khôi phục cơ sở dữ liệu từ trình quản lý cơ sở dữ liệu trên máy chủ cục bộ của bạn bằng bản sao lưu.

### Sang Odoo.sh

1. Đăng nhập vào [trình quản lý cơ sở dữ liệu Odoo Online](https://www.odoo.com/my/databases/) và nhấp vào biểu tượng bánh răng (⚙) bên cạnh tên cơ sở dữ liệu để Tải xuống một bản sao lưu. Nếu quá trình tải xuống không thành công do tệp quá lớn, [hãy liên hệ với bộ phận hỗ trợ của Odoo](https://www.odoo.com/help).
2. Làm theo hướng dẫn trong [phần Nhập cơ sở dữ liệu của bạn](odoo_sh/getting_started/create.md#odoo-sh-import-your-database) của tài liệu Odoo.sh *Tạo dự án của bạn*.

## Chuyển cơ sở dữ liệu Odoo.sh

### Sang Odoo Online

#### IMPORTANT
Odoo Online *không* tương thích với **ứng dụng ngoại chuẩn**.

1. Gỡ cài đặt tất cả **ứng dụng ngoại chuẩn** trong bản dựng staging trước khi tiến hành trên phiên bản production.
2. [Tạo một phiếu hỗ trợ](https://www.odoo.com/help) gồm thông tin sau:
   - **số gói đăng ký** của bạn,
   - **URL** bạn muốn sử dụng cho cơ sở dữ liệu (VD: `company.odoo.com`),
   - **nhánh** nào sẽ được di chuyển,
   - bạn muốn lưu trữ cơ sở dữ liệu ở **khu vực** nào (Châu Mỹ, Châu Âu hoặc Châu Á),
   - (những) người dùng nào sẽ là **quản trị viên**, và
   - **thời gian** (và múi giờ) bạn muốn cơ sở dữ liệu được thiết lập và chạy.
3. Sau đó, Odoo sẽ đảm bảo cơ sở dữ liệu tương thích trước khi chuyển sang online. Trong trường hợp có vấn đề kỹ thuật trong quá trình này, Odoo có thể liên hệ với bạn.

#### NOTE
- Nếu bạn gặp khó khăn về thời gian, [hãy gửi phiếu hỗ trợ](https://www.odoo.com/help) để lên lịch chuyển đổi càng sớm càng tốt.
- Chọn **khu vực** gần với hầu hết người dùng của bạn nhất để giảm độ trễ.
- **(Các) quản trị viên** tương lai phải có tài khoản Odoo.com.
- **Ngày và giờ** bạn muốn cơ sở dữ liệu được thiết lập và chạy là thông tin hữu ích trong việc tiến hành chuyển đổi từ máy chủ Odoo.sh sang máy chủ Odoo Online.
- **Không thể truy cập** cơ sở dữ liệu trong quá trình di chuyển.

### Sang on-premise

1. Tải xuống [bản sao lưu cơ sở dữ liệu production Odoo.sh của bạn](odoo_sh/getting_started/branches.md#odoo-sh-branches-backups).
2. Khôi phục cơ sở dữ liệu từ trình quản lý cơ sở dữ liệu trên máy chủ cục bộ của bạn bằng bản sao lưu.
