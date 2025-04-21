# Tạo báo giá

In Odoo **Sales**, quotations can be created and sent to customers. Once a quotation has been
confirmed, it officially turns into a *sales order*, which can then be invoiced and paid for.

<a id="sales-quotation-settings"></a>

## Cài đặt báo giá

To access these setting options, navigate to Sales app ‣ Configuration ‣
Settings, and scroll to the Quotations & Orders section.

![The Quotations and Orders section on the Odoo Sales app Settings page.](applications/sales/sales/send_quotations/create_quotations/quotations-orders-section.png)
- Quotation Templates: Enable this option to create quotation templates featuring
  standard product offers, which are then selectable on quotation forms. When this checkbox is
  ticked, an additional field, Default Template, appears, along with a link to the
  Quotation Templates page.
- Online Signature: Request an online signature to confirm orders.
- Online Payment: Request an online prepayment from customers to confirm orders. Request
  a full or partial payment (via down payment). When this checkbox is ticked, an additional field,
  Prepayment amount (%), appears. There is also a link to the Payment
  Providers page.
- Default Quotation Validity: Determine a set amount (in days) that
  quotations can remain valid for.
- Default Recurrence: Select a default period from the drop-down menu to use as a
  recurrence period for a new quotation.
- Sale Warnings: Get warning messages about orders that include specific products or
  customers.
- PDF Quote builder: Customize the look of quotations with header pages, product
  descriptions, footer pages, and more.
- Lock Confirmed Sales: Ensure no further edits can be made to confirmed orders.
- Pro-Forma Invoice: Send pro-forma invoices to customers.

To activate any of these settings, tick the checkbox beside the desired option(s). Then, click
Save.

## Trang chủ báo giá

The *Quotations* dashboard is the page that appears when the Sales app is opened.

By default, the Quotations dashboard displays all quotations in the database related to
the current user, as indicated by the default My Quotations filter present in the search
bar.

![The Quotations dashboard present in the Odoo Sales application.](applications/sales/sales/send_quotations/create_quotations/quotations-dashboard.png)

#### NOTE
To view *all* quotations in the database, remove the My Quotations filter from the
search bar.

Quotations on this page appear in a default list view, but can also be viewed in a
<i class="oi oi-view-kanban"></i> Kanban view, <i class="fa fa-calendar"></i> Calendar,
<i class="oi oi-view-pivot"></i> Pivot table, <i class="fa fa-area-chart"></i> Graph, or
<i class="fa fa-clock-o"></i> Activity view.

To view and/or modify any listed quotation from the Quotations dashboard, click on the
desired quotation line from the list, and Odoo reveals the specific form for that selected
quotation.

## Tạo báo giá

To create a quotation, open the Sales app, and click the New button,
located in the upper-left corner of the main Quotations dashboard.

#### IMPORTANT
The New button is **only** present if the Quotations dashboard is in list
or Kanban view.

Clicking the New button reveals a blank quotation form, with various fields and tabs to
configure.

![A typical quotation form in the Odoo Sales application.](applications/sales/sales/send_quotations/create_quotations/quotation-form.png)

Begin by entering the customer's name in the Customer field at the top of the form. This
is a **required** field.

If the customer's information is already in the database, the Invoice Address and
Delivery Address fields auto-populate with the saved information for those respective
fields, based on the data from that customer's contact record (found in the **Contacts**
application).

If the customer was referred by another customer or contact, enter their name in the
Referrer field.

If a Referrer is selected, a new field, Commission Plan appears, in which a
commission can be selected from the drop-down menu. This commission is rewarded to the contact
selected in the Referrer field.

Next, if they have not already been auto-populated with the customer's information, enter the
appropriate addresses in the Invoice Address and Delivery Address fields.
Both of these fields are **required**.

Then, if desired, choose a Quotation Template from the drop-down field to apply to this
quotation. It should be noted that some additional fields may appear, depending on the template
selected.

The default date that appears in the Expiration field is based on the number configured
in the [Default Quotation Validity setting](#sales-quotation-settings) (in
Sales app ‣ Configuration ‣ Settings).

If the quotation is for a recurring product or subscription, select the desired Recurring
Plan from that specific drop-down menu.

If desired, select a specific Pricelist to be applied to this quotation.

Lastly, select any specific Payment Terms to be used for this quotation.

### Order Lines tab

The first tab on the quotation form is the Order Lines tab.

In this tab, select products, and quantities of those products, to add them to the quotation.

There are two ways to add products to the quotation from this tab.

Click Add a product, select the desired item from the Product drop-down
field, and proceed to adjust the quantity of that selected product, if necessary.

Or, click Catalog to reveal a separate page, showcasing every item (and every potential
product variant) in an organized catalog display, with items organizable by Product
Category and Attributes.

![A product catalog accessible via a quotation in the Odoo Sales application.](applications/sales/sales/send_quotations/create_quotations/product-catalog.png)

From here, simply locate the desired items, click the <i class="fa fa-shopping-cart"></i> Add
button on the product card, and adjust the quantity, if needed. When complete, click the
Back to Quotation button in the upper-left corner to return to the quotation, where the
newly-selected catalog items can be found in the Order Lines tab.

If multiple items should be presented in a more organized way on the quotation, click Add
a section, enter a name for the section, and drag-and-drop that section heading in the desired
location amongst the items in the Order Lines tab. The section heading appears in bold.

If needed, click Add a note beneath a certain product line to add a custom note about
that specific product. The note appears in italics. Then, if needed, proceed to drag-and-drop the
note beneath the desired product line.

Beneath the product lines, there are buttons that can be clicked to apply any of the following:
Coupon Code, Promotions, Discount, and/or Add
shipping.

#### SEE ALSO
- [Use eWallets and gift cards](../products_prices/ewallets_giftcards.md)
- [Discount and loyalty programs](../products_prices/loyalty_discount.md)
- [Pricelists, discounts, and formulas](../products_prices/prices/pricing.md)

### Optional Products tab

Open the Optional Products tab to select related products that can be presented to the
customer, which may result in an increased sale.

For example, if the customer wants to buy a car, an optional product that could be offered is a
*Trailer Hitch*.

#### SEE ALSO
[Sản phẩm gốc](optional_products.md)

### Other Info tab

In the Other Info tab, there are various quotation-related configurations separated into
four different sections: Sales, Delivery, Invoicing, and
Tracking.

#### NOTE
Some fields **only** appear if specific settings and options have been configured.

#### Phần bán hàng

In the Sales section of the Other Info tab, there are sales specific fields
that can be configured.

![The Sales section of the Other Info tab of a quotation form in Odoo Sales.](applications/sales/sales/send_quotations/create_quotations/other-info-sales.png)
- Salesperson: Assign a salesperson from the drop-down menu to be associated with this
  quotation. The user who originally created the quotation is selected in this field, by default.
- Sales Team: Assign a specific sales team to this quotation. If the selected
  Salesperson is a member of a sales team, that team is auto-populated in the field.
- Company: Select a company from the drop-down menu this quotation should be associated
  with. This field only appears when working in a multi-company environment.
- Online signature: Tick this checkbox to request an online signature from the customer
  to confirm the order. This field only appears if the *Online Signature* setting has been enabled.
- Online payment: Tick this checkbox, and enter a desired percentage in the adjacent
  field, to request an online payment from the customer (for that designated percentage of the total
  amount) to confirm the order. This field only appears if the *Online Payment* setting has been
  enabled.
- Customer Reference: Enter a custom reference ID for this customer. The entered
  reference ID can contain letters, numbers, or a mix of both.
- Tags: Add specific tags to the quotation for added organization and enhanced
  searchability in the Odoo **Sales** application. Multiple tags can be added, if necessary.

#### Delivery section

In the Delivery section of the Other Info tab, there are delivery-specific
fields that can be configured.

![The Delivery section of the Other Info tab of a quotation form in Odoo Sales.](applications/sales/sales/send_quotations/create_quotations/other-info-delivery.png)
- Shipping Weight: Displays the weight of the items being shipped. This field is not
  modifiable. Product weight is configured on individual product forms.
- Incoterm: Select an Incoterm (International Commerical Term) to use as predefined
  commerical terms for international transactions.
- Incoterm Location: If an Incoterm is being used, enter the international location in
  this field.
- Shipping Policy: Select a desired shipping policy from the drop-down menu. If all
  products are delivered at once, the delivery order is scheduled, based on the greatest product
  lead time. Otherwise, it is based on the shortest lead time. The available options are:
  As soon as possible or When all products are ready.
- Delivery Date: Click into the empty field to reveal a calendar popover, from which a
  customer delivery date can be selected. If no custom date is required, refer to the
  Expected date listed to the right of that field.

#### Invoicing section

In the Invoicing section of the Other Info tab, there are invoicing specific
fields that can be configured.

![The Invoicing section of the Other Info tab of a quotation form in Odoo Sales.](applications/sales/sales/send_quotations/create_quotations/other-info-invoicing.png)
- Vị trí tài chính: Chọn một vị trí tài chính để điều chỉnh thuế và tài khoản cho khách hàng cụ thể hoặc đơn bán hàng/hóa đơn. Giá trị mặc định được lấy từ thông tin khách hàng. Nếu chọn giá trị trong trường này, một liên kết <i class="fa fa-refresh"></i> Cập nhật thuế có thể nhấp sẽ xuất hiện. Khi nhấp, thuế cho khách hàng và báo giá cụ thể này sẽ được cập nhật. Một cửa sổ xác nhận cũng sẽ hiển thị.
- Analytic Account: Select an analytic account to apply to this customer/quotation.

#### Tracking section

In the Tracking section of the Other Info tab, there are tracking specific
fields that can be configured.

![The Tracking section of the Other Info tab of a quotation form in Odoo Sales.](applications/sales/sales/send_quotations/create_quotations/other-info-tracking.png)
- Source Document: Enter the reference of the document that generated the
  quotation/sales order, if applicable.
- Opportunity: Select the specific opportunity (from the **CRM** app) related to this
  quotation, if applicable.
- Campaign: Select the marketing campaign related to this quotation, if applicable.
- Medium: Select the method by which this quotation originated (e.g. *Email*), if
  applicable.
- Source: Select the source of the link used to generate this quotation (e.g.
  *Facebook*), if applicable.

#### SEE ALSO
[Trình theo dõi liên kết](../../../websites/website/reporting/link_tracker.md)

### Tab Ghi chú

In the Notes tab of the quotation form, enter any specific internal notes about the
quotation and/or customer, if desired.

## Sending and confirming quotations

Once all the necessary fields and tabs have been configured, it is time to send the quotation to the
customer for confirmation. Upon confirmation, the quotation turns into an official sales order.

At the top of the form, there is a series of buttons:

- Send by Email: When clicked, a pop-up window appears with the customer's name and
  email address in the Recipients field, the quotation (and reference ID) in the
  Subject field, and a brief default message in the body of the email, which can be
  modified, if needed.

  Below that, a PDF copy of the quotation is attached. When ready, click Send to send
  the quotation, via email, to the customer, so they can review and confirm it.
- Gửi hóa đơn CHIẾU LỆ: Nút này **chỉ** xuất hiện nếu cài đặt *Hóa đơn chiếu lệ* đã được kích hoạt. Khi nhấp, một cửa sổ bật lên sẽ xuất hiện với tên và địa chỉ email của khách hàng trong trường Người nhận, hóa đơn *chiếu lệ* (và ID tham chiếu) trong trường Chủ đề, cùng một thông báo mặc định ngắn trong nội dung email - tất cả đều có thể chỉnh sửa nếu cần.

  Below that, a PDF copy of the quotation is attached. When ready, click Send to send
  the quotation, via email, to the customer, so they can review and confirm it.
- Confirm: When clicked, the quotation is confirmed, and the status changes to
  Sales Order.
- Preview: When clicked, Odoo reveals a preview of the quotation the customer sees when
  they log into their customer portal. Click the <i class="fa fa-arrow-right"></i> Back to edit
  mode link at the top of the preview page, in the blue banner, to return to the quotation form.
- Cancel: When clicked, the quotation is canceled.

#### NOTE
If the *Lock Confirmed Sales* setting is enabled, the sales order becomes Locked, and
is indicated as such on the sales order form.

At this point, the quotation has been confirmed, turned into a sales order, and is now ready to be
invoiced and paid for.

For more information about invoicing, refer to the [Invoice based on delivered or ordered
quantities](../invoicing/invoicing_policy.md)

#### SEE ALSO
- [Mẫu báo giá](quote_template.md)
- [Hạn báo giá](deadline.md)
- [Online signatures for order confirmations](get_signature_to_validate.md)
- [Online payment order confirmation](get_paid_to_validate.md)
- [PDF quote builder](pdf_quote_builder.md)
- [Hóa đơn chiếu lệ](../invoicing/proforma.md)
