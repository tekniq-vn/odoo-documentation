# Split and merge manufacturing orders

In Odoo *Manufacturing*, it is possible to create manufacturing orders for a single unit of an item,
or multiple units of the same item. In some cases, it may be necessary to split a manufacturing
order that contains multiple units into two or more orders, or to merge two or more orders into a
single order.

#### IMPORTANT
A manufacturing order can only contain one unit of a product, or multiple units of a single
product that all use the same Bill of Materials (BoM). As a result, it is only possible to merge
manufacturing orders when every order contains the same product being manufactured with the same
BoM.

## Split manufacturing orders

To split a manufacturing order into multiple orders, begin by navigating to
Manufacturing ‣ Operations ‣ Manufacturing Orders, then select a manufacturing
order. At the top of the page, next to the New button, the manufacturing order's
reference number appears with a ⚙️ (settings) button next to it.

Click the ⚙️ (settings) button to open the general settings for the manufacturing order,
then select Split.

![The Settings and Split buttons on a manufacturing order.](applications/inventory_and_mrp/manufacturing/workflows/split_merge/settings-split.png)

Sau khi chọn Tách, thì cửa sổ bật lên Tách sản lượng sẽ xuất hiện. Trong trường Tách #, hãy nhập số lượng lệnh sản xuất mà lệnh gốc sẽ được chia ra, sau đó nhấp ra ngoài trường. Một bảng sẽ xuất hiện bên dưới và chứa mỗi dòng cho một lệnh sản xuất mới sẽ được tạo ra bởi thao tác chia tách. Trong cột Số lượng cần sản xuất, hãy nhập số lượng đơn vị sẽ được chỉ định cho mỗi lệnh sản xuất mới. Cuối cùng, nhấp vào Tách để tách lệnh sản xuất.

![The Split production pop-up window for a manufacturing order.](applications/inventory_and_mrp/manufacturing/workflows/split_merge/split-production-window.png)

After clicking Split, the original manufacturing order is split into the number of
orders that was specified in the Split # field. The reference numbers for the new
manufacturing orders are the reference number for the original order with  *-###* tags added to the
end.

## Merge manufacturing orders

To merge two or more manufacturing orders into a single order, begin by navigating to
Manufacturing ‣ Operations ‣ Manufacturing Orders. Select the manufacturing
orders that will be merged by activating the checkbox to the left of the name of each order.

![Select manufacturing orders that will be merged by clicking the checkbox for each.](applications/inventory_and_mrp/manufacturing/workflows/split_merge/select-orders.png)

Once all manufacturing orders have been selected, click the Actions button at the top of
the page, then select Merge from the drop-down menu.

![The Actions and Merge buttons on the Manufacturing Orders page.](applications/inventory_and_mrp/manufacturing/workflows/split_merge/actions-merge.png)

The selected manufacturing orders are merged into a single order. The reference number for the new
manufacturing order is the next sequential number that has *not* already been assigned to an order.

In the Source field for the manufacturing order created by the merger, the reference
numbers of the manufacturing orders that were merged are listed.
