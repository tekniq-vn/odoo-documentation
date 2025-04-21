# Use eWallets and gift cards

With Odoo, customers can use **eWallets** and **gift cards** for online and in-store shopping.

To enable eWallets and gift cards for eCommerce and Point of Sale (PoS), first enable
Discounts, Loyalty & Gift Card under Sales app ‣ Configuration ‣
Settings ‣ Pricing section. Once enabled, go to Sales app ‣ Products ‣ Gift
cards & eWallet and Create a new eWallet or gift card program.

## ví điện tử

eWallets allow customers to save credits on their online account and use these credits as a payment
method when buying items in an online store or a brick-and-mortar store. eWallets can also be used
to centralize multiple [gift cards](#ewallet-gift-gift-cards).

Trước khi tạo chương trình Ví điện tử, cần tạo sản phẩm **nạp tiền** Ví điện tử. Nạp tiền là giá trị tín dụng số được xác định trước để thêm vào Ví điện tử đổi lấy giá trị tương đương bằng tiền thật. Tín dụng này sau đó có thể được sử dụng làm phương thức thanh toán trong cửa hàng thương mại điện tử hoặc . Giá trị nạp tiền có thể có nhiều mức khác nhau.

To create a top-up product, go to Sales app ‣ Products ‣ Products and
Create a new product. On the product template, configure the options as follows:

- Product Name: enter a name for the top-up product (for example, `$50 Top-Up`)
- Can be Sold: enabled
- Product Type: select Service
- Invoicing Policy: select Prepaid/Fixed Price
- Create on Order: select Nothing
- Sales Price: enter the amount of the top-up

#### NOTE
In order to have eWallet top-ups of different amounts, create multiple top-up products and
modify the Sales Price accordingly.

Once the top-up is created, go to Sales app ‣ Products ‣ Gift cards & eWallet
to Create an eWallet program. The following configuration options are available:

- Program Name: enter a name for the eWallet program
- Program Type: select eWallet
- eWallet Products: select the eWallet top-up created earlier. Repeat the process if
  you created top-ups of different amounts.
- Email template: select the email template used for the email sent to the customer. To
  create a new template, click on the field, select Search More, and then click
  Create.
- Currency: select the currency to use for the eWallet program
- Company: select the company for which the program is valid and available
- Available On: select the applications on which the program is valid and available
- Website: select the website on which the program is valid and available. Leave this
  field empty to include all websites.
- Point of Sale: select the  in which the program is valid
  and available. Leave this field empty to include all .

![eWallet program configuration page](applications/sales/sales/products_prices/ewallets_giftcards/ewallet-configuration.png)

Once the program is configured, click the Generate eWallet button in the upper-left
corner to generate eWallets. eWallets can be generated based on Customers and/or
Customer Tags. The quantity is automatically adapted according to the
Customers and Customer Tags selected. Then, set the eWallet
value. Finally, set the Valid Until period if applicable.

Generated eWallets can be accessed through the eWallets smart button in the upper-right
corner. From there, Send or Share the eWallets via email or a URL link.

![eWallets send and share buttons](applications/sales/sales/products_prices/ewallets_giftcards/ewallet-share.png)

Click on an eWallet to change the Expiration Date, Partner, or
Balance. The Code of an eWallet *cannot* be changed, deleted, or duplicated.

<a id="ewallet-gift-gift-cards"></a>

## Thẻ quà tặng

Gift cards can be purchased by customers, and in turn used as a payment method upon checkout at an
eCommerce shop or .

Before creating a new gift card program, it is necessary to first create gift cards as products. To
do so, go to Sales app ‣ Products ‣ Products and Create a product.
On the product template, configure the options as follows:

- Product Name: enter a name for the gift card product
- Can be Sold: enabled
- Product Type: select Service
- Invoicing Policy: select Prepaid/Fixed Price
- Create on Order: select Nothing
- Sales Price: enter the amount of the gift card

#### NOTE
In order to have gift cards of different amounts, create multiple gift card products and modify
the Sales Price accordingly.

Once the gift card product is created, go to Sales app ‣ Products ‣ Gift cards
& eWallet to Create a gift card program. The following configuration options are
available:

- Program Name: enter a name for the gift card program
- Program Type: select Gift Card
- Gift Card Products: select the gift card product created earlier. Repeat the process
  if you created gift card products of different amounts.
- Email template: select the default Gift Card: Gift Card Information
  template, or create a new template by clicking on the field, selecting Search More,
  and then clicking Create.
- Print Report: select Gift Card
- Currency: select the currency to use for the gift card program
- Company: select the company for which the program is valid and available
- Available On: select the applications on which the program is valid and available
- Website: select the website on which the program is valid and available. Leave this
  field empty to include all websites.
- Point of Sale: select the  in which the program is valid
  and available. Leave this field empty to include all .

![Gift card program configuration page](applications/sales/sales/products_prices/ewallets_giftcards/giftcard-configuration.png)

Khi chương trình đã được cấu hình, nhấp vào nút Tạo thẻ quà tặng ở góc trên bên trái để tạo các thẻ quà tặng. Thẻ có thể được tạo cho Khách hàng ẩn danh hoặc Khách hàng được chọn. Đặt Số lượng cần tạo đối với Khách hàng ẩn danh, hoặc chọn Khách hàng và/hoặc Thẻ khách hàng đối với Khách hàng được chọn. Sau đó, thiết lập Giá trị thẻ quà tặng. Cuối cùng, nếu cần, hãy đặt khoảng thời gian Hiệu lực đến.

Generated gift cards can be accessed through the Gift Cards smart button in the
upper-right corner. From there, Send or Share the gift cards via email or a
URL link.

![Gift cards send and share buttons](applications/sales/sales/products_prices/ewallets_giftcards/giftcard-share.png)

Click on a gift card to change the Expiration Date, Partner, or
Balance. The Code of a gift card *cannot* be changed, deleted, or
duplicated.
