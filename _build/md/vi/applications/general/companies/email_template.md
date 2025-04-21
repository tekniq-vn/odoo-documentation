# Mẫu Email

Email templates are saved emails that are used repeatedly to send emails from the database. They
allow users to send quality communications, without having to compose the same text repeatedly.

Creating different templates that are tailored to specific situations lets users choose the right
message for the right audience. This increases the quality of the message and the overall
engagement rate with the customer.

#### NOTE
Mẫu email trong Odoo sử dụng QWeb hoặc XML, cho phép chỉnh sửa email trong giao diện hiển thị cuối cùng, giúp tùy chỉnh linh hoạt hơn mà không cần chỉnh sửa bất kỳ mã nào. Điều này có nghĩa là Odoo có thể sử dụng Giao diện người dùng đồ họa (GUI) để chỉnh sửa email, đồng thời cập nhật mã backend. Khi email được người nhận đọc trong chương trình của họ, định dạng và đồ họa sẽ hiển thị đúng theo thiết kế cuối cùng.

Access email templates in [developer mode](../developer_mode.md#developer-mode) by navigating to
Settings app ‣ Technical menu ‣ Email ‣ Email Templates.

## Chỉnh sửa mẫu email

The *powerbox* feature can be used when working with email templates. This feature provides the
ability to directly edit the formatting and text in an email template, as well as the ability to add
links, buttons, appointment options, or images.

Additionally, the XML/HTML code of the email template can be edited directly, via the
</> icon. Dynamic placeholders (referencing fields within Odoo) are also available for
use in the email template.

### Powerbox

The *powerbox* feature is an enriched text editor with various formatting, layout, and text options.
It can also be used to add XML/HTML features in an email template. The powerbox feature is activated
by typing a forward slash `/` in the body of the email template.

When a forward slash `/` is typed in the body of an email template, a drop-down menu appears with
the following options:

Cấu trúc

- Bulleted list: Create a simple bulleted list.
- Numbered list: Create a list with numbering.
- Checklist: Track tasks with a checklist.
- Table: Insert a table.
- Separator: Insert a horizontal rule separator.
- Quote: Add a blockquote section.
- Code: Add a code section.
- 2 columns: Convert into two columns.
- 3 columns: Convert into three columns.
- 4 columns: Convert into four columns.

Định dạng

- Heading 1: Big section heading.
- Heading 2: Medium section heading.
- Heading 3: Small section heading.
- Switch direction: Switch the text's direction.
- Văn bản: Khối đoạn văn.

Phương tiện

- Image: Insert an image.
- Article: Link an article.

Điều hướng

- Link: Add a link.
- Button: Add a button.
- Appointment: Add a specific appointment.
- Calendar: Schedule an appointment.

Tiện ích

- 3 Stars: Insert a rating over three stars.
- 5 Stars: Insert a rating over five stars.

Khối cơ bản

- Signature: Insert your signature.

Công cụ Marketing

- Dynamic Placeholders: Insert personalized content.

#### SEE ALSO
[Using dynamic placeholders](#email-template-dynamic-placeholders)

### Trình soạn thảo mã HTML/XML

To access the XML/HTML editor for an email template, first enter [developer mode](../developer_mode.md#developer-mode). Then, click the </> icon in the upper-right corner of the template,
and proceed to edit the XML/HTML. To return to the standard text editor, click the </>
icon again.

![HTML editor in the email template.](applications/general/companies/email_template/html-code-editor.png)

#### WARNING
The XML/HTML editor should be accessed with caution as this is the backend code of the template.
Editing the code can cause the email template to break immediately or when upgrading the
database.

<a id="email-template-dynamic-placeholders"></a>

### Trình giữ chỗ động

*Dynamic placeholders* reference certain fields within the Odoo database to produce unique data in
the email template.

Dynamic placeholders are encoded to display fields from within the database. Dynamic placeholders
can be used in the Body (Content Tab) of the email template. They can also
be used in the fields present in the Email Configuration tab, the Subject of
the email, and the Language.

Để sử dụng phần giữ chỗ động trong phần Thân của email, hãy mở tính năng **powerbox** bằng cách nhập `/` vào phần thân của mẫu email trong tab Nội dung. Cuộn xuống cuối danh sách tùy chọn, đến Công cụ marketing. Tiếp theo, chọn Phần giữ chỗ động. Sau đó, chọn phần giữ chỗ động từ danh sách các tùy chọn khả dụng và làm theo hướng dẫn để cấu hình phần giữ chỗ động đó với trường Odoo tương ứng mong muốn. Mỗi phần giữ chỗ động sẽ có cấu hình khác nhau.

![Using dynamic placeholders in an email template.](applications/general/companies/email_template/dynamic-placeholders.png)

#### NOTE
Each unique combination of Fields, Sub-models and Sub-fields
creates a different dynamic placeholder. Imagine it as a combination to the field that is being
created.

To search the available fields, simply type in the front-end name (on user-interface) of the
field in the search. This will find a result from all of the available fields for the model that
the email template is created for.

#### WARNING
Customizing email templates are out of the scope of Odoo Support.

### Rich text editor

A rich text editor toolbar can be accessed by highlighting text in the email template. This can be
used to change the heading, font size/style, color, add a list type, or a link.

![Rich text editor in the email template.](applications/general/companies/email_template/rich-text-editor.png)

### Resetting email templates

Should the email template not work because the code has been altered it can be reset to restore it
back to the out-of-box default template. Simply click on the Reset Template button in
the upper left-hand of the screen and the template will be reset.

![Resetting the email template.](applications/general/companies/email_template/reset.png)

### Default reply on email templates

Under the Email Configuration tab on an email template, there is a Reply To
field. In this field, add email addresses to which replies are redirected when sending emails en
masse using this template.

![Reply-to field on template.](applications/general/companies/email_template/reply-to-template-sales.png)

The Reply To field is **only** used for mass mailing (sending emails in bulk). Bulk
emails can be sent in almost every Odoo application that has a list view option.

To send mass mails, while in list view, check the boxes next to the desired records
where the emails are to be sent, click the Action button (represented by a ⚙️
(gear) icon), and select the desired email option from the Action drop-down menu. Email
options can vary by the particular list view and application.

If it is possible to send an email, a mail composer pop-up window appears, with values that can be
defined and customized. This option will be available on the Action button on pages
where emails can be sent in bulk---for example, on the Customers page of the CRM app.
This action occurs throughout the Odoo database.

![Email composer in mass mailing mode with reply-to highlighted.](applications/general/companies/email_template/composer-mass-mailing.png)

## Transactional emails and corresponding URLs

In Odoo, multiple events can trigger the sending of automated emails. These emails are known as
*transactional emails*, and sometimes contain links redirecting to the Odoo database.

By default, links generated by the database use the dynamic `web.base.url` key defined in the system
parameters. For more information about this, see [system parameters](../../websites/website/configuration/domain_names.md#domain-name-web-base-url).

If the *Website* application is not installed, the `web.base.url` key will always be the default
parameter used to generate all the links.

#### IMPORTANT
Khóa `web.base.url` chỉ có thể có một giá trị duy nhất. Điều này nghĩa là trong môi trường cơ sở dữ liệu có nhiều trang web hoặc nhiều công ty, ngay cả khi mỗi trang web có một tên miền riêng biệt, các liên kết được tạo ra để chia sẻ tài liệu (hoặc các liên kết trong email giao dịch) có thể vẫn giống nhau, bất kể trang web/công ty nào liên quan đến việc gửi email/tài liệu.

This is not always the case, as some Odoo applications (*eCommerce*, for example) have a link
established in the database with the *Website* application. In that case, if a specific domain is
defined for the website, the URL generated in the email template uses the domain defined on the
corresponding website of the company.

#### NOTE
A document shared using the *Documents* application will **always** use the `web.base.url` key,
as the document shared is not associated with any particular website. This means that the URL
will always be the same (the `web.base.url` key value), no matter what company it's shared from.
This is a known limitation.

For more information about how to configure domains, check out the [domain name documentation](../../websites/website/configuration/domain_names.md).

### Updating translations within email templates

In Odoo, email templates are automatically translated for all users in the database for all of the
languages installed. Changing the translations shouldn't be necessary. However, if for a specific
reason, some of the translations need to be changed, it can be done.

#### WARNING
Like any modification in the code, if translation changes are not done correctly (for example,
modifications leading to bad syntax), it can break the template, and as a result, the template
will appear blank.

In order to edit translations, first enter [developer mode](../developer_mode.md#developer-mode). Then, on the
email template, click on the Edit button, and then click on the language button,
represented by the initials of the language currently being used (e.g. EN for English).

![Edit the language of a template.](applications/general/companies/email_template/edit-language-template.png)

#### NOTE
If there aren't multiple languages installed and activated in the database, or if the user does
not have administration access rights, the language button will not appear.

A pop-up window with the different languages installed on the database appears. From this pop-up,
editing of translations is possible. When the desired changes have been made, click the
Save button to save the changes.

![Translation of the body of the Appointment Booked template.](applications/general/companies/email_template/translation-body.png)

#### NOTE
When editing the translations, the default language set in the database appears in **bold**.
