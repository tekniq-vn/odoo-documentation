# Quản lý cơ sở dữ liệu

Các bản hướng dẫn này cung cấp chỉ dẫn về cách cài đặt, bảo trì và nâng cấp cơ sở dữ liệu Odoo.

#### SEE ALSO
[Lịch sử Phiên bản](supported_versions.md)

## Cài đặt

Tùy thuộc vào từng trường hợp sử dụng, có nhiều cách để cài đặt Odoo - hoặc không cài đặt gì cả.

- [Online](odoo_online.md) là cách dễ dàng nhất để sử dụng Odoo trong production hoặc để dùng thử Odoo.
- [Trình cài đặt trọn gói](on_premise/packages.md) phù hợp để kiểm thử Odoo và phát triển các phân hệ. Chúng có thể được sử dụng cho production lâu dài với triển khai và bảo trì bổ sung.
- [Cài đặt nguồn](on_premise/source.md) cung cấp tính linh hoạt cao hơn, ví dụ như nó cho phép chạy nhiều phiên bản Odoo trên cùng một hệ thống. Cài đặt này là đủ để phát triển các phân hệ và có thể được sử dụng làm cơ sở để triển khai production.
- Hình ảnh cơ sở [Docker](https://hub.docker.com/_/odoo/) khả dụng cho phát triển hoặc triển khai.

<a id="install-editions"></a>

## Các phiên bản

Có hai phiên bản khác nhau.

**Odoo Community** là phiên bản phần mềm miễn phí và có mã nguồn mở, được cấp phép theo [GNU LGPLv3](https://github.com/odoo/odoo/blob/master/LICENSE). Đây là cốt lõi để tạo dựng Odoo Enterprise.

**Odoo Enterprise** là phiên bản nguồn chia sẻ của phần mềm, cho phép truy cập vào nhiều chức năng hơn, bao gồm hỗ trợ chức năng, nâng cấp và lưu trữ. [Các gói giá](https://www.odoo.com/pricing-plan) bắt đầu từ một ứng dụng miễn phí.

* [Lưu trữ](hosting.md)
* [Odoo Online](odoo_online.md)
* [Odoo.sh](odoo_sh/)
  * [Tổng quan](odoo_sh/overview/)
    * [Giới thiệu về Odoo.sh](odoo_sh/overview/introduction.md)
  * [Bắt đầu](odoo_sh/getting_started/)
    * [Tạo dự án của bạn](odoo_sh/getting_started/create.md)
    * [Nhánh](odoo_sh/getting_started/branches.md)
    * [Bản dựng](odoo_sh/getting_started/builds.md)
    * [Trạng thái](odoo_sh/getting_started/status.md)
    * [Cài đặt](odoo_sh/getting_started/settings.md)
    * [Trình soạn thảo online](odoo_sh/getting_started/online-editor.md)
    * [Phân hệ đầu tiên của bạn](odoo_sh/getting_started/first_module.md)
  * [Nâng cao](odoo_sh/advanced/)
    * [Container](odoo_sh/advanced/containers.md)
    * [Phân hệ phụ](odoo_sh/advanced/submodules.md)
    * [Câu hỏi về Kỹ thuật Thường gặp](odoo_sh/advanced/frequent_technical_questions.md)
* [On-premise](on_premise/)
  * [Trình cài đặt trọn gói](on_premise/packages.md)
  * [Cài đặt nguồn](on_premise/source.md)
  * [Cập nhật gỡ lỗi](on_premise/update.md)
  * [Cấu hình hệ thống](on_premise/deploy.md)
  * [Cổng email](on_premise/email_gateway.md)
  * [Geo IP](on_premise/geo_ip.md)
  * [Chuyển từ Community sang Enterprise](on_premise/community_to_enterprise.md)
* [Nâng cấp](upgrade.md)
* [Cơ sở dữ liệu bị vô hiệu hoá một phần](neutralized_database.md)
* [Phiên bản được hỗ trợ](supported_versions.md)
* [Ứng dụng Odoo trên thiết bị di động](mobile.md)
* [Tài khoản Odoo.com](odoo_accounts.md)
