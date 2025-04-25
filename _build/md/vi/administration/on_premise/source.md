# Cài đặt nguồn

'Cài đặt' nguồn không phải là cài đặt Odoo mà là chạy Odoo trực tiếp từ nguồn.

Việc sử dụng nguồn Odoo có thể thuận tiện hơn cho các lập trình viên phân hệ vì nó dễ truy cập hơn so với việc sử dụng trình cài đặt trọn gói.

Việc khởi động và dừng Odoo trở nên linh hoạt và rõ ràng hơn so với các dịch vụ được thiết lập bởi trình cài đặt trọn gói. Ngoài ra, nó cho phép ghi đè cài đặt bằng cách sử dụng [tham số dòng lệnh](../../developer/reference/cli.md#reference-cmdline) mà không cần chỉnh sửa tệp cấu hình.

Cuối cùng là nó nâng cao khả năng kiểm soát đối với thiết lập hệ thống và cho phép dễ dàng duy trì (và chạy) nhiều phiên bản Odoo song song.

## Lấy nguồn

Có hai cách để lấy mã nguồn của Odoo: dưới dạng **lưu trữ** ZIP hoặc thông qua **Git**.

### Lưu trữ

Phiên bản Community:

- [Trang Tải xuống của Odoo](https://www.odoo.com/page/download)
- [Kho lưu trữ GitHub Community](https://github.com/odoo/odoo)
- [Máy chủ ban đêm](https://nightly.odoo.com)

Phiên bản Enterprise:

- [Trang Tải xuống của Odoo](https://www.odoo.com/page/download)
- [Kho lưu trữ GitHub Enterprise](https://github.com/odoo/enterprise)

<a id="install-source-git"></a>

### Git

#### NOTE
Bạn cần phải cài đặt [Git](https://git-scm.com/) và nên có kiến ​​thức cơ bản về các lệnh Git để có thể tiếp tục.

Để sao chép kho lưu trữ Git, hãy chọn một trong hai cách sao chép bằng HTTPS hoặc SSH. Trong hầu hết trường hợp, tùy chọn tốt nhất là HTTPS. Tuy nhiên, hãy chọn SSH nếu bạn muốn đóng góp vào mã nguồn Odoo hoặc khi làm theo [Hướng dẫn bắt ​​đầu dành cho lập trình viên](../../developer/tutorials/server_framework_101/).

Linux

Sao chép với HTTPS

```console
$ git clone https://github.com/odoo/odoo.git
$ git clone https://github.com/odoo/enterprise.git
```

Sao chép với SSH

```console
$ git clone git@github.com:odoo/odoo.git
$ git clone git@github.com:odoo/enterprise.git
```

Windows

Sao chép với HTTPS

```doscon
C:\> git clone https://github.com/odoo/odoo.git
C:\> git clone https://github.com/odoo/enterprise.git
```

Sao chép với SSH

```doscon
C:\> git clone git@github.com:odoo/odoo.git
C:\> git clone git@github.com:odoo/enterprise.git
```

Mac OS

Sao chép với HTTPS

```console
$ git clone https://github.com/odoo/odoo.git
$ git clone https://github.com/odoo/enterprise.git
```

Sao chép với SSH

```console
$ git clone git@github.com:odoo/odoo.git
$ git clone git@github.com:odoo/enterprise.git
```

#### NOTE
**Kho lưu trữ git Enterprise không chứa mã nguồn Odoo đầy đủ**. Nó chỉ là một tập hợp các add-on bổ sung. Mã máy chủ chính nằm trong phiên bản Community. Chạy phiên bản Enterprise có nghĩa là chạy máy chủ từ phiên bản Community với tùy chọn `addons-path` được thiết lập cho phiên bản Enterprise trong một thư mục cụ thể. Cần phải sao chép cả kho lưu trữ Community và Enterprise để bản cài đặt Odoo Enterprise hoạt động.

<a id="install-source-prepare"></a>

## Chuẩn bị

### Python

Odoo yêu cầu **Python 3.10** trở lên để có thể hoạt động.

#### Versionchanged
Thay đổi trong phiên bản 17: Yêu cầu tối thiểu được cập nhật từ Python 3.7 lên Python 3.10.

Linux

Sử dụng trình quản lý gói để tải xuống và cài đặt Python 3 nếu cần.

Windows

[Tải xuống phiên bản mới nhất của Python 3](https://www.python.org/downloads/windows/) và cài đặt.

Trong quá trình cài đặt, hãy kiểm tra **Thêm Python 3 vào PATH**, sau đó nhấp vào **Tùy chỉnh cài đặt** và đảm bảo rằng **pip** đã được chọn.

Mac OS

Sử dụng trình quản lý gói ([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org)) để tải xuống và cài đặt Python 3 nếu cần.

#### NOTE
Nếu Python 3 đã được cài đặt, hãy đảm bảo đó là phiên bản 3.10 trở lên vì các phiên bản trước đó không tương thích với Odoo.

Linux

```console
$ python3 --version
```

Windows

```doscon
C:\> python --version
```

Mac OS

```console
$ python3 --version
```

Hãy xác nhận [pip](https://pip.pypa.io) cũng được cài đặt cho phiên bản này.

Linux

```console
$ pip3 --version
```

Windows

```doscon
C:\> pip --version
```

Mac OS

```console
$ pip3 --version
```

### PostgreSQL

Odoo sử dụng PostgreSQL làm hệ thống quản lý cơ sở dữ liệu.

Linux

Sử dụng trình quản lý gói để tải xuống và cài đặt PostgreSQL (phiên bản được hỗ trợ: 12.0 trở lên). Bạn có thể tiến hành bằng cách thực hiện lệnh sau:

```console
$ sudo apt install postgresql postgresql-client
```

Windows

[Tải xuống PostgreSQL](https://www.postgresql.org/download/windows) (phiên bản được hỗ trợ: 12.0 trở lên) và cài đặt.

Mac OS

Sử dụng [Postgres.app](https://postgresapp.com) để tải xuống và cài đặt PostgreSQL (phiên bản được hỗ trợ: 12.0 trở lên).

Theo mặc định, người dùng duy nhất là `postgres`. Vì Odoo cấm kết nối dưới dạng `postgres`, hãy tạo một người dùng PostgreSQL mới.

Linux

```console
$ sudo -u postgres createuser -d -R -S $USER
$ createdb $USER
```

#### NOTE
Vì người dùng PostgreSQL có cùng tên với tên đăng nhập Unix nên có thể kết nối với cơ sở dữ liệu mà không cần mật khẩu.

Windows

1. Thêm thư mục `bin` của PostgreSQL (theo mặc định: `C:\Program Files\PostgreSQL\<version>\bin`) vào `PATH`.
2. Tạo người dùng postgres có mật khẩu bằng giao diện người dùng đồ hoạ pg admin:
   1. Mở **pgAdmin**.
   2. Nhấp đúp vào máy chủ để tạo kết nối.
   3. Chọn Đối tượng ‣ Tạo ‣ Đăng nhập/Vai trò nhóm.
   4. Nhập tên người dùng vào trường **Tên vai trò** (ví dụ: `odoo`).
   5. Mở tab **Định nghĩa**, nhập mật khẩu (ví dụ: `odoo`) và nhấp vào **Lưu**.
   6. Mở tab **Quyền hạn** và chuyển **Có thể đăng nhập không?** thành `Có` và **Có tạo cơ sở dữ liệu không?** thành `Có`.

Mac OS

```console
$ sudo -u postgres createuser -d -R -S $USER
$ createdb $USER
```

#### NOTE
Vì người dùng PostgreSQL có cùng tên với tên đăng nhập Unix nên có thể kết nối với cơ sở dữ liệu mà không cần mật khẩu.

<a id="install-dependencies"></a>

### Phần phụ thuộc

Linux

Việc sử dụng **gói phân phối** là cách cài đặt phụ thuộc được ưu tiên. Ngoài ra, hãy cài đặt các phụ thuộc Python bằng **pip**.

Debian/Ubuntu

Trên Debian/Ubuntu, các lệnh sau sẽ cài đặt các gói cần thiết:

```console
$ cd odoo #CommunityPath
$ sudo ./setup/debinstall.sh
```

Tập lệnh `setup/debinstall.sh` sẽ phân tích tệp [debian/control](https://github.com/odoo/odoo/blob/17.0/debian/control) và cài đặt các gói được tìm thấy.

Cài đặt với pip

#### WARNING
Việc sử dụng pip có thể dẫn đến các vấn đề bảo mật và làm hỏng phụ thuộc; chỉ thực hiện việc này nếu bạn nắm rõ quy trình.

Vì một số gói Python cần bước biên dịch, nên chúng yêu cầu phải cài đặt thư viện hệ thống.

Trên Debian/Ubuntu, các lệnh sau sẽ cài đặt các thư viện cần thiết:

```console
$ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev
```

Các phụ thuộc của Odoo được liệt kê trong tệp `requirements.txt` nằm ở thư mục gốc của Odoo Community.

#### NOTE
Các gói Python trong `requirements.txt` dựa trên phiên bản Ubuntu/LTS Debian/ổn định tương ứng tại thời điểm phát hành Odoo. Ví dụ, đối với Odoo 15.0, phiên bản gói `python3-babel` là 2.8.0 trong Debian Bullseye và 2.6.0 trong Ubuntu Focal. Sau đó, phiên bản thấp nhất được chọn trong `requirements.txt`.

Điều hướng đến đường dẫn cài đặt Odoo Communit (`CommunityPath`) và chạy **pip** trên tệp yêu cầu để cài đặt các yêu cầu cho người dùng hiện tại.

```console
$ cd /CommunityPath
$ pip install -r requirements.txt
```

Windows

Trước khi cài đặt các phụ thuộc, hãy tải xuống và cài đặt [Công cụ Dựng Dành cho Visual Studio](https://visualstudio.microsoft.com/downloads/). Chọn **công cụ dựng C++** trong tab **Workload** và cài đặt chúng khi được nhắc.

Các phụ thuộc của Odoo được liệt kê trong tệp `requirements.txt` nằm ở thư mục gốc của Odoo Community.

Điều hướng đến đường dẫn cài đặt Odoo Community (`CommunityPath`) và chạy **pip** trên tệp yêu cầu trong terminal **với quyền Quản trị viên**:

```doscon
C:\> cd \CommunityPath
C:\> pip install setuptools wheel
C:\> pip install -r requirements.txt
```

Mac OS

Các phụ thuộc của Odoo được liệt kê trong tệp `requirements.txt` nằm ở thư mục gốc của Odoo Community.

Điều hướng đến đường dẫn cài đặt Odoo Community (`CommunityPath`) và chạy **pip** trên tệp yêu cầu:

```console
$ cd /CommunityPath
$ pip3 install setuptools wheel
$ pip3 install -r requirements.txt
```

#### WARNING
Các phụ thuộc không phải Python phải được cài đặt bằng trình quản lý gói ([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org)).

1. Tải xuống và cài đặt **Công cụ Dòng Lệnh**:
   ```console
   $ xcode-select --install
   ```
2. Sử dụng trình quản lý gói để cài đặt các phụ thuộc không phải Python.

#### NOTE
Đối với các ngôn ngữ sử dụng giao diện **từ phải sang trái** (như tiếng Ả Rập hoặc tiếng Do Thái), gói `rtlcss` là điều kiện bắt buộc.

Linux

1. Tải xuống và cài đặt **nodejs** và **npm** bằng trình quản lý gói.
2. Cài đặt `rtlcss`:
   ```console
   $ sudo npm install -g rtlcss
   ```

Windows

1. Tải xuống và cài đặt [nodejs](https://nodejs.org/en/download).
2. Cài đặt `rtlcss`:
   ```doscon
   C:\> npm install -g rtlcss
   ```
3. Chỉnh sửa biến môi trường hệ thống `PATH` để thêm thư mục chứa `rtlcss.cmd` (thường là: `C:\Users\<user>\AppData\Roaming\npm\`).

Mac OS

1. Tải xuống và cài đặt **nodejs** bằng trình quản lý gói ([Homebrew](https://brew.sh/), [MacPorts](https://www.macports.org)).
2. Cài đặt `rtlcss`:
   ```console
   $ sudo npm install -g rtlcss
   ```

#### WARNING
`wkhtmltopdf` không được cài đặt thông qua **pip** và phải được cài đặt thủ công trong [phiên bản 0.12.6](https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3) để hỗ trợ header và footer. Tham khảo [wiki wkhtmltopdf](https://github.com/odoo/odoo/wiki/Wkhtmltopdf) để biết thêm chi tiết về các phiên bản khác nhau.

<a id="install-source-running-odoo"></a>

## Chạy Odoo

Sau khi tất cả phụ thuộc được thiết lập, bạn có thể khởi chạy Odoo bằng cách chạy `odoo-bin`, giao diện dòng lệnh của máy chủ. Giao diện này nằm ở gốc của thư mục Odoo Community.

Để cấu hình máy chủ, hãy chỉ định [đối số dòng lệnh](../../developer/reference/cli.md#reference-cmdline-server) hoặc [tệp cấu hình](../../developer/reference/cli.md#reference-cmdline-config).

Cấu hình cần thiết phổ biến là:

- Người dùng và mật khẩu PostgreSQL.
- Đường dẫn add-on tùy chỉnh ngoài đường dẫn mặc định để tải các phân hệ tùy chỉnh.

Một cách điển hình để chạy máy chủ là:

Linux

```console
$ cd /CommunityPath
$ python3 odoo-bin --addons-path=addons -d mydb
```

Trong đó `CommunityPath` là đường dẫn cài đặt Odoo Community và `mydb` là tên cơ sở dữ liệu PostgreSQL.

Windows

```doscon
C:\> cd CommunityPath/
C:\> python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
```

Trong đó `CommunityPath` là đường dẫn cài đặt Odoo Community, `dbuser` là tên đăng nhập PostgreSQL, `dbpassword` là mật khẩu PostgreSQL và `mydb` là tên cơ sở dữ liệu PostgreSQL.

Mac OS

```console
$ cd /CommunityPath
$ python3 odoo-bin --addons-path=addons -d mydb
```

Trong đó `CommunityPath` là đường dẫn cài đặt Odoo Community và `mydb` là tên cơ sở dữ liệu PostgreSQL.

Sau khi máy chủ khởi động (nhật ký INFO `odoo.modules.loading: Modules loaded.` được in), hãy mở [http://localhost:8069](http://localhost:8069) trong trình duyệt web và đăng nhập vào cơ sở dữ liệu Odoo bằng tài khoản quản trị viên cơ sở: sử dụng `admin` làm email và `admin` làm mật khẩu.

#### SEE ALSO
[Danh sách các đối số CLI cho odoo-bin](../../developer/reference/cli.md)
