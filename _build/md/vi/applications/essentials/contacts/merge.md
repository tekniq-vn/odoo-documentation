# Gộp liên hệ

Ứng dụng *Liên hệ* của Odoo cho phép người dùng gộp các liên hệ trùng lặp mà không làm mất bất kỳ thông tin nào trong quá trình này. Điều này giúp cơ sở dữ liệu được sắp xếp hợp lý và ngăn việc nhiều chuyên viên sales liên hệ với cùng một liên hệ.

<a id="contacts-merge-duplicate"></a>

## Gộp liên hệ trùng lặp

Đi đến ứng dụng Liên hệ, và chọn biểu tượng <i class="oi oi-view-list"></i> (danh sách). Chọn hai hoặc nhiều liên hệ trùng lặp từ danh sách và đánh dấu vào hộp kiểm (ở bên trái) của các liên hệ cần được gộp. Sau đó, nhấp vào biểu tượng <i class="fa fa-cog"></i> Tác vụ, và chọn Gộp từ menu kết quả thả xuống.

![Tùy chọn gộp liên hệ trong ứng dụng Liên hệ.](applications/essentials/contacts/merge/merge-menu.png)

Thao tác này sẽ mở cửa sổ bật lên Gộp. Từ đây, hãy xem lại thông tin của các liên hệ trước khi xác nhận có nên gộp chúng hay không. Nếu có bất kỳ liên hệ nào trong danh sách **không** nên gộp, hãy nhấp vào biểu tượng <i class="fa fa-times"></i> (xoá) ở phía bên phải của liên hệ.

![Cửa sổ bật lên để gộp trong ứng dụng Liên hệ.](applications/essentials/contacts/merge/merge-window.png)

Nhấp vào trường Liên hệ đích và chọn một tùy chọn từ danh sách thả xuống. Trường này mặc định là bản ghi liên hệ được tạo đầu tiên trong hệ thống.

Sau khi xác nhận thông tin trên cửa sổ bật lên, hãy nhấp vào Gộp liên hệ.

## Chống trùng lặp liên hệ

Sau khi quá trình gộp hoàn tất, một cửa sổ bật lên sẽ xuất hiện để xác nhận quá trình gộp đã hoàn tất. Cửa sổ bật lên này cũng chứa nút Chống trùng lặp các liên hệ khác. Tính năng này tìm kiếm các bản ghi trùng lặp, dựa trên những tiêu chí đã chọn và tự động gộp chúng hoặc gộp sau khi phê duyệt thủ công.

Nhấp vào nút Chống trùng lặp các liên hệ khác để mở cửa sổ bật lên Chống trùng lặp liên hệ.

Chọn một hoặc nhiều trường để sử dụng trong tìm kiếm các bản ghi trùng lặp. Có thể tìm kiếm các liên hệ trùng lặp dựa trên những tiêu chí sau:

- Email
- Tên
- Công ty
- Thuế GTGT
- Công ty mẹ

#### NOTE
Nếu chọn nhiều hơn một trường, chỉ những bản ghi có **tất cả** các trường giống nhau mới được đề xuất là bản ghi trùng lặp.

Nếu cần, hãy chọn tiêu chí được sử dụng để loại trừ các bản sao tiềm ẩn khỏi tìm kiếm. Các bản sao tiềm ẩn có thể bị loại trừ khỏi tìm kiếm dựa trên những tiêu chí sau:

- Người dùng liên kết với liên hệ
- Hạng mục bút toán liên quan đến liên hệ

Sau khi xác nhận tiêu chí tìm kiếm, hãy nhấp vào :guilabel: `Gộp thông qua kiểm tra thủ công`, :guilabel: `Gộp tự động` hoặc :guilabel: `Gộp tự động tất cả quy trình`.

Nếu chọn Gộp thông qua kiểm tra thủ công, hãy hoàn tất quá trình gộp bằng cách làm theo [các bước trên](#contacts-merge-duplicate).
