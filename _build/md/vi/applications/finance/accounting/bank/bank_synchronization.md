# Đồng bộ hoá ngân hàng

Odoo can synchronize directly with your bank institution to get all bank statements imported
automatically into your database.

To check if your bank is compatible with Odoo, go to [Odoo Accounting Features](https://www.odoo.com/page/accounting-features), and click on
See list of supported institutions.

Odoo supports more than 25,000 institutions around the world.

To connect to the banks, Odoo uses multiple web-services:

- **Plaid**: United States of America and Canada
- **Yodlee**: Toàn cầu
- [Salt Edge](applications/finance/accounting/bank/bank_synchronization/saltedge.md): Worldwide
- [Ponto](applications/finance/accounting/bank/bank_synchronization/ponto.md): Europe
- [Enable Banking](applications/finance/accounting/bank/bank_synchronization/enablebanking.md): Scandinavian countries

#### SEE ALSO
[Giao dịch](applications/finance/accounting/bank/transactions.md)

## Cấu hình

### Người dùng on-premise

Để sử dụng dịch vụ này, bạn cần có gói đăng ký Odoo Enterprise hợp lệ. Vì vậy hãy đảm bảo rằng cơ sở dữ liệu của bạn đã được đăng ký theo hợp đồng Odoo Enterprise. Chúng tôi cũng sử dụng proxy giữa cơ sở dữ liệu của bạn và nhà cung cấp bên thứ ba, nên trong trường hợp có lỗi kết nối, vui lòng kiểm tra xem bạn có đang sử dụng tường lửa hoặc proxy chặn địa chỉ sau không:

- [https://production.odoofin.com/](https://production.odoofin.com/)

### Đồng bộ hoá lần đầu

You can start synchronization either by going to the Accounting app and
Accounting ‣ Configuration ‣ Add a Bank Account.

Now you can search for your bank institution. Select it and follow the steps to synchronize with it.

#### NOTE
If you have any issues during your first synchronization, please verify that your
web browser doesn't block pop-ups and that your ad-blocker is disabled.

#### IMPORTANT
Khi thiết lập đồng bộ sao kê ngân hàng, Odoo tự động bắt đầu ghi lại các giao dịch kế toán từ ngày giao dịch cuối cùng +1 ngày (nếu ngày giao dịch cuối cùng là 31/12/2022, quá trình ghi nhận bắt đầu vào ngày 01/01/2023). Nếu sổ nhật ký không chứa giao dịch nào, Odoo sẽ truy xuất các giao dịch xa nhất có thể. Bạn có thể giới hạn thời gian Odoo truy xuất các giao dịch bằng cách mở ứng dụng Kế toán, vào Kế toán ‣ Ngày khoá sổ và cài đặt ngày trong trường Ngày khóa sổ bút toán.

Bạn phải cung cấp số điện thoại trong lần đồng bộ hóa đầu tiên để bảo vệ tài khoản của mình. Chúng tôi yêu cầu thông tin này vì chúng tôi không muốn dữ liệu của bạn rơi vào tay những đối tượng xấu. Do đó, nếu hiện hoạt động đáng ngờ trên tài khoản của bạn, chúng tôi sẽ chặn tất cả yêu cầu từ tài khoản, và bạn cần kích hoạt lại tài khoản bằng số điện thoại đó.

The third-party provider may request more information in order to connect with your bank
institution. This information is not stored on Odoo's servers.

By default, transactions fetched from an online source are grouped inside the same statement, and
one bank statement is created per month. You can change the bank statement creation periodicity
in your journal settings.

To view all your synchronizations, activate the [developer mode](applications/general/developer_mode.md#developer-mode) and go to
Accounting ‣ Configuration ‣ Online Synchronization.

### Đồng bộ thủ công

After your first synchronization, the created journals are synchronized by default every 12 hours.
If you wish, you can synchronize them manually by clicking on the Synchronize Now button
on the dashboard.

Alternatively, activate the [developer mode](applications/general/developer_mode.md#developer-mode), go to
Accounting ‣ Configuration ‣ Online Synchronization, select your institution,
and then click the Fetch transactions button.

#### IMPORTANT
Some institutions do not allow transactions to be fetched automatically. For such institutions,
during the automatic synchronization of the account, you receive an error message asking you to
disable the automatic synchronization. This message can be found in the chatter of your online
synchronizations. In this case, make sure to perform manual synchronizations.

## Các vấn đề

### Synchronization in error

To report a connection error to the [Odoo support](https://www.odoo.com/help), activate the
[developer mode](applications/general/developer_mode.md#developer-mode), go to Accounting ‣ Configuration ‣
Online Synchronization, select the connection that failed, and copy the error description and the
reference.

### Đồng bộ hóa bị ngắt kết nối

If your connection with the proxy is disconnected, you can reconnect with the proxy using the
Fetch Account button.

#### NOTE
If you are unable to reconnect using the Reconnect button, please contact the
[support](https://www.odoo.com/help) directly with your client id or the reference of the error
listed in the chatter.

<a id="migrationonlinesync"></a>

## Migration process for users having installed Odoo before December 2020

If you are on-premise, please first make sure that your source is up-to-date with the latest version
of Odoo.

Users who have created a database before December 2020 need to install the new module manually to
use the new functionalities.

To do so, go to Apps ‣ Update Apps List, remove the default filter in the search
bar and type `account_online_synchronization`. You can then click on Install.
Finally, make sure all your users refresh their Odoo page by pressing CTRL+F5.

#### NOTE
- All previous synchronizations are disconnected during the installation and will not work
  anymore. To view them, activate the [developer mode](applications/general/developer_mode.md#developer-mode) and go to
  Accounting ‣ Configuration ‣ Online Synchronization). It is not possible
  to resynchronize these connections; you have to make new ones.
- Do not uninstall the `account_online_sync` module, which is the previous module for online
  synchronization. The new one overrides it.
- By default, the `account_online_synchronization` module is installed automatically with
  Accounting.

## Câu hỏi thường gặp

### The synchronization is not working in real-time. Is that normal?

Quy trình này không hoạt động theo thời gian thực vì các nhà cung cấp bên thứ ba đồng bộ hóa tài khoản của bạn theo những khoảng thời gian khác nhau. Để bắt buộc đồng bộ và lấy báo cáo, hãy vào Trang chủ Kế toán của bạn và nhấp vào nút Đồng bộ ngay. Đồng bộ và lấy giao dịch bằng cách kích hoạt [chế độ lập trình viên](applications/general/developer_mode.md#developer-mode) và vào Kế toán ‣ Cấu hình ‣ Đồng bộ online. Một số nhà cung cấp chỉ cho phép làm mới một lần mỗi ngày; do đó, có thể việc nhấp vào Đồng bộ ngay sẽ không nhận được các giao dịch mới nhất của bạn nếu trước đó bạn đã thực hiện hành động này trong ngày.

A transaction can be visible on your bank account but not be fetched if it has the status
Pending. Only transactions with the Posted status will be retrieved. If the
transaction is not **Posted** yet, you will have to wait until the status changes.

### Is the Online Bank Synchronization feature included in my contract?

- **Community Edition**: No, this feature is not included in the Community Version.
- **Online Edition**: Yes, even if you benefit from the One App Free contract.
- **Enterprise Edition**: Yes, if you have a valid enterprise contract linked to your database.

### Some banks have a status "Beta." What does this mean?

Điều này có nghĩa là các tổ chức ngân hàng chưa được hỗ trợ hoàn toàn bởi Nhà cung cấp bên thứ ba của chúng tôi. Các lỗi hoặc vấn đề khác có thể xảy ra. Odoo không hỗ trợ những vấn đề kỹ thuật phát sinh với các ngân hàng trong giai đoạn Beta, nhưng người dùng vẫn có thể chọn kết nối. Việc kết nối với các ngân hàng này sẽ đóng góp vào quá trình phát triển vì Nhà cung cấp sẽ có dữ liệu thực và phản hồi từ kết nối.

### Why do my transactions only synchronize when I refresh manually?

Some banks have additional security measures and require extra steps, such as an SMS/email
authentication code or another type of MFA. Because of this, the integrator cannot pull transactions
until the security code is provided.

### Not all of my past transactions are in Odoo, why?

For some institutions, transactions can only be fetched up to 3 months in the past.

### Why don't I see any transactions?

During your first synchronization, you selected the bank accounts you decided to synchronize with
Odoo. If you didn't synchronize any of your accounts, activate the [developer mode](applications/general/developer_mode.md#developer-mode), go to Accounting ‣ Configuration ‣ Online Synchronization,
and click the Fetch Account button on the connection.

There may also be no new transactions.

If your bank account is properly linked to a journal and posted transactions are not visible in your
database, please [submit a support ticket](https://www.odoo.com/help).

### How can I update my bank credentials?

To update your credentials, activate the [developer mode](applications/general/developer_mode.md#developer-mode) and go to
Accounting ‣ Configuration ‣ Online Synchronization. Open the connection you
want to update your credentials and click the Update Credentials button.

* [Salt Edge](applications/finance/accounting/bank/bank_synchronization/saltedge.md)
* [Ponto](applications/finance/accounting/bank/bank_synchronization/ponto.md)
* [Enable Banking](applications/finance/accounting/bank/bank_synchronization/enablebanking.md)
