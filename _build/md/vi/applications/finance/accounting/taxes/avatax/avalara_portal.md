<a id="avatax-portal"></a>

# Cổng thông tin Avalara (Avatax)

Avalara's (*AvaTax*) management console offers account management options including: viewing/editing
the transactions sent from Odoo to *AvaTax*, details on how the taxes are calculated, tax reporting,
tax exemption management, and tax return resources.

To access the console, first, navigate to either Avalara's [sandbox](https://sandbox.admin.avalara.com/) or [production](https://admin.avalara.com/) environment.
This will depend on which type of account was set in the [integration](./). Log in to
the management console.

![Avalara dashboard after logging into management portal.](../../../../../.gitbook/assets/avalara-portal.png)

#### SEE ALSO
For more information see Avalara's documentation: [Activate your Communications Customer Portal
account](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=qvv1656594440497&topicId=Activate_your_Communications_Customer_Portal_account.html&_LANG=enus).

<a id="avalara-portal-transactions"></a>

## Giao dịch

To access transactions, click in the Transactions link on the main dashboard upon
logging into the [Cổng thông tin Avalara (Avatax)](#avatax-portal). To manually access the *Transactions* page, while logged into
the Avalara console, navigate to Transactions ‣ Transactions.

![Avalara portal with the transactions shortcut highlighted.](../../../../../.gitbook/assets/avalara-transactions.png)

### Edit transaction

Click into a transaction to reveal more details about the transaction. These details include
sections on Invoice detail, Additional info, and Customer info.
Click <i class="fa fa-pencil"></i> Edit document details to make changes to the transaction.

A Discount can be added to adjust the invoice. This is especially useful in cases where
the transaction has already synced with Avalara / *AvaTax*, and changes need to be made afterward.

<a id="avalara-portal-filter"></a>

### Bộ lọc

Filter transactions on the Transactions page, by setting the From and
To fields, and configuring other fields to filter by, including:

- Document Status: any of the following options, All, Voided,
  Committed, Uncommitted, or Locked.
- Document Code: any of the following options, Exactly match,
  Starts with, or Contains.
- Customer/Vendor Code: the customer/vendor code in Odoo (e.g. `Contact18`).
- Country: the country this tax was calculated in; this is a text field.
- Region: the region of the country, which varies based on the Country
  selection.

Click <i class="fa fa-plus"></i> Filters to access the following filter conditions:

- Document Type: any of the following selections, All, Sales
  Invoice, Purchase Invoice, Return Invoice, Inventory Transfer
  Inbound Invoice, Inventory Transfer Outbound Invoice, or Customs
  Invoice.
- Import ID: represents the import ID of the document.

### Sắp xếp theo

On the Transactions page, transactions will be listed below, according to the set
[Bộ lọc](#avalara-portal-filter), located in the top half of the page. The following columns are
available by default, to sort by ascending or descending order:

- Doc Code: either of the following options, Exactly match,
  Starts with, or Contains.
- Doc Status: either of the following options, All, Voided,
  Committed, Uncommitted, or Locked.
- Cust/Vendor Code : this is the customer/vendor code in Odoo (e.g. Contact18).
- Region: this is the region of the country, this will vary based on the
  Country selection.
- Amount: the numeric amount of the total amount on the Odoo document.
- Tax: the numeric amount of the tax applied to the total.

![Transactions page on the Avalara portal with the filter and sort-by options highlighted.](../../../../../.gitbook/assets/transactions.png)

#### Customize columns

Additional columns can be added by clicking the <i class="fa fa-cog"></i> Customize columns. On the
resulting popover window, click the drop-down menu for the column that should be
changed.

The following columns can be added for additional transactional information:

- AvaTax calculated: the amount of tax calculated by *AvaTax*.
- Country: the country this tax was calculated in; this is a text field.
- Cust/vendor code: the customer/vendor code in Odoo (e.g. `Contact18`).
- Currency: the standardized abbreviation for the currency the amount total is in.
- Doc date: the document's date of creation.
- Doc status: any of the following options, All, Voided,
  Committed, Uncommitted, or Locked.
- Doc type: any of the following selections, All, Sales
  Invoice, Purchase Invoice, Return Invoice, Inventory Transfer
  Inbound Invoice, Inventory Transfer Outbound Invoice, or Customs
  Invoice.
- Import ID: represents the import ID of the document.
- Last modified: timestamp of the last time the document was modified.
- Location code: the location code used to calculate the tax, based on the delivery
  address.
- PO number: the purchase order number.
- Reference code: the Odoo reference code (e.g. NV/2024/00003)
- Region: the region of the country,which varies based on the Country
  selection.
- Salesperson code: the numeric ID of the user assigned to the sales order in Odoo.
- Tax date: the month/day/year of the tax calculation.
- Tax override type: where an exemption would appear, should there be none, the field
  populates with None.

To add a new column click the <i class="fa fa-plus"></i> Column.

#### SEE ALSO
For more information on *AvaTax* transactions, refer to this Avalara documentation: [Transactions](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=qvv1656594440497&topicId=transactions.html&_LANG=enus).

### Nhập-xuất

While on the [Giao dịch](#avalara-portal-transactions), click <i class="fa fa-download"></i> Import
transactions or <i class="fa fa-upload"></i> Export transactions to import or export transactions.

### Báo cáo

To access reporting, navigate to the Reports link in the top menu of the Avalara
management console. Next, select from one of the available reporting tabs: Transactions
reports, Liability & tax return reports, or Exemption reports.

Make a selection for the Report Category, and the Report Name, under the
Select a report section.

Next, fill out the Select report details section. These options will vary based on the
tab selected above.

Tùy thuộc vào kích thước báo cáo, có hai tùy chọn khả dụng trong phần Chọn số lượng giao dịch ước tính cho báo cáo của bạn: Tạo và tải xuống báo cáo ngay lập tức (đối với báo cáo nhỏ) và Tạo và tải xuống báo cáo trong nền (đối với báo cáo lớn hơn). Hãy chọn một trong hai tùy chọn tùy theo lượng giao dịch trong báo cáo này.

Finally, under the section labeled, Report preview and export make a selection of the
file type to download. Either a .PDF or .XLS can be chosen. Alternatively,
the file can be previewed by selecting the Preview option.

After making all the configurations, click Create report to download the report. Click
<i class="fa fa-star-o"></i> Make this report a favorite to save the report configuration to the
user's favorites.

After the report is created, click <i class="fa fa-download"></i> Download to download the file to
the device.

#### SEE ALSO
[See Avalara's documentation: Reports in AvaTax](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=rjq1671176624730&topicId=Reports_in_AvaTax.html&_LANG=enus).

## Add more jurisdictions

Additional jurisdictions (tax locations) can be added in the Avalara management console. Navigate to
either Avalara's [sandbox](https://sandbox.admin.avalara.com/) or [production](https://admin.avalara.com/) environment. This will depend on which type of account was set in the
[integration](./).

Tiếp theo, đi đến Cài đặt ‣ Nơi bạn thu thuế. Chọn một trong ba tab khác nhau tùy theo nhu cầu kinh doanh. Tab đầu tiên là Thuế bán hàng và sử dụng, nơi có thể thu thuế cho Hoa Kỳ. Nhấp vào <i class="fa fa-plus"></i> Thêm vào nơi bạn thu thuế bán hàng và sử dụng để thêm một địa điểm khác mà công ty thu thuế bán hàng và sử dụng.

The second option, is the VAT/GST tab where the <i class="fa fa-plus"></i> Add a country
or territory where you collect VAT/GST can be selected to add another country or territory where
the company collects VAT/GST.

Finally, on the far-right, is the Customs duty tab, where a country can be added where
the company collects customs duty. Simply click on the <i class="fa fa-plus"></i> Add a country
where you calculate customs duty icon below the tab.

![AvaTax management console, on the Where you collect tax page, with the add button and
sales and use tax tab highlighted.](../../../../../.gitbook/assets/where-you-collect-tax.png)

#### SEE ALSO
[See Avalara's documentation: Add local jurisdiction taxes](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=bla1700809896571_bla1700809896571&topicId=nbw1698727575499.html&_LANG=enus).

## Tax exemption certificate

Tax exemption certificates for customers can be added into the Avalara management console, so that
*AvaTax* is aware of which customers may be exempt from paying certain taxes. To add an *exception
certificate* navigate to Exemptions ‣ Customer certificates. From there, click on
the <i class="fa fa-plus"></i> Add a certificate to configure an exemption.

#### WARNING
An Avalara subscription to Exemption Certificate Management (ECM) is required in order to attach
certificate images, and to be ready for an audit. For more on subscribing to this add-on, visit
[Avalara](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=hff1682048150115_hff1682048150115&topicId=fol1682356576230.html&_LANG=enus).

## End-of-year operations

Dịch vụ của Avalara bao gồm cả dịch vụ khai thuế, dành cho thời điểm nộp thuế vào cuối năm. Để truy cập vào dịch vụ thuế của Avalara, hãy đăng nhập vào cổng quản lý <[https://admin.avalara.com/](https://admin.avalara.com/)>_. Sau đó, từ trang chủ, nhấp vào Khai thuế. Avalara sẽ yêu cầu người dùng Avalara đăng nhập lại vì lý do bảo mật và sẽ chuyển hướng người dùng đến cổng thông tin *Khai thuế*.

![Avalara portal with the returns shortcut highlighted.](../../../../../.gitbook/assets/avalara-returns.png)

Click Get started to begin the tax return process. For more information, refer to this
Avalara documentation: [About Managed Returns](https://community.avalara.com/support/s/document-item?language=en_US&bundleId=hps1656397152776_hps1656397152776&topicId=Learn_about_Managed_Returns.html&_LANG=enus).

#### SEE ALSO
- [AvaTax integration](./)
- [AvaTax use](avatax_use.md)
- [US Tax Compliance: Avatax elearning video](https://www.odoo.com/slides/slide/us-tax-compliance-avatax-2858?fullscreen=1)
