<a id="setup-update"></a>

# Cập nhật gỡ lỗi

## Giới thiệu

Để được hưởng lợi từ những cải tiến mới nhất, bản sửa lỗi bảo mật, sửa lỗi và tăng hiệu suất, thỉnh thoảng bạn có thể cần cập nhật cài đặt Odoo của mình.

Hướng dẫn này chỉ áp dụng khi bạn sử dụng Odoo trên cơ sở hạ tầng lưu trữ của riêng bạn. Nếu bạn đang sử dụng một trong các giải pháp Odoo Đám mây, các bản cập nhật sẽ tự động được thực hiện.

Thuật ngữ liên quan đến cập nhật phần mềm thường gây nhầm lẫn. Vì vậy, sau đây là một số định nghĩa sơ bộ:

Cập nhật (một cài đặt Odoo)
: Chỉ quá trình lấy bản sửa đổi mã nguồn mới nhất cho Phiên bản Odoo hiện tại của bạn. Ví dụ: cập nhật Odoo Enterprise 13.0 lên bản sửa đổi mới nhất. Việc này không trực tiếp gây ra bất kỳ thay đổi nào về nội dung của cơ sở dữ liệu Odoo của bạn và có thể được hoàn tác bằng cách cài đặt lại bản sửa đổi mã nguồn trước đó.

Nâng cấp (một cơ sở dữ liệu Odoo)
: Chỉ một hoạt động xử lý dữ liệu phức tạp trong đó cấu trúc và nội dung cơ sở dữ liệu của bạn được thay đổi vĩnh viễn để tương thích với phiên bản mới của Odoo. Hoạt động này không thể được hoàn tác và thường được thực hiện thông qua [dịch vụ nâng cấp cơ sở dữ liệu](https://upgrade.odoo.com) của Odoo, khi bạn quyết định chuyển sang phiên bản mới hơn. Thông thường, quá trình này cũng được gọi là "di chuyển" vì nó liên quan đến việc di chuyển dữ liệu trong cơ sở dữ liệu, dù cơ sở dữ liệu có thể vẫn nằm tại cùng một vị trí vật lý sau khi nâng cấp.

Trang này mô tả các bước thông thường cần thiết để *cập nhật* cài đặt Odoo lên phiên bản mới nhất. Nếu bạn muốn biết thêm thông tin về việc nâng cấp cơ sở dữ liệu, vui lòng truy cập [Trang Nâng cấp Odoo](https://upgrade.odoo.com).

## Tóm tắt

Việc cập nhật Odoo được thực hiện đơn giản bằng cách cài đặt lại bản mới nhất của Phiên bản Odoo trên bản cài đặt hiện tại của bạn. Việc này sẽ bảo toàn dữ liệu của bạn mà không gây ra bất kỳ thay đổi nào, miễn là bạn không gỡ cài đặt PostgreSQL (hệ quản trị cơ sở dữ liệu đi kèm với Odoo).

Tài liệu tham khảo chính về cập nhật là [hướng dẫn cài đặt](administration/on_premise.md) của Odoo, trong đó giải thích các phương pháp cài đặt phổ biến.

Việc cập nhật cũng nên được thực hiện bởi người triển khai Odoo lúc ban đầu, vì quy trình này rất giống nhau.

#### NOTE
Chúng tôi luôn khuyến khích tải xuống phiên bản Odoo hoàn chỉnh mới, thay vì sử dụng các bản vá thủ công, chẳng hạn như các bản vá bảo mật đi kèm với Tư vấn Bảo mật. Các bản vá chủ yếu được cung cấp cho các cài đặt được tùy chỉnh nhiều hoặc cho chuyên viên kỹ thuật muốn áp dụng các thay đổi nhỏ tạm thời trong khi kiểm thử bản cập nhật hoàn chỉnh.

## Bước 1: Tải xuống phiên bản Odoo đã cập nhật

Trang tải xuống chính là [https://www.odoo.com/page/download](https://www.odoo.com/page/download). Nếu bạn thấy liên kết "Mua" để tải xuống Odoo Enterprise, hãy đảm bảo bạn đã đăng nhập vào Odoo.com bằng cùng thông tin đăng nhập được liên kết với gói đăng ký Odoo Enterprise của bạn.

Ngoài ra, bạn có thể sử dụng liên kết tải xuống duy nhất có trong email xác nhận mua Odoo Enterprise của mình.

#### NOTE
Không cần tải xuống bản cập nhật nếu bạn cài đặt qua Github (xem thông tin dưới đây)

## Bước 2: Sao lưu cơ sở dữ liệu của bạn

Dù quy trình cập nhật khá an toàn và không làm thay đổi dữ liệu của bạn, nhưng tốt nhất là luôn sao lưu toàn bộ cơ sở dữ liệu trước khi thực hiện bất kỳ thay đổi nào trên bản cài đặt và lưu trữ ở nơi an toàn trên một máy tính khác.

Nếu bạn chưa vô hiệu hóa màn hình quản lý cơ sở dữ liệu (xem lý do bạn nên làm vậy [tại đây](administration/on_premise/deploy.md#security)), bạn có thể sử dụng nó (liên kết ở cuối màn hình lựa chọn cơ sở dữ liệu) để tải xuống bản sao lưu (các) cơ sở dữ liệu của bạn. Nếu đã vô hiệu hóa, hãy thực hiện đúng theo quy trình như các bản sao lưu thông thường của bạn.

## Bước 3: Cài đặt bản cập nhật

Chọn phương pháp phù hợp với cài đặt hiện tại của bạn:

### Trình cài đặt trọn gói

Nếu bạn đã cài đặt Odoo bằng gói cài đặt được tải xuống trên trang web của chúng tôi (phương pháp được đề xuất), thì việc cập nhật diễn ra rất đơn giản. Tất cả những gì bạn phải làm là tải xuống gói cài đặt tương ứng với hệ thống (xem bước #1) và cài đặt nó trên máy chủ của mình. Chúng được cập nhật hàng ngày và bao gồm các bản sửa lỗi bảo mật mới nhất. Thông thường, bạn chỉ cần nhấp đúp vào gói để cài đặt nó trên bản cài đặt hiện tại. Sau khi cài đặt gói, hãy nhớ khởi động lại dịch vụ Odoo hoặc khởi động lại máy chủ của bạn. Thế là bạn đã hoàn tất.

### Cài đặt nguồn (Tarball)

Nếu ban đầu bạn cài đặt Odoo với phiên bản "tarball" (kho lưu trữ mã nguồn), bạn phải thay thế thư mục cài đặt bằng phiên bản mới hơn. Trước tiên, hãy tải xuống tarball mới nhất từ ​​Odoo.com. Chúng được cập nhật hàng ngày và bao gồm các bản sửa lỗi bảo mật mới nhất (xem bước #1) Sau khi tải xuống gói này, hãy giải nén nó trong một vị trí tạm thời trên máy chủ của bạn.

Bạn sẽ nhận được một thư mục được gắn nhãn với phiên bản mã nguồn, ví dụ "odoo-13.0+e.20190719", chứa một thư mục "odoo.egg-info" và thư mục mã nguồn thực tế có tên "odoo" (đối với Odoo 10 trở lên) hoặc "openerp" đối với các phiên bản cũ hơn. Bạn có thể bỏ qua thư mục odoo.egg-info. Xác định vị trí thư mục mà cài đặt hiện tại của bạn được triển khai và thay thế bằng thư mục "odoo" hoặc "openerp" mới hơn có trong tệp lưu trữ mà bạn vừa giải nén.

Hãy chắc chắn rằng bố cục thư mục trùng khớp, ví dụ thư mục "addons" mới có trong mã nguồn phải nằm chính xác tại cùng đường dẫn trước đó. Tiếp theo, hãy chú ý đến bất kỳ tệp cấu hình cụ thể nào mà bạn có thể đã sao chép hoặc sửa đổi thủ công trong thư mục cũ và sao chép chúng sang thư mục mới. Cuối cùng, hãy khởi động lại dịch vụ Odoo hoặc khởi động lại máy. Thế là bạn đã hoàn tất.

### Cài đặt nguồn (Github)

Nếu ban đầu bạn cài đặt Odoo bằng bản sao Github đầy đủ của kho lưu trữ chính thức, thì quy trình cập nhật yêu cầu bạn phải pull mã nguồn mới nhất qua git. Tiến hành thay đổi trong thư mục cho mỗi kho lưu trữ (kho lưu trữ Odoo chính và kho lưu trữ Enterprise) và chạy các lệnh sau:

```default
git fetch
git rebase --autostash
```

Lệnh cuối cùng có thể gặp xung đột mã nguồn nếu bạn đã chỉnh sửa mã nguồn Odoo cục bộ. Thông báo lỗi sẽ cung cấp cho bạn danh sách các tệp có xung đột và bạn sẽ cần xử lý xung đột theo cách thủ công, bằng cách chỉnh sửa chúng và quyết định cần giữ lại phần nào của mã.

Ngoài ra, nếu bạn chỉ muốn loại bỏ những thay đổi xung đột và khôi phục bản chính thức, bạn có thể sử dụng lệnh sau:

```default
git reset --hard
```

Cuối cùng, khởi động lại dịch vụ Odoo hoặc khởi động lại máy là xong.

### Docker

Vui lòng tham khảo [Tài liệu hình ảnh Docker](https://hub.docker.com/_/odoo/) của chúng tôi để biết hướng dẫn cập nhật cụ thể.
