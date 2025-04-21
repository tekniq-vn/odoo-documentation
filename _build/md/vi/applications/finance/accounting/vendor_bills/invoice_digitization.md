# AI-powered document digitization

**Invoice digitization** is the process of converting paper documents into vendor bill and customer
invoice forms in your accounting.

Odoo uses  and artificial intelligence technologies to
recognize the content of the documents. Vendor bill and customer invoice forms are automatically
created and populated based on the scanned invoices.

#### SEE ALSO
- [Test Odoo's invoice digitization](https://www.odoo.com/app/invoice-automation)
- [Odoo Tutorials: Vendor Bill Digitization](https://www.odoo.com/slides/slide/vendor-bill-digitization-7065)

## Cấu hình

In Accounting ‣ Configuration ‣ Settings ‣ Digitization, check the box
Document Digitization and choose whether Vendor Bills and
Customer Invoices (this includes customer credit notes) should be processed
automatically or on demand.

If you enable the Single Invoice Line Per Tax option, only one line is created per tax
in the new bill, regardless of the number of lines on the invoice.

## Invoice upload

### Upload invoices manually

From the Accounting Dashboard, click on the Upload button of your vendor
bills journal.
Alternatively, go to Accounting ‣ Customers ‣ Invoices or
Accounting ‣ Vendors ‣ Bills and select Upload.

<a id="invoice-digitization-email-alias"></a>

### Upload invoices using an email alias

You can configure your connected scanner to send scanned documents to an email alias. Emails sent to
these aliases are converted into new draft customer invoices or vendor bills.

You can modify the email alias of a journal. To do so, go to the Settings app. Under
General Settings: Discuss, enable Custom Email Servers, add an
Alias Domain, and Save.

The email alias is now available in the Advanced Settings tab of the journal. Emails
sent to this address will be converted automatically into new invoices or bills.

#### NOTE
If you use the [Documents](../../../productivity/documents.md) app, you can automatically
send your scanned invoices to the Finance workspace (e.g.,
`inbox-financial@example.odoo.com`).

The default email aliases `vendor-bills@` and `customer-invoices@` followed by the
Alias Domain you set are automatically created for the Vendor Bills and
Customer Invoices journals, respectively. Emails sent to these addresses are converted
automatically into new invoices or bills.

To change a default email alias, go to
Accounting ‣ Configuration ‣ Accounting: Journals. Select the journal you want
to edit, click on the Advanced Settings tab, and edit the `Email Alias`.

## Invoice digitization

According to your settings, the document is either processed automatically, or you need to click on
Send for digitization to do it manually.

Once the data is extracted from the PDF, you can correct it if necessary by clicking on the
respective tags (available in Edit mode) and selecting the proper information instead.

## Data recognition with AI

It is essential to review and correct (if needed) the information uploaded during digitization.
Then, you have to post the document by clicking on Confirm. In this manner, the AI
learns, and the system identifies the correct data for future digitizations.

## Định giá

The **invoice digitization** is an In-App Purchase (IAP) service that requires prepaid credits to
work. Digitizing one document consumes one credit.

To buy credits, go to Accounting ‣ Configuration ‣ Settings ‣ Digitization
and click on Buy credits, or go to Settings ‣ Odoo IAP and click on
View My Services.

#### NOTE
Người dùng Odoo Enterprise có đăng ký hợp lệ sẽ nhận được tín dụng miễn phí để kiểm thử các tính năng IAP trước khi quyết định mua thêm tín dụng cho cơ sở dữ liệu; bao gồm cơ sở dữ liệu demo/đào tạo, cơ sở dữ liệu giáo dục và cơ sở dữ liệu có một ứng dụng miễn phí.

#### SEE ALSO
- [Our Privacy Policy](https://iap.odoo.com/privacy#header_6)
- [Mua hàng trong ứng dụng (IAP)](../../../essentials/in_app_purchase.md)
