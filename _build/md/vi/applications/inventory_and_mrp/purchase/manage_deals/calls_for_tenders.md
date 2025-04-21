# Call for tenders

Sometimes, companies might want to invite vendors to submit offers for similar goods or services all
at once. This helps companies select the cheapest, fastest vendors for their specific business
needs.

In Odoo, this can be done by creating alternative requests for quotation (RfQs) for different
vendors. Once a response is received from each vendor, the product lines from each  can be
compared, and a decision can be made for which products to purchase from which vendors.

#### NOTE
Sometimes referred to as a *call for tender*, this process is primarily used by organizations in
the public sector, who are legally bound to use it when making a purchase. However, private
companies can also use alternative  to spend money efficiently.

## Cấu hình

To create alternative , the *Purchase Agreements* feature **must** be enabled in the
*Purchase* app settings. To enable the feature, navigate to Purchase app ‣
Configuration ‣ Settings. Under the Orders section, click the checkbox for
Purchase Agreements.

Then, click Save to apply the change.

![Purchase Agreements enabled in the Purchase app settings.](applications/inventory_and_mrp/purchase/manage_deals/calls_for_tenders/calls-for-tenders-enabled-setting.png)

<a id="purchase-manage-deals-create-rfq"></a>

## Tạo một

To create a new , follow the instructions in the [Yêu cầu báo giá](rfq.md) documentation.

#### SEE ALSO
[Odoo Tutorial: Purchase Basics and Your First Request for Quotation](https://www.youtube.com/watch?v=o_uI718P1Dc)

<a id="purchase-manage-deals-create-alternatives"></a>

## Tạo  dự trù

Once a  is created and sent to a vendor, alternative  can be created for additional
vendors to compare prices, delivery times, and other factors, to help make a decision for the order.

To create alternative  from the original, click the Alternatives tab. Then, click
Create Alternative. When clicked, a Create alternative pop-up window
appears.

![Calls for tenders pop-up to create alternative quotation.](applications/inventory_and_mrp/purchase/manage_deals/calls_for_tenders/calls-for-tenders-create-alternative.png)

From this window, select an alternative vendor from the drop-down menu next to the
Vendor field, to whom the alternative quotation is assigned.

Next to this, there is a Copy Products checkbox that is selected by default. When
selected, the product quantities of the original  are copied over to the alternative. For this
first alternative quotation, leave the checkbox checked. Once finished, click Create
Alternative. This opens a new  form.

Since the Create Alternative checkbox was left checked, the new form is already
pre-populated with the same products, quantities, and other details as the previous, original .

#### NOTE
When the Copy Products checkbox is selected while creating an alternative quotation,
additional products do **not** need to be added, unless desired.

However, if a chosen vendor is listed in the Vendor column under a specific product
form included in the order, the values set on the product form carry over to the , and
**must** be changed manually, if necessary.

Once ready, create a second alternative quotation by clicking the Alternatives tab,
followed by Create Alternative.

Thao tác này sẽ mở cửa sổ bật lên Tạo đơn dự trù. Chọn một nhà cung cấp khác từ menu thả xuống kế bên mục Nhà cung cấp. Đối với  này, cần *bỏ chọn* hộp kiểm Sao chép sản phẩm. Thao tác này sẽ xóa toàn bộ sản phẩm khỏi  dự trù mới, để trống RfQ này. Các sản phẩm cụ thể cần đặt từ nhà cung cấp này có thể được thêm vào khi cần.

Once ready, click Create Alternative.

This creates a third, new . But, since the product quantities of the original  were
**not** copied over, the product lines are empty, and new products can be added as needed by
clicking Add a product, and selecting the desired products from the drop-down menu.

Once the desired number of specific products are added, click Send by Email.

![Blank alternative quotation with alternatives in breadcrumbs.](applications/inventory_and_mrp/purchase/manage_deals/calls_for_tenders/calls-for-tenders-blank-quotation.png)

This opens a Compose Email pop-up window, wherein the message to the vendor can be
customized, and attachments can be added, if necessary. Once ready, click Send.

From this newest form, click the Alternatives tab. Under this tab, all three  can
be seen in the Reference column. Additionally, the vendors are listed under the
Vendor column, and the order Total (and Status) of the orders
are in the rows, as well.

The date in the Expected Arrival column is calculated for each vendor, based on any
pre-configured lead times in the vendor and product forms.

<a id="purchase-manage-deals-link-rfq"></a>

## Link new  to existing quotations

Even if a quotation is not created directly from the Alternatives tab of another ,
it can still be linked to existing .

To do that, begin by creating a new . Navigate to Purchase app ‣ New. Fill
out the , according to the [previous instructions](#purchase-manage-deals-create-rfq).

Then, once ready, click the Alternatives tab. Since this new  was created
separately, there are no other orders linked yet.

However, to link this  with existing alternatives, click Link to Existing RfQ on
the first line in the Vendor column.

![Pop-up to link new quotation to existing RFQs.](applications/inventory_and_mrp/purchase/manage_deals/calls_for_tenders/calls-for-tenders-link-rfq-popup.png)

This opens an Add: Alternative POs pop-up window. Select the desired previously-created
, and click Select. All of these orders are now copied to this , and can be
found under the Alternatives tab.

<a id="purchase-manage-deals-compare-product-lines"></a>

## Compare product lines

Alternative  can be compared side-by-side, in order to determine which vendors offer the best
deals on the products included in the orders.

To compare alternative , navigate to the Purchase app, and select one of the
previously-created .

Then, click the Alternatives tab to see all linked . Next, under the
Create Alternative option, click Compare Product Lines. This navigates to
the Compare Order Lines page.

![Compare Product Lines page for alternative RFQs.](applications/inventory_and_mrp/purchase/manage_deals/calls_for_tenders/calls-for-tenders-compare-products.png)

The Compare Order Lines page, by default, groups by Product. Each product
included in any of the  is displayed in its own nested drop-down list, and features all of the
 numbers in the Reference column.

#### NOTE
To remove product lines from the Compare Order Lines page, click Clear at
the far-right end of that product line's row.

Doing so removes this specific product as a selectable option from the page, and changes the
Total price of that product on the page to `0`.

Additionally, on the  form, in which that product was included, its ordered quantity is also
changed to `0`.

Once the best offers have been identified, individual products can be selected by clicking the
Choose button at the end of each corresponding row.

Once all desired products have been chosen, click Requests for Quotation (in the
breadcrumbs, at the top of the page) to navigate back to an overview of all .

<a id="purchase-manage-deals-cancel-keep-alternatives"></a>

## Cancel (or keep) alternatives

Once the desired products have been chosen from the Compare Order Lines page, the
remaining , from which no products were chosen, can be canceled.

The cost in the Total column for each product that wasn't chosen is automatically set to
`0`, indicated at the far-right of each corresponding row.

Although they haven't been canceled yet, this indicates that each of those orders can be canceled
without having an effect on the other live orders, once those orders have been confirmed.

![Canceled quotations in the Purchase app overview.](applications/inventory_and_mrp/purchase/manage_deals/calls_for_tenders/calls-for-tenders-zero-total.png)

To confirm an  for which products were selected, click into an , and click
Confirm Order.

This causes a What about the alternative Requests for Quotations? pop-up window
to appear.

To view a detailed form of one of the  listed, click the line item for that quotation. This
opens an Open: Alternative POs pop-up window, from which all details of that particular
 can be viewed.

Once ready, click Close to close the pop-up window.

In the What about the alternative Requests for Quotations? pop-up window, two options
are presented: Cancel Alternatives and Keep Alternatives.

If this  should **not** be confirmed, click Discard.

Selecting Cancel Alternatives automatically cancels the alternative . Selecting
Keep Alternatives keeps the alternative  open, so they can still be accessed, if
any additional product quantities need to be ordered later.

Once all products are ordered, select Cancel Alternatives from whichever 
is open at that time.

![Keep or cancel pop-up for alternative RFQs.](applications/inventory_and_mrp/purchase/manage_deals/calls_for_tenders/calls-for-tenders-keep-or-cancel.png)

Finally, using the breadcrumbs at the top of the page, click Requests for Quotation to
navigate back to an overview of all .

The canceled orders can be seen, greyed out and listed with a Cancelled status, under
the Status column at the far-right of their respective rows.

Now that all product quantities have been ordered, the purchase process can be completed, and the
products can be received into the warehouse.

#### SEE ALSO
[Blanket orders](blanket_orders.md)
