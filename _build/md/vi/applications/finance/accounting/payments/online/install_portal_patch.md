# Install the patch to disable online invoice payment

Following recent changes in Odoo 16, you might be warned that disabling the Invoice\
Online Payment setting will uninstall modules. If you want to disable the feature without\
uninstalling modules, follow the steps below to install the module **Payment - Account / Invoice**\
**Online Payment Patch**.

#### NOTE

If your Odoo database is created after the module **Payment - Account / Invoice Online Payment**\
**Patch** was released, you don't have anything to do.\
To check if the module is already installed, go to Apps, remove the `Apps` filter,\
and search for `account_payment`. If the module **Payment - Account / Invoice Online Payment**\
**Patch** is present and marked as installed, your Odoo database is already up-to-date and you\
are able to disable the feature without side-effect.\


## Update Odoo to the latest release

The possibility to disable the Invoice Online Payment setting without side-effect is\
made available through a new Odoo module; to be able to install it, you must make sure that your\
Odoo source code is up-to-date.

If you use Odoo on Odoo.com or Odoo.sh platform, your code is already up-to-date and you can proceed\
to the next step.

If you use Odoo with an on-premise setup or through a partner, you must update your installation as\
detailed in [this documentation page](administration/on_premise/update.md), or by contacting\
your integrating partner.

## Update the list of available modules

New modules must be _discovered_ by your Odoo instance to be available in the **Apps** menu.

To do so, activate the [developer mode](applications/general/developer_mode.md#developer-mode), and go to Apps ‣\
Update Apps List. A wizard will ask for confirmation.

## Install the module Invoice Online Payment Patch

#### WARNING

Bạn không bao giờ nên cài đặt phân hệ mới trong cơ sở dữ liệu production mà không thử nghiệm trước trên một bản sao hoặc môi trường staging. Đối với khách hàng Odoo.com, có thể tạo một cơ sở dữ liệu sao chép từ trang quản lý cơ sở dữ liệu. Đối với người dùng Odoo.sh, bạn nên sử dụng một cơ sở dữ liệu staging hoặc bản sao. Đối với người dùng on-premise, bạn nên sử dụng môi trường staging---liên hệ với đối tác tích hợp của bạn để biết thêm thông tin về cách kiểm thử một phân hệ mới trong thiết lập cụ thể của bạn.

Phân hệ hiện đã có sẵn trong menu Ứng dụng của bạn. Bỏ bộ lọc `Ứng dụng` và tìm kiếm `account_payment`; phân hệ Thanh toán - Bản vá thanh toán online cho tài khoản/hóa đơn sẽ hiển thị để cài đặt. Nếu không tìm thấy phân hệ sau khi đã cập nhật danh sách phân hệ có sẵn, nghĩa là mã nguồn Odoo của bạn chưa được cập nhật; hãy tham khảo lại bước đầu tiên trên trang này.

Once the module is installed, disabling the feature will work as intended and will not ask you to\
uninstall installed applications or modules.
