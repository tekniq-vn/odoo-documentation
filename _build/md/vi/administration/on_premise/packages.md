# Trình cài đặt trọn gói

Odoo cung cấp trình cài đặt trọn gói cho các bản phân phối Linux dựa trên Debian (Debian, Ubuntu,...), các bản phân phối Linux dựa trên RPM (Fedora, CentOS, RHEL,...) và Windows cho phiên bản Community và Enterprise.

Các gói ban đêm **Community** chính thức với tất cả yêu cầu phụ thuộc liên quan đều có sẵn trên [máy chủ ban đêm](https://nightly.odoo.com).

#### NOTE
Có thể khó cập nhật liên tục các gói ban đêm.

Bạn có thể tải xuống các gói **Community** và **Enterprise** chính thức từ [trang Tải xuống của Odoo](https://www.odoo.com/page/download).

#### NOTE
Bạn phải đăng nhập với tư cách là khách hàng hoặc đối tác trả phí on-premise để tải xuống các gói Enterprise.

<a id="install-packages-linux"></a>

## Linux

### Chuẩn bị

Odoo cần một máy chủ [PostgreSQL](https://www.postgresql.org/) để có thể hoạt động bình thường.

Debian/Ubuntu

Cấu hình mặc định cho gói Odoo 'deb' là sử dụng máy chủ PostgreSQL trên cùng một hệ thống lưu trữ với phiên bản Odoo. Thực hiện lệnh sau để cài đặt máy chủ PostgreSQL:

```console
$ sudo apt install postgresql -y
```

Fedora

Hãy đảm bảo lệnh `sudo` đã có sẵn và được cấu hình đúng, sau đó mới thực hiện lệnh sau để cài đặt máy chủ PostgreSQL:

```console
$ sudo dnf install -y postgresql-server
$ sudo postgresql-setup --initdb --unit postgresql
$ sudo systemctl enable postgresql
$ sudo systemctl start postgresql
```

#### WARNING
`wkhtmltopdf` không được cài đặt thông qua **pip** và phải được cài đặt thủ công trong [phiên bản 0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) để hỗ trợ header và footer. Tham khảo [wiki wkhtmltopdf](https://github.com/odoo/odoo/wiki/Wkhtmltopdf) để biết thêm chi tiết về các phiên bản khác nhau.

### Kho lưu trữ

Odoo S.A. cung cấp kho lưu trữ có thể được sử dụng để cài đặt phiên bản **Community** bằng cách thực hiện các lệnh sau:

Debian/Ubuntu

```console
$ wget -q -O - https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg
$ echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/17.0/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list
$ sudo apt-get update && sudo apt-get install odoo
```

Sử dụng lệnh `apt-get upgrade` thông thường để duy trì cập nhật cài đặt.

Fedora

```console
$ sudo dnf config-manager --add-repo=https://nightly.odoo.com/17.0/nightly/rpm/odoo.repo
$ sudo dnf install -y odoo
$ sudo systemctl enable odoo
$ sudo systemctl start odoo
```

#### NOTE
Hiện tại, không có kho lưu trữ ban đêm cho phiên bản Enterprise.

### Gói phân phối

Thay vì sử dụng kho lưu trữ, các gói cho cả phiên bản **Community** và **Enterprise** đều có thể được tải xuống từ [trang Tải xuống của Odoo](https://www.odoo.com/page/download).

Debian/Ubuntu

#### NOTE
Gói 'deb' của Odoo 17 hiện hỗ trợ các phiên bản [Debian Buster](https://www.debian.org/releases/buster/) và [Ubuntu 18.04](https://releases.ubuntu.com/18.04) trở lên.

Sau khi tải xuống, hãy thực hiện các lệnh sau **làm root** để cài đặt Odoo dưới dạng dịch vụ, tạo người dùng PostgreSQL cần thiết và tự động khởi động máy chủ:

```console
# dpkg -i <path_to_installation_package> # this probably fails with missing dependencies
# apt-get install -f # should install the missing dependencies
# dpkg -i <path_to_installation_package>
```

#### WARNING
- Gói Debian `python3-xlwt`, cần xuất sang định dạng XLS, không tồn tại trong Debian Buster hoặc Ubuntu 18.04. Nếu cần, hãy cài đặt thủ công bằng lệnh sau:
  ```console
  $ sudo pip3 install xlwt
  ```
- Gói Python `num2words` - cần thiết để hiển thị số lượng văn bản - không tồn tại trong Debian Buster cũng như Ubuntu 18.04, điều này có thể gây ra sự cố với phân hệ `l10n_mx_edi`. Nếu cần, hãy cài đặt thủ công bằng lệnh sau:
  ```console
  $ sudo pip3 install num2words
  ```

Fedora

#### NOTE
Odoo 17 'rpm' package supports Fedora 38.

Sau khi tải xuống, bạn có thể cài đặt gói này bằng trình quản lý gói 'dnf':

```console
$ sudo dnf localinstall odoo_17.0.latest.noarch.rpm
$ sudo systemctl enable odoo
$ sudo systemctl start odoo
```

<a id="install-packages-windows"></a>

## Windows

> #### WARNING
> Gói Windows được cung cấp để thuận tiện cho việc kiểm thử hoặc chạy các phiên bản cục bộ một người dùng nhưng không khuyến khích triển khai trong production do một số hạn chế và rủi ro liên quan đến việc triển khai Odoo trên nền tảng Windows.
1. Tải xuống trình cài đặt từ [máy chủ ban đêm](https://nightly.odoo.com) (Chỉ dành cho Community) hoặc trình cài đặt Windows từ [trang tải xuống Odoo](https://www.odoo.com/page/download) (bất kỳ phiên bản nào).
2. Chạy tệp đã tải xuống.

   #### WARNING
   Trên Windows 8 trở lên, cảnh báo có tiêu đề *Windows đã bảo vệ PC của bạn* có thể hiển thị. Nhấp vào **Thêm thông tin** rồi **Vẫn chạy** để tiếp tục.
3. Chấp nhận nhắc nhở [UAC](https://en.wikipedia.org/wiki/User_Account_Control).
4. Thực hiện các bước cài đặt.

Odoo khởi chạy tự động sau khi cài đặt.
