# Bộ kit

In Odoo, a *kit* is a type of bill of materials (BoM) that can be manufactured and sold. Kits are
sets of unassembled components sold to customers. They may be sold as standalone products, and are
also useful tools for managing more complex bills of materials (BoMs).

#### NOTE
Để sử dụng, sản xuất và bán kit, bạn cần cài đặt cả hai ứng dụng Sản xuất và Tồn kho.

## Tạo kit dưới dạng một sản phẩm

To use a kit as a sellable product, or as a component organization tool, the kit should first be
created as a product.

To create a kit product, go to Inventory app ‣ Products ‣ Products, and then
click New.

Then, assign a name to the new kit product. Next, set the kit's product type depending on inventory
tracking needs and accounting requirements. To do this, under the General Information
tab, set the Product Type to either Consumable or Storable.

Các thành phần của kit cũng phải được cấu hình như sản phẩm thông qua Ứng dụng Tồn kho ‣ Sản phẩm ‣ Sản phẩm. Bạn không cần cài đặt đặc biệt nào cho chúng.

### Consumable kit setup details

Consumable products do not have inventory tracking. Consider setting the kit as a consumable product
when the kit is used in other manufacturing processes or when tracking inventory for the kit itself
is not needed.

* **Recommended for Continental Accounting**: If costs are expensed immediately upon purchase, then
  setting the kit's type to *consumable* is recommended.
* **Replenishment via Components**: Inventory count is managed at the component level, so reordering
  rules must be set to individual components.
* **Selling & Stock Constraints**: Kits cannot be sold if any required component is out of stock.
  Since availability depends on individual components, a sales order may appear valid, but delivery
  can be delayed if components are unavailable.

### Storable kit setup details

Storable products have detailed tracking and inventory management since they are expected to be
*stored* once they are created. Consider setting the kit as a storable product when the kit is a
tangible product or warehouse and inventory tracking is essential.

* **Recommended for Angle-Saxon Accounting**: If the Cost of Goods Sold (COGS) needs to be recorded
  in journals, then setting the kit's type to *storable* is recommended.
* **Component Purchase Constraints**: Only the kit's minimum required components can be added to an
  **eCommerce** cart unless the option to [continue
  selling](applications/websites/ecommerce/products.md) is disabled.
* **No Kit Serial Numbers**: Serial number tracking does not track the kit, only its shipped
  components.
* **Reordering Rule Recommendation**: Reordering rules should be set at the component-level.
* **Stock Replenishment Recommendation**: Stock replenishment should also be done at the
  component-level.

### Kit setup similarities

Regardless of which setup is used, there are some similarities between the two options.

* **No Kit-Level Stock Adjustments**: Stock adjustments cannot be handled at the kit-level.
* **Kit Value Does Not Change**: The stock's value is the same whether the kit is consumable or
  storable.
* **Kit Internal Transfers**: An internal transfer for the kit breaks it into components.

## Thiết lập BoM kit

Sau khi cấu hình xong sản phẩm kit và các thành phần của nó, bạn có thể tạo một  mới cho sản phẩm kit.

To do so, go to Manufacturing app ‣ Products ‣ Bills of Materials, and then
click New. Next to the Product field, click the drop-down menu to reveal a
list of products, and then select the previously configured kit product.

Then, for the BoM Type field, click the Kit option. Finally, under the
Components tab, click Add a line, and add each desired component, and
specify their quantities under the Quantity column.

Once ready, click Save to save the newly created .

![Chọn kit trên danh mục vật tư.](../../../../.gitbook/assets/bom-kit-selection.png)

Nếu kit chỉ được sử dụng như một sản phẩm có thể bán được thì chỉ cần thêm các thành phần vào tab Thành phần và không cần cấu hình hoạt động sản xuất.

#### NOTE
Khi kit được bán như một sản phẩm, nó sẽ xuất hiện riêng trên một dòng trong báo giá và đơn bán hàng. Tuy nhiên, mỗi thành phần của kit sẽ được liệt kê chi tiết trên lệnh giao hàng.

## Sử dụng kit để quản lý BoM phức tạp

Kits can also be used for complex . This method nests BoMs within
other BoMs, organizing complex products while simplifying manufacturing by defining each procurement
and production step separately.

Sublevel BoMs (subassemblies or semi-finished products) streamline these workflows, helping with
traceability efforts.

#### SEE ALSO
[Quản lý bán thành phẩm](applications/inventory_and_mrp/manufacturing/advanced_configuration/sub_assemblies.md)
