# Double Opt-in

A _double opt-in_, also referred to as a _confirmed opt-in_, may be required in some countries\
for marketing communications, due to anti-SPAM laws. Confirming consent has several other benefits,\
as well: it validates email addresses, avoids spam/robo subscribers, keeps mailing lists clean, and\
only includes engaged contacts in the mailing list.

Khi sử dụng mẫu chiến dịch _Đăng ký kép_, một danh sách liên hệ mới có tên _Liên hệ đã xác nhận_ sẽ được tạo trong ứng dụng _Marketing qua Email_. Mọi liên hệ mới được thêm vào danh sách liên hệ _Bản tin email_ mặc định sẽ nhận được email xác nhận để thực hiện đăng ký kép. Các liên hệ nhấp vào liên kết xác nhận trong email sẽ tự động được thêm vào danh sách liên hệ _Liên hệ đã xác nhận_ trong Odoo.

#### IMPORTANT

When using the _Double Opt-in_ campaign template, only the contacts in the _Confirmed contacts_\
_mailing_ list are considered to have confirmed their consent.

## Use the Double Opt-in campaign template

Open the Marketing Automation app, and select the Double Opt-in\
campaign template to create a new campaign for confirming consent.

### Campaign configuration

Upon creation of the campaign, the campaign form loads with a new preconfigured campaign.

The Target and Filter configurations of the campaign are as follows:

* Name: `Double Opt-in`
* Responsible\*: The user who created the campaign.
* Target: Mailing Contact
* Unicity based on: Email (Mailing Contact)
* Bộ lọc:
  * Email is set
  * Blacklist is not set
  * Mailing lists contains `Newsletter`

\* The Responsible field is only visible with [Chế độ lập trình viên (chế độ gỡ lỗi)](../../../general/developer_mode.md#developer-mode) activated.

#### IMPORTANT

The Target model of the campaign should **not** be modified. Changing the\
Target model with activities in the Workflow invalidates the existing\
activities in the Workflow.

The _Double Opt-in_ campaign template is intended to **only** use the Mailing Contact\
model.

The campaign loads two activities in the Workflow section of the campaign: an email\
activity, with a child server action activity that triggers _on click_.

By default, the `Confirmation` email activity is set to trigger 1 Hours after the\
beginning of the workflow. In other words, the email is sent 1 hour after a new contact is added to\
the _Newsletter_ mailing list.

The email activity uses the preconfigured _Confirmation_ email template, which contains a button for\
the contact to click to confirm their consent.

To modify the email template, select the Templates smart button at\
the top of the campaign form. Then, in the list of templates, select the `Confirmation` email\
template.

Be sure to personalize the contents of the email template; however, it is recommended to keep the\
contents of double opt-in confirmation emails short and to-the-point.

The default confirmation button, in the body of the template, links directly to the database's\
website homepage. Click on the button to edit the button text and URL.

#### IMPORTANT

The email template should only include a single call-to-action link for confirmation, other than\
an unsubscribe link.

Any click on a link (or button) included in the confirmation email, besides the unsubscribe\
button, triggers the _Add to list_ server action.

The child activity _Add to list_ server action's _On click_ trigger cannot differentiate between\
multiple URLs in an email, besides the `/unsubscribe_from_list` unsubscribe button that is\
included in any one of the footer blocks.

The `Add to list` server action activity triggers immediately after a click in the parent`Confirmation` email activity is detected.

When triggered, the `Add to list` activity executes the _Add To Confirmed List_ server action,\
automatically adding the contact to the _Confirmed contacts_ mailing list, if they are not already\
in the mailing list.

To modify the server action, select the title of the activity to open the Open:\
Activities pop-up window and edit the server action activities configuration.

#### IMPORTANT

It is not recommended to modify the preconfigured Python code in the Add To Confirmed\
List server action, as doing so may trigger a change in the database's pricing plan.

Once the campaign configuration is complete, consider [launching a test](../testing_running.md)\
to verify the campaign executes as expected. If the campaign testing is successful,\
Start the campaign to begin sending double opt-in confirmation emails to _Newsletter_\
mailing list contacts, and fill the _Confirmed contacts_ mailing list with engaged contacts.

## Double Opt-in use-case

#### SEE ALSO

* [Campaign metrics](../understanding_metrics.md)
* [Mailing lists](../../email_marketing/mailing_lists.md)
* [Email Marketing](../../email_marketing.md)
