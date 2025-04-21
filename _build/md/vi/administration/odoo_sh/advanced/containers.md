# Container

## Tổng quan

Mỗi bản dựng được cô lập trong container riêng (container có namespace Linux).

Cơ sở là hệ thống Ubuntu, nơi tất cả các phụ thuộc cần thiết của Odoo, cũng như các gói hữu ích và phổ biến, được cài đặt.

Nếu dự án của bạn yêu cầu các phụ thuộc Python bổ sung hoặc các bản phát hành gần đây hơn, bạn có thể xác định tệp `requirements.txt` trong thư mục gốc của các nhánh liệt kê chúng. Nền tảng sẽ đảm nhiệm việc cài đặt các phụ thuộc này trong container của bạn. Tài liệu [Các yêu cầu pip](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers) có thể giúp bạn viết tệp `requirements.txt`. Để có ví dụ cụ thể, hãy xem tệp [requirements.txt của Odoo](https://github.com/odoo/odoo/blob/17.0/requirements.txt).

Các tệp `requirements.txt` của phân hệ phụ cũng được tính. Nền tảng tìm kiếm tệp `requirements.txt` trong mỗi thư mục chứa các phân hệ Odoo: Không phải trong thư mục phân hệ mà trong thư mục chính của chúng.

## Cấu trúc thư mục

Vì các container dựa trên Ubuntu nên cấu trúc thư mục của chúng tuân theo Tiêu chuẩn Phân cấp Hệ thống Tập tin của Linux. [Tổng quan về cây hệ thống tập tin của Ubuntu](https://help.ubuntu.com/community/LinuxFilesystemTreeOverview#Main_directories) giải thích các thư mục chính.

Sau đây là các thư mục liên quan đến Odoo.sh:

```default
.
├── home
│    └── odoo
│         ├── src
│         │    ├── odoo                Odoo Community source code
│         │    │    └── odoo-bin       Odoo server executable
│         │    ├── enterprise          Odoo Enterprise source code
│         │    ├── themes              Odoo Themes source code
│         │    └── user                Your repository branch source code
│         ├── data
│         │    ├── filestore           database attachments, as well as the files of binary fields
│         │    └── sessions            visitors and users sessions
│         └── logs
│              ├── install.log         Database installation logs
│              ├── odoo.log            Running server logs
│              ├── update.log          Database updates logs
│              └── pip.log             Python packages installation logs
└── usr
     ├── lib
     │    ├── python2.7
     │         └── dist-packages       Python 2.7 standard libraries
     │    ├── python3
     │         └── dist-packages       Python 3 standard libraries
     │    └── python3.5
     │         └── dist-packages       Python 3.5 standard libraries
     ├── local
     │    └── lib
     │         ├── python2.7
     │         │    └── dist-packages  Python 2.7 third-party libraries
     │         └── python3.5
     │              └── dist-packages  Python 3.5 third-party libraries
     └── usr
          └── bin
               ├── python2.7           Python 2.7 executable
               └── python3.5           Python 3.5 executable
```

Cả Python 2.7 và 3.5 đều được cài đặt trong các container. Tuy nhiên:

* Nếu dự án của bạn được cấu hình để sử dụng Odoo 10.0, máy chủ Odoo sẽ chạy bằng Python 2.7.
* Nếu dự án của bạn được cấu hình để sử dụng Odoo 11.0 trở lên, máy chủ Odoo sẽ chạy bằng Python 3.5.

## Shell cơ sở dữ liệu

Khi truy cập vào một container bằng shell, bạn có thể truy cập cơ sở dữ liệu bằng cách sử dụng *psql*.

```bash
odoo@odoo-addons-master-1.odoo.sh:~$ psql
psql (9.5.2, server 9.5.11)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

odoo-addons-master-1=>
```

**Hãy cẩn thận!** [Việc sử dụng các giao dịch](https://www.postgresql.org/docs/current/static/sql-begin.html) (*BEGIN...COMMIT/ROLLBACK*) cho mọi câu lệnh *sql* sẽ dẫn đến các thay đổi (*UPDATE*, *DELETE*, *ALTER*,...), đặc biệt là đối với cơ sở dữ liệu production của bạn.

Cơ chế giao dịch là mạng lưới an toàn của bạn trong trường hợp xảy ra lỗi. Bạn chỉ cần khôi phục các thay đổi để đưa cơ sở dữ liệu về trạng thái trước đó.

Ví dụ, giả sử bạn quên đặt điều kiện *WHERE*.

```sql
odoo-addons-master-1=> BEGIN;
BEGIN
odoo-addons-master-1=> UPDATE res_users SET password = '***';
UPDATE 457
odoo-addons-master-1=> ROLLBACK;
ROLLBACK
```

Trong trường hợp đó, bạn có thể khôi phục lại những thay đổi không mong muốn mà bạn vừa vô tình thực hiện và viết lại câu lệnh:

```sql
odoo-addons-master-1=> BEGIN;
BEGIN
odoo-addons-master-1=> UPDATE res_users SET password = '***' WHERE id = 1;
UPDATE 1
odoo-addons-master-1=> COMMIT;
COMMIT
```

Tuy nhiên, đừng quên commit hoặc khôi phục giao dịch của bạn sau khi đã thực hiện. Giao dịch mở có thể khóa các bản ghi trong bảng của bạn và cơ sở dữ liệu đang chạy có thể chờ chúng được giải phóng. Điều này có thể khiến máy chủ bị treo vô thời hạn.

Ngoài ra, nếu có thể, hãy sử dụng cơ sở dữ liệu staging để kiểm thử các câu lệnh của bạn trước. Đây là một giải pháp an toàn bổ sung dành cho bạn.

## Chạy máy chủ Odoo

Bạn có thể khởi động một phiên bản máy chủ Odoo từ một shell container. Bạn sẽ không thể truy cập nó từ bên ngoài bằng trình duyệt, nhưng bạn có thể:

* sử dụng shell Odoo,

```bash
$  odoo-bin shell
>>> partner = env['res.partner'].search([('email', '=', 'asusteK@yourcompany.example.com')], limit=1)
>>> partner.name
'ASUSTeK'
>>> partner.name = 'Odoo'
>>> env['res.partner'].search([('email', '=', 'asusteK@yourcompany.example.com')], limit=1).name
'Odoo'
```

* cài đặt một phân hệ,

```bash
$  odoo-bin -i sale --without-demo=all --stop-after-init
```

* cập nhật một phân hệ,

```bash
$  odoo-bin -u sale --stop-after-init
```

* chạy kiểm thử cho một phân hệ,

```bash
$  odoo-bin -i sale --test-enable --log-level=test --stop-after-init
```

Trong các lệnh trên, đối số:

* `--without-demo=all` ngăn dữ liệu demo được tải cho tất cả phân hệ
* `--stop-after-init` sẽ ngay lập tức tắt máy chủ sau khi các thao tác bạn yêu cầu hoàn tất.

Nhiều tùy chọn khác có sẵn và được trình bày chi tiết trong [Tài liệu CLI](../../../developer/reference/cli.md).

Bạn có thể tìm thấy đường dẫn addon được Odoo.sh sử dụng để chạy máy chủ của bạn trong nhật ký ( *~/logs/odoo.log*). Tìm "*odoo: addons paths*":

```default
2018-02-19 10:51:39,267 4 INFO ? odoo: Odoo version 17.0
2018-02-19 10:51:39,268 4 INFO ? odoo: Using configuration file at /home/odoo/.config/odoo/odoo.conf
2018-02-19 10:51:39,268 4 INFO ? odoo: addons paths: ['/home/odoo/data/addons/17.0', '/home/odoo/src/user', '/home/odoo/src/enterprise', '/home/odoo/src/themes', '/home/odoo/src/odoo/addons', '/home/odoo/src/odoo/odoo/addons']
```

**Hãy cẩn thận**, đặc biệt là với cơ sở dữ liệu production. Các thao tác bạn thực hiện khi chạy phiên bản máy chủ Odoo này không bị cô lập: Các thay đổi sẽ có hiệu lực trong cơ sở dữ liệu. Luôn luôn tiến hành kiểm thử trên cơ sở dữ liệu staging.

## Gỡ lỗi trong Odoo.sh

Việc gỡ lỗi bản dựng Odoo.sh không hẳn khác biệt so với ứng dụng Python khác. Bài viết này chỉ giải thích các đặc điểm và hạn chế của nền tảng Odoo.sh và giả định rằng bạn đã biết cách sử dụng trình gỡ lỗi.

#### NOTE
Nếu chưa biết cách gỡ lỗi ứng dụng Python, bạn có thể dễ dàng tìm thấy nhiều khóa học cơ bản trên Internet.

Bạn có thể sử dụng `pdb`, `pudb` hoặc `ipdb` để gỡ lỗi mã trên Odoo.sh. Vì máy chủ được chạy bên ngoài shell, bạn không thể khởi chạy trình gỡ lỗi trực tiếp từ backend của phiên bản Odoo vì trình gỡ lỗi cần có shell để hoạt động.

- [pdb](https://docs.python.org/3/library/pdb.html) được cài đặt trong mọi container theo mặc định.
- Nếu bạn muốn sử dụng [pudb](https://pypi.org/project/pudb/) hoặc [ipdb](https://pypi.org/project/ipdb/) bạn cần cài đặt chúng trước.

  Để thực hiện, bạn có hai tuỳ chọn:
  > - tạm thời (chỉ có trong bản dựng hiện tại):
  >   ```bash
  >   $  pip install pudb --user
  >   ```

  >   hoặc
  >   ```bash
  >   $  pip install ipdb --user
  >   ```
  > - vĩnh viễn: thêm `pudb` hoặc `ipdb` vào tệp `requirements.txt` của dự án.

Sau đó chỉnh sửa mã, nơi bạn muốn kích hoạt trình gỡ lỗi và thêm mã này:

```python
import sys
if sys.__stdin__.isatty():
    import pdb; pdb.set_trace()
```

Điều kiện `sys.__stdin__.isatty()` là một hack phát hiện xem bạn có chạy Odoo từ shell hay không.

Lưu tệp và sau đó chạy Odoo Shell:

```bash
$ odoo-bin shell
```

Cuối cùng, *thông qua* Odoo Shell, bạn có thể kích hoạt đoạn mã/hàm/phương thức mà bạn muốn gỡ lỗi.

![Ảnh chụp màn hình bảng điều khiển hiển thị ``pdb`` đang chạy trong shell Odoo.sh.](administration/odoo_sh/advanced/containers/pdb_sh.png)
