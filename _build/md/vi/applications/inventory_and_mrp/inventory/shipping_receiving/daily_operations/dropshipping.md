# Dropship

Dropshipping là một chiến lược xử lý đơn hàng cho phép người bán gửi hàng trực tiếp từ nhà cung cấp đến khách hàng. Thông thường, người bán mua sản phẩm từ nhà cung cấp, lưu trữ trong kho của họ và vận chuyển đến khách hàng cuối cùng khi có đơn hàng. Với dropshipping, nhà cung cấp chịu trách nhiệm lưu trữ và vận chuyển hàng hóa. Điều này giúp người bán giảm chi phí tồn kho, bao gồm cả chi phí vận hành nhà kho.

## Configure products to be dropshipped

To use dropshipping as a fulfillment strategy, navigate to the Purchase app and
select Configuration ‣ Settings. Under the Logistics heading, click
the Dropshipping checkbox, and Save to finish.

Next, go to the Sales app, click Products ‣ Products and choose
an existing product or select Create to configure a new one. On the Product
page, make sure that the Can be Sold and Can be Purchased checkboxes are
enabled.

![Enable the "Can be Sold" and "Can be Purchased" checkboxes on the product form.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping/sold-purchased-checkboxes.png)

Click on the Purchase tab and specify a vendor and the price that they sell the product
for. Multiple vendors can be added, but the vendor at the top of the list will be the one
automatically selected for purchase orders.

![The product form with a vendor specified.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping/product-vendor-config.png)

Finally, select the Inventory tab and enable the Dropship checkbox in the
Routes section.

![Enable the Dropship option in the product inventory tab.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping/enable-dropship-route.png)

#### NOTE
While it is not necessary to enable the Buy route in addition to the
Dropship route, enabling both provides the option of dropshipping the product or
purchasing it directly.

## Fulfill orders using dropshipping

Khi một đơn bán hàng được tạo cho sản phẩm dropship, một yêu cầu báo giá (RfQ) liên quan sẽ tự động được tạo để mua sản phẩm từ nhà cung cấp. Bạn có thể xem đơn bán hàng trong ứng dụng Bán hàng bằng cách chọn Đơn hàng ‣ Đơn hàng. Nhấp vào nút thông minh Mua hàng ở góc trên bên phải của đơn hàng bán để xem  liên quan.

![A dropship sales order with the Purchase smart button in the top right corner.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping/dropship-sales-order.png)

Once the  is confirmed, it becomes a purchase order, and a
dropship receipt is created and linked to it. The receipt can be viewed by clicking the
Dropship smart button in the top-right corner of the purchase order form.

![A dropship purchase order with the Receipt smart button in the top right corner.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping/dropship-purchase-order.png)

The dropship receipt displays Partners/Vendors in the Source Location field,
and Partners/Customers in the Destination Location field. Upon delivery of
the product to the customer, click on the Validate button at the top-left of the
dropship receipt to confirm the delivered quantity.

![Validate the dropship receipt after delivery.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping/validate-dropship-receipt.png)

To view all dropship orders, simply navigate to the Inventory Overview
dashboard and click the teal # TO PROCESS button on the Dropship card.

![Click the green button on the Dropship card to view all dropship orders.](applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/dropshipping/view-all-dropship-orders.png)
