# Đánh giá

Vào cuối cuộc *Trò chuyện trực tiếp*, khách hàng có cơ hội đánh giá chất lượng hỗ trợ mà họ nhận được từ *nhân viên* hỗ trợ. Khách hàng sẽ đưa ra đánh giá ngay khi họ đóng cuộc trò chuyện. Điều này giúp nhân viên nhận được phản hồi tức thì về hiệu quả làm việc của mình, đồng thời tạo cơ hội để khách hàng chia sẻ bất kỳ ý kiến hoặc nhận xét cuối cùng nào trước khi rời khỏi cửa sổ trò chuyện.

## Rate live chat conversations

Customers end a *live chat* conversation by clicking the X in the upper right-hand
corner of the chat window. They are then prompted to select an icon that reflects their level of
satisfaction. The icons represent the following ratings:

> - **Satisfied** - *green smiling face*
> - **Okay** - *yellow neutral face*
> - **Dissatisfied** - *red frowning face*
![View of the chat window from a user's side for Odoo Live Chat.](applications/websites/livechat/ratings/live-chat-ratings-faces.png)

#### NOTE
When customers end a conversation, a field marked Receive a copy of this conversation
appears under the *ratings* icons. Customers can enter their email either before or after they
submit a rating.

If the customer selects Satisfied (smile) icon, they are presented with a thank you
message and a Close Conversation link.

![View of customer's live chat window with thank you message.](applications/websites/livechat/ratings/live-chat-thank-you.png)

If the customer selects either Okay (neutral) icon or Dissatisfied (frown)
icon, a text box will appear. Customers can add comments in this text box to explain why they chose
this rating. This message will be sent to the live chat operator, along with the rating icon.

![View of a chat window from an operator's window highlighting a rating for Odoo Live Chat.](applications/websites/livechat/ratings/live-chat-ratings-operator-window.png)

## Publish customer ratings

To publish a channel's ratings on the website, first navigate to a live chat channel's record by
going to the Live Chat app and clicking on the kanban card for that team. Then
click on the Go to Website smart button. This will open the Live Chat Channel
Statistics page.

In the upper right corner of the page, click the red Unpublished slider.  The slider
changes from Unpublished to Published.

![View of the published ratings on the portal for Odoo Live Chat.](applications/websites/livechat/ratings/live-chat-ratings-unpublished.png)

#### NOTE
The customer notes that are submitted with the rating will *not* be published on the website.
These are kept internal. Only a statistical overview of the operators' performance for the
*channel* appears on the website.

### Add ratings page to site

Once the rating page has been published, it has to be manually added to the website. To do this, go
to the main Odoo dashboard and open the *Website* application. Website app‣ Site
‣ Content ‣ Pages, then click New.

This will open a New Page pop-up window. In the Page Title field, enter
`livechat`. This acts as the URL for the published webpage.

#### IMPORTANT
The URL *must* be named `livechat` in order for the database to recognize and connect the
ratings page. After the page has been published, the page title can be changed later under the
Menu Editor.

Click Create, and the newly created webpage will open. The Webpage Editor
appears in the right panel.

The page lists the names of the Live Chat Channels whose ratings pages have been
published. On the left side of the channel name is a speech bubble icon, which users can click on to
go to the ratings' page for the respective channel.

![View of the webpage for Live Chat ratings emphasizing the channel icon.](applications/websites/livechat/ratings/live-chat-published-icon.png)

Make any desired changes or additions to this page, then click Save in the top right of
the webpage editor. The website editor side panel closes, and the webpage remains on the screen.

Để đăng trang `trò chuyện trực tiếp`, hãy quay lại danh sách các trang của trang web bằng cách đi đến Trang web ‣ Nội dung ‣ Trang. Nhấp vào hộp kiểm bên trái `trò chuyện trực tiếp` trong danh sách các trang để chọn trang và tô sáng dòng. Sau đó, nhấp vào hộp kiểm bên dưới cột có nhãn Được đăng. Trường có hộp kiểm được tô sáng màu trắng. Nhấp vào hộp kiểm lần thứ hai để kích hoạt hộp Được đăng. Giờ đây, trang đã được đăng

![View of the list of pages for a website with the 'is published' box emphasized.](applications/websites/livechat/ratings/live-chat-is-published.png)

Khi trang đã được thêm vào trang web, các đánh giá sẽ được thiết lập để công khai theo mặc định. Tuy nhiên, các đánh giá riêng lẻ có thể được chọn thủ công để ẩn khỏi công chúng. Đánh giá đó vẫn sẽ được đưa vào các báo cáo nội bộ và vẫn có thể được xem bởi các nhóm nội bộ. Tuy nhiên, khách truy cập trang web công khai và người dùng cổng thông tin sẽ không có quyền truy cập.

See [Hide individual ratings](#livechat-overview-hide-ratings) for more information.

## Customer ratings report

The Customer Ratings report (Live Chat ‣ Report ‣ Customer Ratings)
displays an overview of the ratings received on individual support tickets, as well as any
additional comments submitted with the rating.

![View of the customer ratings report in Odoo Live Chat.](applications/websites/livechat/ratings/live-chat-ratings-report.png)

The report defaults to a kanban view, with each rating represented by a different card. To switch to
a different view, click on one of the icons in the upper-right corner of the screen. The report is
available in *list* view, *pivot* view, and *graph* view.

Click on an individual rating to see additional details about the conversation, and the rating.

<a id="livechat-overview-hide-ratings"></a>

### Hide individual ratings

Ratings are set to be published by default. However, individual ratings can be manually selected to
be hidden from the public. The rating will still be included in internal reports, and can still be
viewed by internal teams. However, public website visitors and portal users will not have access.

To hide a rating, go to Live Chat app ‣ Reports ‣ Customer Ratings. Click on
the kanban card for the rating to be hidden. On the individual rating's detail page, check the box
labeled Visible Internally Only.

![View of an individual rating's detail page with the visible internally setting checked.](applications/websites/livechat/ratings/live-chat-ratings-visible-internally.png)

#### SEE ALSO
- [Trò chuyện Trực tiếp](../livechat.md)
- [Commands and canned responses](responses.md)
- [Trang web](../website.md)
