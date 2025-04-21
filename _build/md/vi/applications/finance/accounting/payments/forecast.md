# Forecast future bills to pay

In Odoo, you can manage payments by setting automatic **Payments Terms** and **follow-ups**.

## Configuration: payment terms

In order to track vendor conditions, we use **Payment Terms** in Odoo. They allow keeping track of
due dates on invoices. Examples of **Payment Terms** are:

- 50% within 30 days
- 50% within 45 days

To create them, go to Accounting ‣ Configuration ‣ Invoicing: Payment Terms and
click on Create to add new terms or click existing ones to modify them.

#### SEE ALSO
[Odoo Tutorials: Payment Terms](https://www.odoo.com/slides/slide/payment-terms-1679?fullscreen=1)

Once **Payment Terms** are defined, you can assign them to your vendor by default. To do so, go to
Vendors ‣ Vendors, select a vendor, click the Sales & Purchase tab,
and select a specific **Payment Term**. This way, every time you purchase from this vendor, Odoo
automatically proposes the chosen Payment Term.

#### NOTE
If you do not set a specific Payment Term on a vendor, you can still set one on the vendor bill.

## Forecast bills to pay with the aged payable report

Để theo dõi các khoản phải trả nhà cung cấp, sử dụng báo cáo **Công nợ phải trả theo tuổi nợ**. Truy cập bằng cách vào Kế toán ‣ Báo cáo ‣ Báo cáo đối tác: Công nợ phải trả theo tuổi nợ. Báo cáo này cung cấp bản tóm tắt theo từng nhà cung cấp về số tiền phải thanh toán, so với ngày đến hạn (ngày đến hạn được tính trên từng hóa đơn theo điều khoản thanh toán) và cho biết số tiền bạn sẽ phải thanh toán trong các tháng tới.

## Select bills to pay

You can get a list of all your vendor bills by going to Vendors ‣ Bills. To view
only the bills that you need to pay, click Filters ‣ Bills to Pay. To view only
overdue payments, select the Overdue filter instead.

You can also group bills by their due date by clicking Group By ‣ Due Date and
selecting a time period.
