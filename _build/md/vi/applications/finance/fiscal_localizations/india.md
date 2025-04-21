# Ấn Độ

<a id="india-installation"></a>

## Cài đặt

[Install](../../general/apps_modules.md#general-install) the following modules to get all the features of the Indian
localization:

| Tên                         | Tên kỹ thuật             | Mô tả                                                                                           |
|-----------------------------|--------------------------|-------------------------------------------------------------------------------------------------|
| Ấn Độ - Kế toán             | `l10n_in`                | Default [fiscal localization package](../fiscal_localizations.md#fiscal-localizations-packages) |
| Indian E-invoicing          | `l10n_in_edi`            | [Indian e-invoicing integration](#india-e-invoicing)                                            |
| Indian E-waybill            | `l10n_in_edi_ewaybill`   | [Indian E-way bill integration](#india-e-waybill)                                               |
| Indian E-waybill Stock      | `l10n_in_ewaybill_stock` | [E-waybill creation from the Inventory app](#india-e-waybill-stock)                             |
| Indian - GSTR India eFiling | `l10n_in_reports_gstr`   | [Indian GST Return filing](#india-gstr)                                                         |
| Indian - Accounting Reports | `l10n_in_reports`        | [Indian tax reports](#india-gstr-reports)                                                       |
![Indian localization modules](applications/finance/fiscal_localizations/india/india-modules.png)

<a id="india-e-invoicing"></a>

## e-Invoice system

Odoo is compliant with the **Indian Goods and Services Tax (GST) e-Invoice system** requirements.

### Thiết lập

<a id="india-e-invoicing-api"></a>

#### NIC e-Invoice registration

You must register on the  e-Invoice portal to get your
**API credentials**. You need these credentials to [configure your Odoo Accounting app](#india-e-invoicing-configuration).

1. Log in to the [NIC e-Invoice portal](https://einvoice1.gst.gov.in/) by clicking
   Login and entering your Username and Password;

   #### NOTE
   If you are already registered on the NIC portal, you can use the same login credentials.

   ![Register Odoo ERP system on e-invoice web portal](applications/finance/fiscal_localizations/india/e-invoice-system-login.png)
2. From the dashboard, go to API Registration ‣ User Credentials ‣ Create API
   User;
3. After that, you should receive an  code on your registered mobile
   number. Enter the OTP code and click Verify OTP;
4. Select Through GSP for the API interface, set Tera Software Limited as
   GSP, and type in a Username and Password for your API. Once it is done,
   click Submit.
   ![Submit API specific Username and Password](applications/finance/fiscal_localizations/india/submit-api-registration-details.png)

<a id="india-e-invoicing-configuration"></a>

#### Cấu hình trong Odoo

To enable the e-Invoice service in Odoo, go to Accounting ‣ Configuration ‣
Settings ‣ Indian Electronic Invoicing, and enter the Username and
Password previously set for the API.

![Setup e-invoice service](applications/finance/fiscal_localizations/india/e-invoice-setup.png)

<a id="india-e-invoicing-journals"></a>

##### Sổ nhật ký

To automatically send e-Invoices to the NIC e-Invoice portal, you must first configure your *sales*
journal by going to Accounting ‣ Configuration ‣ Journals, opening your *sales*
journal, and in the Advanced Settings tab, under Electronic Data
Interchange, enable E-Invoice (IN) and save.

<a id="india-e-invoicing-workflow"></a>

### Quy trình

<a id="india-invoice-validation"></a>

#### Invoice validation

Once an invoice is validated, a confirmation message is displayed at the top. Odoo automatically
uploads the JSON-signed file of validated invoices to the NIC e-Invoice portal after some time. If
you want to process the invoice immediately, click Process now.

![Indian e-invoicing confirmation message](applications/finance/fiscal_localizations/india/e-invoice-process.png)

#### NOTE
- You can find the JSON-signed file in the attached files in the chatter.
- You can check the document's  status under the
  EDI Document tab or the Electronic invoicing field of the invoice.

<a id="india-invoice-pdf-report"></a>

#### Báo cáo hoá đơn PDF

Once an invoice is validated and submitted, the invoice PDF report can be printed. The report
includes the , Ack. No (acknowledgment number) and
Ack. Date (acknowledgment date), and QR code. These certify that the invoice is a valid
fiscal document.

![IRN and QR code](applications/finance/fiscal_localizations/india/invoice-report.png)

<a id="india-edi-cancellation"></a>

#### e-Invoice cancellation

If you want to cancel an e-Invoice, go to the Other info tab of the invoice and fill out
the Cancel reason and Cancel remarks fields. Then, click Request
EDI cancellation. The status of the Electronic invoicing field changes to To
Cancel.

#### IMPORTANT
Doing so cancels both the [e-Invoice](#india-e-invoicing) and the [E-Way bill](#india-e-waybill).

![cancel reason and remarks](applications/finance/fiscal_localizations/india/e-invoice-cancellation.png)

#### NOTE
- If you want to abort the cancellation before processing the invoice, then click Call
  Off EDI Cancellation.
- Once you request to cancel the e-Invoice, Odoo automatically submits the JSON-signed file to
  the NIC e-Invoice portal. You can click Process now if you want to process the
  invoice immediately.

<a id="india-verify-e-invoice"></a>

#### GST e-Invoice verification

After submitting an e-Invoice, you can verify if the invoice is signed from the GST e-Invoice system
website itself.

1. Download the JSON file from the attached files. It can be found in the chatter of the related
   invoice;
2. Open the [NIC e-Invoice portal](https://einvoice1.gst.gov.in/) and go to
   Search ‣ Verify Signed Invoice;
3. Select the JSON file and submit it;
   ![select the JSON file for verify invoice](applications/finance/fiscal_localizations/india/verify-invoice.png)

   If the file is signed, a confirmation message is displayed.
   ![verified e-invoice](applications/finance/fiscal_localizations/india/signed-invoice.png)

<a id="india-e-waybill"></a>

## E-Way bill

<a id="india-e-waybill-setup"></a>

### Thiết lập

Odoo is compliant with the **Indian Goods and Services Tax (GST) E-waybill system** requirements.

<a id="india-e-waybill-api"></a>

#### API registration on NIC E-Way bill

You must register on the  E-Way bill portal to create your
**API credentials**. You need these credentials to [configure your Odoo Accounting app](#india-e-waybill-configuration).

1. Log in to the [NIC E-Way bill portal](https://ewaybillgst.gov.in/) by clicking
   Login and entering your Username and Password;
2. From your dashboard, go to Registration ‣ For GSP;
3. Click Send OTP. Once you have received the code on your registered mobile number,
   enter it and click Verify OTP;
4. Check if Tera Software Limited is already on the registered GSP/ERP list. If so, use
   the username and password used to log in to the NIC portal. Otherwise, follow the next steps;
   ![E-Way bill list of registered GSP/ERP](applications/finance/fiscal_localizations/india/e-waybill-gsp-list.png)
5. Select Add/New, select Tera Software Limited as your GSP Name, create a
   Username and a Password for your API, and click Add.
   ![Submit GSP API registration details](applications/finance/fiscal_localizations/india/e-waybill-registration-details.png)

<a id="india-e-waybill-configuration"></a>

#### Cấu hình trong Odoo

To set up the E-Way bill service, go to Accounting ‣ Configuration ‣ Settings
‣ Indian Electronic WayBill ‣ Setup E-Way bill, and enter your Username and
Password.

![E-way bill setup odoo](applications/finance/fiscal_localizations/india/e-waybill-configuration.png)

<a id="india-e-waybill-workflow"></a>

### Quy trình

<a id="india-e-waybill-send"></a>

#### Send an E-Way bill

To send an E-Way bill, confirm the customer invoice/vendor bill and click Send E-Way
bill.

![Send E-waybill button on invoices](applications/finance/fiscal_localizations/india/e-waybill-send-button.png)

<a id="india-invoice-validation-e-way"></a>

#### Invoice validation

Once an invoice/bill has been issued and sent via Send E-Way bill, a confirmation
message is displayed.

![Indian e-Way bill confirmation message](applications/finance/fiscal_localizations/india/e-waybill-process.png)

#### NOTE
- You can find the JSON-signed file in the attached files in the chatter.
- Odoo automatically uploads the JSON-signed file to the government portal after some time. Click
  Process now if you want to process the invoice/bill immediately.

#### Báo cáo hoá đơn PDF

You can print the invoice PDF report once you have submitted the E-Way bill. The report includes the
**E-Way bill number** and the **E-Way bill validity date**.

![E-way bill acknowledgment number and date](applications/finance/fiscal_localizations/india/e-waybill-invoice-report.png)

<a id="india-e-waybill-cancellation"></a>

#### E-Way bill cancellation

If you want to cancel an E-Way bill, go to the E-Way bill tab of the related
invoice/bill and fill out the Cancel reason and Cancel remarks fields. Then,
click Request EDI Cancellation.

#### IMPORTANT
Doing so cancels both the [e-Invoice](#india-e-invoicing) (if applicable) and the
[E-Way bill](#india-e-waybill).

![Cancel reason and remarks](applications/finance/fiscal_localizations/india/e-waybill-cancellation.png)

#### NOTE
- If you want to abort the cancellation before processing the invoice, click Call Off
  EDI Cancellation.
- Once you request to cancel the E-Way bill, Odoo automatically submits the JSON-signed file to
  the government portal. You can click Process Now if you want to process the invoice
  immediately.

<a id="india-e-waybill-stock"></a>

### E-waybill creation from receipts and delivery orders

#### NOTE
Make sure the **E-Way bill Stock** module is [installed](../../general/apps_modules.md#general-install) and
the [E-Way bill setup](#india-e-waybill-setup) is complete.

To create E-Way bills from [receipts and deliveries](../../inventory_and_mrp/inventory/shipping_receiving/daily_operations.md) in the Inventory
app, follow these steps:

1. Go to Inventory ‣ Operations ‣ Deliveries or Inventory ‣
   Operations ‣ Receipts and select an existing delivery order/receipt or create a new one.
2. Click Create E-waybill/Challan.

   #### NOTE
   To create an E-way bill:
   - A delivery order must be in the Done state (i.e., validated)
   - A receipt must have the Ready or Done state.
3. Click Generate e-Waybill to validate the E-Way bill and send it to the NIC E-Way
   bill portal.

To print the E-waybill or the challan, click the <i class="fa fa-cog"></i> (gear) icon and select
<i class="fa fa-print"></i> Ewaybill / Delivery Challan.

<a id="india-gstr"></a>

## Indian GST Return filing

<a id="india-gstr-api"></a>

### Enable API access

To file GST Returns in Odoo, you must first enable API access on the GST portal.

1. Log into the [GST portal](https://services.gst.gov.in/services/login) by entering your
   Username and Password, and go to My Profile on your **profile
   menu**;
   ![Click On the My Profile from profile](applications/finance/fiscal_localizations/india/gst-portal-my-profile.png)
2. Select Manage API Access, and click Yes to enable API access;
   ![Click Yes](applications/finance/fiscal_localizations/india/gst-portal-api-yes.png)

#### NOTE
It is recommended to set the Duration to 30 days to avoid the need for
frequent token reauthentication.

1. Doing so enables a Duration drop-down menu. Select the Duration of your
   preference, and click Confirm.

<a id="india-gstr-configuration"></a>

### Indian GST Service In Odoo

Once you have enabled the [API access](#india-gstr-api) on the GST portal, you can set up the
Indian GST Service in Odoo.

Go to Accounting ‣ Configuration ‣ Settings ‣ Indian GST Service and enter
the GST Username. Click Send OTP, enter the code, and finally,
Validate.

> ![Please enter your GST portal Username as Username](applications/finance/fiscal_localizations/india/gst-setup.png)

<a id="india-gstr-workflow"></a>

### File-in GST Return

When the Indian GST Service is configured, you can file your GST return. Go to
Accounting ‣ Reporting ‣ India ‣ GST Return periods and create a new **GST
Return Period** if it does not exist. GST Return file-in is done in **three steps** in Odoo:

#### NOTE
**Tax Return Periodicity** can be
[configured](../accounting/reporting/tax_returns.md) according to the user's
needs.

<a id="india-gstr-1"></a>

#### Gửi GSTR-1

1. The user can verify the [GSTR-1](#india-gstr-1-report) report before uploading it to the
   **GST portal** by clicking GSTR-1 Report;
2. The user can also get details to be submitted in **GSTR-1** in **Spreadsheet view** by clicking
   on Generate;
   ![GSTR-1 generate](applications/finance/fiscal_localizations/india/gst-gstr-1-generate.png)![GSTR-1 Spreadsheet View](applications/finance/fiscal_localizations/india/gst-gstr-1-spreadsheet-view.png)
3. If the **GSTR-1** report is correct, then click Push to GSTN to send it to the **GST
   portal**. The status of the GSTR-1 report changes to Sending;
   ![GSTR-1 in the Sending Status](applications/finance/fiscal_localizations/india/gst-gstr-1-sending.png)
4. After a few seconds, the status of the **GSTR-1** report changes to Waiting for
   Status. It means that the **GSTR-1** report has been sent to the GST Portal and is
   being verified on the GST Portal;
   ![GSTR-1 in the Waiting for Status](applications/finance/fiscal_localizations/india/gst-gstr-1-waiting.png)
5. Once more, after a few seconds, the status either changes to Sent or Error
   in Invoice. The status Error in Invoice indicates that some of the invoices are not
   correctly filled out to be validated by the **GST portal**;
   - If the state of the **GSTR-1** is Sent, it means your **GSTR-1** report is ready to
     be filed on the **GST portal**.
     ![Đã gửi GSTR-1](applications/finance/fiscal_localizations/india/gst-gstr-1-sent.png)
   - If the state of the **GSTR-1** is Error in Invoice, invoices can be checked for
     errors in the Log Note. Once issues have been resolved, the user can click
     Push to GSTN to submit the file again on the **GST portal**.
     ![GSTR-1 Error in Invoice](applications/finance/fiscal_localizations/india/gst-gstr-1-error.png)

   ![GSTR-1 Error in Invoice Log](applications/finance/fiscal_localizations/india/gst-gstr-1-error-log.png)
6. Click Mark as Filed after filing the **GSTR-1** report on the **GST portal**. The
   status of the report changes to Filed in **Odoo**.
   ![GSTR-1 in the Filed Status](applications/finance/fiscal_localizations/india/gst-gstr-1-filed.png)

<a id="india-gstr-2b"></a>

#### Nhận GSTR-2B

Users can retrieve the **GSTR-2B Report** from the **GST portal**. This automatically reconciles
the **GSTR-2B** report with your Odoo bills;

1. Click Fetch GSTR-2B Summary to retrieve the **GSTR-2B** summary. After a few seconds,
   the status of the report changes to Waiting for Reception. This means Odoo is trying
   to receive the **GSTR-2B** report from the **GST portal**;
   ![GSTR-2B in Waiting for Reception](applications/finance/fiscal_localizations/india/gst-gstr-2b-waiting.png)
2. Once more, after a few seconds, the status of the **GSTR-2B** changes to the Being
   Processed. It means Odoo is reconciling the **GSTR-2B** report with your Odoo bills;
   ![GSTR-2B in Waiting for Reception](applications/finance/fiscal_localizations/india/gst-gstr-2b-processed.png)
3. Once it is done, the status of the **GSTR-2B** report changes to either Matched or
   Partially Matched;
   - If the status is Matched:
     > ![GSTR-2B Matched](applications/finance/fiscal_localizations/india/gst-gstr-2b-matched.png)
   - If the status is Partially Matched, you can make changes in bills by clicking
     View Reconciled Bills. Once it is done, click re-match.
     > ![GSTR-2B Partially Matched](applications/finance/fiscal_localizations/india/gst-gstr-2b-partially.png)![GSTR-2B Reconciled Bills](applications/finance/fiscal_localizations/india/gst-gstr-2b-reconcile.png)

<a id="india-gstr-3"></a>

#### Báo cáo GSTR-3

The [GSTR-3](#india-gstr-3-report) report is a monthly summary of **sales** and **purchases**.
This return is auto-generated by extracting information from **GSTR-1** and **GSTR-2**.

1. Users can compare the **GSTR-3** report with the **GSTR-3** report available on the
   **GST portal** to verify if they match by clicking GSTR-3 Report;
2. Once the **GSTR-3** report has been verified by the user and the tax amount on the **GST portal**
   has been paid. Once paid, the report can be **closed** by clicking Closing Entry;
   ![GSTR-3](applications/finance/fiscal_localizations/india/gst-gstr-3.png)
3. In Closing Entry, add the tax amount paid on the **GST portal** using challan, and
   click POST to post the Closing Entry;
   ![GSTR-3 Post Entry](applications/finance/fiscal_localizations/india/gst-gstr-3-post.png)
4. Once posted, the **GSTR-3** report status changes to Filed.
   ![GSTR-3 Filed](applications/finance/fiscal_localizations/india/gst-gstr-3-filed.png)

<a id="india-gstr-reports"></a>

## Tax reports

<a id="india-gstr-1-report"></a>

### Báo cáo GSTR-1

The GSTR-1 report is divided into sections. It displays the Base amount,
, ,
, and CESS for each section.

> ![Báo cáo GSTR-1](applications/finance/fiscal_localizations/india/gst-gstr-1-sale-report.png)

<a id="india-gstr-3-report"></a>

### Báo cáo GSTR-3

The GSTR-3 report contains different sections:

- Details of inward and outward supply subject to a **reverse charge**;
- Eligible ;
- Values of **exempt**, **Nil-rated**, and **non-GST** inward supply;
- Details of inter-state supplies made to **unregistered** persons.
  > ![Báo cáo GSTR-3](applications/finance/fiscal_localizations/india/gst-gstr-3-report.png)
