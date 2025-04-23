# Geo IP

#### NOTE
Tài liệu này chỉ áp dụng cho cơ sở dữ liệu On-premise.

## Cài đặt

1. Tải xuống cả cơ sở dữ liệu <[https://dev.maxmind.com/geoip/geoip2/geolite2/](https://dev.maxmind.com/geoip/geoip2/geolite2/)>\`_ Thành phố và Quốc gia GeoLite2. Bạn sẽ có được hai tệp có tên là `GeoLite2-City.mmdb` và `GeoLite2-Country.mmdb`.
2. Chuyển tệp đến thư mục `/usr/share/GeoIP/`.
   ```bash
   mv ~/Downloads/GeoLite2-City.mmdb /usr/share/GeoIP/
   mv ~/Downloads/GeoLite2-Country.mmdb /usr/share/GeoIP/
   ```
3. Khởi động lại máy chủ

#### NOTE
Nếu bạn không muốn định vị cơ sở dữ liệu geoip trong `/usr/share/GeoIP/`, hãy sử dụng tùy chọn [`--geoip-city-db`](../../developer/reference/cli.md#cmdoption-odoo-bin-geoip-city-db) và [`--geoip-country-db`](../../developer/reference/cli.md#cmdoption-odoo-bin-geoip-country-db) của giao diện dòng lệnh Odoo. Các tùy chọn này lấy đường dẫn tuyệt đối đến tệp cơ sở dữ liệu GeoIP và sử dụng nó làm cơ sở dữ liệu GeoIP. Ví dụ:

```bash
./odoo-bin --geoip-city-db= ~/Downloads/GeoLite2-City.mmdb
```

#### SEE ALSO
- [Tài liệu CLI](../../developer/reference/cli.md).

## Kiểm tra vị trí địa lý GeoIP trong trang web Odoo của bạn

Chỉnh sửa trang web để bao gồm một số thông tin geo-ip như tên quốc gia của địa chỉ IP yêu cầu hiện tại. Các bước thực hiện như sau:

1. Truy cập trang web của bạn. Mở trang trên trang web mà bạn muốn kiểm tra `GeoIP`.
2. Chọn Tuỳ chỉnh ‣ Trình soạn thảo HTML/CSS/JS.
3. Thêm đoạn XML sau vào trang:
   ```xml
   <h1 class="text-center" t-esc="request.geoip.country.name or 'geoip failure'"/>
   ```
4. Lưu và làm mới trang.

Geo-ip sẽ hoạt động nếu bạn thấy tên quốc gia của mình được hiển thị đậm ở giữa trang.

Nếu bạn thấy "**lỗi geoip**" thì lỗi định vị địa lý đã xảy ra. Các nguyên nhân phổ biến là:

1. Địa chỉ IP duyệt là localhost (`127.0.0.1`) hoặc mạng cục bộ. Nếu không biết, bạn có thể truy cập trang web của mình bằng dữ liệu di động.
2. Bạn đang sử dụng proxy đảo ngược (apache, nginx) trước Odoo nhưng không bật chế độ proxy khi khởi động Odoo. Tham khảo [`proxy mode`](../../developer/reference/cli.md#cmdoption-odoo-bin-proxy-mode).
3. Cơ sở dữ liệu GeoIP bị hỏng, bị thiếu hoặc không thể truy cập được. Trong trường hợp đó, cảnh báo đã được ghi vào nhật ký máy chủ.
