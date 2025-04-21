# Cơ sở dữ liệu bị vô hiệu hoá một phần

Cơ sở dữ liệu bị vô hiệu hoá một phần là cơ sở dữ liệu không dùng cho production và chứa một số tham số bị vô hiệu hóa. Điều này cho phép bạn thực hiện các kiểm thử mà không lo khởi chạy các quy trình tự động nhất định có thể ảnh hưởng đến dữ liệu production (ví dụ: gửi email cho khách hàng). Quyền truy cập trực tiếp bị xóa và chuyển thành môi trường kiểm thử.

#### NOTE
**Mọi cơ sở dữ liệu kiểm thử được tạo ra đều là cơ sở dữ liệu bị vô hiệu hóa một phần:**

- cơ sở dữ liệu sao lưu kiểm thử
- bản sao cơ sở dữ liệu
- đối với Odoo.sh: cơ sở dữ liệu staging và phát triển

#### IMPORTANT
Cơ sở dữ liệu cũng có thể bị vô hiệu hóa một phần khi nâng cấp, vì việc kiểm thử trước khi chuyển sang phiên bản mới là điều quan trọng.

## Tính năng bị vô hiệu hoá

Sau đây là danh sách chưa đầy đủ gồm các tính năng bị vô hiệu hóa:

- tất cả tác vụ đã lên kế hoạch (VD: tự động lập hóa đơn đăng ký, gửi thư hàng loạt,...)
- thư đi
- đồng bộ hoá ngân hàng
- nhà cung cấp dịch vụ thanh toán
- phương thức giao hàng
- token 
- chế độ hiển thị của trang web (ngăn chặn các công cụ tìm kiếm lập chỉ mục trang web của bạn)

#### NOTE
**Một banner màu đỏ sẽ hiển thị trên đầu màn hình cơ sở dữ liệu bị vô hiệu hóa một phần để bạn có thể nhìn thấy ngay lập tức.**
