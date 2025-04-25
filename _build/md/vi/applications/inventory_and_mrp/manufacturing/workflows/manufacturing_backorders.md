# Manufacturing backorders

In some cases, the full quantity of a manufacturing order cannot be produced immediately. When this
happens, Odoo *Manufacturing* allows for the manufacturing of partial quantities of the order and
creates a *backorder* for the remaining amount.

In the *Manufacturing* app, creating a backorder splits the original manufacturing order into two
orders. The reference tag for each order is the tag used for the original order, followed by a
hyphen and then an additional number to indicate that it's a backorder.

## Create a manufacturing backorder

To create a backorder for part of a manufacturing order, begin by navigating to
Manufacturing ‣ Operations ‣ Manufacturing Orders. Select a manufacturing order
with a quantity of two or more or create one by clicking Create.

If a new manufacturing order is created, select a product from the Product drop-down
menu and enter a quantity of two or more in the Quantity field, then click
Confirm to confirm the order.

After manufacturing the quantity that is being produced immediately, enter that number in the
Quantity field at the top of the manufacturing order.

![The quantity field on a manufacturing order.](../../../../_images/quantity-field.png)

Next, click Validate, and a You produced less than initial demand pop-up
window appears, from which a backorder can be created. Click Create Backorder to split
the manufacturing order into two separate orders, with the reference tags *WH/MO/XXXXX-001* and
*WH/MO/XXXXX-002*.

![The Create Backorder button on the "You produced less than initial demand" pop-up window.](../../../../_images/create-backorder-button.png)

Order *001* contains the items that have been manufactured, and is closed immediately. Order *002*
is the backorder that contains the items that have yet to be manufactured, and remains open, to be
completed at a later date.

Once the remaining units can be manufactured, navigate to Manufacturing ‣
Operations ‣ Manufacturing Orders, and then select the backorder manufacturing order. If all of
the remaining units are manufactured immediately, simply click Validate to close the
order.

If only some of the remaining units are manufactured immediately, create another backorder for the
remainder by following the steps detailed in this section.

## Create a backorder in Shop Floor

Backorders for manufacturing orders can also be created from the *Shop Floor* module.

#### NOTE
In order to use the *Shop Floor* module, the *Work Orders* setting must be enabled. To do so,
navigate to Manufacturing ‣ Configuration ‣ Settings, enable the
Work Orders checkbox, and then click Save.

To create a backorder from the *Shop Floor* module, begin by navigating to
Manufacturing ‣ Operations ‣ Manufacturing Orders. Select an  for multiple
units of a product, for which a backorder needs to be created.

On the , select the Work Orders tab, and then click the Open Work Order
(external link icon) button on the line of the work order to be processed. On the resulting
Work Orders pop-up window, click the Open Shop Floor button to open the
*Shop Floor* module.

When accessed from a specific work order, the *Shop Floor* module opens to the page for the work
center where the order is configured to be processed, and isolates the work order's card so that no
other cards are shown.

Complete the steps on the work order's card until the Register Production step is
reached, and then click on it to open the Register Production pop-up window.

#### IMPORTANT
Do **not** click the # Units button on the right side of the step. Doing so
automatically registers the full amount of units as having been produced.

On the Register Production pop-up window, enter the number of units produced in the
Quantity field. Make sure the number entered is *less* than the number of units listed
to the right of the field. Then, click Validate.

![The Register Production pop-up window in the Shop Floor module.](../../../../_images/register-production1.png)

The pop-up window disappears and the # Units button on the work order's card updates to
reflect the number of units produced, as a fraction of the number of units for which the  was
originally created.

Next, click the Mark as Done button at the bottom-right of the work order's card. The
work order card begins to fade away. Once it disappears completely, a new work order card appears,
titled with the original 's reference number with a `-002` tag added to the end of it.

This new reference number represents the backorder . The original 's reference number now
appears with a `-001` tag added to the end of it to distinguish it from the backorder .

If the original  has no remaining work orders, it can be closed by selecting the All
filter in the top navigation of the *Shop Floor* module, and then clicking Close
Production at the bottom of the 's card.

Nếu  ban đầu còn các công đoạn chưa hoàn thành trước khi có thể được đóng, thì các thẻ của công đoạn sẽ xuất hiện trên trang *Xưởng* tại những khu vực sản xuất được cấu hình để thực hiện các công đoạn đó. Các thẻ này có thể được xử lý như bình thường, và những đơn hàng tách kiện tiếp theo có thể được tạo thêm từ các thẻ công đoạn này theo hướng dẫn chi tiết trong phần này.

Once the current work order for the backorder  is ready to be processed, this can also be
completed as normal, and an additional backorder can be created from its work order card by
following the instructions detailed in this section.

After the final work order for the backorder  has been completed, the  can be closed by
clicking the Close Production button at the bottom of the work order's card.
