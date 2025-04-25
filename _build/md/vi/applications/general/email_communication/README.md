# Communication in Odoo by email

Communication in Odoo related to records such as CRM opportunities, sales orders, invoices, ...
have a discussion thread called **chatter**, often displayed on the right side of the record.

On the chatter, you can send direct emails or Odoo notifications to the followers of a document
(depending on their notification preferences), log internal notes, send WhatsApp messages or SMSes,
and schedule activities.

If a follower replies to a message, the reply updates the chatter, and Odoo relays it to the
followers as a notification. All emails - outgoing and incoming - appear in the same chatter.

<a id="email-online-sh"></a>

## Odoo Online and Odoo.sh users

On Odoo Online and Odoo.sh, outgoing and incoming emails work out of the box, **nothing needs to be
done**. Everything is already configured on your subdomain.

By default, outgoing emails use the following [notification email address](email_servers_outbound.md#email-outbound-notifications) `notifications@company-name.odoo.com`.

<a id="email-online-sh-domain"></a>

### Using another domain

If you prefer not to have outgoing emails sent from Odoo's subdomain `@company-name.odoo.com` but
instead [from your own domain](email_servers_outbound.md#email-outbound-custom-domain), **additional configuration will
be necessary** on the domain and within Odoo. This introduces an extra layer of complexity and
necessitates technical knowledge (mainly regarding DNS and mail protocols).

By adding a domain and configuring the administration access rights, you can also access the
[new domain alias](email_servers_outbound.md#email-outbound-alias-domain) page to configure the alias of your companies.
If only one domain is configured, this domain will be shared by all companies on the database.

If you want to keep using Odoo's mail server, you will have to [configure the SPF and DKIM](email_domain.md#email-domain-spf).

If [you want to use your own mail server](email_servers_outbound.md#email-outbound-custom-domain-smtp-server), you will
have to follow the mail server provider's specific documentation.

Đối với email đến, sau khi thêm miền riêng của bạn, [phản hồi từ khách hàng sẽ gửi về miền của bạn](email_servers_inbound.md#email-inbound-custom-domain), và bạn sẽ cần sử dụng một trong ba cách sau để nhận email trở lại Odoo (sử dụng [máy chủ thư đến](email_servers_inbound.md#email-inbound-custom-domain-incoming-server), [chuyển hướng/chuyển tiếp](email_servers_inbound.md#email-inbound-custom-domain-redirections) hoặc [bản ghi DNS MX](email_servers_inbound.md#email-inbound-custom-domain-mx)). Tất cả đều được đề cập trong [tài liệu quản lý tin nhắn đến](email_servers_inbound.md).

<a id="email-on-premise"></a>

## On-premise users

If you are on-premise, you will have to completely configure your outgoing and incoming emails:

- For outgoing emails, you will need [to use an SMTP server and a custom domain](email_servers_outbound.md#email-outbound-custom-domain-odoo-server).
- Đối với email đến, hãy đặt tần suất lấy email mới đủ thấp để đảm bảo phản hồi kịp thời, nhưng cũng đủ cao để không gây quá tải cho hệ thống hoặc nhà cung cấp của bạn. Vì lý do này và do cấu hình này khá đơn giản, chúng tôi thường khuyến khích sử dụng máy chủ thư đến. Để sử dụng máy chủ SMTP, hãy tham khảo tài liệu ["Sử dụng miền tùy chỉnh cho thư đến"](email_servers_inbound.md#email-inbound-custom-domain).

<a id="email-third-party-server"></a>

## Using a third-party provider's mail server

Odoo's documentation also covers several popular mail servers. As they require specific
authorizations and configuration, they add a layer of complexity. For this reason, using Odoo's
outgoing mail server is recommended.

- [Tài liệu Outlook](azure_oauth.md)
- [Tài liệu Gmail](google_oauth.md)
- [Tài liệu Mailjet](mailjet_api.md)

#### NOTE
Every provider has its own limitations. Research the desired provider *before* configuring it.
For example, Outlook and Gmail might not be suitable for large marketing campaigns.

#### SEE ALSO
- [Hoạt động](../../essentials/activities.md)
- [Ứng dụng Thảo luận](../../productivity/discuss/)
- [Digest emails](../companies/digest_emails.md)
- [Email Marketing app](../../marketing/email_marketing/)
- [Mẫu email](../companies/email_template.md)
- [Expense creation using an email alias](../../finance/expenses/log_expenses.md#expenses-email-expense)
- [Helpdesk ticket creation using an email alias](../../services/helpdesk/overview/receiving_tickets.md#helpdesk-receiving-tickets-email-alias)
- [Lead creation using an email alias](../../sales/crm/acquire_leads/email_manual.md#crm-configure-email-alias)
- [Project task creation using an email alias](../../services/project/tasks/task_creation.md#task-creation-email-alias)
- [Technical mail gateway for on-premise users](../../../administration/on_premise/email_gateway.md)
- [Technical start of Odoo database with an outgoing mail server configured from the
  command-line interface](../../../developer/reference/cli.md#reference-cmdline-server-emails)

* [Manage inbound messages](email_servers_inbound.md)
* [Manage outbound messages](email_servers_outbound.md)
* [Configure DNS records to send emails in Odoo](email_domain.md)
* [Connect Microsoft Outlook 365 to Odoo using Azure OAuth](azure_oauth.md)
* [Connect Gmail to Odoo using Google OAuth](google_oauth.md)
* [API Mailjet](mailjet_api.md)
* [Common emailing issues and solutions](faq.md)
