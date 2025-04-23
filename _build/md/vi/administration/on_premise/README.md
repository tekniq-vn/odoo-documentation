# On-premise

## Đăng ký cơ sở dữ liệu

Để đăng ký cơ sở dữ liệu của bạn, hãy nhập mã đăng ký vào banner trong trang chủ ứng dụng. Nếu đăng ký thành công, banner sẽ chuyển sang màu xanh lá cây và hiển thị ngày hết hạn của cơ sở dữ liệu.

<a id="on-premise-duplicate"></a>

## Sao chép cơ sở dữ liệu

Sao chép cơ sở dữ liệu bằng cách truy cập trình quản lý cơ sở dữ liệu trên máy chủ của bạn (`<odoo-server>/web/database/manager`). Thông thường, bạn nên sao chép cơ sở dữ liệu production thành cơ sở dữ liệu kiểm thử bị vô hiệu hóa một phần. Bạn có thể thực hiện bằng cách chọn ô vô hiệu hóa một phần khi được nhắc, điều này sẽ thực thi tất cả các tập lệnh `neutralize.sql` cho mọi phân hệ đã cài đặt.

## Các thông báo lỗi thường gặp và giải pháp

### Lỗi đăng ký

Trong trường hợp xảy ra lỗi đăng ký, thông báo sau sẽ hiển thị.

![Thông báo lỗi đăng ký cơ sở dữ liệu](../.gitbook/assets/error-message-sub-code.png)

Để xử lý vấn đề:

- Kiểm tra **tính hợp lệ của gói đăng ký Odoo Enterprise** của bạn bằng cách xác minh xem thông tin đăng ký của bạn có thẻ Đang hoạt động trên [Tài khoản Odoo](https://accounts.odoo.com/my/subscription) hay không hoặc liên hệ với Chuyên viên Quản lý Tài khoản của bạn.
- Đảm bảo rằng **không có cơ sở dữ liệu nào khác được liên kết** với mã đăng ký, vì mỗi gói đăng ký chỉ có thể liên kết với một cơ sở dữ liệu.
- Xác minh rằng **không có cơ sở dữ liệu nào dùng cùng một UUID** (Mã định danh duy nhất) bằng cách mở [Odoo Hợp đồng](https://accounts.odoo.com/my/subscription). Nếu hai hoặc nhiều cơ sở dữ liệu đang dùng cùng một UUID, tên của chúng sẽ được hiển thị.
  ![Thông báo lỗi UUID cơ sở dữ liệu](../.gitbook/assets/unlink-db-name-collision.png)

  Nếu đúng như vậy, hãy thay đổi UUID của (các) cơ sở dữ liệu theo cách thủ công hoặc [gửi phiếu hỗ trợ](https://www.odoo.com/help).
- Vì thông báo cập nhật phải có thể đến được máy chủ xác thực đăng ký của Odoo, hãy đảm bảo **cài đặt mạng và tường lửa** của bạn cho phép máy chủ Odoo mở các kết nối đi tới:
  - Odoo 18.0 trở lên: `services.odoo.com` trên cổng `80`
  - Odoo 17.0 trở về: `services.odoo.com` trên cổng `80`

  Các cổng này phải được để mở ngay cả sau khi đăng ký cơ sở dữ liệu thành công, vì thông báo cập nhật sẽ chạy mỗi tuần một lần.

### Lỗi quá nhiều người dùng

Nếu bạn có nhiều người dùng trong cơ sở dữ liệu cục bộ hơn số lượng được cung cấp trong gói đăng ký Odoo Enterprise, thông báo sau sẽ hiển thị.

![Thông báo lỗi quá nhiều người dùng trên một cơ sở dữ liệu](../.gitbook/assets/add-more-users.png)

Khi thông báo này xuất hiện, bạn có 30 ngày để hành động trước khi cơ sở dữ liệu hết hạn. Số ngày đếm ngược sẽ được cập nhật mỗi ngày.

Để xử lý vấn đề:

- **Thêm người dùng** vào gói đăng ký của bạn bằng cách nhấp vào liên kết Nâng cấp gói đăng ký hiển thị trong thông báo để xác thực báo giá bán thêm và thanh toán cho số lượng người dùng bổ sung.
- [Huỷ kích hoạt người dùng](../applications/general/users.md#users-deactivate) và **từ chối** báo giá bán thêm.

Khi cơ sở dữ liệu của bạn có đúng số lượng người dùng, thông báo hết hạn sẽ tự động biến mất sau vài ngày khi xác minh tiếp theo diễn ra.

### Lỗi cơ sở dữ liệu hết hạn

Nếu cơ sở dữ liệu hết hạn trước khi bạn gia hạn gói đăng ký, thông báo sau sẽ hiển thị.

![Thông báo lỗi cơ sở dữ liệu hết hạn](../.gitbook/assets/database-expired.png)

Thông báo này sẽ xuất hiện nếu bạn không hành động trước khi thời gian đếm ngược 30 ngày kết thúc.

Để xử lý vấn đề:

- Nhấp vào liên kết Gia hạn gói đăng ký hiển thị trong thông báo và hoàn tất quy trình. Nếu bạn thanh toán bằng chuyển khoản, gói đăng ký của bạn sẽ được gia hạn khi khoản thanh toán được nhận, có thể mất vài ngày. Thanh toán bằng thẻ tín dụng sẽ được xử lý ngay lập tức.
- [Gửi phiếu hỗ trợ qua](https://www.odoo.com/help).

* [Trình cài đặt trọn gói](on_premise/packages.md)
  * [Linux](on_premise/packages.md#linux)
    * [Chuẩn bị](on_premise/packages.md#prepare)
    * [Kho lưu trữ](on_premise/packages.md#repository)
    * [Gói phân phối](on_premise/packages.md#distribution-package)
  * [Windows](on_premise/packages.md#windows)
* [Cài đặt nguồn](on_premise/source.md)
  * [Lấy nguồn](on_premise/source.md#fetch-the-sources)
    * [Lưu trữ](on_premise/source.md#archive)
    * [Git](on_premise/source.md#git)
  * [Chuẩn bị](on_premise/source.md#prepare)
    * [Python](on_premise/source.md#python)
    * [PostgreSQL](on_premise/source.md#postgresql)
    * [Phần phụ thuộc](on_premise/source.md#dependencies)
  * [Chạy Odoo](on_premise/source.md#running-odoo)
* [Cập nhật gỡ lỗi](on_premise/update.md)
  * [Giới thiệu](on_premise/update.md#introduction)
  * [Tóm tắt](on_premise/update.md#in-a-nutshell)
  * [Bước 1: Tải xuống phiên bản Odoo đã cập nhật](on_premise/update.md#step-1-download-an-updated-odoo-version)
  * [Bước 2: Sao lưu cơ sở dữ liệu của bạn](on_premise/update.md#step-2-make-a-backup-of-your-database)
  * [Bước 3: Cài đặt bản cập nhật](on_premise/update.md#step-3-install-the-updated-version)
    * [Trình cài đặt trọn gói](on_premise/update.md#packaged-installers)
    * [Cài đặt nguồn (Tarball)](on_premise/update.md#source-install-tarball)
    * [Cài đặt nguồn (Github)](on_premise/update.md#source-install-github)
    * [Docker](on_premise/update.md#docker)
* [Cấu hình hệ thống](on_premise/deploy.md)
  * [dbfilter](on_premise/deploy.md#dbfilter)
    * [Cấu hình mẫu](on_premise/deploy.md#configuration-samples)
  * [PostgreSQL](on_premise/deploy.md#postgresql)
    * [Cấu hình mẫu](on_premise/deploy.md#configuration-sample)
    * [Cấu hình Odoo](on_premise/deploy.md#configuring-odoo)
      * [Cấu hình mẫu](on_premise/deploy.md#id4)
    * [SSL giữa Odoo và PostgreSQL](on_premise/deploy.md#ssl-between-odoo-and-postgresql)
  * [Máy chủ tích hợp](on_premise/deploy.md#builtin-server)
    * [Tính toán số lượng worker](on_premise/deploy.md#worker-number-calculation)
    * [tính toán kích thước bộ nhớ](on_premise/deploy.md#memory-size-calculation)
    * [LiveChat](on_premise/deploy.md#livechat)
    * [Cấu hình mẫu](on_premise/deploy.md#id6)
  * [HTTPS](on_premise/deploy.md#https)
    * [Cấu hình mẫu](on_premise/deploy.md#id8)
    * [Nâng cao bảo mật HTTPS](on_premise/deploy.md#https-hardening)
  * [Odoo dưới dạng Ứng dụng WSGI](on_premise/deploy.md#odoo-as-a-wsgi-application)
    * [Cron Worker](on_premise/deploy.md#cron-workers)
    * [LiveChat](on_premise/deploy.md#id9)
  * [Phục vụ tệp tĩnh và tệp đính kèm](on_premise/deploy.md#serving-static-files-and-attachments)
    * [Phục vụ tệp tĩnh](on_premise/deploy.md#serving-static-files)
    * [Phục vụ tệp đính kèm](on_premise/deploy.md#serving-attachments)
  * [Bảo mật](on_premise/deploy.md#security)
    * [Chặn các Cuộc Tấn công Brute Force](on_premise/deploy.md#blocking-brute-force-attacks)
    * [Bảo mật Trình Quản lý Cơ sở Dữ liệu](on_premise/deploy.md#database-manager-security)
    * [Đặt lại Mật khẩu Chính](on_premise/deploy.md#reset-the-master-password)
      * [Xác định vị trí tệp cấu hình](on_premise/deploy.md#locate-configuration-file)
      * [Thay đổi mật khẩu cũ](on_premise/deploy.md#change-old-password)
      * [Khởi động lại máy chủ Odoo](on_premise/deploy.md#restart-odoo-server)
      * [Sử dụng giao diện web để mã hóa lại mật khẩu](on_premise/deploy.md#use-web-interface-to-re-encrypt-password)
  * [Các trình duyệt được hỗ trợ](on_premise/deploy.md#supported-browsers)
* [Cổng email](on_premise/email_gateway.md)
  * [Điều kiện tiên quyết](on_premise/email_gateway.md#prerequisites)
  * [Đối với Postfix](on_premise/email_gateway.md#for-postfix)
  * [Đối với Exim](on_premise/email_gateway.md#for-exim)
* [Geo IP](on_premise/geo_ip.md)
  * [Cài đặt](on_premise/geo_ip.md#installation)
  * [Kiểm tra vị trí địa lý GeoIP trong trang web Odoo của bạn](on_premise/geo_ip.md#test-geoip-geolocation-in-your-odoo-website)
* [Chuyển từ Community sang Enterprise](on_premise/community_to_enterprise.md)
  * [Trên Linux, sử dụng trình cài đặt](on_premise/community_to_enterprise.md#on-linux-using-an-installer)
  * [Trên Linux, sử dụng mã nguồn](on_premise/community_to_enterprise.md#on-linux-using-the-source-code)
  * [Trên Windows](on_premise/community_to_enterprise.md#on-windows)
