# Thanh toán online

* [Chuyển khoản ngân hàng](payment_providers/wire_transfer.md)
* [Adyen](payment_providers/adyen.md)
* [Alipay](payment_providers/alipay.md)
* [Dịch vụ thanh toán Amazon](payment_providers/amazon_payment_services.md)
* [AsiaPay](payment_providers/asiapay.md)
* [Authorize.Net](payment_providers/authorize.md)
* [Buckaroo](payment_providers/buckaroo.md)
* [Demo](payment_providers/demo.md)
* [Flutterwave](payment_providers/flutterwave.md)
* [Mercado Pago](payment_providers/mercado_pago.md)
* [Mollie](payment_providers/mollie.md)
* [Ogone](payment_providers/ogone.md)
* [PayPal](payment_providers/paypal.md)
* [Razorpay](payment_providers/razorpay.md)
* [SIPS](payment_providers/sips.md)
* [Stripe](payment_providers/stripe.md)
* [Xendit](payment_providers/xendit.md)

Odoo embeds several **payment providers** that allow your customers to pay online, on their
*customer portals*, or on your *eCommerce website*. They can pay sales orders, invoices, or
subscriptions with recurring payments using their favorite payment methods, such as
**credit cards**.

Each payment provider is linked to a list of supported [payment methods](#payment-providers-payment-methods) that can be (de)activated based on your needs.

![Online payment form](../../.gitbook/assets/online-payment.png)

#### NOTE
Các ứng dụng Odoo ủy quyền việc xử lý thông tin nhạy cảm cho nhà cung cấp dịch vụ thanh toán đã được chứng nhận, để bạn không cần lo lắng về việc tuân thủ PCI. Không có thông tin nhạy cảm nào (như số thẻ tín dụng) được lưu trữ trên máy chủ Odoo hoặc trong cơ sở dữ liệu Odoo được lưu trữ ở nơi khác. Thay vào đó, các ứng dụng Odoo sử dụng một mã tham chiếu duy nhất cho dữ liệu được lưu trữ an toàn trong hệ thống của nhà cung cấp dịch vụ thanh toán.

<a id="payment-providers-supported-providers"></a>

## Supported payment providers

To access the supported payment providers, go to Accounting ‣ Configuration ‣
Payment Providers, Website ‣ Configuration ‣ Payment Providers, or
Sales ‣ Configuration ‣ Payment Providers.

<a id="payment-providers-online-providers"></a>

### Online payment providers

|                                                                         | Payment flow from          | [Token hoá](#payment-providers-tokenization)   | [Thu hồi thủ công](#payment-providers-manual-capture)   | [Hoàn tiền](#payment-providers-refunds)   | [Thanh toán nhanh](#payment-providers-express-checkout)   |
|-------------------------------------------------------------------------|----------------------------|------------------------------------------------|---------------------------------------------------------|-------------------------------------------|-----------------------------------------------------------|
| [Adyen](payment_providers/adyen.md)                                     | Odoo                       | ✔                                              | Toàn bộ và một phần                                     | Toàn bộ và một phần                       |                                                           |
| [Amazon Payment Services](payment_providers/amazon_payment_services.md) | Trang web của nhà cung cấp |                                                |                                                         |                                           |                                                           |
| [AsiaPay](payment_providers/asiapay.md)                                 | Trang web của nhà cung cấp |                                                |                                                         |                                           |                                                           |
| [Authorize.Net](payment_providers/authorize.md)                         | Odoo                       | ✔                                              | Full only                                               | Full only                                 |                                                           |
| [Buckaroo](payment_providers/buckaroo.md)                               | Trang web của nhà cung cấp |                                                |                                                         |                                           |                                                           |
| [Flutterwave](payment_providers/flutterwave.md)                         | Trang web của nhà cung cấp | ✔                                              |                                                         |                                           |                                                           |
| [Mercado Pago](payment_providers/mercado_pago.md)                       | Trang web của nhà cung cấp |                                                |                                                         |                                           |                                                           |
| [Mollie](payment_providers/mollie.md)                                   | Trang web của nhà cung cấp |                                                |                                                         |                                           |                                                           |
| [PayPal](payment_providers/paypal.md)                                   | Trang web của nhà cung cấp |                                                |                                                         |                                           |                                                           |
| [Razorpay](payment_providers/razorpay.md)                               | Odoo                       | ✔                                              | Full only                                               | Toàn bộ và một phần                       |                                                           |
| [SIPS](payment_providers/sips.md)                                       | Trang web của nhà cung cấp |                                                |                                                         |                                           |                                                           |
| [Stripe](payment_providers/stripe.md)                                   | Odoo                       | ✔                                              | Full only                                               | Toàn bộ và một phần                       | ✔                                                         |
| [Xendit](payment_providers/xendit.md)                                   | Trang web của nhà cung cấp |                                                |                                                         |                                           |                                                           |

#### NOTE
- Each provider has its own specific configuration flow, depending on which feature is
  available.
- Some of these online payment providers can also be added as [bank accounts](accounting/bank.md), but this is **not** the same process as adding them as payment
  providers. Payment providers allow customers to pay online, and bank accounts are added and
  configured in the Accounting app to do a [bank reconciliation](accounting/bank/reconciliation.md).

<a id="payment-providers-bank-payments"></a>

### Bank payments

- [Chuyển khoản ngân hàng](payment_providers/wire_transfer.md)
  <br/>
  When selected, Odoo displays your payment information with a payment reference. You have to
  approve the payment manually once you have received it in your bank account.
  <br/>
- [SEPA Direct Debit](accounting/payments/batch_sdd.md)
  <br/>
  Your customers can make a bank transfer to register a SEPA Direct Debit mandate and get their
  bank account charged directly.
  <br/>

<a id="payment-providers-add-new"></a>

## Enabling a payment provider

To add a new payment provider and make its related payment methods available to your customers,
proceed as follows:

1. Go to the payment provider's website, create an account, and make sure you have the API
   credentials requested for third-party use. These are necessary for Odoo to communicate with the
   payment provider.
2. In Odoo, navigate to the Payment providers by going to Accounting ‣
   Configuration ‣ Payment Providers, Website ‣ Configuration ‣ Payment
   Providers, or Sales ‣ Configuration ‣ Payment Providers.
3. Select the provider and configure the Credentials tab.
4. Set the State field to Enabled.

#### NOTE
- The fields available in the Credentials tab depend on the payment provider. Refer
  to the [related documentation](#payment-providers-supported-providers) for more
  information.
- Once you have enabled the payment provider, it is automatically published on your website.
  If you wish to unpublish it, click the Published button. Customers cannot make
  payments through an unpublished provider, but they can still manage
   their existing tokens linked to such a provider.

<a id="payment-providers-test-mode"></a>

### Chế độ kiểm tử

If you wish to try the payment provider as a test, set the State field in the payment
provider form to Test mode, then enter your provider's test/sandbox credentials in the
Credentials tab.

#### NOTE
By default, the payment provider remains **unpublished** in test mode so that it's not visible to
visitors.

#### WARNING
We recommend using the test mode on a duplicate or a test database to avoid potential issues
with your invoice numbering.

<a id="payment-providers-payment-methods"></a>

## Phương thức thanh toán

Mỗi nhà cung cấp dịch vụ thanh toán liên quan đến một danh sách các phương thức thanh toán được hỗ trợ; các phương thức được liệt kê trong trường Phương thức thanh toán tại tab Cấu hình của biểu mẫu nhà cung cấp dịch vụ thanh toán là những phương thức đã được kích hoạt. Để kích hoạt hoặc hủy kích hoạt một phương thức thanh toán cho nhà cung cấp, nhấp Kích hoạt phương thức thanh toán, sau đó nhấp nút bật/tắt của phương thức liên quan.

### Icons and brands

Các biểu tượng hiển thị bên cạnh phương thức thanh toán trên trang web của bạn là biểu tượng của các thương hiệu đã được kích hoạt cho phương thức thanh toán hoặc, nếu không có, là biểu tượng của chính phương thức thanh toán đó. Để chỉnh sửa chúng, hãy vào Kế toán ‣ Cấu hình ‣ Phương thức thanh toán, Trang web ‣ Cấu hình ‣ Phương thức thanh toán hoặc Bán hàng ‣ Cấu hình ‣ Phương thức thanh toán, sau đó nhấp vào phương thức thanh toán bạn muốn chỉnh sửa.

To modify a payment method's icon, hover your mouse over the image in the upper-right corner of the
payment method's form and click the pencil icon (✎).

Select the Brands tab to view the brands that have been activated for the payment
method. The brands and their related icons are displayed based on their sequence order; to reorder
them, drag and drop them in the desired order. To modify a brand's icon, select the brand, then,
in the popup window that opens, hover the mouse over the image in the upper-right corner and click
the pencil icon (✎).

### Advanced configuration

To configure payment methods further, go to Accounting ‣ Configuration ‣ Payment
Methods, Website ‣ Configuration ‣ Payment Methods or Sales
‣ Configuration ‣ Payment Methods. Click on the payment method, then activate the
[developer mode](../general/developer_mode.md#developer-mode). Click the Configuration tab to adapt the
features.

<a id="payment-providers-tokenization"></a>

## Token hoá

[If the payment provider supports this feature](#payment-providers-online-providers), customers
can save their payment method details for later. To enable this feature, go to the
Configuration tab of the selected payment provider and enable Allow Saving
Payment Methods.

In this case, a **payment token** is created in Odoo to be used as a payment method for subsequent
payments without the customer having to enter their payment method details again. This is
particularly useful for the eCommerce conversion rate and subscriptions that use recurring payments.

<a id="payment-providers-manual-capture"></a>

## Manual capture

[If the payment provider supports this feature](#payment-providers-online-providers), you can
authorize and capture payments in two steps instead of one. To enable this feature, go to the
Configuration tab of the selected payment provider and enable Capture Amount
Manually.

When you authorize a payment, the funds are reserved on the customer's payment method but not
immediately charged. They are charged when you manually capture the payment later on. You can also
void the authorization to cancel it and release the reserved funds. Capturing payments manually is
helpful in many situations:

- Receive the payment confirmation and wait until the order is shipped to capture the payment.
- Review and verify that orders are legitimate before the payment is completed and the fulfillment
  process starts.
- Avoid potentially high refund fees for refunded payments: payment providers will not charge you
  for voiding an authorization.
- Hold a security deposit to return later, minus any deductions (e.g., in case of damages).

To capture the payment after it was authorized, go to the related sales order or invoice and click
the Capture Transaction button. To release the funds, click the Void
Transaction button.

#### NOTE
- Some payment providers support capturing only part of the authorized amount. The remaining
  amount can then be either captured or voided. These providers have the value **Full and
  partial** in the [table above](#payment-providers-online-providers). The providers that
  only support capturing or voiding the total amount have the value **Full only**.
- The funds are likely not reserved forever. After a certain time, they may be automatically
  released back to the customer's payment method. Refer to your payment provider's documentation
  for the exact reservation duration.
- Odoo does not support this feature for all payment providers, but some allow the manual capture
  from their website interface.

<a id="payment-providers-refunds"></a>

## Hoàn tiền

If your payment provider supports this feature, you can refund payments directly from Odoo. It does
not need to be enabled first. To refund a customer payment, navigate to it and click the
Refund button.

#### NOTE
- Some payment providers support refunding only part of the amount. The remaining amount can then
  optionally be refunded, too. These providers have the value **Full and partial** in the
  [table above](#payment-providers-online-providers). The providers that only support
  refunding the total amount have the value **Full only**.
- Odoo does not support this feature for all payment providers, but some allow to refund payments
  from their website interface.

<a id="payment-providers-express-checkout"></a>

## Thanh toán nhanh

[Nếu nhà cung cấp dịch vụ thanh toán hỗ trợ tính năng này](#payment-providers-online-providers), bạn có thể cho phép khách hàng sử dụng các nút Google Pay và Apple Pay để thanh toán đơn hàng Thương mại điện tử của họ chỉ với một cú nhấp chuột. Khi sử dụng một trong các nút này, khách hàng sẽ đi trực tiếp từ giỏ hàng đến trang xác nhận mà không cần điền thông tin liên hệ. Họ chỉ cần xác nhận thanh toán trên mẫu thanh toán của Google hoặc Apple.

To enable this feature, go to the Configuration tab of the selected payment provider and
enable Allow Express Checkout.

#### NOTE
All prices shown on the express checkout payment form always include taxes.

## Trạng thái khả dụng

You can adapt the payment provider's availability by specifying the Maximum amount
allowed and modifying the Currencies and Countries in the
Configuration tab.

<a id="payment-providers-currencies-countries"></a>

### Tiền tệ và quốc gia

Tất cả nhà cung cấp dịch vụ thanh toán đều có danh sách các loại tiền tệ và quốc gia khả dụng khác nhau. Chúng đóng vai trò là bộ lọc đầu tiên trong quá trình thanh toán, tức là các phương thức thanh toán được liên kết với nhà cung cấp dịch vụ thanh toán sẽ không khả dụng để lựa chọn nếu loại tiền tệ hoặc quốc gia của khách hàng không nằm trong danh sách được hỗ trợ. Vì có thể có lỗi, cập nhật và thông tin chưa biết trong danh sách các loại tiền tệ và quốc gia khả dụng, nên bạn có thể thêm hoặc xóa các loại tiền tệ hoặc quốc gia được hỗ trợ của nhà cung cấp dịch vụ thanh toán.

#### NOTE
- [Payment methods](#payment-providers-payment-methods) also have their own list of
  available currencies and countries that serves as another filter during payment operations.
- Nếu danh sách các loại tiền tệ hoặc quốc gia được hỗ trợ trống, điều đó có nghĩa là danh sách quá dài để hiển thị hoặc Odoo không có thông tin về nhà cung cấp dịch vụ thanh toán đó. Nhà cung cấp dịch vụ thanh toán vẫn khả dụng, mặc dù có khả năng giao dịch sẽ bị từ chối ở bước sau nếu quốc gia hoặc tiền tệ không được hỗ trợ.

### Maximum amount

You can restrict the Maximum Amount that can be paid with the selected provider. Leave
the field to `0.00` to make the payment provider available regardless of the payment amount.

#### IMPORTANT
This feature is not intended to work on pages that allow the customer to update the payment
amount, e.g., the **Donation** snippet and the **Checkout** page when paid [shipping methods](../websites/ecommerce/shipping.md) are enabled.

<a id="payment-providers-journal"></a>

## Payment journal

A [payment journal](accounting/bank.md) must be defined for the payment provider to record the
payments on an **outstanding account**. By default, the Bank journal is added as the
payment journal for all payment providers. To modify it, go to the Configuration tab of
the selected payment provider and select another Payment journal.

#### NOTE
- The payment journal must be a Bank journal.
- The same journal can be used for several payment providers.
- Payment journals must only be configured if the [Invoicing or Accounting app](accounting.md)
  is installed.

### Accounting perspective

Từ góc độ kế toán, có hai loại quy trình thanh toán online: các khoản thanh toán được chuyển trực tiếp vào tài khoản ngân hàng của bạn và tuân theo quy trình [đối chiếu](accounting/bank/reconciliation.md) thông thường, và các khoản thanh toán từ [nhà cung cấp dịch vụ thanh toán online bên thứ ba](#payment-providers-online-providers) yêu cầu bạn tuân theo một quy trình kế toán khác. Đối với các khoản thanh toán này, bạn cần xem xét cách ghi nhận bút toán sổ nhật ký. Chúng tôi khuyên bạn nên tham khảo ý kiến kế toán viên.

By default, the Bank Account defined for the [payment journal](#payment-providers-journal) is used, but you can also specify an [outstanding account](accounting/bank.md#bank-outstanding-accounts) for each payment provider to separate the provider's payments from
other payments.

![Define an outstanding account for a payment provider.](../../.gitbook/assets/bank_journal.png)

#### SEE ALSO
- [Chuyển khoản ngân hàng](payment_providers/wire_transfer.md)
- [Adyen](payment_providers/adyen.md)
- [Alipay](payment_providers/alipay.md)
- [Authorize.Net](payment_providers/authorize.md)
- [AsiaPay](payment_providers/asiapay.md)
- [Buckaroo](payment_providers/buckaroo.md)
- [Demo](payment_providers/demo.md)
- [Mercado Pago](payment_providers/mercado_pago.md)
- [Mollie](payment_providers/mollie.md)
- [Ogone](payment_providers/ogone.md)
- [PayPal](payment_providers/paypal.md)
- [Razorpay](payment_providers/razorpay.md)
- [SIPS](payment_providers/sips.md)
- [Stripe](payment_providers/stripe.md)
- [Xendit](payment_providers/xendit.md)
- [Bank and cash accounts](accounting/bank.md)
