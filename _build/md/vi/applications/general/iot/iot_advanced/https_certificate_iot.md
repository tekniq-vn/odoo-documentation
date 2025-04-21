<a id="iot-https-certificate-iot"></a>

# Chứng chỉ HTTPS (IoT)

*Giao thức truyền tải siêu văn bản bảo mật* (HTTPS) là phiên bản mã hóa và an toàn của *Giao thức truyền tải siêu văn bản* (HTTP), giao thức chính được sử dụng để truyền dữ liệu giữa trình duyệt web và trang web. HTTPS bảo mật thông tin liên lạc bằng cách sử dụng giao thức mã hóa gọi là *Bảo mật tầng giao vận* (TLS), trước đây có tên là *Lớp cổng bảo mật* (SSL). Tính bảo mật của  dựa trên chứng chỉ /, giúp xác thực nhà cung cấp và kiểm tra danh tính của họ.

The use of HTTPS is required to communicate with certain network devices, particularly payment
terminals. If the HTTPS certificate is not valid, some devices cannot interact with the IoT
system.

#### NOTE
In this documentation and throughout Odoo, the term *HTTPS certificate*  refers to a valid
SSL certificate that allows an HTTPS connection.

<a id="iot-https-certificate-iot-generation"></a>

## HTTPS certificate generation

The HTTPS certificate is generated automatically. When the IoT system is (re-)started (e.g., after
it is connected to the Odoo database), a request is sent to [https://www.odoo.com](https://www.odoo.com), which returns
the HTTPS certificate if the IoT system and database meet the eligibility criteria:

<a id="iot-https-certificate-iot-iot-eligibility"></a>
- The database must be a **production** instance. The database instance should not be a copy, a
  duplicate, a staging, or a development environment.
- The Odoo subscription must be ongoing (In Progress status) and have an [IoT
  box subscription](../../iot.md#iot-iot-iot-subscription) line.

When the certificate has been received:

- The IoT system's homepage address is updated to a new HTTPS URL ending with `.odoo-iot.com`. Click
  the URL to establish a secure HTTPS connection.
  ![Odoo IoT app IoT box with .odoo-iot.com domain.](applications/general/iot/iot_advanced/https_certificate_iot/iot-new-domain.png)
- The HTTPS certificate banner displays the certificate's validity period. To view this
  information, click the <i class="fa fa-cogs"></i> (cogs) button on the IoT system's homepage.
  ![IoT box homepage with HTTPS certificate validity date.](applications/general/iot/iot_advanced/https_certificate_iot/https-valid.png)

## HTTPS certificate generation issues and errors

### The HTTPS certificate does not generate

Potential causes include the following:

- No [IoT box subscription](../../iot.md#iot-iot-iot-subscription) is linked to your account.
- The [IoT box subscription](../../iot.md#iot-iot-iot-subscription) was added *after* connecting the IoT
  system to the database. In this case, refresh the IoT system's homepage or reboot/[restart](../windows_iot.md#iot-windows-iot-restart) the IoT system to regenerate the HTTPS certificate.
- The firewall is preventing the HTTPS certificate from generating correctly. In this case,
  deactivate the firewall until the certificate is successfully generated.

  #### NOTE
  Some devices, such as routers with a built-in firewall, can prevent the HTTPS certificate from
  generating.

### The IoT system's homepage can be accessed using its IP address but not the `xxx.odoo-iot.com` URL

Contact your system or network administrator to address the issue. Network-related problems are
beyond the scope of Odoo support services.

- If the router allows manual  configuration, update the settings to
  use [Google DNS](https://developers.google.com/speed/public-dns).
- If the router does not support this, you need to update the DNS settings directly on each device
  that interacts with the IoT system to use [Google DNS](https://developers.google.com/speed/public-dns). Instructions for configuring DNS on individual
  devices can be found on the respective manufacturer's website.

#### NOTE
- Some IoT devices, such as payment terminals, likely do not require DNS changes, as they are
  typically pre-configured with custom DNS settings.
- On some browsers, an error code mentioning the DNS (such as `DNS_PROBE_FINISHED_NXDOMAIN`) is
  displayed.

### Lỗi

A specific error code is displayed on the IoT system's homepage if any issues occur during the
generation or reception of the HTTPS certificate.

#### `ERR_IOT_HTTPS_CHECK_NO_SERVER`

The server configuration is missing, i.e., the Odoo instance is not [connected](../connect.md) to
the IoT system.

#### `ERR_IOT_HTTPS_CHECK_CERT_READ_EXCEPTION`

An error occurred while attempting to read the existing HTTPS certificate.
Verify that the HTTPS certificate file is readable.

#### `ERR_IOT_HTTPS_LOAD_NO_CREDENTIAL`

The contract and/or database  is missing form the IoT.

Verify that both values are correctly configured. To update them, [access the IoT box's](../iot_box.md#iot-iot-box-homepage) or [Windows virtual IoT's homepage](../windows_iot.md#iot-windows-iot-homepage),
click the <i class="fa fa-cogs"></i> (cogs) button, then click Credential.

#### `ERR_IOT_HTTPS_LOAD_REQUEST_EXCEPTION`

An unexpected error occurred while the IoT system tried to reach [https://www.odoo.com](https://www.odoo.com). This is
likely due to network-related issues, such as:

- The IoT system does not have Internet access.
- Network restrictions (e.g., firewalls or VPNs) are preventing communication with
  [https://www.odoo.com](https://www.odoo.com).

#### NOTE
- Để xem đầy đủ chi tiết lỗi yêu cầu cùng thông tin liên quan đến lỗi, [kích hoạt chế độ lập trình viên](../../developer_mode.md#developer-mode), nhấp vào thẻ hệ thống IoT trong ứng dụng IoT, và chọn Tải nhật ký trên [biểu mẫu hệ thống IoT](../connect.md#iot-connect-iot-form). Để xác định mức độ nhật ký được ghi trong tệp nhật ký hệ thống IoT, [truy cập trang chủ hộp IoT](../windows_iot.md#iot-windows-iot-homepage) hoặc [IoT ảo Windows](../iot_box.md#iot-iot-box-homepage), nhấp vào nút <i class="fa fa-cogs"></i> (bánh răng), sau đó chọn Mức độ nhật ký ở cuối trang.
- To address network-related issues, contact your system or network administrator; these issues
  are beyond the scope of Odoo support services.

#### `ERR_IOT_HTTPS_LOAD_REQUEST_STATUS`

The IoT system successfully reached [https://www.odoo.com](https://www.odoo.com) but received an unexpected
[HTTP response (status codes)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

This error code includes the HTTP status. For example, `ERR_IOT_HTTPS_LOAD_REQUEST_STATUS 404` means
the server returned a "Page Not Found" response.

To solve this issue:

1. Open [https://www.odoo.com](https://www.odoo.com) in a web browser to check if the website is temporarily down for
   maintenance.
2. If [https://www.odoo.com](https://www.odoo.com) is down for maintenance, wait for it to resume.
   <br/>
   If the website is operational, open a [support ticket](https://www.odoo.com/help) and make
   sure to include the 3-digit HTTPS status code in the ticket.
   <br/>

#### `ERR_IOT_HTTPS_LOAD_REQUEST_NO_RESULT`

The IoT system successfully connected to [https://www.odoo.com](https://www.odoo.com), but the server refused to
provide the HTTPS certificate.

Check that the IoT system and database meet the [eligibility requirements](#iot-https-certificate-iot-iot-eligibility) for an HTTPS certificate.
