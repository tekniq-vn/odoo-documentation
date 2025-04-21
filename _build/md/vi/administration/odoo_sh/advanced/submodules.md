<a id="odoosh-advanced-submodules"></a>

# Phân hệ phụ

## Tổng quan

[Phân hệ phụ Git](https://git-scm.com/book/en/v2/Git-Tools-Submodules) cho phép bạn tích hợp các dự án Git khác vào mã của mình mà không cần phải sao chép-dán toàn bộ mã của chúng.

Các phân hệ tùy chỉnh của bạn có thể phụ thuộc vào phân hệ từ các kho lưu trữ khác. Đối với Odoo, tính năng này cho phép bạn thêm phân hệ từ các kho lưu trữ Git khác vào các nhánh kho lưu trữ của bạn. Việc thêm các phụ thuộc này vào nhánh của bạn thông qua phân hệ phụ giúp bạn triển khai mã và máy chủ dễ dàng hơn, vì bạn có thể sao chép các kho lưu trữ được thêm dưới dạng phân hệ phụ cùng lúc sao chép kho lưu trữ của riêng mình.

Ngoài ra, bạn có thể chọn nhánh kho lưu trữ được thêm vào dưới dạng phân hệ phụ và có thể kiểm soát bản sửa đổi mà bạn muốn. Bạn có quyền quyết định xem có muốn ghim phân hệ phụ vào một bản sửa đổi cụ thể hay không và khi nào bạn muốn cập nhật lên bản sửa đổi mới hơn.

Trong Odoo.sh, các phân hệ phụ cung cấp cho bạn khả năng sử dụng và phụ thuộc vào những phân hệ có sẵn trong các kho lưu trữ khác. Nền tảng sẽ phát hiện việc bạn thêm phân hệ thông qua phân hệ phụ  trong nhánh và tự động thêm chúng vào đường dẫn addon của bạn để bạn có thể cài đặt chúng trong cơ sở dữ liệu của mình.

Nếu bạn thêm kho lưu trữ riêng tư dưới dạng phân hệ phụ trong các nhánh, bạn cần cấu hình mã khóa triển khai trong cài đặt dự án Odoo.sh và trong cài đặt kho lưu trữ của mình. Nếu không, Odoo.sh sẽ không được phép tải chúng xuống. Quy trình này được trình bày chi tiết trong chương [Cài đặt > Phân hệ phụ](../getting_started/settings.md#odoosh-gettingstarted-settings-submodules).

## Thêm một phân hệ phụ

### Với Odoo.sh (đơn giản)

#### WARNING
Hiện tại không thể thêm kho lưu trữ **riêng tư** bằng phương pháp này. Tuy nhiên, bạn vẫn có thể tiến hành [qua Git](#odoosh-advanced-submodules-withgit).

Trên Odoo.sh, trong chế độ xem nhánh của dự án, hãy chọn nhánh mà bạn muốn thêm phân hệ phụ.

Ở góc trên bên phải, nhấp vào nút *Phân hệ phụ*, sau đó nhấp vào *Chạy*.

![image](administration/odoo_sh/advanced/submodules/advanced-submodules-button.png)

Một hộp thoại có biểu mẫu sẽ hiển thị. Điền các thông tin đầu vào như sau:

* URL kho lưu trữ: URL SSH của kho lưu trữ.
* Nhánh: Nhánh bạn muốn sử dụng.
* Đường dẫn: Thư mục mà bạn muốn thêm phân hệ phụ này vào nhánh của mình.

![image](administration/odoo_sh/advanced/submodules/advanced-submodules-dialog.png)

Trên Github, bạn có thể lấy URL kho lưu trữ bằng nút *Sao chép hoặc tải xuống* của kho lưu trữ. Hãy nhớ *sử dụng SSH*.

![image](administration/odoo_sh/advanced/submodules/advanced-submodules-github-sshurl.png)

<a id="odoosh-advanced-submodules-withgit"></a>

### Với Git (nâng cao)

Trong terminal, trong thư mục nơi kho lưu trữ Git của bạn được sao chép, checkout nhánh mà bạn muốn thêm phân hệ phụ:

```bash
$ git checkout <branch>
```

Sau đó, thêm phân hệ phụ bằng lệnh dưới đây:

```bash
$ git submodule add -b <branch> <git@yourprovider.com>:<username/repository.git> <path>
```

Thay thế

*  *<git@yourprovider.com>:<username/repository.git>* bằng URL SSH của kho lưu trữ mà bạn muốn thêm dưới dạng phân hệ phụ,
*  *<branch>* bằng nhánh bạn muốn sử dụng trong kho lưu trữ trên,
*  *<path>* bằng thư mục mà bạn muốn thêm phân hệ phụ này.

Commit và push thay đổi của bạn:

```bash
$ git commit -a && git push -u <remote> <branch>
```

Thay thế

* <remote> bằng kho lưu trữ mà bạn muốn push các thay đổi của mình. Đối với thiết lập Git tiêu chuẩn, đây là *gốc*.
* <branch> bằng nhánh mà bạn muốn push các thay đổi của mình. Thường là nhánh mà bạn đã sử dụng `git checkout` ở bước đầu tiên.

Bạn có thể đọc [tài liệu git-scm.com](https://git-scm.com/book/en/v2/Git-Tools-Submodules) để tìm hiểu thêm về các phân hệ phụ Git. Ví dụ, nếu bạn muốn cập nhật phân hệ phụ của mình để có bản sửa đổi mới nhất, bạn có thể làm theo chương [Pull các thay đổi upstream](https://git-scm.com/book/en/v2/Git-Tools-Submodules#_pulling_in_upstream_changes_from_the_submodule_remote).

## Bỏ qua phân hệ

Nếu bạn thêm một kho lưu trữ chứa nhiều phân hệ, bạn có thể muốn bỏ qua một số phân hệ trong trường hợp có phân hệ được cài đặt tự động. Để làm như vậy, bạn có thể thêm tiền tố vào thư mục phân hệ phụ của mình bằng `.`. Nền tảng sẽ bỏ qua thư mục này và bạn có thể tự tay chọn phân hệ của mình bằng cách tạo liên kết tượng trưng đến chúng từ một thư mục khác.
