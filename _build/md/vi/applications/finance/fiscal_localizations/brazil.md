# Brazil

## Đầu trang

With the Brazilian localization, sales taxes can be automatically computed and electronic invoices
for goods (NF-e) and services (NFS-e) can be sent using AvaTax (Avalara) through  calls.
Moreover, taxes for services can be configured.

For the goods and services tax computation and electronic invoicing process, you need to configure
the [contacts](#brazil-contacts), [company](#brazil-company), [products](#brazil-products), and [create an account in AvaTax](#brazil-avatax-account) which needs to be
configured in the general settings.

For the services taxes, you can create and configure them from Odoo directly without computing them
with AvaTax.

The localization also includes taxes and a chart of accounts template that can be modified if
needed.

#### SEE ALSO
Links to helpful resources for the Brazilian localization, including onboarding materials and
videos:

- [Onboarding checklist for new users](https://docs.google.com/document/d/e/2PACX-1vSNYTYVnR_BzvQKL3kn5YdVzPjjHc-WHw_U3udk5tz_dJXo69woj9QrTMinH_siyOX2rLGjvspvc8AF/pub).
- [YouTube playlist - Brazil (Localization)](https://youtube.com/playlist?list=PL1-aSABtP6ADqexw4YNCbKPmpFggajxlX&si=RgmZR3Jco3223Np4).
- [YouTube playlist - Tutoriais Odoo em Português](https://youtube.com/playlist?list=PL1-aSABtP6ACGOW2UREePGjHQ2Bgdy-UZ&si=j6tiI36eB7BoKVQB).

## Cấu hình

### Modules installation

[Install](../../general/apps_modules.md#general-install) the following modules to get all the features of the Brazilian
localization:

| Tên                                                              | Tên kỹ thuật                                 | Mô tả                                                                                                                                                                                                                                      |
|------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Brazil - Kế toán                                                 | `l10n_br`                                    | Default [fiscal localization package](../fiscal_localizations.md#fiscal-localizations-packages), which represents<br/>having the Generic Brazilian chart of accounts and Taxes, together with document types and<br/>identification types. |
| Brazil - Accounting Reports                                      | `l10n_br_reports`                            | Accounting reports for Brazil.                                                                                                                                                                                                             |
| AvaTax Brazil & AvaTax Brazil for Services                       | `l10n_br_avatax` & `l10n_br_avatax_services` | Goods and Services tax computation through Avalara.                                                                                                                                                                                        |
| Brazilian Accounting EDI & Brazilian Accounting EDI for services | `l10n_br_edi` & `l10n_br_edi_services`       | Provides electronic invoicing for goods and services for Brazil through AvaTax.                                                                                                                                                            |
| Brazil Pix QR codes                                              | `l10n_br_pix`                                | Implements Pix QR codes for Brazil.                                                                                                                                                                                                        |

<a id="brazil-company"></a>

### Cấu hình công ty của bạn

To configure your company information, go to the Contacts app and search the name
given to your company.

1. Select the Company option at the top of the page. Then, configure the following
   fields:
   - Tên
   - Address: add City, State, Zip Code,
     Country
     - In the Street field, enter the street name, number, and any additional address
       information.
     - In the Street 2 field, enter the neighborhood.
   - Identification Number: CNPJ or CPF
   - Tax ID: associated with the identification type
   - IE: State registration
   - IM: Municipal registration
   - SUFRAMA code: Superintendence of the Manaus Free Trade Zone - add if applicable
   - Điện thoại
   - Email

   ![Cấu hình công ty.](applications/finance/fiscal_localizations/brazil/contact-configuration.png)
2. Configure the Fiscal Information within the Sales and Purchase tab:
   - Add the Fiscal Position for [AvaTax Brazil](#brazil-fiscal-positions).
   - Tax Regime: Federal Tax Regime
   - ICMS Taxpayer Type: indicates ICMS regime, Exempt status,
     or Non-Taxpayer
   - Main Activity Sector

   ![Company fiscal configuration.](applications/finance/fiscal_localizations/brazil/contact-fiscal-configuration.png)
3. Configure the following extra Fiscal Information if you are going to issue NFS-e:
   - Add the Fiscal Position for [AvaTax Brazil](#brazil-fiscal-positions).
   - COFINS Details: Taxable, Not Taxable, Taxable with rate 0%, Exempt,
     Suspended
   - PIS Details Taxable, Not Taxable, Taxable with rate 0%, Exempt,
     Suspended
   - CSLL Taxable If the company is subject to CSLL or not

   ![Company fiscal configuration for NFSe.](applications/finance/fiscal_localizations/brazil/contact-fiscal-configuration-nfse.png)
4. Finally, upload a company logo and save the contact.

#### NOTE
If you are a simplified regime, you need to configure the ICMS rate under
Accounting ‣ Configuration ‣ Settings ‣ Taxes ‣ AvaTax Brazil.

<a id="brazil-avatax-account"></a>

### Configure AvaTax integration

Avalara AvaTax is a tax calculation and electronic invoicing provider that can be integrated in Odoo
to automatically compute taxes by taking into account the company, contact (customer), product, and
transaction information to retrieve the correct tax to be used and process the e-invoice afterward
with the government.

Using this integration requires [In-App-Purchases (IAPs)](../../essentials/in_app_purchase.md) to
compute the taxes and to send the electronic invoices. Whenever you compute taxes, send an
electronic document (NF-e, NFS-e, etc), or perform any electronic flow (NF-e Cancellation,
Correction letter, Invalidate invoice number range), an API call is made using credits from your
[IAP credits balance](https://iap.odoo.com/iap/in-app-services/819).

#### NOTE
- Odoo is a certified partner of Avalara Brazil.
- You can [buy IAP credit on odoo.com](https://iap.odoo.com/iap/in-app-services/819).
- On creation, new databases receive 500 free credits.

#### Credential configuration

To activate AvaTax in Odoo, you need to create an account. To do so, go to
Accounting ‣ Configuration ‣ Settings ‣ Taxes, and in the AvaTax
Brazil section, add the administration email address to be used for the AvaTax portal in the
AvaTax Portal Email, and then click on Create account.

#### WARNING
When **testing** or **creating a production** AvaTax Portal Email integration in a
sandbox or production database, use a real email address, as it is needed to log in to the
Avalara Portal and set up the certificates, whether you want to test or use it on production.

There are two different Avalara Portals, one for testing and one for production:

- Sandbox: [https://portal.sandbox.avalarabrasil.com.br/](https://portal.sandbox.avalarabrasil.com.br/)
- Production: [https://portal.avalarabrasil.com.br/](https://portal.avalarabrasil.com.br/)

When you create the account from Odoo, be sure to select the right environment. Moreover, the
email used to open the account cannot be used to open another account. Save your API
ID and API Key when you create the account from Odoo.

![Transfer API Credentials.](applications/finance/fiscal_localizations/brazil/transfer-api-credentials.png)

After you create the account from Odoo, you need to go to the Avalara Portal to set up your
password:

1. Access the [Avalara portal](https://portal.avalarabrasil.com.br/Login).
2. Click on Meu primeiro acesso.
3. Add the email address you used in Odoo to create the Avalara/AvaTax account, and then click
   Solicitar Senha.
4. You will receive an email with a token and a link to create your password. Click on this link and
   copy-paste the token to allocate your desired password.

![AvaTax account configuration.](applications/finance/fiscal_localizations/brazil/avatax-account-configuration.png)

#### NOTE
You can transfer  credentials. Use this only when you have already created an account in
another Odoo instance and wish to reuse it.

#### A1 certificate upload

In order to issue electronic invoices, a certificate needs to be uploaded to the [AvaTax portal](https://portal.avalarabrasil.com.br/Login).

The certificate will be synchronized with Odoo, as long as the external identifier number in the
AvaTax portal matches - without special characters - with the CNPJ number, and the identification
number (CNPJ) in Odoo matches with the CNPJ in AvaTax.

#### IMPORTANT
To issue NFS-e, some cities require that you link the certificate within the City Portal system
before issuing NFS-e from Odoo.

If you receive an error message from the city that says Your certificate is not linked
to the user, that means this process needs to be done in the city portal.

### Configure master data

#### Hệ thống tài khoản

The [chart of accounts](../accounting/get_started/chart_of_accounts.md) is installed by default
as part of the data set included in the localization module. The accounts are mapped automatically
in their corresponding taxes, and the default account payable and account receivable fields.

#### NOTE
The chart of accounts for Brazil is based on the SPED CoA, which gives a baseline of the accounts
needed in Brazil.

You can add or delete accounts according to the company's needs.

#### Sổ nhật ký

Tại Brazil, một số *sê-ri* được liên kết với một dải số thứ tự dùng cho hóa đơn điện tử. Số sê-ri này có thể được cấu hình trong Odoo trên sổ nhật ký bán hàng, thông qua trường Sê-ri. Nếu cần sử dụng nhiều hơn một sê-ri, thì cần tạo thêm một sổ nhật ký bán hàng mới, và gán một số sê-ri mới cho từng sê-ri cần thiết.

The Use Documents field needs to be selected. When issuing electronic and non-electronic
invoices, the Type field selects the document type used when creating the invoice. The
Type field will only be displayed if the Use Documents field is selected on
the journal.

![Journal configuration with the Use Documents? field checked.](applications/finance/fiscal_localizations/brazil/journal-configuration.png)

#### NOTE
When creating the journal, ensure the field Dedicated Credit Note Sequence is
unchecked, as in Brazil, sequences between invoices, credit notes, and debit notes are shared per
series number, which means per journal.

#### Thuế

Taxes are automatically created when installing the Brazilian localization. Taxes are already
configured, and some of them are used by Avalara when computing taxes on the sales order or invoice.

Taxes can be edited, or more taxes can be added. For example, some taxes used for services need to
be manually added and configured, as the rate may differ depending on the city where you are
offering the service.

#### IMPORTANT
If you decide to do service taxes manually, you won't be able to issue an NFS-e. To
electronically send an NFS-e, you need to compute taxes using Avalara.

#### WARNING
Không xóa các loại thuế vì chúng được sử dụng để tính toán thuế AvaTax. Nếu bị xóa, Odoo sẽ tạo lại chúng khi được sử dụng trong  hoặc hóa đơn và tính thuế bằng AvaTax, nhưng tài khoản dùng để ghi nhận thuế cần được cấu hình lại trong tab Định nghĩa của thuế, dưới các phần Phân bổ cho hóa đơn và Phân bổ cho đơn hoàn tiền.

#### SEE ALSO
[Taxes functional documentation](../accounting/taxes.md)

<a id="brazil-products"></a>

#### Sản phẩm

To use the AvaTax integration on sale orders and invoices, first specify the following information
on the product depending on its intended use:

##### E-Invoice for goods (NF-e)

- CEST Code: Code for products subject to ICMS tax substitution
- Mercosul NCM Code: Mercosur Common Nomenclature Product Code
- Source of Origin: Indicates the origin of the product, which can be foreign or
  domestic, among other possible options depending on the specific use case
- SPED Fiscal Product Type: Fiscal product type according to SPED list table
- Purpose of Use: Specify the intended purpose of use for this product

![Product configuration.](applications/finance/fiscal_localizations/brazil/product-configuration.png)

#### NOTE
Odoo automatically creates three products to be used for transportation costs associated with
sales. These are named `Freight`, `Insurance`, and `Other Costs`. They are already configured, if
more need to be created, duplicate and use the same configuration (configuration needed:
Product Type `Service`, Transportation Cost Type `Insurance`, `Freight`,
or `Other Costs`).

##### E-Invoice for services (NFS-e)

- Mercosul NCM Code: Mercosur Common Nomenclature Product Code
- Purpose of Use: Specify the intended purpose of use for this product
- Service Code Origin: City Service Code where the provider is registered
- Service Codes: City Service Code where the service will be provided, if no
  code is added, the Origin City Code will be used
- Labor Assignment: Defines if your services includes labor

<a id="brazil-contacts"></a>

#### Liên hệ

Before using the integration, specify the following information on the contact:

1. General information about the contact:
   - Select the Company option for a contact with a tax ID (CNPJ), or check
     Individual for a contact with a CPF.
   - Tên
   - Address: add City, State, Zip Code,
     Country
     - In the Street field, enter the street, number, and any extra address information.
     - In the Street 2 field, enter the neighborhood.
   - Identification Number: CNPJ or CPF
   - Tax ID: associated with the identification type
   - IE: state tax identification number
   - IM: municipal tax identification number
   - SUFRAMA code: SUFRAMA registration number
   - Điện thoại
   - Email

   ![Contact configuration.](applications/finance/fiscal_localizations/brazil/contact-configuration.png)

   #### NOTE
   The CPF, IE, IM, and SUFRAMA code fields are
   are hidden until the Country is set to `Brazil`.
2. Fiscal information about the contact under the Sales & Purchase tab:
   - Fiscal Position: add the AvaTax fiscal position to automatically compute taxes on
     sale orders and invoices automatically
   - Tax Regime: federal tax regime
   - ICMS Taxpayer Type: taxpayer type determines if the contact is within the
     ICMS regime, Exempt status, or Non-taxpayer
   - Main Activity Sector: list of main activity sectors of the contact

   ![Contact fiscal configuration.](applications/finance/fiscal_localizations/brazil/contact-fiscal-configuration.png)
3. Configure the following extra Fiscal Information if you are going to issue NFS-e:
   - Add the Fiscal Position for [AvaTax Brazil](#brazil-fiscal-positions)
   - COFINS Details: Taxable, Not Taxable, Taxable with rate 0%, Exempt,
     Suspended
   - PIS Details: Taxable, Not Taxable, Taxable with rate 0%, Exempt,
     Suspended
   - CSLL Taxable: If the company is subject to CSLL or not

   ![Contact fiscal configuration for NFSe.](applications/finance/fiscal_localizations/brazil/contact-fiscal-configuration-nfse.png)

<a id="brazil-fiscal-positions"></a>

#### Fiscal positions

To compute taxes and send electronic invoices on sale orders and invoices, both the
Detect Automatically and the Use AvaTax API options need to be enabled in
the Fiscal Position.

The Fiscal Position can be configured on the [contact](#brazil-contacts) or
selected when creating a sales order or an invoice.

![Fiscal position configuration](applications/finance/fiscal_localizations/brazil/fiscal-position-configuration.png)

## Quy trình

This section provides an overview of the actions that trigger [API calls](https://en.wikipedia.org/wiki/API) for tax computation, along with instructions on how to send
electronic invoices for goods (NF-e) and services (NFS-e) for government validation.

#### WARNING
Please note that each  call incurs a cost. Be mindful of the actions that trigger these
calls to manage costs effectively.

### Tax computation

#### Tax calculations on quotations and sales orders

Trigger an  call to calculate taxes on a quotation or sales order automatically with AvaTax in
any of the following ways:

- **Xác nhận báo giá**
  : Confirm a quotation into a sales order.
- **Manual trigger**
  : Click on Compute Taxes Using AvaTax.
- **Xem trước**
  : Click on the Preview button.
- **Email a quotation / sales order**
  : Send a quotation or sales order to a customer via email.
- **Online quotation access**
  : When a customer accesses the quotation online (via the portal view), the  call is
    triggered.

#### Tax calculations on invoices

Trigger an  call to calculate taxes on a customer invoice automatically with AvaTax in any of
the following ways:

- **Manual trigger**
  : Click on Compute Taxes Using AvaTax.
- **Xem trước**
  : Click on the Preview button.
- **Online invoice access**
  : When a customer accesses the invoice online (via the portal view), the  call is triggered.

#### NOTE
The Fiscal Position must be set to `Automatic Tax Mapping (Avalara Brazil)` for any
of these actions to compute taxes automatically.

#### SEE ALSO
[Fiscal positions (tax and account mapping)](../accounting/taxes/fiscal_positions.md)

<a id="brazil-electronic-documents"></a>

### Chứng từ điện tử

#### Hóa đơn bán hàng

Để xử lý hóa đơn điện tử cho hàng hóa (NF-e) hoặc dịch vụ (NFS-e), hóa đơn cần được xác nhận và thuế cần được tính bởi Avalara. Sau khi hoàn tất bước đó, hãy nhấp vào nút :guilabel: `Gửi & In` ở góc trên bên trái. Trong cửa sổ bật lên xuất hiện, hãy nhấp vào :guilabel: `Xử lý hóa đơn điện tử` và bất kỳ tùy chọn nào khác - :guilabel: `Tải xuống` hoặc :guilabel: `Email`. Cuối cùng, hãy nhấp vào :guilabel: `Gửi & In` để xử lý hóa đơn với chính phủ.

Before sending the electronic invoice for goods (NF-e) or services (NFS-e), some fields need to be
filled out on the invoice:

- Customer, with all the customer information
- Payment Method: Brazil: how the invoice is planned to be paid
- Fiscal Position set as the Automatic Tax Mapping (Avalara Brazil)
- Document Type set as (55) Electronic Invoice (NF-e) or (SE)
  Electronic Service Invoice (NFS-e)

There are some other optional fields that depend on the nature of the transaction. These fields are
not required, so no errors will appear from the government if these optional fields are not
populated for most cases:

- Freight Model determines how the goods are planned to be transported - domestic
- Transporter Brazil determines who is doing the transportation

![Invoice information needed to process an electronic invoice.](applications/finance/fiscal_localizations/brazil/invoice-info-needed.png)![Process electronic invoice pop-up in Odoo.](applications/finance/fiscal_localizations/brazil/process-electronic-invoice.png)

#### NOTE
All of the fields available on the invoice used to issue an electronic invoice are also available
on the sales order, if needed. When creating the first invoice, the field Document
Number is displayed, allocated as the first number to be used sequentially for subsequent
invoices.

#### Giấy báo có

If a sales return needs to be registered, then a credit note can be created in Odoo to be sent to
the government for validation.

#### NOTE
Credit notes are only available for electronic invoices for goods (NF-e).

#### SEE ALSO
[Issue a credit note](../accounting/customer_invoices/credit_notes.md#accounting-credit-notes-issue-credit-note)

#### Giấy báo Nợ

If additional information needs to be included, or values need to be corrected that were not
accurately provided in the original invoice, a debit note can be issued.

#### NOTE
Debit notes are only available for electronic invoices for goods (NF-e).

Chỉ những sản phẩm đã có trong hóa đơn gốc mới được phép đưa vào giấy báo nợ. Mặc dù bạn có thể thay đổi đơn giá hoặc số lượng sản phẩm, nhưng **không** được phép thêm sản phẩm vào giấy báo có. Mục đích của chứng từ này là để khai báo phần giá trị bạn muốn cộng thêm vào hóa đơn gốc cho cùng sản phẩm hoặc ít hơn.

#### SEE ALSO
[Issue a debit note](../accounting/customer_invoices/credit_notes.md#accounting-credit-notes-issue-debit-note)

#### Huỷ hoá đơn

It is possible to cancel an electronic invoice that was validated by the government.

#### NOTE
Check whether the electronic invoice is still within the cancellation deadline, which may vary
according to the legislation of each state.

##### E-invoices for goods (NF-e)

Cancel an e-invoice for goods (NF-e) in Odoo by clicking Request Cancel and adding a
cancellation Reason on the pop-up that appears. If you want to send this cancellation
reason to the customer via email, activate the E-mail checkbox.

![Invoice cancellation reason in Odoo.](applications/finance/fiscal_localizations/brazil/invoice-cancellation.png)

#### NOTE
This is an electronic cancellation, which means that Odoo will send a request to the government
to cancel the NF-e, and it will then consume one  credit, as an  call occurs.

##### E-invoices for services (NFS-e)

Hủy hóa đơn điện tử cho dịch vụ (NFS-e) trong Odoo bằng cách nhấp vào Yêu cầu hủy. Trong trường hợp này, không có quy trình hủy điện tử vì không phải thành phố nào cũng cung cấp dịch vụ này. Người dùng cần tự hủy NFS-e này trên cổng thông tin của thành phố. Sau khi hoàn tất bước đó, họ có thể yêu cầu hủy trong Odoo, và hóa đơn sẽ được hủy.

#### Correction letter

A correction letter can be created and linked to an electronic invoice for goods (NF-e) that was
validated by the government.

This can be done in Odoo by clicking Correction Letter and adding a correction
Reason on the pop-up that appears. To send this correction reason to a customer via
email, activate the E-mail checkbox.

![Correction letter reason in Odoo.](applications/finance/fiscal_localizations/brazil/correction-letter.png)

#### NOTE
Correction letters are only available for electronic invoices for goods (NF-e).

#### Invalidate invoice number range

A range of sequences that are assigned to sales journals can be invalidated with the government if
they are not currently used, **and** will not be used in the future. To do so, navigate to the
journal, and click the ⚙️ (gear) icon ‣ Invalidate Number Range (BR). On the
Invalidate Number Range (BR) wizard, add the Initial Number and
End Number of the range that should be canceled, and enter an invalidation
Reason.

![Number range invalidation selection in Odoo.](applications/finance/fiscal_localizations/brazil/range-number-invalidation.png)![Number range invalidation wizard in Odoo.](applications/finance/fiscal_localizations/brazil/range-number-invalidation-wizard.png)

#### NOTE
Invalidate invoice number range documents are only available for electronic invoices for goods
(NF-e).

#### NOTE
The log of the canceled numbers along with the XML file are recorded in the chatter of the
journal.

### Vendor bills

On the vendor bills side, when receiving an invoice from a supplier, you can encode the bill in Odoo
by adding all the commercial information together with the same Brazilian specific information that
is recorded on the [customer invoices](#brazil-electronic-documents).

These Brazilian specific fields are:

- Payment Method: Brazil: how the invoice is planned to be paid
- Document Type: used by your vendor
- Document Number: the invoice number from your supplier
- Freight Model: **NF-e specific** how goods are planned to be transported - domestic
- Transporter Brazil: **NF-e specific** who is doing the transportation.
