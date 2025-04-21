# B2B (tax excluded) and B2C (tax included) pricing

When working with consumers, prices are usually expressed with taxes
included in the price (e.g., in most eCommerce). But, when you work in a
B2B environment, companies usually negotiate prices with taxes excluded.

Odoo manages both use cases easily, as long as you register your prices
on the product with taxes excluded or included, but not both together.
If you manage all your prices with tax included (or excluded) only, you
can still easily do sales order with a price having taxes excluded (or
included): that's easy.

Tài liệu này chỉ áp dụng cho từng trường hợp sử dụng cụ thể khi bạn cần có hai mức giá tham chiếu (đã bao gồm thuế hoặc chưa bao gồm thuế) cho cùng một sản phẩm. Nguyên nhân của sự phức tạp này là do không tồn tại mối quan hệ đối xứng giữa giá đã bao gồm thuế và giá chưa bao gồm thuế, như được minh họa trong trường hợp sử dụng tại Bỉ với thuế suất 21%:

- Your eCommerce has a product at **10€ (taxes included)**
- This would do **8.26€ (taxes excluded)** and a **tax of 1.74€**

But for the same use case, if you register the price without taxes on
the product form (8.26€), you get a price with tax included at 9.99€,
because:

- **8.26€ \* 1.21 = 9.99€**

So, depending on how you register your prices on the product form, you
will have different results for the price including taxes and the price
excluding taxes:

- Taxes Excluded: **8.26€ & 10.00€**
- Taxes Included: **8.26€ & 9.99€**

#### NOTE
If you buy 100 pieces at 10€ taxes included, it gets even more
tricky. You will get: **1000€ (taxes included) = 826.45€ (price) +
173.55€ (taxes)** Which is very different from a price per piece at
8.26€ tax excluded.

This documentation explains how to handle the very specific use case
where you need to handle the two prices (tax excluded and included) on
the product form within the same company.

#### NOTE
Về mặt tài chính, bạn không có thêm doanh thu khi bán sản phẩm của mình với giá 10€ thay vì 9,99€ (đối với mức thuế 21%), vì doanh thu của bạn sẽ vẫn như ở mức 9,99€, chỉ có điều thuế cao hơn 0,01€. Vì vậy, nếu bạn điều hành một cửa hàng thương mại điện tử tại Bỉ, hãy làm hài lòng khách hàng với mức giá 9,99€ thay vì 10€. Xin lưu ý rằng điều này không áp dụng cho 20€ hoặc 30€, hoặc các mức thuế khác, hoặc số lượng >1. Bạn cũng sẽ làm hài lòng chính mình vì bạn có thể quản lý mọi thứ không bao gồm thuế, điều này giúp giảm lỗi và dễ dàng hơn cho chuyên viên sales của bạn.

## Cấu hình

### Đầu trang

Cách tốt nhất để tránh sự phức tạp này là chỉ chọn một cách quản lý giá và tuân thủ theo cách đó: giá chưa bao gồm thuế hoặc giá đã bao gồm thuế. Xác định cách nào là mặc định được lưu trên biểu mẫu sản phẩm (trên thuế mặc định liên quan đến sản phẩm) và để Odoo tự động tính toán cách còn lại, dựa trên bảng giá và vị trí tài chính. Đàm phán hợp đồng của bạn với khách hàng theo cách phù hợp. Cách này hoạt động mượt mà ngay khi cài đặt và bạn không cần phải cấu hình.

If you can not do that and if you really negotiate some prices with tax
excluded and, for other customers, others prices with tax included, you
must:

1. always store the default price **tax excluded** on the product form, and
   apply a tax (price excluded on the product form)
2. create a pricelist with prices in **tax included**, for specific
   customers
3. create a fiscal position that switches the tax excluded to a tax
   included
4. assign both the pricelist and the fiscal position to customers who
   want to benefit to this pricelist and fiscal position

For the purpose of this documentation, we will use the above use case:

- your product default sale price is 8.26€ tax excluded
- but we want to sell it at 10€, tax included, in our shops or
  eCommerce website

<a id="b2b-b2c-ecommerce"></a>

### thương mại điện tử

If you only use B2C or B2B prices on your website, simply select the appropriate setting in the
**Website** app settings.

If you have both B2B and B2C prices on a single website, please follow these instructions:

1. Activate the [developer mode](../../../general/developer_mode.md#developer-mode) and go to General Settings
   ‣ Users & Companies ‣ Groups.
2. Open either `Technical / Tax display B2B` or `Technical / Tax display B2C`.
3. Under the Users tab, add the users requiring access to the price type. Add B2C users
   in the B2C group and B2B users in the B2B group.

### Cài đặt sản phẩm của bạn

Your company must be configured with tax excluded by default. This is
usually the default configuration, but you can check your **Default Sale
Tax** from the menu Configuration ‣ Settings
of the Accounting application.

![image](applications/finance/accounting/taxes/B2B_B2C/price_B2C_B2B01.png)

Once done, you can create a **B2C** pricelist. You can activate the
pricelist feature per customer from the menu:
Configuration ‣ Settings of the Sale application.
Choose the option **different prices per customer segment**.

Once done, create a B2C pricelist from the menu
Configuration ‣ Pricelists.
It's also good to rename the default pricelist into B2B to avoid confusion.

Then, create a product at 8.26€, with a tax of 21% (defined as tax not
included in price) and set a price on this product for B2C customers at
10€, from the Sales ‣ Products
menu of the Sales application:

![image](applications/finance/accounting/taxes/B2B_B2C/price_B2C_B2B02.png)

### Setting the B2C fiscal position

From the accounting application, create a B2C fiscal position from this
menu: Configuration ‣ Fiscal Positions.
This fiscal position should map the VAT 21% (tax excluded of price)
with a VAT 21% (tax included in price)

![image](applications/finance/accounting/taxes/B2B_B2C/price_B2C_B2B03.png)

## Test by creating a quotation

Create a quotation from the Sale application, using the
Sales ‣ Quotations menu. You should have the
following result: 8.26€ + 1.73€ = 9.99€.

![image](applications/finance/accounting/taxes/B2B_B2C/price_B2C_B2B04.png)

Then, create a quotation but **change the pricelist to B2C and the
fiscal position to B2C** on the quotation, before adding your product.
You should have the expected result, which is a total price of 10€ for
the customer: 8.26€ + 1.74€ = 10.00€.

![image](applications/finance/accounting/taxes/B2B_B2C/price_B2C_B2B05.png)

This is the expected behavior for a customer of your shop.

## Avoid changing every sale order

If you negotiate a contract with a customer, whether you negotiate tax
included or tax excluded, you can set the pricelist and the fiscal
position on the customer form so that it will be applied automatically
at every sale of this customer.

The pricelist is in the **Sales & Purchases** tab of the customer form,
and the fiscal position is in the accounting tab.

Note that this is error prone: if you set a fiscal position with tax
included in prices but use a pricelist that is not included, you might
have wrong prices calculated for you. That's why we usually recommend
companies to only work with one price reference.
