# Use channels for team communication

Use channels in the Odoo *Discuss* app to organize discussions between individual teams,
departments, projects, or any other group that requires regular communication. With channels,
employees can communicate inside dedicated spaces within the Odoo database around specific topics,
updates, and latest developments having to do with the organization.

## Public and private channels

Mọi người đều có thể xem kênh *Công khai*, trong khi kênh *Riêng tư* chỉ hiển thị với những người dùng được mời. Để tạo kênh mới, đi đến ứng dụng Thảo luận, sau đó nhấp vào biểu tượng ➕ (dấu cộng) bên cạnh tiêu đề Kênh trong menu bên trái. Sau khi nhập tên kênh, hai tùy chọn có thể chọn sẽ xuất hiện: Tùy chọn đầu tiên là kênh có dấu thăng (`#`) để chỉ ra rằng đó là kênh công khai; tùy chọn thứ hai là kênh có biểu tượng ổ khóa (`🔒`) bên cạnh để chỉ ra rằng đó là kênh riêng tư. Chọn loại kênh phù hợp nhất với nhu cầu trao đổi thông tin.

![View of discuss's sidebar and a channel being created in Odoo Discuss.](applications/productivity/discuss/team_communication/public-private-channel.png)

### Tuỳ chọn cấu hình

The channel's Group Name, Description, and Privacy settings can
be modified by clicking on the channel's settings, represented by a ⚙️ (gear) icon in
the left sidebar menu, next to the channel's name.

![View of a channel's settings form in Odoo Discuss.](applications/productivity/discuss/team_communication/channel-settings.png)

#### Privacy and Members tabs

Changing Who can follow the group's activities? controls which groups can have access to
the channel.

#### NOTE
Allowing Everyone to follow a private channel lets other users view and join it, as
they would a public one.

When choosing Invited people only, specify in the Members tab which members
should be invited. Inviting members can also be done from the *Discuss* app's main dashboard, by
selecting the channel, clicking the *add user* icon in the top-right corner of the dashboard, and
finally clicking Invite to Channel once all the users have been added.

![View of Discuss' option to invite members in Odoo Discuss.](applications/productivity/discuss/team_communication/invite-channel.png)

When the Selected group of users option is selected, it reveals the ability to add an
Authorized Group, along with the options to Auto Subscribe Groups and
Auto Subscribe Departments.

The option to Auto Subscribe Groups automatically adds users of that particular user
group as followers. In other words, while Authorized Groups limits which users can
access the channel, Auto Subscribe Groups automatically adds users as members as long as
they are part of a specific user group. The same is true for Auto Subscribe Departments.

## Thanh tìm kiếm nhanh

Once at least 20 channels, direct messages, or live chat conversations (if *Live Chat* module is
installed on the database) are pinned in the sidebar, a Quick search… bar is displayed.
This feature is a convenient way to filter conversations and quickly find relevant communications.

![View of the Discuss' sidebar emphasizing the quick search bar in Odoo Discuss.](applications/productivity/discuss/team_communication/quick-search.png)

### Tìm kênh

Nhấp vào biểu tượng cài đặt ⚙️ (bánh răng) nằm trên thanh bên trái, bên phải mục menu có thể thu gọn KÊNH. Thao tác này sẽ dẫn đến chế độ xem dạng lưới hiển thị tất cả các kênh công khai có sẵn. Người dùng có thể tham gia hoặc rời kênh trên màn hình này bằng cách nhấp vào nút THAM GIA hoặc RỜI KHỎI xuất hiện trong các ô kênh.

There is also the ability to apply filtering criteria and save them for later use. The
Search... function accepts wildcards by using the underscore character [ `_` ], and
specific searches can be saved by using the Favorites ‣ Save Current Search
drop-down menu.

![View of a channel being searched through filters in Odoo Discuss](applications/productivity/discuss/team_communication/filter.png)

## Linking channel in chatter

Các kênh có thể được liên kết trong phần cửa sổ trò chuyện (ghi chú nhật ký) của một bản ghi trong Odoo. Để thực hiện, chỉ cần nhập: `#` và tên kênh. Nhấp hoặc nhấn Enter vào tên *kênh*. Sau khi ghi lại ghi chú, liên kết đến kênh sẽ xuất hiện. Khi nhấp vào liên kết, cửa sổ trò chuyện với kênh sẽ hiện lên ở góc dưới bên phải màn hình.

Users are able to contribute to this group channel (either public or member based) by typing
messages in window and pressing *enter*.

![Channel linked in chatter with the channel open on the lower right quadrant.](applications/productivity/discuss/team_communication/chatter-channel.png)

#### SEE ALSO
- [Thảo luận](../discuss.md)
- [Hoạt động](../../essentials/activities.md)
