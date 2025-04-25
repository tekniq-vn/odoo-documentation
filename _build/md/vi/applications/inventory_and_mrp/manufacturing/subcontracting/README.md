# Thầu phụ

In manufacturing, *subcontracting* is the process of a company engaging a third-party manufacturer,
or subcontractor, to manufacture products that are then sold by the contracting company.

Subcontracting provides a variety of benefits for both the contracting company and the
subcontractor.

For the contracting company, subcontracting allows them to sell a wide variety of manufactured
products, without having to worry about investing in and maintaining the equipment and labor
required to handle the manufacturing themselves.

This helps contracting companies stay flexible throughout economic cycles, as they can easily
increase or decrease their engagements with subcontractors, as necessitated by the current moment.
It also means they are able to focus on tasks they excel at, while delegating more specialized work
to subcontractors.

Mặt khác, hoạt động gia công cho phép các đơn vị gia công chuyên môn hóa vào những lĩnh vực sản xuất chuyên biệt hơn, những lĩnh vực có thể không mang lại lợi nhuận nếu thực hiện bên ngoài phạm vi của một hợp đồng gia công. Trong một số thỏa thuận nhất định, nó cũng mang lại cho họ sự linh hoạt trong việc lựa chọn dự án nào nên nhận hay từ chối, cũng như số lượng dự án mà họ muốn thực hiện tại bất kỳ thời điểm nào.

In Odoo, companies can configure their subcontracting workflows based on a variety of different
factors, including how components are sourced, and what happens to finished products once they are
manufactured.

## Cấu hình

To enable subcontracting in Odoo, navigate to Manufacturing app ‣ Configuration
‣ Settings, and tick the checkbox next to the Subcontracting setting, under the
Operations heading. Then, click Save.

![The Subcontracting setting in the manufacturing app.](../../../../.gitbook/assets/subcontracting-setting.png)

With subcontracting enabled, a few different features become available in Odoo:

- On bills of materials (BoMs), the *BoM Type* field now includes a *Subcontracting* option.
  Enabling the *Subcontracting*  type designates the 's product as a subcontracted
  product, which means Odoo knows that it is produced by a subcontractor, and not by the company
  that owns the Odoo database.
- Two subcontracting routes become available in the *Inventory* app, and can be assigned to specific
  products, on the *Inventory* tab of their product pages:
  - *Resupply Subcontractor on Order*
  - *Dropship Subcontractor on Order*

## Subcontracting workflows

In Odoo, there are three subcontracting workflows, the main difference between them being *how* the
subcontractor obtains the necessary components:

- In the *basic* subcontracting workflow, the subcontractor is fully responsible for obtaining the
  components. This workflow is outlined in the [Basic subcontracting](subcontracting_basic.md)
  documentation.
- In the *Resupply Subcontractor on Order* workflow, the contracting company sends the components
  from their warehouse to the subcontractor. This workflow is outlined in the
  [Resupply subcontractor](subcontracting_resupply.md) documentation.
- In the *Dropship Subcontractor on Order* workflow, the contracting company purchases the
  components from a vendor, and has them delivered directly to the subcontractor. This workflow is
  outlined in the [Dropship to subcontractor](subcontracting_dropship.md) documentation.

In addition to how a subcontractor obtains components, it is also necessary to consider why a
product is being subcontracted, as well as what happens to products once they are manufactured by
the subcontractor.

In terms of why a product is being subcontracted, the two main reasons are to fulfill a customer
order, or to replenish the quantity of stock on-hand.

In terms of what happens to products once they are manufactured, they can either be shipped to the
contracting company, or dropshipped directly to an end customer.

Each of the three subcontracting workflows described above can be configured to facilitate any of
these possibilities, and the methods for doing so are outlined in their respective documentation.

## Subcontracted product valuation

The valuation of a subcontracted product depends upon a few different variables:

- The cost of the required components, if provided by the contracting company; from here on referred
  to as `C`.
- The price paid to the subcontractor for the service of manufacturing the subcontracted product;
  from here on referred to as `M`.
- The cost of shipping components to the subcontractor, and having them shipped back to the
  contracting company; from here on referred to as `S`.
- The cost of dropshipping, if the components are shipped by the subcontractor to the end customer;
  from here on referred to as `D`.
- Any other associated costs, like import taxes, etc.; from here on referred to as `x`.

Therefore, the total valuation of a subcontracted product (`P`) can be represented by the following
equation:

$$
P = C + M + S + D + x

$$

It is important to note that not every subcontracted product valuation will include all of these
variables. For example, if the product is not dropshipped to the end customer, then there is no need
to factor in the cost of dropshipping.

* [Basic subcontracting](subcontracting_basic.md)
  * [Cấu hình](subcontracting_basic.md#configuration)
    * [Cấu hình sản phẩm](subcontracting_basic.md#configure-product)
    * [Configure BoM](subcontracting_basic.md#configure-bom)
  * [Basic subcontracting workflow](subcontracting_basic.md#basic-subcontracting-workflow)
    * [Create SO](subcontracting_basic.md#create-so)
    * [Process PO](subcontracting_basic.md#process-po)
    * [Process receipt or dropship order](subcontracting_basic.md#process-receipt-or-dropship-order)
      * [Process receipt](subcontracting_basic.md#process-receipt)
      * [Process dropship order](subcontracting_basic.md#process-dropship-order)
    * [Process delivery order](subcontracting_basic.md#process-delivery-order)
* [Basic subcontracting lead times](basic_subcontracting_lead_times.md)
  * [Cấu hình](basic_subcontracting_lead_times.md#configuration)
    * [Product delivery lead time](basic_subcontracting_lead_times.md#product-delivery-lead-time)
  * [Lead time workflow](basic_subcontracting_lead_times.md#lead-time-workflow)
* [Resupply subcontractor](subcontracting_resupply.md)
  * [Cấu hình](subcontracting_resupply.md#configuration)
    * [Cấu hình sản phẩm](subcontracting_resupply.md#configure-product)
    * [Configure BoM](subcontracting_resupply.md#configure-bom)
    * [Configure components](subcontracting_resupply.md#configure-components)
  * [Resupply subcontractor on order workflow](subcontracting_resupply.md#resupply-subcontractor-on-order-workflow)
    * [Create SO](subcontracting_resupply.md#create-so)
    * [Process PO](subcontracting_resupply.md#process-po)
    * [Process Resupply Subcontractor order](subcontracting_resupply.md#process-resupply-subcontractor-order)
    * [Process receipt or dropship order](subcontracting_resupply.md#process-receipt-or-dropship-order)
      * [Process receipt](subcontracting_resupply.md#process-receipt)
      * [Process dropship order](subcontracting_resupply.md#process-dropship-order)
    * [Process delivery order](subcontracting_resupply.md#process-delivery-order)
* [Resupply subcontracting lead times](resupply_subcontracting_lead_times.md)
  * [Cấu hình](resupply_subcontracting_lead_times.md#configuration)
    * [Product delivery lead time](resupply_subcontracting_lead_times.md#product-delivery-lead-time)
    * [Product manufacturing lead time](resupply_subcontracting_lead_times.md#product-manufacturing-lead-time)
    * [Resupply subcontracting workflow](resupply_subcontracting_lead_times.md#resupply-subcontracting-workflow)
* [Dropship to subcontractor](subcontracting_dropship.md)
  * [Cấu hình](subcontracting_dropship.md#configuration)
    * [Cấu hình sản phẩm](subcontracting_dropship.md#configure-product)
    * [Configure bill of materials](subcontracting_dropship.md#configure-bill-of-materials)
    * [Configure Components](subcontracting_dropship.md#configure-components)
  * [Dropship subcontractor on order workflow](subcontracting_dropship.md#dropship-subcontractor-on-order-workflow)
    * [Tạo một SO](subcontracting_dropship.md#create-an-so)
    * [Process subcontractor PO](subcontracting_dropship.md#process-subcontractor-po)
    * [Xác nhận RFQ của nhà cung cấp](subcontracting_dropship.md#confirm-vendor-rfq)
    * [Process Dropship Subcontractor order](subcontracting_dropship.md#process-dropship-subcontractor-order)
    * [Process receipt or dropship order](subcontracting_dropship.md#process-receipt-or-dropship-order)
    * [Process delivery order](subcontracting_dropship.md#process-delivery-order)
* [Dropship subcontracting lead times](dropship_subcontracting_lead_times.md)
  * [Cấu hình](dropship_subcontracting_lead_times.md#configuration)
    * [Product delivery lead time](dropship_subcontracting_lead_times.md#product-delivery-lead-time)
    * [Product manufacturing lead time](dropship_subcontracting_lead_times.md#product-manufacturing-lead-time)
    * [Component delivery lead time](dropship_subcontracting_lead_times.md#component-delivery-lead-time)
  * [Dropship subcontracting workflow](dropship_subcontracting_lead_times.md#dropship-subcontracting-workflow)
