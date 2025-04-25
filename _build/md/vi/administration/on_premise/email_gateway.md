# Cổng email

Cổng email Odoo cho phép bạn trực tiếp chèn tất cả email đã nhận vào Odoo.

Nguyên lý của nó rất đơn giản: máy chủ SMTP của bạn sẽ thực thi tập lệnh "mailgate" cho mỗi email mới đến.

Tập lệnh này sẽ xử lý việc kết nối với cơ sở dữ liệu Odoo của bạn thông qua XML-RPC và gửi email qua tính năng `MailThread.message_process()`.

## Điều kiện tiên quyết

- Quyền truy cập cấp quản trị viên vào cơ sở dữ liệu Odoo.
- Máy chủ email của riêng bạn, ví dụ như Postfix hoặc Exim.
- Kiến thức chuyên môn về cách cấu hình máy chủ email.

## Đối với Postfix

Trong cấu hình bí danh của bạn (`/etc/aliases`):

```text
email@address: "|/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>"
```

#### NOTE
Nguồn lực

- [Postfix](http://www.postfix.org/documentation.html)
- [bí danh Postfix](http://www.postfix.org/aliases.5.html)
- [Postfix virtual](http://www.postfix.org/virtual.8.html)

## Đối với Exim

```text
*: |/odoo-directory/addons/mail/static/scripts/odoo-mailgate.py -d <database-name> -u <userid> -p <password>
```

#### NOTE
Nguồn lực

- [Exim](https://www.exim.org/docs.html)
