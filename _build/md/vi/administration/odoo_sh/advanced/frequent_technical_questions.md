<a id="odoosh-advanced-frequent-technical-questions"></a>

# Câu hỏi về Kỹ thuật Thường gặp

## "Tác vụ đã lên lịch không diễn ra đúng vào thời điểm dự kiến"

Trên nền tảng Odoo.sh, chúng tôi không thể đảm bảo thời gian chạy chính xác của các tác vụ đã lên lịch.

Điều này là do có thể có nhiều khách hàng trên cùng một máy chủ và chúng tôi phải đảm bảo phân chia máy chủ một cách công bằng cho mỗi khách hàng. Do đó, các tác vụ đã lên lịch được triển khai hơi khác so với trên máy chủ Odoo thông thường và được chạy theo chính sách *nỗ lực hết sức*.

#### WARNING
Xin đừng mong đợi bất kỳ tác vụ đã lên lịch nào được thực hiện thường xuyên hơn 5 phút một lần.

## Có "giải pháp tối ưu nhất" về các tác vụ đã lên lịch không?

**Odoo.sh luôn giới hạn thời gian thực hiện các tác vụ đã lên lịch (\*hay còn gọi là\* cron).** Do đó, bạn cần ghi nhớ điều này khi phát triển cron của riêng mình.

Chúng tôi khuyên rằng:

- Các tác vụ đã lên lịch của bạn nên áp dụng cho các lô bản ghi nhỏ.
- Các tác vụ đã lên lịch của bạn sẽ hoạt động sau khi xử lý từng đợt; như vậy, nếu chúng bị gián đoạn do giới hạn thời gian, thì bạn sẽ không cần phải bắt đầu lại.
- Các tác vụ đã lên lịch của bạn phải [có tính bất biến](https://stackoverflow.com/a/1077421/3332416): chúng không được gây ra tác dụng phụ nếu được thực hiện thường xuyên hơn dự kiến.

<a id="ip-address-change"></a>

## Làm thế nào tôi có thể tự động hóa các nhiệm vụ khi địa chỉ IP thay đổi?

**Odoo.sh thông báo cho quản trị viên dự án về những thay đổi địa chỉ IP.** Ngoài ra, khi địa chỉ IP của phiên bản production thay đổi, yêu cầu HTTP `GET` sẽ được gửi đến đường dẫn `/_odoo.sh/ip-change` với địa chỉ IP mới được bao gồm dưới dạng tham số chuỗi truy vấn (`new`), cùng với địa chỉ IP trước đó dưới dạng tham số bổ sung (`old`).

Cơ chế này cho phép áp dụng các tác vụ tùy chỉnh để phản hồi lại sự thay đổi địa chỉ IP (VD: gửi email, liên hệ với API tường lửa, cấu hình đối tượng cơ sở dữ liệu,...)

Vì lý do bảo mật, tuyến `/_odoo.sh/ip-change` chỉ có thể được chính nền tảng truy cập nội bộ và sẽ trả về phản hồi `403` nếu được truy cập thông qua bất kỳ phương tiện nào khác.

Sau đây là một ví dụ triển khai giả lập:

```python
class IPChangeController(http.Controller):

    @http.route('/_odoo.sh/ip-change', auth='public')
    def ip_change(self, old=None, new=None):
        _logger.info("IP address changed from %s to %s", old, new)
        # Then perform whatever action required for your use case, e.g., update an
        # ir.config_parameter, send an email, contact an external firewall service's API, ...
        return 'ok'
```
