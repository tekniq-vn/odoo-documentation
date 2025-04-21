# Tích hợp Silverfin

[Silverfin](https://www.silverfin.com) is a third-party service provider that offers a cloud
platform for accountants.

Odoo and Silverfin provide an integration to automate the synchronization of data.

## Cấu hình

To configure this integration, you need to input the following data into your Silverfin account:

- địa chỉ email của người dùng
- [Odoo API key](#silverfin-api-key)
- URL of the Odoo database
- name of your Odoo database

<a id="silverfin-api-key"></a>

### Khoá Odoo API

You can create Odoo external API keys either [for a single database](#silverfin-api-singledb)
(hosting: Odoo Online, On-premise, and Odoo.sh) or [for all databases managed by a single user](#silverfin-api-multipledb) (hosting: Odoo Online).

#### IMPORTANT
- These API keys are personal and provide full access to your user account. Store it securely.
- You can copy the API key only at its creation. It is not possible to retrieve it later.
- If you need it again, create a new API key (and delete the old one).

#### SEE ALSO
[External API](../../../../developer/reference/external_api.md)

<a id="silverfin-api-singledb"></a>

#### Per database

To add an API key to a **single** database, connect to the database, enable the [developer
mode](../../../general/developer_mode.md#developer-mode), click on the user menu, and then My Profile /
Preferences. Under the Account Security tab, click on New API
Key, confirm your password, give a descriptive name to your new key, and copy the API key.

![creation of an Odoo external API key for a database](applications/finance/accounting/reporting/silverfin/api-key-db.png)

#### SEE ALSO
[API Keys](../../../../developer/reference/external_api.md#api-external-api-keys)

<a id="silverfin-api-multipledb"></a>

#### For all databases (fiduciaries)

Để thêm một khóa API vào *tất cả* cơ sở dữ liệu được quản lý bởi một người dùng duy nhất cùng lúc **(phương pháp dễ dàng nhất cho những người làm công việc tài chính)**, hãy truy cập vào trang web của Odoo <[https://www.odoo.com](https://www.odoo.com)>_ và đăng nhập bằng tài khoản quản trị viên của bạn. Sau đó, mở cài đặt bảo mật tài khoản ở chế độ lập trình viên <[https://www.odoo.com/my/security?debug=1](https://www.odoo.com/my/security?debug=1)>_, nhấp vào Khoá API mới, xác nhận mật khẩu của bạn, đặt tên mô tả cho khóa API mới của bạn và sao chép khóa API mới.

![creation of an Odoo external API key for an Odoo user](applications/finance/accounting/reporting/silverfin/api-key-user.png)
