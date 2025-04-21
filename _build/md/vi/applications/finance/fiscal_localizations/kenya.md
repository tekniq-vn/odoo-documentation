# Kenya

<a id="localization-kenya-configuration"></a>

## Cấu hình

Install the 🇰🇪 **Kenyan** [fiscal localization package](../fiscal_localizations.md#fiscal-localizations-packages) to get
all the features of the Kenyan localization.

## eTIMS

The [Kenya Revenue Authority (KRA)](https://www.kra.go.ke/) has implemented the
[electronic Tax Invoice Management System (eTIMS)](https://www.kra.go.ke/online-services/etims)
for tax collection.

To submit documents through eTIMS, you must use an  that
integrates with the existing **Trader Invoicing System (TIS)**, such as the one provided by Odoo.
The OSCU is used to validate, encrypt, sign, transmit, and store tax invoices.

#### NOTE
Make sure to [install](../../general/apps_modules.md#general-install) the **Kenya eTIMS EDI** modules to use the OSCU
device fully.

<a id="kenya-initialization"></a>

### OSCU device initialization

The OSCU must be initialized before use. To do so, navigate to Settings ‣ General
Settings, click Update Info in the Companies section, and enter your
Tax ID.

To initialize the OSCU:

1. Go to Settings ‣ General Settings and scroll down to the Kenya
   eTIMS Integration section.
2. Set the eTIMS Server Mode to Test for the initialization.
3. Enter the Serial Number of the device and tick the two check boxes.
4. Click Initialize OSCU.

#### NOTE
Three server modes are available:

- Demo: Designed for demo purposes; it uses mock data and does not require an
  initialized OSCU;
- Test: Used to test the connection to eTIMS;
- Production: Used for live databases that are ready to send data.

#### IMPORTANT
If your device has **already been initialized** (through another ERP, for example), enable the
[Chế độ lập trình viên (chế độ gỡ lỗi)](../../general/developer_mode.md). Then, in the Kenya eTIMS Integration section,
enter the ID of the unit in the Unit ID field and the key obtained through a previous
initialization in the CMC Key field. Click Save when done.

Sau khi **phân hệ OSCU** được [khởi tạo](#kenya-initialization), một số sê-ri OSCU sẽ được tạo cho mỗi công ty trên cơ sở dữ liệu đó có **quốc gia** đặt là Kenya. Số sê-ri được tạo dựa trên mã số thuế GTGT của công ty (bất kể mã đó có hợp lệ hay không). Đây là số sê-ri duy nhất và tuần tự, bắt đầu bằng tiền tố `ODOO` theo sau là **mã số thuế GTGT** của công ty và một chuỗi số.

### Registering on eTIMS

Taxpayers *must* sign up and create an account on the [KRA portal](https://etims.kra.go.ke/basic/login/indexLogin).
If you do not have an account yet:

1. Sign up, enter your **PIN**, and verify that all information is correct, including your phone
   number, email address, and postal address. Correct any errors on the [iTax page](https://itax.kra.go.ke/KRA-Portal/).
2. An  is sent to the phone number provided. Unblock promotional
   messages if you do not receive it.
3. Upload the **business owner ID** *or* **director's ID** (as listed on iTax), along with the
   filled-out and signed **commitment form** .
4. On the **eTIMS dashboard**, click Service request at the top of the page. Select
   OSCU as the **eTIMS type**, enter `Odoo KE LTD` as the third-party integrator, and
   enter your company's OSCU serial number retrieved earlier.

#### NOTE
Service request approvals are usually quick. If there's a delay, contact the eTIMS operation
or KRA office.

### eTIMS codes

Common standard codes are **automatically** fetched from the KRA eTIMS API servers every two days.
To fetch them manually, proceed as follows:

1. Bật [Chế độ lập trình viên (chế độ gỡ lỗi)](../../general/developer_mode.md).
2. Go to Settings ‣ Technical ‣ Automation: Scheduled Actions and search for
   KE eTIMS: Fetch KRA standard codes.
3. Click the action in the list, then click Run Manually to fetch the codes.

Go to Accounting ‣ Configuration ‣ KE OSCU Codes to view the complete list of
fetched OSCU codes.

![List of fetched OSCU codes.](applications/finance/fiscal_localizations/kenya/oscu-codes.png)

<a id="etims-unspsc"></a>

### UNSPSC codes

The KRA needs UNSPSC codes for a product to be **registered**. UNSPSC codes are **automatically**
fetched from the KRA eTIMS API servers every day. To fetch them manually, proceed as follows:

1. Bật [Chế độ lập trình viên (chế độ gỡ lỗi)](../../general/developer_mode.md).
2. Go to Settings ‣ Technical ‣ Automation: Scheduled Actions and search for
   KE eTIMS: Fetch UNSPSC codes from eTIMS.
3. Click the action in the list, then click Run Manually to fetch the codes.

Go to the **product form**, and in the Accounting tab, click the UNSPSC
Category field to view the complete list of fetched UNSPSC codes.

### Thông báo

Notices are **automatically** fetched from the KRA eTIMS API servers every day. To fetch them
**manually**, proceed as follows:

1. Bật [Chế độ lập trình viên (chế độ gỡ lỗi)](../../general/developer_mode.md).
2. Go to Settings ‣ Technical ‣ Automation: Scheduled Actions and search for
   KE eTIMS: Fetch KRA notices from eTIMS.
3. Click the action in the list, then click Run Manually to fetch the notices.

Go to Accounting ‣ Configuration ‣ KE OSCU Notices to view the complete list of
fetched notices.

### Đa công ty

<a id="kenya-branch"></a>

#### SEE ALSO
[Công ty](../../general/companies.md)

If you have [multiple companies](../accounting.md#accounting-multi-company), you can centralize and manage them
all on a single Odoo database. The KRA identifies and differentiates the **main** company from
its **subsidiaries** by using IDs. Furthermore, subsidiaries are classified as **branches** of the
main company.

Để cấu hình ID công ty, mở ứng dụng **Cài đặt**, nhấp Cập nhật thông tin trong phần Công ty và tìm trường Mã chi nhánh eTIMS. **Công ty chính** có ID chi nhánh là `00` trong môi trường đa công ty. Các công ty *không phải* công ty chính có ID chi nhánh khác `00` và được KRA cấp ID riêng.

To add a branch, go to the Branches tab in the **company settings** and click
Add a line.

To fetch the **branch ID** from the KRA for your non-main companies, ensure the main company has a
Kenyan Tax ID and the OSCU device has been [initialized](#kenya-initialization).
Then, go to the Branches tab and click Populate from KRA.

#### NOTE
- The KRA considers each **place of supply** as a separate branch (ID).
- The **OSCU** device must be [initialized independently](#kenya-initialization) for each
  branch.

### Contact branch ID

To attribute a branch ID to a contact, access the contact form, go to the Accounting
tab, and enter the branch code in the eTIMS Branch Code field.

#### NOTE
By default, contacts' branch IDs are set to `OO`.

### KRA sequences

#### IMPORTANT
Odoo invoice sequences and KRA sequences are **different**.

In Odoo, invoice sequences depend on the **main company**. Main companies can see the invoices of
branches, but branches **cannot** see the main company's invoices or those of other branches.

The KRA needs **independent** sequences per branch. Therefore, Odoo manages sequences individually
per branch.

## Bảo hiểm

For **health service providers**, you can send insurance information about the main and branch
companies and update it in eTIMS. To do so, go to Accounting ‣ Configuration ‣
Settings, scroll to the Kenya eTIMS Integration section, and fill in the
Code, Name, and Rate fields. Click Send Insurance
Details when done.

<a id="kenya-product-registration"></a>

## Product registration

The KRA requires **products to be registered** first before conducting business operations (such as
stock movements, , customer invoices, etc.). For a product to be
registered, the following fields must be defined on the product form:

- In the General Information tab: Cost.
- Trong tab Kế toán:
  - Packaging Unit;
  - Packaging Quantity;
  - Origin Country;
  - eTIMS Product Type;
  - Insurance Applicable;
  - [Danh mục UNSPSC](#etims-unspsc).

If the elements above are defined, the product is automatically registered while sending the
operation to the KRA. If not, you will be alerted by a yellow banner at the top of the screen
inviting you to check the missing elements.

![Product registration template.](applications/finance/fiscal_localizations/kenya/product-registration.png)

## Stock movements

All **stock movements** must be sent to the KRA. They do not require an invoice if they are
internal operations or stock adjustments; therefore, Odoo automatically sends them if at least one
of the following conditions are met:

1. No contact is set for the move;
2. The contact is your main company or a branch of the main company.

If the stock moves are **external operations** (e.g., to contacts that are not part of the main
company or its branches), the stock moves are automatically sent *after* the invoice is sent to
eTIMS.

#### NOTE
- The stock move must be confirmed before sending the invoice to eTIMS.
- The product(s) must be [registered](#kenya-product-registration) for the stock move to be
  sent to eTIMS. If the product has not been registered yet, a yellow banner will prompt the
  products' registration.

## Mua hàng

Odoo automatically fetches new vendor bills from eTIMS every day. You need to confirm the fetched
vendor bills and send the confirmation to the KRA. To confirm a vendor bill, it must be linked to
one or several confirmed purchase order line(s).

<a id="kenya-purchases"></a>

In the case of purchases (not customs imports), the steps to link purchase order lines with bills
are the following:

1. Go to Accounting ‣ Vendors ‣ Bills.
   The vendor bill is fetched from the KRA servers. The JSON file is available in the chatter of the
   vendor bill if needed.
2. Odoo looks at the Tax ID (PIN) of the vendor (partner);
   - If it is unknown, a new contact (partner) is created.
   - If it is known and the branch ID is the same, Odoo uses the known contact.
3. In the fetched bill from the KRA, select the Product. Each vendor bill *must* contain
   a product to be confirmed and sent to eTIMS later on.
4. Odoo checks existing purchase order lines matching the product(s) entered at the previous step
   and the partner (if any). Click the Purchase Order Line field, and select the correct
   related purchase order line(s) matching the product(s). The quantities on the bill *must* be the
   same as the received quantities indicated on the purchase order.

   If no existing purchase order line matches the lines of the fetched bill, click
   Create Purchase Order and create a purchase order based on the unmatched line(s).
   Validate the resulting stock move and Confirm the bill.
5. Set a method in the eTIMS Payment Method field..
6. Once all steps are completed, click Send to eTIMS to send the vendor bill. When the
   vendor bill has been confirmed on eTIMS, the **KRA invoice number** can be found in the
   eTIMS Details tab.

![Bill registration steps.](applications/finance/fiscal_localizations/kenya/purchase-order-lines.png)

## Xuất hóa đơn

#### NOTE
The KRA does *not* accept sales if the product is not in stock.

This is the **advised sales flow** in Odoo when selling:

1. Create a **sales order**.
2. Validate the delivery.
3. Confirm the invoice.
4. Click Send and print, and then enable Send to eTIMS.
5. Click Send & print to send the invoice.

Once the invoice has been sent and signed by the KRA, the following information can be found on
it:

- **số hoá đơn KRA**;
- Mandatory KRA invoice fields, such as **SCU information**, **date**, **SCU ID**, **receipt
  number**, **item count**, **internal date**, and **receipt signature**;
- The **KRA tax table**;
- A unique **KRA QR code** for the signed invoice.

## Nhập

Customs import codes are **automatically** fetched from the KRA eTIMS API servers every day. To
fetch them manually, proceed as follows:

1. Bật [Chế độ lập trình viên (chế độ gỡ lỗi)](../../general/developer_mode.md).
2. Go to Settings ‣ Technical ‣ Automation: Scheduled Actions and search for
   KE eTIMS: Receive Customs Imports from the OSCU.
3. Click the action in the list, then click Run Manually to fetch the codes.

Go to Accounting ‣ Vendors ‣ Customs Imports to view the imported codes.

The following steps are required to send and have **customs imports** signed by the KRA:

1. Go to Accounting ‣ Vendors ‣ Customs Imports; The customs import is fetched
   automatically from the KRA.
2. Match the imported item with an existing registered product in the Product field (or
   create a product if no related product exists).
3. Set a vendor in the Partner field.
4. Based on the partner, match the imported item with its related purchase order (see
   [purchase steps](#kenya-purchases)). The stock must be correctly adjusted when the customs
   import is approved.

   If no related purchase order exists, create one and Confirm it. Then, confirm the
   delivery by clicking Receive Products, then Validate on the purchase
   order.
5. Click Match and Approve or Match and Reject, depending on the
   situation of the goods.

#### NOTE
The JSON file received from the KRA is attached to the chatter of the customs import.

## ĐMNL

The KRA requires all BOMs to be sent to them. To send BOMs to eTIMS, the product and its components
*must* be [registered](#kenya-product-registration). To access a product's BOM, click on the
product and then click the Bill of Materials smart button.

Make sure the [KRA's required fields](#kenya-product-registration) are filled in the
KRA eTIMS details section of the Accounting tab in the product form, and
click Send to eTIMS. The successful sending of the BOM is confirmed in the chatter,
where you can also find the sent information in an attached JSON file.

## Giấy báo có

The KRA does not accept credit notes with quantities or prices higher than the initial invoice. When
creating a credit note, a KRA reason must be indicated: In the credit note form, go to the
eTIMS Details tab, select the eTIMS Credit Note Reason, and then select the
invoice number in the Reversal of field.
