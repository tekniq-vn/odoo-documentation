# Stripe

Connecting a payment terminal allows you to offer a fluid payment flow to your customers and ease
the work of your cashiers.

#### IMPORTANT
- Stripe payment terminals do not require an [IoT Box](../../../../general/iot.md)
- Stripe terminals can be used in many countries, but not worldwide. Check the [global
  availability for Stripe Terminal](https://support.stripe.com/questions/global-availability-for-stripe-terminal).
- Stripe's integration works with [Stripe Terminal smart readers](https://docs.stripe.com/terminal/smart-readers)

#### SEE ALSO
- [Stripe as payment provider](../../../../finance/payment_providers/stripe.md)
- [List of payment methods supported by Stripe](https://stripe.com/payments/payment-methods)

## Cấu hình

### Configure the payment method

Activate **Stripe** in the settings by going to Point of Sale ‣ Configuration ‣
Settings ‣ Payment Terminals and enabling Stripe.

Then, create the payment method:

- Go to Point of Sale ‣ Configuration ‣ Payment Methods, click
  Create, and complete the Method field with your payment method's name;
- Set the Journal field as Bank and the Use a Payment Terminal
  field as Stripe;
- Enter your payment terminal serial number in the Stripe Serial Number field;
- Click Don't forget to complete Stripe connect before using this payment method.

![payment method creation form](applications/sales/point_of_sale/payment_methods/terminals/stripe/create-method-stripe.png)

#### NOTE
- Click Identify Customer to allow this payment method **exclusively** for identified
  customers. For any unidentified customers to be able to pay with Stripe, leave the
  Identify Customer field unchecked.
- The Outstanding Account and the Intermediary Account can stay empty to
  use the default accounts.
- Find your payment terminal serial number under the device or on [Stripe's dashboard](https://dashboard.stripe.com).

### Connect Stripe to Odoo

Nhấp vào Kết nối Stripe. Thao tác này sẽ tự động chuyển hướng bạn đến trang cấu hình. Điền tất cả thông tin để tạo tài khoản Stripe của bạn và liên kết với Odoo. Sau khi hoàn tất biểu mẫu, bạn có thể lấy khóa API (Khóa có thể hiển thị và Khóa bí mật) trên trang web **Stripe**. Để thực hiện, hãy nhấp vào Lấy khóa bí mật và có thể hiển thị của bạn, nhấp vào khóa để sao chép chúng và dán chúng vào các trường tương ứng trong Odoo. Giờ đây, thiết bị đầu cuối của bạn đã sẵn sàng để được cấu hình trong POS.

![stripe connection form](applications/sales/point_of_sale/payment_methods/terminals/stripe/stripe-connect.png)

#### NOTE
- When you use **Stripe** exclusively in Point of Sale, you only need the **Secret Key** to use
  your terminal.
- When you use Stripe as **payment provider**, the State can stay set as
  Disabled.
- For databases hosted **On-Premise**, the Connect Stripe button does not work. To
  retrieve the API keys manually, log in to your [Stripe dashboard](https://dashboard.stripe.com), type `API` in the search bar, and click
  Developers > API.

### Configure the payment terminal

Swipe right on your payment terminal, click Settings, enter the admin PIN code, validate
and select your network.

#### NOTE
- The user's device and the terminal must share the same network.
- In case of a Wi-Fi connection, the network must be secured.
- You must enter the admin PIN code to access your payment terminal settings. By default, this
  code is `07139`.

### Link the payment method to a POS

To add a **payment method** to your point of sale, go to Point of Sale ‣
Configuration ‣ Settings. Select the POS, scroll down to the Payments section, and
add your payment method for **Stripe** in the Payment Methods field.

## Khắc phục sự cố

### Payment terminal unavailable in your Stripe account

If the payment terminal is unavailable in your Stripe account, you must add it manually:

1. Log into your [Stripe's dashboard](https://dashboard.stripe.com) and go to
   Stripe dashboard ‣ Payments ‣ Readers ‣ Locations;
2. Add a location by clicking the + New button or selecting an already created location;
3. Click the + New button in the Readers box and fill in the required
   information.

#### NOTE
You must provide a **registration code**. To retrieve that code, swipe right on your device,
enter the admin PIN code (by default: `07139`), validate, and click Generate a
registration code.
