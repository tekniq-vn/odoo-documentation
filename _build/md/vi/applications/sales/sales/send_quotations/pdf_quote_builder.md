# PDF quote builder

The *PDF Quote Builder* in Odoo *Sales* provides the opportunity to send customers a fully
customized PDF file for quotes, showcasing the company and products, with various information and
design elements, instead of just showing the price and total.

The PDF Quote Builder groups header pages, product descriptions, the price(s), and footer pages to
create a detailed quote. It can also inject dynamic texts in the PDF to personalize the offer for
the customer.

Having a customized PDF in quotes provides a heightened conclusion to the shopping experience for
customers, and adds an elegant level of professionalism to a company.

#### SEE ALSO
[Odoo Quick Tips - Create a PDF quote [video]](https://www.youtube.com/watch?v=tQNydBZt-VI)

#### NOTE
It is recommended to edit PDF forms with Adobe software. The form fields on the header and footer
PDF templates are necessary to get dynamic values with Odoo.

## Cấu hình

In order to add custom PDF files for quotes, the PDF Quote builder feature *must* be
configured.

To do that, navigate to Sales app ‣ Configuration ‣ Settings. Then, on the
Settings page, scroll to the Quotations & Orders section, and locate the
PDF Quote builder feature.

![The PDF Quote Builder feature located on the Settings page of the Sales application.](applications/sales/sales/send_quotations/pdf_quote_builder/pdf-quote-builder-feature.png)

Here, custom Header pages and Footer pages can be uploaded. To upload
either, click the Upload your file button, or the ✏️ (pencil) icon to the
right of the desired field, and proceed to locate, select, and upload the desired PDF file.

#### NOTE
Headers and footers can also be added directly in a quotation template, so it's possible to have
different variations per template.

Clicking the 🗑️ (trash) icon deletes the current PDF file and replaces the blank field
with an Upload your file button.

Once the desired PDF file(s) are uploaded in the appropriate fields in the PDF Quote
builder section of the *Sales* Settings page, be sure to click Save.

The files uploaded here will be the default PDF used for all quotes.

#### NOTE
Values set in the PDF Quote Builder settings are company-specific.

## Dynamic text in PDFs

While creating custom PDFs for quotes, use *dynamic text* for Odoo to auto-fill the PDF content with
information related to the quote from the Odoo database, like names, prices, etc.

Dynamic text values are form components (text inputs) that can be added in a PDF file, and Odoo
automatically fills those values in with information related to the quote.

### Dynamic text values

Below are common dynamic text values used in custom PDFs, and what they represent:

- name: Sales Order Reference
- partner_id_\_name: Customer Name
- user_id_\_name: Salesperson Name
- amount_untaxed: Untaxed Amount
- amount_total: Total Amount
- delivery_date: Delivery Date
- validity_date: Expiration Date
- client_order_ref: Customer Reference

#### NOTE
Double underscore notation for partner_id_\_name and user_id_\_name values
are used in place of the typically used `.` symbol because the library currently does not support
the `.` symbol.

Product-specific dynamic text values are as follows:

- description: Product Description
- quantity: Quantity
- uom: Unit of Measure (UoM)
- price_unit: Price Unit
- discount: Discount
- product_sale_price: Product List Price
- taxes: Taxes name joined by a comma (`,`)
- tax_excl_price: Tax Excluded Price
- tax_incl_price: Tax Included Price

Once the PDF file(s) are complete, save them to the computer's hard drive, and proceed to upload
them to Odoo via Sales app ‣ Configuration ‣ Settings ‣ PDF Quote builder.

Upload the created PDF in the Header pages or Footer pages field.

Once the upload(s) are complete, click Save.

## Add PDF to product

In Odoo *Sales*, it's also possible to add a custom PDF to a product form. When a PDF is added to a
product, and that product is used in a quotation, that PDF is also inserted in the final PDF.

To add a custom PDF to a product, start by navigating to Sales app ‣ Products ‣
Products, and select the desired product to which a custom PDF should be added.

#### NOTE
A document could also be added to a product variant, instead of a product. If there are documents
on a product *and* on its variant, **only** the documents in the variant are shown.

To add a custom document to a product variant, navigate to Sales app ‣ Products
‣ Product Variants. Select the desired variant, click the Documents smart button,
and proceed to upload the custom document(s) to the specific product variant.

On the product page, click the Documents smart button at the top of the page.

![The Documents smart button on a product form in Odoo Sales.](applications/sales/sales/send_quotations/pdf_quote_builder/documents-smart-button.png)

Doing so reveals a separate Documents page for that product, wherein files related to
that product can be uploaded. From this page, either click New or Upload.

Clicking Upload instantly provides the opportunity to upload the desired document. Then,
the document can be further configured on the document card, or by clicking the three dots icon in
the top right corner of the document card, and then clicking Edit.

Clicking New reveals a blank documents form, in which the desired PDF can be uploaded
via the Upload your file button on the form, located in the File Content
field.

![A standard document form with various fields for a specific product in Odoo Sales.](applications/sales/sales/send_quotations/pdf_quote_builder/blank-document-form.png)

Various information and configurations related to the uploaded document can be modified here.

The first field on the documents form is for the Name of the document, and it is
grayed-out (not clickable) until a document is uploaded. Once a PDF has been uploaded, the
Name field is auto-populated with the name of the PDF, and it can then be edited.

Prior to uploading a document, there's the option to designate whether the document is a
File or URL from the Type drop-down field menu.

![A standard document form with an uploaded pdf in Odoo Sales.](applications/sales/sales/send_quotations/pdf_quote_builder/document-form-uploaded-pdf.png)

#### NOTE
If a PDF is uploaded, the Type field is auto-populated to File, and it
cannot be modified.

Then, in the Sales section, in the Visible at field, click the drop-down
menu, and select either: Quotation, Confirmed order, or Inside
quote.

- Quotation: the document is sent to (and accessible by) customers at any time.
- Confirmed order: the document is sent to customers upon the confirmation of an order.
  This is best for user manuals and other supplemental documents.
- Inside quote: the document is included in the PDF of the quotation, between the header
  pages and the Pricing section of the quote.

Lastly, in the E-Commerce section, decide whether or not to Show on product
page on the front-end (in the online store).

## Báo giá PDF

Once a quote with a pre-configured PDF has been confirmed, Odoo provides the option to print the
confirmed quote to check for errors, or to keep for records.

To print the PDF quote, navigate to the confirmed quote, and click the ⚙️ (gear) icon to
reveal a drop-down menu. From this drop-down menu, select Print, then select
PDF Quote.

![Print pdf quote option on drop-down menu located on confirmed sales order in Odoo Sales.](applications/sales/sales/send_quotations/pdf_quote_builder/drop-down-print-pdf.png)

Doing so instantly downloads the PDF quote. When opened, the PDF quote, along with the configured
product PDF that was set to be visible inside the quote, can be viewed and printed.

#### NOTE
Download these [`PDF quote builder examples`](pdf_quote_builder/pdfquotebuilderexamples.zip) for added reference.

#### SEE ALSO
- [Mẫu báo giá](quote_template.md)
