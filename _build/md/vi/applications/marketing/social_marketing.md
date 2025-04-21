# Marketing trên Mạng xã hội

Odoo's *Social Marketing* application helps content marketers create and schedule posts, manage
various social media accounts, analyze content effectiveness, and engage directly with social media
followers in one, centralized location.

#### SEE ALSO
- [Odoo Tutorials: Marketing](https://www.odoo.com/slides/marketing-27)

## Social media accounts

In order to create social posts and analyze content with Odoo *Social Marketing*, social media
accounts **must** be added as a *stream* on the application's main dashboard.

#### NOTE
Be aware that personal profiles **cannot** be added as a stream. The main use of Odoo *Social
Marketing* is to manage and analyze business accounts on social media platforms.

#### WARNING
Odoo *Social Marketing* has some limitations in regards to social media accounts. For example,
Odoo **cannot** handle a large quantity of various pages (e.g. ~40 pages) under the same company.
The same limitations are present in a multi-company environment because of how the API is
constructed.

#### WARNING
In multi-company environments, if every company doesn't activate a page at once, it will result
in a permission error.

For example, if Company 1 is the only company selected from the main Odoo dashboard, and
activates *Facebook Page 1* and *Facebook Page 2*, then those pages will be accesible on the
*Social Marketing* dashboard.

However, if on that same database, the user adds Company 2 from the company drop-down menu in the
header, and attempts to add those same streams, it results in a permission error.

![View of the permission error that appears when incorrectly attempting to add stream.](applications/marketing/social_marketing/permission-error.png)

## Social media streams

To add a social media business account as a stream, navigate to Social Marketing
app and select the Add A Stream button located in the upper-left corner. Doing so
reveals an Add a Stream pop-up window.

![View of the pop-up window that appears when Add a Stream is selected in Odoo.](applications/marketing/social_marketing/add-stream-social-popup.png)

In the Add a Stream pop-up window, choose to Link a new account for a
business from any of the following popular social media platforms: Facebook,
Instagram, LinkedIn, Twitter, and YouTube.

After clicking the desired social media outlet from the Add a Stream pop-up window, Odoo
navigates directly to that specific social media outlet's authorization page, where permission must
be granted, in order for Odoo to add that particular social media account as a stream to the *Social
Marketing* application.

![Sample of a populated social marketing dashboard with social media streams and content.](applications/marketing/social_marketing/social-marketing-dashboard.png)

Once permission is granted, Odoo navigates back to the Feed on the main
Social Marketing dashboard, and a new column, with that account's posts, is added.
Accounts/streams can be added at any time.

#### IMPORTANT
A Facebook page can be added as long as the Facebook account that grants
permission is the administrator for the page. It should also be noted that different pages can be
added for different streams.

#### NOTE
Instagram accounts are added through a Facebook login because it uses the
same API. This means, an Instagram account needs to be linked to a
Facebook account in order for it to show up as a stream in Odoo.

## Social media page

Another way to quickly link social media accounts to Odoo *Social Marketing* can be done on the
Social Media page. To access the Social Media page, navigate to
Social Marketing app ‣ Configuration ‣ Social Media.

On the Social Media page there is a collection of all social media options, each
complete with a Link account button: Facebook, Instagram,
LinkedIn, Twitter, YouTube, and Push Notifications.

![View of the social media page in the Odoo Social Marketing application.](applications/marketing/social_marketing/social-media-page.png)

## Social accounts page

To see a list of all social accounts and websites linked to the database, go to
Social Marketing app ‣ Configuration ‣ Social Accounts. This Social
Accounts display the Name, the Handle/Short Name, the Social
Media platform, who it was Created by, and the Company to which it is
associated.

![View of the social accounts page in the Odoo Social Marketing application.](applications/marketing/social_marketing/social-accounts-page.png)

To edit/modify any of the social accounts on this page, simply select the desired account from the
list on this page, and proceed to make any adjustments necessary.

## Social streams page

To view a separate page with all the social media streams that have been added to the main *Social
Marketing* dashboard, navigate to Social Marketing app ‣ Configuration ‣ Social
Streams.

![View of the social accounts page in the Odoo Social Marketing application.](applications/marketing/social_marketing/social-streams-page.png)

Here, the social stream information is organized in a list with the Social Media, the
Title of the stream, the Type of the stream (e.g. Posts,
Keyword, etc.), who it was Created by, and  the Company to which
it is associated.

To modify any stream's information, simply click the desired stream from the list, and proceed to
make any necessary adjustments.

## Khách truy cập

To see a complete overview of all the people who have visited the website(s) connected to the
database, navigate to Social Marketing app ‣ Visitors.

![View of the Visitors page in the Odoo Social Marketing application.](applications/marketing/social_marketing/visitors.png)

Here, Odoo provides a detailed layout of all the visitors' pertinent information in a default kanban
view. If visitors already have contact information in the database, the option to send them an
Email and/or an SMS is available.

This same visitor data can also be viewed as a list or a graph. Those view options are located in
the upper-right corner of the Visitors page.

* [Social posts](social_marketing/social_posts.md)
  * [Posts page](social_marketing/social_posts.md#posts-page)
    * [Bài viết](social_marketing/social_posts.md#posts)
    * [Create leads from comments](social_marketing/social_posts.md#create-leads-from-comments)
    * [Thông tin chi tiết](social_marketing/social_posts.md#insights)
  * [Create and post social media content](social_marketing/social_posts.md#create-and-post-social-media-content)
    * [Post detail form](social_marketing/social_posts.md#post-detail-form)
      * [Công ty](social_marketing/social_posts.md#company)
      * [Đăng lên](social_marketing/social_posts.md#post-on)
      * [Tin nhắn](social_marketing/social_posts.md#message)
      * [Đính kèm hình ảnh](social_marketing/social_posts.md#attach-images)
      * [Chiến dịch](social_marketing/social_posts.md#campaign)
      * [Khi](social_marketing/social_posts.md#when)
      * [Tuỳ chọn thông báo đẩy](social_marketing/social_posts.md#push-notification-options)
* [Social marketing campaigns](social_marketing/social_campaigns.md)
  * [Campaigns page](social_marketing/social_campaigns.md#campaigns-page)
  * [Create social marketing campaigns](social_marketing/social_campaigns.md#create-social-marketing-campaigns)
  * [Edit social marketing campaigns](social_marketing/social_campaigns.md#edit-social-marketing-campaigns)
  * [Social marketing campaign templates](social_marketing/social_campaigns.md#social-marketing-campaign-templates)
  * [Add content and communications to campaigns](social_marketing/social_campaigns.md#add-content-and-communications-to-campaigns)
