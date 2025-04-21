# Hạn báo giá

Trong ứng dụng *Bán hàng* của Odoo, có thể đặt thời hạn cho báo giá bán hàng. Việc này khuyến khích khách hàng hành động nhanh chóng trong quá trình đàm phán, vì họ có thể lo sợ bỏ lỡ một cơ hội tốt. Bên cạnh đó, thời hạn cũng có thể đóng vai trò bảo vệ doanh nghiệp trong trường hợp phải thực hiện đơn hàng với mức giá không còn mang lại lợi nhuận.

## Ngày hết hạn báo giá

In Odoo *Sales*, there's the option to add an expiration date to a quotation.

To add an expiration date to a quotation, navigate to Sales app, and select a
desired quotation, or create a new one by clicking New.

On the quotation form, click the Expiration field to reveal a pop-up calendar. From this
pop-up calendar, select the desired month and date as the expiration date for the quotation.

![The expiration field on a standard quotation form in Odoo Sales.](applications/sales/sales/send_quotations/deadline/quotation-deadlines-expiration-field.png)

## Quotation template expiration

The Odoo *Sales* application also makes it possible to add a deadline expiration date to quotation
templates.

To add a deadline expiration date to a quotation template, navigate to Sales app ‣
Configuration ‣ Quotation Templates, and either select the desired quotation template to which a
deadline should be added, or click New to build a new quotation template from scratch.

On the quotation template form, add a specific number of days to the Quotation expires
after field, located beneath the quotation template name. The number of days represents how long
the quotation will be valid for, before it expires.

![The quotation expires after field on a quotation template form in Odoo Sales.](applications/sales/sales/send_quotations/deadline/quotation-deadlines-expires-after.png)

Then, whenever that specific quotation template is used in a quote, an expiration date is
automatically calculated, based on the number of days designated above. However, this date can be
overwritten before sending the quotation to the customer.

#### SEE ALSO
[Mẫu báo giá](quote_template.md)
