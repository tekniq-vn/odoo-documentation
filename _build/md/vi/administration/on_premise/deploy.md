# Cấu hình hệ thống

Tài liệu này mô tả các bước cơ bản để thiết lập Odoo trong môi trường production hoặc trên máy chủ kết nối internet. Tài liệu này tuân theo [cài đặt](administration/on_premise.md) và thường không cần thiết cho các hệ thống phát triển không được triển khai trên internet.

#### WARNING
Nếu bạn đang thiết lập máy chủ công khai, hãy nhớ tham khảo các khuyến nghị về bảo mật của chúng tôi!

<a id="dbfilter"></a>

## dbfilter

Odoo là hệ thống multi-tenant: một hệ thống Odoo duy nhất có thể chạy và phục vụ nhiều phiên bản cơ sở dữ liệu. Nó cũng có khả năng tùy chỉnh cao và các tùy chỉnh (bắt đầu từ các phân hệ được tải) phụ thuộc vào "cơ sở dữ liệu hiện tại".

Không có vấn đề gì khi làm việc với backend (máy khách web) với tư cách là người dùng công ty đã đăng nhập: có thể chọn cơ sở dữ liệu khi đăng nhập và tải các tùy chỉnh sau đó.

Tuy nhiên, lại có vấn đề đối với người dùng không đăng nhập (cổng thông tin, trang web) mà không ràng buộc với cơ sở dữ liệu nào: Odoo cần biết cơ sở dữ liệu nào nên được sử dụng để tải trang web hoặc thực hiện thao tác. Sẽ không thành vấn đề nếu không sử dụng multi-tenancy, vì chỉ có một cơ sở dữ liệu để sử dụng. Nhưng nếu có thể truy cập nhiều cơ sở dữ liệu, thì Odoo cần một quy tắc để biết nên sử dụng cơ sở dữ liệu nào.

Đó là một trong những mục đích của [`--db-filter`](developer/reference/cli.md#cmdoption-odoo-bin-db-filter): nó chỉ định cách cơ sở dữ liệu sẽ được chọn dựa trên tên máy chủ (miền) đang được yêu cầu. Giá trị là một [biểu thức chính quy](https://docs.python.org/3/library/re.html), có thể bao gồm tên máy chủ được cung cấp động (`%h`) hoặc miền phụ đầu tiên (`%d`) mà hệ thống đang được truy cập.

Đối với các máy chủ lưu trữ nhiều cơ sở dữ liệu trong production, đặc biệt nếu sử dụng `trang web`, dbfilter **phải** được thiết lập, nếu không một số tính năng sẽ không hoạt động chính xác.

### Cấu hình mẫu

* Chỉ hiển thị các cơ sở dữ liệu có tên bắt đầu bằng 'mycompany'

trong [tệp cấu hình](developer/reference/cli.md#reference-cmdline-config-file) thiết lập:

```ini
[options]
dbfilter = ^mycompany.*$
```

* Chỉ hiển thị các cơ sở dữ liệu khớp với tên miền phụ đầu tiên sau `www`: ví dụ cơ sở dữ liệu “mycompany” sẽ được hiển thị nếu yêu cầu đến được gửi đến `www.mycompany.com` hoặc `mycompany.co.uk`, nhưng không hiển thị đối với `www2.mycompany.com` hoặc `helpdesk.mycompany.com`.

trong [tệp cấu hình](developer/reference/cli.md#reference-cmdline-config-file) thiết lập:

```ini
[options]
dbfilter = ^%d$
```

#### NOTE
Thiết lập [`--db-filter`](developer/reference/cli.md#cmdoption-odoo-bin-db-filter) phù hợp là một phần quan trọng trong việc bảo mật triển khai của bạn. Khi nó hoạt động chính xác và chỉ khớp với một cơ sở dữ liệu duy nhất cho mỗi tên máy chủ, chúng tôi khuyến nghị bạn nên chặn quyền truy cập vào màn hình trình quản lý cơ sở dữ liệu và sử dụng tham số khởi động `--no-database-list` để ngăn việc công khai cơ sở dữ liệu của bạn và chặn quyền truy cập vào màn hình quản lý cơ sở dữ liệu. Đọc thêm về [security]().

## PostgreSQL

Theo mặc định, PostgreSQL chỉ cho phép kết nối qua UNIX socket và kết nối vòng lặp (từ "localhost", cùng một máy mà máy chủ PostgreSQL được cài đặt).

UNIX socket hoạt động bình thường nếu bạn muốn Odoo và PostgreSQL thực thi trên cùng một máy và là tuỳ chọn mặc định khi không cung cấp máy chủ. Tuy nhiên, nếu bạn muốn Odoo và PostgreSQL thực thi trên các máy khác nhau <sup>[1](#different-machines)</sup> thì nó sẽ cần phải [tuân thủ giao diện mạng](https://www.postgresql.org/docs/12/static/runtime-config-connection.html) <sup>[2](#remote-socket)</sup>, theo một trong hai cách sau:

* Chỉ chấp nhận các kết nối vòng lặp và [sử dụng SSH tunnel](https://www.postgresql.org/docs/12/static/ssh-tunnels.html) giữa máy chạy Odoo và máy chạy PostgreSQL, sau đó cấu hình Odoo để kết nối đến cuối tunnel của nó
* Chấp nhận kết nối tới máy mà Odoo được cài đặt, có thể qua ssl (tham khảo [Cài đặt kết nối PostgreSQL](https://www.postgresql.org/docs/12/static/runtime-config-connection.html) để biết thêm chi tiết), sau đó cấu hình Odoo để kết nối qua mạng

### Cấu hình mẫu

* Cho phép kết nối tcp trên localhost
* Cho phép kết nối tcp từ mạng 192.168.1.x

trong `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/pg_hba.conf` cài đặt:

```text
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
host    all             all             192.168.1.0/24          md5
```

trong `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/postgresql.conf` cài đặt:

```text
listen_addresses = 'localhost,192.168.1.2'
port = 5432
max_connections = 80
```

<a id="setup-deploy-odoo"></a>

### Cấu hình Odoo

Odoo có sẵn kết nối với postgres cục bộ qua UNIX socket thông qua cổng 5432. Bạn có thể ghi đè tùy chọn này bằng cách sử dụng [tùy chọn cơ sở dữ liệu](developer/reference/cli.md#reference-cmdline-server-database) khi triển khai Postgres của bạn không phải là cục bộ và/hoặc không sử dụng cài đặt mặc định.

[Trình cài đặt trọn gói](administration/on_premise/packages.md) sẽ tự động tạo một người dùng mới (`odoo`) và thiết lập người dùng đó làm người dùng cơ sở dữ liệu.

* Màn hình quản lý cơ sở dữ liệu được bảo vệ bằng cài đặt `admin_passwd`. Cài đặt này chỉ có thể được thiết lập bằng cách sử dụng các tệp cấu hình và chỉ cần kiểm tra trước khi thực hiện thay đổi cơ sở dữ liệu. Nó nên được thiết lập thành một giá trị được tạo ngẫu nhiên để đảm bảo bên thứ ba không thể sử dụng giao diện này.
* Tất cả hoạt động cơ sở dữ liệu đều sử dụng [tuỳ chọn cơ sở dữ liệu](developer/reference/cli.md#reference-cmdline-server-database), bao gồm cả màn hình quản lý cơ sở dữ liệu. Để màn hình quản lý cơ sở dữ liệu hoạt động, người dùng PostgreSQL phải có quyền `createdb`.
* Người dùng luôn có thể xóa cơ sở dữ liệu mà họ sở hữu. Để màn hình quản lý cơ sở dữ liệu ngừng hoạt động hoàn toàn, người dùng PostgreSQL cần được tạo bằng `no-createdb` và cơ sở dữ liệu phải thuộc sở hữu của một người dùng PostgreSQL khác.

  #### WARNING
  người dùng PostgreSQL *không được* là siêu người dùng

#### Cấu hình mẫu

* kết nối tới máy chủ PostgreSQL trên 192.168.1.2
* cổng 5432
* sử dụng một tài khoản người dùng 'odoo'
* với 'pwd' là mật khẩu
* chỉ lọc db có tên bắt đầu bằng 'mycompany'

trong [tệp cấu hình](developer/reference/cli.md#reference-cmdline-config-file) thiết lập:

```ini
[options]
admin_passwd = mysupersecretpassword
db_host = 192.168.1.2
db_port = 5432
db_user = odoo
db_password = pwd
dbfilter = ^mycompany.*$
```

<a id="postgresql-ssl-connect"></a>

### SSL giữa Odoo và PostgreSQL

Kể từ Odoo 11.0, bạn có thể thực thi kết nối ssl giữa Odoo và PostgreSQL. Trong Odoo, db_sslmode kiểm soát bảo mật ssl của kết nối với giá trị được chọn từ 'disable', 'allow', 'prefer', 'require', 'verify-ca' hoặc 'verify-full'

[PostgreSQL Doc](https://www.postgresql.org/docs/12/static/libpq-ssl.html)

<a id="builtin-server"></a>

## Máy chủ tích hợp

Odoo tích hợp sẵn các máy chủ HTTP, cron và livechat, sử dụng đa luồng hoặc đa xử lý.

Máy chủ **đa luồng** là máy chủ đơn giản hơn, chủ yếu được sử dụng để phát triển và trình bày, và tương thích với nhiều hệ điều hành (bao gồm Windows). Một luồng mới được tạo ra cho mỗi yêu cầu HTTP mới, ngay cả đối với các kết nối tồn tại lâu dài như websocket. Các luồng daemon cron bổ sung cũng được tạo ra. Do hạn chế của Python (GIL), phần cứng không được tận dụng tối đa.

Máy chủ đa luồng là máy chủ mặc định, cũng dành cho các container docker. Bạn có thể chọn nó bằng cách bỏ tùy chọn [`--workers`](developer/reference/cli.md#cmdoption-odoo-bin-workers) hoặc đặt thành `0`.

Máy chủ **đa xử lý** là máy chủ toàn diện được sử dụng chủ yếu cho production. Nó không chịu trách nhiệm về giới hạn Python (GIL) tương tự đối với việc sử dụng tài nguyên và do đó tận dụng tốt nhất phần cứng. Một nhóm worker được tạo khi khởi động máy chủ. Các yêu cầu HTTP mới được hệ điều hành xếp vào hàng đợi cho đến khi có worker sẵn sàng xử lý chúng. Một worker HTTP theo sự kiện bổ sung dành cho livechat được tạo ra trên một cổng thay thế. Worker cron bổ sung cũng được tạo ra. Trình thu thập quy trình có thể cấu hình sẽ giám sát việc sử dụng tài nguyên và có thể loại bỏ/khởi động lại các worker bị lỗi.

Máy chủ đa xử lý là máy chủ tuỳ chọn. Bạn có thể chọn nó bằng cách đặt tùy chọn [`--workers`](developer/reference/cli.md#cmdoption-odoo-bin-workers) thành số nguyên không null.

#### NOTE
Vì được tùy chỉnh cao cho máy chủ Linux nên máy chủ đa xử lý không khả dụng trên Windows.

### Tính toán số lượng worker

* Nguyên tắc chung: (#CPU \* 2) + 1
* Cron worker cần CPU
* 1 worker ~= 6 người dùng đồng thời

### tính toán kích thước bộ nhớ

* Chúng tôi coi 20% yêu cầu là yêu cầu nặng, trong khi 80% là yêu cầu đơn giản hơn
* Một worker nặng, khi tất cả các trường tính toán được thiết kế tốt, các yêu cầu SQL cũng được thiết kế tốt,... ước tính sẽ tiêu thụ khoảng 1GB RAM
* Trong tình huống tương tự, một worker nhẹ hơn ước tính sẽ tiêu thụ khoảng 150MB RAM

RAM cần thiết = #worker \* ( (tỷ lệ_worker_nhẹ \* ước tính_ram_cho_worker_nhẹ) + (tỷ lệ_worker_nặng \* ước tính_ram_cho_worker_nặng) )

### LiveChat

Trong đa xử lý, một worker LiveChat riêng sẽ tự động được khởi động và nghe trên [`--gevent-port`](developer/reference/cli.md#cmdoption-odoo-bin-gevent-port). Theo mặc định, các yêu cầu HTTP sẽ tiếp tục truy cập vào các worker HTTP thông thường thay vì worker LiveChat. Bạn phải triển khai một proxy trước Odoo và chuyển hướng các yêu cầu đến có đường dẫn bắt đầu bằng `/websocket/` đến worker LiveChat. Bạn cũng phải khởi động Odoo trong [`--proxy-mode`](developer/reference/cli.md#cmdoption-odoo-bin-proxy-mode) để nó sử dụng các header máy khách thực (như tên máy chủ, lược đồ và IP) thay vì các header proxy.

### Cấu hình mẫu

* Máy chủ với 4 core CPU, 8 luồng
* 60 người dung truy cập đồng thời
* 60 người dùng/6 = 10 <- số lượng worker cần thiết theo lý thuyết
* (4 \* 2) + 1 = 9 <- số lượng worker tối đa theo lý thuyết
* Chúng tôi sẽ sử dụng 8 worker + 1 cho cron. Chúng tôi cũng sẽ sử dụng hệ thống giám sát để đo tải CPU và kiểm tra xem nó có nằm trong khoảng từ 7 đến 7,5 không.
* RAM = 9 \* ((0.8\*150) + (0.2\*1024)) ~= 3GB RAM for Odoo

trong [tệp cấu hình](developer/reference/cli.md#reference-cmdline-config-file):

```ini
[options]
limit_memory_hard = 1677721600
limit_memory_soft = 629145600
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200
max_cron_threads = 1
workers = 8
```

<a id="https-proxy"></a>

## HTTPS

Cho dù được truy cập thông qua trang web/máy khách web hay dịch vụ web, Odoo đều truyền thông tin xác thực dưới dạng văn bản thuần túy. Điều này có nghĩa là việc triển khai Odoo an toàn phải sử dụng HTTPS<sup>[3](#switching)</sup>. Có thể triển khai SSL termination thông qua hầu hết mọi proxy SSL termination, nhưng yêu cầu thiết lập sau:

* Bật [`chế độ proxy`](developer/reference/cli.md#cmdoption-odoo-bin-proxy-mode) của Odoo. Chỉ nên bật tùy chọn này khi Odoo nằm sau proxy đảo ngược
* Thiết lập proxy chấm dứt SSL ([Ví dụ chấm dứt Nginx](https://nginx.com/resources/admin-guide/nginx-ssl-termination/))
* Thiết lập proxy ([Ví dụ proxy Nginx](https://nginx.com/resources/admin-guide/reverse-proxy/))
* Proxy chấm dứt SSL của bạn cũng sẽ tự động chuyển hướng các kết nối không an toàn đến cổng an toàn

### Cấu hình mẫu

* Chuyển hướng yêu cầu http sang https
* Yêu cầu proxy tới Odoo

trong [tệp cấu hình](developer/reference/cli.md#reference-cmdline-config-file) thiết lập:

```ini
proxy_mode = True
```

trong `/etc/nginx/sites-enabled/odoo.conf` cài đặt:

```nginx
#odoo server
upstream odoo {
  server 127.0.0.1:8069;
}
upstream odoochat {
  server 127.0.0.1:8072;
}
map $http_upgrade $connection_upgrade {
  default upgrade;
  ''      close;
}

# http -> https
server {
  listen 80;
  server_name odoo.mycompany.com;
  rewrite ^(.*) https://$host$1 permanent;
}

server {
  listen 443 ssl;
  server_name odoo.mycompany.com;
  proxy_read_timeout 720s;
  proxy_connect_timeout 720s;
  proxy_send_timeout 720s;

  # SSL parameters
  ssl_certificate /etc/ssl/nginx/server.crt;
  ssl_certificate_key /etc/ssl/nginx/server.key;
  ssl_session_timeout 30m;
  ssl_protocols TLSv1.2;
  ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
  ssl_prefer_server_ciphers off;

  # log
  access_log /var/log/nginx/odoo.access.log;
  error_log /var/log/nginx/odoo.error.log;

  # Redirect websocket requests to odoo gevent port
  location /websocket {
    proxy_pass http://odoochat;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    proxy_cookie_flags session_id samesite=lax secure;  # requires nginx 1.19.8
  }

  # Redirect requests to odoo backend server
  location / {
    # Add Headers for odoo proxy mode
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_redirect off;
    proxy_pass http://odoo;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    proxy_cookie_flags session_id samesite=lax secure;  # requires nginx 1.19.8
  }

  # common gzip
  gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
  gzip on;
}
```

### Nâng cao bảo mật HTTPS

Thêm header `Strict-Transport-Security` vào tất cả yêu cầu để ngăn trình duyệt gửi yêu cầu HTTP thuần túy đến miền này. Bạn luôn cần duy trì dịch vụ HTTPS đang hoạt động với chứng chỉ hợp lệ trên miền này. Nếu không, người dùng của bạn sẽ thấy cảnh báo bảo mật hoặc hoàn toàn không thể truy cập.

Bắt buộc kết nối HTTPS trong năm cho mọi khách truy cập vào NGINX bằng dòng lệnh:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
```

Cấu hình bổ sung có thể được xác định cho cookie `session_id`. Bạn có thể thêm cờ `Secure` để đảm bảo nó không bao giờ được truyền qua HTTP và `SameSite=Lax` để ngăn chặn [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) đã xác thực.

```nginx
# requires nginx 1.19.8
proxy_cookie_flags session_id samesite=lax secure;
```

## Odoo dưới dạng Ứng dụng WSGI

Cũng có thể coi Odoo như một ứng dụng [WSGI](https://wsgi.readthedocs.org/) chuẩn. Odoo cung cấp cơ sở cho một tập lệnh khởi chạy WSGI là `odoo-wsgi.example.py`. Tập lệnh đó phải được tùy chỉnh (có thể sau khi sao chép từ thư mục thiết lập) để thiết lập cấu hình chính xác ngay trong `odoo.tools.config` thay vì thông qua dòng lệnh hoặc tệp cấu hình.

Tuy nhiên, máy chủ WSGI sẽ chỉ hiển thị endpoint HTTP chính cho máy khách web, trang web và API dịch vụ web. Vì Odoo không còn kiểm soát việc tạo worker, nên không thể thiết lập worker cron hoặc livechat

### Cron Worker

Việc khởi chạy một trong các máy chủ Odoo tích hợp cạnh máy chủ WSGI là điều kiện bắt buộc để xử lý các tác vụ cron. Máy chủ đó phải được cấu hình để chỉ xử lý cron mà không phải các yêu cầu HTTP bằng tùy chọn cli [`--no-http`](developer/reference/cli.md#cmdoption-odoo-bin-no-http) hoặc cài đặt tệp cấu hình `http_enable = False`.

Trên các hệ thống giống Linux, bạn nên sử dụng máy chủ đa xử lý thay vì máy chủ đa luồng để tận dụng tối đa phần cứng và tăng tính ổn định. Điều này có nghĩa là sử dụng các tùy chọn cli [`--workers=-1`](developer/reference/cli.md#cmdoption-odoo-bin-workers) và [`--max-cron-threads=n`](developer/reference/cli.md#cmdoption-odoo-bin-max-cron-threads).

### LiveChat

Phải sử dụng máy chủ WSGI tương thích với gevent để tính năng live chat hoạt động chính xác. Máy chủ đó phải có khả năng xử lý nhiều kết nối dài và đồng thời nhưng không cần nhiều sức mạnh xử lý. Tất cả các yêu cầu có đường dẫn bắt đầu bằng `/websocket/` phải được chuyển hướng đến máy chủ đó. Một máy chủ WSGI thông thường (dựa trên luồng/quy trình) phải được sử dụng cho tất cả các yêu cầu khác.

Máy chủ cron Odoo cũng có thể được sử dụng để phục vụ các yêu cầu live chat. Chỉ cần thả tùy chọn cli [`--no-http`](developer/reference/cli.md#cmdoption-odoo-bin-no-http) từ máy chủ cron và đảm bảo các yêu cầu có đường dẫn bắt đầu bằng `/websocket/` được chuyển hướng đến máy chủ này, trên [`--http-port`](developer/reference/cli.md#cmdoption-odoo-bin-http-port) (máy chủ đa luồng) hoặc trên [`--gevent-port`](developer/reference/cli.md#cmdoption-odoo-bin-gevent-port) (máy chủ đa xử lý).

<a id="deploy-streaming"></a>

## Phục vụ tệp tĩnh và tệp đính kèm

Để thuận tiện cho việc phát triển, Odoo trực tiếp phục vụ tất cả các tệp tĩnh và tệp đính kèm trong các phân hệ. Điều này có thể không lý tưởng về hiệu suất, và các tệp tĩnh thường phải được phục vụ bởi một máy chủ HTTP tĩnh.

### Phục vụ tệp tĩnh

Các tệp tĩnh của Odoo nằm trong thư mục `static/` của mỗi phân hệ. Do đó, các tệp tĩnh có thể được phục vụ bằng cách chặn tất cả yêu cầu tới `/*MODULE*/static/*FILE*` và tìm đúng phân hệ (và tệp) trong các đường dẫn addon khác nhau.

Bạn nên thiết lập header `Content-Security-Policy: default-src 'none'` trên tất cả hình ảnh được máy chủ web phân phối. Dù không hoàn toàn bắt buộc vì người dùng không thể sửa đổi/chèn nội dung bên trong thư mục `static/` của phân hệ và hình ảnh hiện có là hình ảnh cuối cùng (chúng không tự tìm nạp tài nguyên mới), nhưng đây là một thiết lập hữu ích.

Khi sử dụng cấu hình NGINX (https) ở trên, các khối `map` và `location` sau đây sẽ được thêm vào để phục vụ các tệp tĩnh thông qua NGINX.

```nginx
map $sent_http_content_type $content_type_csp {
    default "";
    ~image/ "default-src 'none'";
}

server {
    # the rest of the configuration

    location @odoo {
        # copy-paste the content of the / location block
    }

    # Serve static files right away
    location ~ ^/[^/]+/static/.+$ {
        # root and try_files both depend on your addons paths
        root ...;
        try_files ... @odoo;
        expires 24h;
        add_header Content-Security-Policy $content_type_csp;
    }
}
```

Các lệnh `root` và `try_files` thực tế phụ thuộc vào cài đặt của bạn, cụ thể là trên [`--addons-path`](developer/reference/cli.md#cmdoption-odoo-bin-addons-path).

### Phục vụ tệp đính kèm

Tệp đính kèm là các tệp được lưu trữ trong filestore mà Odoo quy định quyền truy cập. Không thể truy cập trực tiếp qua máy chủ web tĩnh vì việc truy cập chúng đòi hỏi nhiều lần tra cứu trong cơ sở dữ liệu để xác định nơi lưu trữ tệp và liệu người dùng hiện tại có thể truy cập chúng hay không.

Tuy nhiên, sau khi tệp đã được định vị và quyền truy cập đã được Odoo xác minh, bạn nên phục vụ tệp bằng máy chủ web tĩnh thay vì Odoo. Để Odoo ủy quyền phục vụ tệp cho máy chủ web tĩnh, tiện ích mở rộng X-Sendfile <[https://tn123.org/mod_xsendfile/](https://tn123.org/mod_xsendfile/)>\`_ (apache) hoặc [X-Accel](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/) (nginx) phải được bật và cấu hình trên máy chủ web tĩnh. Sau khi thiết lập xong, hãy khởi động Odoo bằng cờ CLI [`--x-sendfile`](developer/reference/cli.md#cmdoption-odoo-bin-x-sendfile) (cờ duy nhất này được sử dụng cho cả X-Sendfile và X-Accel).

#### NOTE
- Tiện ích mở rộng X-Sendfile dành cho apache (và các máy chủ web tương thích) không yêu cầu bất kỳ cấu hình bổ sung nào.
- Tiện ích mở rộng X-Accel cho NGINX **yêu cầu** cấu hình bổ sung sau:
  ```nginx
  location /web/filestore {
      internal;
      alias /path/to/odoo/data-dir/filestore;
  }
  ```

  Nếu bạn không biết đường dẫn đến filestore của mình là gì, hãy khởi động Odoo với tùy chọn [`--x-sendfile`](developer/reference/cli.md#cmdoption-odoo-bin-x-sendfile) và điều hướng đến URL `/web/filestore` trực tiếp qua Odoo (không điều hướng đến URL qua NGINX). Thao tác này sẽ tạo ra cảnh báo với thông báo chứa cấu hình bạn cần.

<a id="security"></a>

## Bảo mật

Trước hết, bạn nên nhớ rằng bảo mật hệ thống thông tin là một quá trình liên tục, không phải là một thao tác diễn ra một lần. Hãy luôn đảm bảo tính bảo mật của từng chi tiết nhỏ trong hệ thống của bạn.

Vì vậy, mong rằng bạn không coi phần này là danh sách cuối cùng về các biện pháp sẽ ngăn ngừa mọi vấn đề bảo mật. Nó chỉ có mục đích tóm tắt những điều quan trọng hàng đầu mà bạn nên đưa vào kế hoạch bảo mật của mình. Phần còn lại sẽ đến từ các biện pháp bảo mật tốt nhất cho hệ điều hành và bản phân phối của bạn, các biện pháp tốt nhất về người dùng, mật khẩu và quản lý kiểm soát truy cập,...

Khi triển khai máy chủ kết nối Internet, hãy nhớ cân nhắc các chủ đề liên quan đến bảo mật sau:

- Luôn đặt mật khẩu quản trị viên mạnh và hạn chế quyền truy cập vào các trang quản lý cơ sở dữ liệu ngay khi hệ thống được thiết lập. Tham khảo [Bảo mật Trình Quản lý Cơ sở Dữ liệu](#db-manager-security).
- Chọn tên đăng nhập duy nhất và mật khẩu mạnh cho tất cả tài khoản quản trị viên trên tất cả cơ sở dữ liệu. Không sử dụng 'admin' làm tên đăng nhập. Không sử dụng những tên đăng nhập đó cho các hoạt động thường xuyên mà chỉ sử dụng để kiểm soát/quản lý cài đặt. *Không bao giờ* sử dụng bất kỳ mật khẩu mặc định nào như admin/admin, ngay cả đối với cơ sở dữ liệu kiểm thử/staging.
- **Không** cài đặt dữ liệu demo trên các máy chủ kết nối internet. Cơ sở dữ liệu có dữ liệu demo chứa tên đăng nhập và mật khẩu mặc định có thể được sử dụng để xâm nhập vào hệ thống của bạn và gây ra sự cố nghiêm trọng, ngay cả trên hệ thống staging/phát triển.
- Sử dụng bộ lọc cơ sở dữ liệu phù hợp ( [`--db-filter`](developer/reference/cli.md#cmdoption-odoo-bin-db-filter)) để giới hạn chế độ hiển thị cơ sở dữ liệu của bạn theo tên máy chủ. Tham khảo [dbfilter](#dbfilter). Bạn cũng có thể sử dụng [`-d`](developer/reference/cli.md#cmdoption-odoo-bin-d) để cung cấp danh sách (được phân tách bằng dấu phẩy) các cơ sở dữ liệu có sẵn để lọc, thay vì để hệ thống lấy tất cả chúng từ cơ sở dữ liệu backend.
- Sau khi `db_name` và `dbfilter` của bạn được cấu hình và chỉ khớp với một cơ sở dữ liệu duy nhất cho mỗi tên máy chủ, bạn nên đặt tùy chọn cấu hình `list_db` thành `False` để ngăn chặn việc công khai toàn bộ cơ sở dữ liệu và chặn quyền truy cập vào màn hình quản lý cơ sở dữ liệu (điều này cũng được hiển thị dưới dạng tùy chọn dòng lệnh [`--no-database-list`](developer/reference/cli.md#cmdoption-odoo-bin-no-database-list))
- Đảm bảo người dùng PostgreSQL ([`--db_user`](developer/reference/cli.md#cmdoption-odoo-bin-r)) *không* phải là siêu người dùng và cơ sở dữ liệu của bạn thuộc sở hữu của một người dùng khác. Ví dụ, chúng có thể thuộc sở hữu của siêu người dùng `postgres` nếu bạn đang sử dụng `db_user` chuyên dụng không có đặc quyền. Tham khảo thêm [Cấu hình Odoo](#setup-deploy-odoo).
- Luôn cập nhật các cài đặt bằng cách thường xuyên cài đặt các bản dựng mới nhất, thông qua GitHub hoặc bằng cách tải xuống phiên bản mới nhất từ ​​https://www.odoo.com/page/download hoặc [http://nightly.odoo.com](http://nightly.odoo.com)
- Cấu hình máy chủ của bạn ở chế độ đa xử lý với các giới hạn phù hợp với mức sử dụng thông thường của bạn (bộ nhớ/CPU/thời gian chờ). Tham khảo thêm [Máy chủ tích hợp](#builtin-server).
- Chạy Odoo sau máy chủ web cung cấp HTTPS termination với chứng chỉ SSL hợp lệ, để ngăn chặn việc nghe lén các liên lạc bằng văn bản thuần tuý. Chứng chỉ SSL không tốn kém và có nhiều tùy chọn miễn phí. Cấu hình proxy web để giới hạn kích thước yêu cầu, cài đặt thời gian chờ thích hợp, sau đó bật tùy chọn [`proxy mode`](developer/reference/cli.md#cmdoption-odoo-bin-proxy-mode). Tham khảo thêm [HTTPS](#https-proxy).
- Nếu bạn cần cho phép truy cập SSH từ xa vào máy chủ của mình, hãy đảm bảo đặt mật khẩu mạnh cho **tất cả** tài khoản, không chỉ `root`. Chúng tôi khuyến khích tắt hoàn toàn xác thực bằng mật khẩu và chỉ cho phép xác thực bằng mã khóa công khai. Ngoài ra, hãy cân nhắc hạn chế quyền truy cập qua VPN, chỉ cho phép các IP đáng tin cậy trong tường lửa và/hoặc chạy hệ thống phát hiện tấn công brute-force như `fail2ban` hoặc tương đương.
- Hãy cân nhắc cài đặt giới hạn tốc độ phù hợp trên proxy hoặc tường lửa của bạn để ngăn chặn các cuộc tấn công brute-force và tấn công từ chối dịch vụ. Tham khảo thêm [Chặn các Cuộc Tấn công Brute Force](#login-brute-force) để biết các biện pháp cụ thể.

  Nhiều nhà cung cấp mạng cung cấp dịch vụ giảm thiểu tự động cho các cuộc Tấn công Từ chối Dịch vụ Phân tán (DDOS), nhưng đây thường là dịch vụ tùy chọn, vì vậy bạn nên tham khảo với nhà cung cấp của mình.
- Nếu có thể, hãy luôn lưu trữ các phiên bản demo/kiểm thử/staging công khai của bạn trên các máy khác với máy production. Và áp dụng các biện pháp phòng ngừa bảo mật tương tự như đối với production.
- Nếu máy chủ Odoo công khai của bạn có quyền truy cập vào các tài nguyên hoặc dịch vụ mạng nội bộ nhạy cảm (ví dụ: thông qua VLAN riêng), hãy triển khai những quy tắc tường lửa thích hợp để bảo vệ các tài nguyên nội bộ đó. Điều này sẽ đảm bảo rằng máy chủ Odoo không thể bị sử dụng một cách vô ý (hoặc do tác vụ nguy hại của người dùng) để truy cập hoặc làm gián đoạn các tài nguyên nội bộ đó. Thông thường, điều này có thể được thực hiện bằng cách áp dụng quy tắc DENY mặc định outbound trên tường lửa, sau đó chỉ cho phép quyền truy cập một cách rõ ràng vào các tài nguyên nội bộ mà máy chủ Odoo cần truy cập. [Kiểm soát truy cập lưu lượng IP Systemd](http://0pointer.net/blog/ip-accounting-and-access-lists-with-systemd.html) cũng có thể hữu ích trong triển khai kiểm soát truy cập mạng theo quy trình.
- Nếu máy chủ Odoo công khai của bạn nằm sau Tường lửa ứng dụng web, bộ cân bằng tải, dịch vụ bảo vệ DDoS minh bạch (như CloudFlare) hoặc một thiết bị cấp độ mạng tương tự, bạn có thể nên tránh truy cập trực tiếp vào hệ thống Odoo. Nhìn chung, rất khó để giữ bí mật địa chỉ IP endpoint của máy chủ Odoo của bạn. Ví dụ: chúng có thể xuất hiện trong nhật ký máy chủ web khi truy vấn hệ thống công cộng hoặc trong tiêu đề email từ Odoo. Trong tình huống như vậy, bạn có thể nên cấu hình tường lửa của mình để ngăn chặn việc truy cập công khai endpoint, trừ truy cập từ các địa chỉ IP cụ thể của dịch vụ WAF, cân bằng tải hoặc proxy của bạn. Các nhà cung cấp dịch vụ như CloudFlare thường duy trì danh sách công khai các dải địa chỉ IP của họ cho mục đích này.
- Nếu bạn đang lưu trữ nhiều khách hàng, hãy cô lập dữ liệu và tệp khách hàng khỏi nhau bằng cách sử dụng container hoặc các kỹ thuật "rào chắn" thích hợp.
- Tạo sao lưu hàng ngày cho cơ sở dữ liệu và dữ liệu filestore của bạn và sao chép chúng vào một máy chủ lưu trữ từ xa mà chính máy chủ đó không thể truy cập được.
- Triển khai Odoo trên Linux được khuyến khích hơn là Windows. Tuy nhiên, nếu bạn vẫn chọn triển khai trên nền tảng Windows, bạn nên tiến hành đánh giá bảo mật toàn diện cho máy chủ và phạm vi hướng dẫn này không bao gồm hoạt động đó.

<a id="login-brute-force"></a>

### Chặn các Cuộc Tấn công Brute Force

Với các triển khai kết nối internet, những cuộc tấn công brute force vào mật khẩu người dùng rất phổ biến và không nên bỏ qua mối đe dọa này đối với các máy chủ Odoo. Odoo tạo một mục nhật ký bất cứ khi nào một nỗ lực đăng nhập được thực hiện và báo cáo kết quả (thành công hay không thành công) cùng với mục tiêu đăng nhập và IP nguồn.

Mục nhật ký có dạng như sau.

Đăng nhập thất bại:

```default
2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login failed for db:db_name login:admin from 127.0.0.1
```

Đăng nhập thành công:

```default
2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login successful for db:db_name login:admin from 127.0.0.1
```

Các nhật ký này có thể dễ dàng được phân tích bởi hệ thống phòng chống xâm nhập như `fail2ban`.

Ví dụ: định nghĩa bộ lọc fail2ban sau đây phải khớp với đăng nhập không thành công:

```default
[Definition]
failregex = ^ \d+ INFO \S+ \S+ Login failed for db:\S+ login:\S+ from <HOST>
ignoreregex =
```

Bạn có thể sử dụng với định nghĩa rào chắn để chặn IP tấn công trên HTTP(S).

Sau đây là những gì có thể xảy ra khi chặn IP trong 15 phút khi phát hiện 10 lần đăng nhập không thành công từ cùng một IP trong vòng 1 phút:

```default
[odoo-login]
enabled = true
port = http,https
bantime = 900  ; 15 min ban
maxretry = 10  ; if 10 attempts
findtime = 60  ; within 1 min  /!\ Should be adjusted with the TZ offset
logpath = /var/log/odoo.log  ;  set the actual odoo log path here
```

<a id="db-manager-security"></a>

### Bảo mật Trình Quản lý Cơ sở Dữ liệu

[Cấu hình Odoo](#setup-deploy-odoo) cho `admin_passwd` một cách ngắn gọn.

Thiết lập này được sử dụng trên tất cả các màn hình quản lý cơ sở dữ liệu (để tạo, xóa, kết xuất hoặc khôi phục cơ sở dữ liệu).

Nếu không muốn truy cập vào màn hình quản lý, bạn nên đặt tùy chọn cấu hình `list_db` thành `False` để chặn quyền truy cập vào tất cả các màn hình quản lý và lựa chọn cơ sở dữ liệu.

#### WARNING
Chúng tôi khuyến nghị bạn tắt Trình quản lý cơ sở dữ liệu cho mọi hệ thống có kết nối internet! Nó được dùng làm công cụ phát triển/demo để bạn có thể dễ dàng tạo và quản lý cơ sở dữ liệu nhanh chóng; nhưng không được thiết kế để sử dụng trong production và thậm chí có thể làm lộ các tính năng nguy hiểm cho kẻ tấn công. Nó cũng không có khả năng xử lý cơ sở dữ liệu lớn và có thể kích hoạt giới hạn bộ nhớ.

Trên các hệ thống production, quản trị viên hệ thống luôn là người thực hiện hoạt động quản lý cơ sở dữ liệu, bao gồm việc cung cấp cơ sở dữ liệu mới và sao lưu tự động.

Hãy nhớ thiết lập tham số `db_name` phù hợp (và `dbfilter`, nếu muốn) để hệ thống có thể xác định cơ sở dữ liệu đích cho mỗi yêu cầu. Nếu không, người dùng sẽ bị chặn vì họ không được phép tự chọn cơ sở dữ liệu.

Nếu màn hình quản lý chỉ có thể truy cập từ một nhóm máy được chọn, hãy sử dụng các tính năng của máy chủ proxy để chặn quyền truy cập vào tất cả tuyến bắt đầu bằng `/web/database` ngoại trừ (có thể) `/web/database/selector` hiển thị màn hình chọn cơ sở dữ liệu.

Nếu bạn muốn để màn hình quản lý cơ sở dữ liệu ở chế độ có thể truy cập được, cài đặt `admin_passwd` phải được thay đổi từ cài đặt mặc định `admin`: mật khẩu này được kiểm tra trước khi cho phép các thao tác thay đổi cơ sở dữ liệu.

Nó phải được lưu trữ an toàn và phải được tạo ngẫu nhiên, ví dụ:

```console
$ python3 -c 'import base64, os; print(base64.b64encode(os.urandom(24)))'
```

tạo ra một chuỗi ký tự giả ngẫu nhiên có thể in được gồm 32 ký tự.

### Đặt lại Mật khẩu Chính

Có thể xảy ra trường hợp mật khẩu chính bị thất lạc hoặc bị xâm phạm và cần phải đặt lại. Quy trình sau đây dành cho quản trị viên hệ thống của cơ sở dữ liệu Odoo on-premise, nêu chi tiết cách đặt lại và mã hóa lại mật khẩu chính theo cách thủ công.

#### SEE ALSO
Để biết thêm thông tin về cách thay đổi mật khẩu tài khoản Odoo.com, vui lòng tham khảo tài liệu này: [thay đổi mật khẩu tài khoản Odoo.com](administration/odoo_accounts.md#odoocom-change-password).

Khi tạo cơ sở dữ liệu on-premise mới, một mật khẩu chính ngẫu nhiên sẽ được tạo. Odoo khuyến khích sử dụng mật khẩu này để bảo mật cơ sở dữ liệu. Mật khẩu này được triển khai theo mặc định, do đó bất kỳ triển khai Odoo on-premise nào đều có một mật khẩu chính an toàn.

#### WARNING
Khi tạo cơ sở dữ liệu Odoo on-premise và chưa đặt mật khẩu này để bảo mật cơ sở dữ liệu, thì bất kỳ ai trên internet cũng có thể truy cập cài đặt.

Mật khẩu chính được xác định trong tệp cấu hình Odoo (`odoo.conf` hoặc `odoorc` (tệp ẩn)). Cần có mật khẩu chính Odoo để sửa đổi, tạo hoặc xóa cơ sở dữ liệu thông qua giao diện người dùng đồ họa (GUI).

#### Xác định vị trí tệp cấu hình

Đầu tiên, mở tệp cấu hình Odoo (`odoo.conf` hoặc `odoorc` (tệp ẩn)).

Windows

Tệp cấu hình nằm tại: `c:\ProgramFiles\Odoo{VERSION}\server\odoo.conf`

Linux

Tùy thuộc vào cách Odoo được cài đặt trên máy Linux, tệp cấu hình sẽ nằm ở một trong hai vị trí khác nhau:

- Cài đặt gói: `/etc/odoo.conf`
- Cài đặt nguồn: `~/.odoorc`

#### Thay đổi mật khẩu cũ

Sau khi mở tệp thích hợp, hãy tiến hành sửa đổi mật khẩu cũ trong tệp cấu hình thành mật khẩu tạm thời.

Giao diện đồ họa người dùng

Sau khi định vị được tệp cấu hình, hãy mở tệp đó bằng (). Bạn có thể thực hiện việc này chỉ bằng cách nhấp đúp vào tệp. Sau đó,  mặc định trên thiết bị sẽ mở tệp.

Tiếp theo, sửa đổi dòng mật khẩu chính, ví dụ `admin_passwd = $pbkdf2-sha…` thành `admin_passwd = newpassword1234`. Mật khẩu này có thể được đặt bất kỳ, miễn là nó được lưu tạm thời. Hãy nhớ sửa đổi tất cả ký tự sau dấu `=`.

Giao diện dòng lệnh

Sửa đổi dòng mật khẩu chính bằng lệnh Unix được trình bày chi tiết dưới đây.

Kết nối với thiết bị đầu cuối của máy chủ Odoo qua giao thức Secure Shell (SSH) và chỉnh sửa tệp cấu hình. Để chỉnh sửa tệp cấu hình, hãy nhập lệnh sau: **sudo nano /etc/odoo.conf**

Sau khi mở tệp cấu hình, sửa đổi dòng mật khẩu chính `admin_passwd = $pbkdf2-sha…` thành `admin_passwd = newpassword1234`. Mật khẩu này có thể được đặt bất kỳ, miễn là nó được lưu tạm thời. Hãy nhớ sửa đổi tất cả ký tự sau dấu `=`.

#### IMPORTANT
Điều quan trọng là phải đổi mật khẩu thành mật khẩu khác, thay vì kích hoạt đặt lại mật khẩu mới bằng cách thêm dấu chấm phẩy `;` vào đầu dòng. Điều này đảm bảo cơ sở dữ liệu được bảo mật trong suốt quá trình đặt lại mật khẩu.

#### Khởi động lại máy chủ Odoo

Sau khi đặt mật khẩu tạm thời, bạn **phải** khởi động lại máy chủ Odoo.

Giao diện đồ họa người dùng

Để khởi động lại máy chủ Odoo, trước tiên, hãy nhập `services` vào thanh Tìm kiếm của Windows. Sau đó, chọn ứng dụng Dịch vụ và cuộn xuống dịch vụ Odoo.

Tiếp theo, nhấp chuột phải vào Odoo và chọn Khởi động hoặc Khởi động lại. Hành động này sẽ khởi động lại máy chủ Odoo theo cách thủ công.

Giao diện dòng lệnh

Khởi động lại máy chủ Odoo bằng cách nhập lệnh: **sudo service odoo15 restart**

#### NOTE
Thay đổi số sau `odoo` cho phù hợp với phiên bản mà máy chủ đang chạy.

#### Sử dụng giao diện web để mã hóa lại mật khẩu

Đầu tiên, đi đến `/web/database/manager` hoặc `http://server_ip:port/web/database/manager` trong trình duyệt.

#### NOTE
Thay thế `server_ip` bằng địa chỉ IP của cơ sở dữ liệu. Thay thế `port` bằng cổng được đánh số mà cơ sở dữ liệu có thể truy cập được.

Tiếp theo, nhấp vào Đặt mật khẩu chính và nhập mật khẩu tạm thời đã chọn trước đó vào trường Mật khẩu chính. Sau bước này, nhập Mật khẩu chính mới. Mật khẩu chính mới sẽ được hash (hoặc mã hóa) sau khi nhấp vào nút Tiếp tục.

Đến đây thì mật khẩu đã được đặt lại thành công và phiên bản hash của mật khẩu mới sẽ xuất hiện trong tệp cấu hình.

#### SEE ALSO
Để biết thêm thông tin về bảo mật cơ sở dữ liệu Odoo, vui lòng tham khảo tài liệu này: [Bảo mật Trình Quản lý Cơ sở Dữ liệu](#db-manager-security).

## Các trình duyệt được hỗ trợ

Odoo hỗ trợ tất cả trình duyệt máy tính để bàn và thiết bị di động phổ biến hiện có trên thị trường, miễn là chúng được nhà phát hành hỗ trợ.

Đây là các trình duyệt được hỗ trợ:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Apple Safari

#### WARNING
Hãy đảm bảo trình duyệt của bạn là phiên bản mới và vẫn được nhà phát hành hỗ trợ trước khi gửi báo cáo lỗi.

#### NOTE
Kể từ Odoo 13.0, ES6 được hỗ trợ. Do đó, hỗ trợ IE bị loại bỏ.

* <a id='different-machines'>**[1]**</a> để nhiều cài đặt Odoo sử dụng cùng một cơ sở dữ liệu PostgreSQL hoặc cung cấp nhiều tài nguyên điện toán hơn cho cả hai phần mềm.
* <a id='remote-socket'>**[2]**</a> về mặt kỹ thuật, một công cụ như [socat](http://www.dest-unreach.org/socat/) có thể được sử dụng để ủy quyền các UNIX socket trên các mạng, nhưng chủ yếu dành cho phần mềm chỉ có thể được sử dụng trên các UNIX socket
* <a id='switching'>**[3]**</a> hoặc chỉ có thể truy cập qua mạng chuyển mạch gói nội bộ, nhưng điều đó đòi hỏi phải có các công tắc được bảo mật, bảo vệ chống lại [ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing) và ngăn chặn việc sử dụng WiFi. Ngay cả trên các mạng chuyển mạch gói an toàn, chúng tôi khuyến khích triển khai qua HTTPS, và các khoản chi phí có thể phát sinh sẽ giảm bớt vì chứng chỉ "tự ký" dễ triển khai hơn trên môi trường được kiểm soát so với qua internet.

<a id="postgresql-connection-settings"></a>
