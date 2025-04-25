# Ký tên

**Odoo Sign** allows you to send, sign, and approve documents online, using electronic signatures.

An **electronic signature** shows a person's agreement to the content of a document. Just like a
handwritten signature, the electronic one represents a legal bounding by the terms of the signed
document.

With Sign, you can upload any PDF file and add fields to it. These fields can be automatically
filled in with the user's details present in your database.

#### SEE ALSO
- [Odoo Sign: product page](https://www.odoo.com/app/sign)
- [Odoo Tutorials: Sign [video]](https://www.odoo.com/slides/sign-61)

## Validity of electronic signatures

Các tài liệu được ký qua ứng dụng Ký tên là chữ ký điện tử hợp lệ tại Liên minh Châu Âu và Hoa Kỳ. Chúng cũng đáp ứng các yêu cầu về chữ ký điện tử tại hầu hết các quốc gia. Tính hợp pháp của chữ ký điện tử được tạo bởi Odoo phụ thuộc vào pháp luật của quốc gia bạn. Các công ty kinh doanh quốc tế cũng nên xem xét luật chữ ký điện tử của những quốc gia khác.

#### IMPORTANT
The below information has no legal value; it is only provided for general informational purposes.
As laws governing electronic signatures rapidly evolve, we cannot guarantee that all information
is up-to-date. We advise contacting a local attorney for legal advice regarding electronic
signature compliance and validity.

### Liên minh Châu Âu

The [eIDAS regulation](http://data.europa.eu/eli/reg/2014/910/oj) establishes the framework for
electronic signatures in the [27 member states of the European Union](https://europa.eu/european-union/about-eu/countries_en). It distinguishes three types of
electronic signatures:

1. Simple electronic signatures
2. Advanced electronic signatures
3. Qualified electronic signatures

Odoo generates the first type, **simple electronic signatures**; these signatures are legally valid
in the EU, as stated in the eIDAS regulation.

Electronic signatures may not be automatically recognized as valid. You may need to bring
supporting evidence of a signature's validity. While the Sign app provides a simple electronic
signature, some supporting evidence is automatically collected during the signature process, such
as:

1. Email and SMS validation (if enabled)
2. Strong identity proof through itsme® (available in Belgium and the Netherlands)
3. Timestamped, IP and geographically traceable access logs to the documents and their associated
   signatures
4. Document traceability and inalterability (any alteration made to a signed document is detected by
   Odoo with the use of cryptographic proofs)

#### NOTE
[Documentation for Germany](sign/germany.md)

### Hoa Kỳ

The [ESIGN Act (Electronic Signatures in Global and National Commerce Act)](https://www.fdic.gov/regulations/compliance/manual/10/X-3.1.pdf), at the interstate and
international levels, and the [UETA (Uniform Electronic Transactions Act)](https://www.uniformlaws.org/committees/community-home/librarydocuments?communitykey=2c04b76c-2b7d-4399-977e-d5876ba7e034&tab=librarydocuments),
at the state level, provide the legal framework for electronic signatures. Note that [Illinois](https://www.ilga.gov/legislation/ilcs/ilcs5.asp?ActID=89&) and [New York](https://its.ny.gov/electronic-signatures-and-records-act-esra) have not adopted the UETA, but
similar acts instead.

Overall, to be recognized as valid, electronic signatures have to meet five criteria:

1. The signer must show a clear **intent to sign**. For example, using a mouse to draw a signature
   can show intent. The signer must also have the option to opt out of the electronic document.
2. The signer must first express or imply their **consent to conduct business electronically**.
3. **The signature must be clearly attributed**. In Odoo, metadata, such as the signer's IP address,
   is added to the signature, which can be used as supporting evidence.
4. **The signature must be associated with the signed document**, for example, by keeping a record
   detailing how the signature was captured.
5. Electronically signed documents need to be **retained and stored** by all parties involved; for
   example, by providing the signer either a fully-executed copy or the possibility to download a
   copy.

### Quốc gia khác

- [Algeria](sign/algeria.md)
- [Angola](sign/angola.md)
- [Argentina](sign/argentina.md)
- [Úc](sign/australia.md)
- [Azerbaijan](sign/azerbaijan.md)
- [Bangladesh](sign/bangladesh.md)
- [Brazil](sign/brazil.md)
- [Canada](sign/canada.md)
- [Chile](sign/chile.md)
- [Trung Quốc](sign/china.md)
- [Colombia](sign/colombia.md)
- [Cộng hoà Dominica](sign/dominican_republic.md)
- [Ecuador](sign/ecuador.md)
- [Egypt](sign/egypt.md)
- [Ethiopia](sign/ethiopia.md)
- [Guatemala](sign/guatemala.md)
- [Hồng Kông](sign/hong_kong.md)
- [Ấn Độ](sign/india.md)
- [Indonesia](sign/indonesia.md)
- [Iran](sign/iran.md)
- [Iraq](sign/iraq.md)
- [Israel](sign/israel.md)
- [Nhật Bản](sign/japan.md)
- [Kazakhstan](sign/kazakhstan.md)
- [Kenya](sign/kenya.md)
- [Kuwait](sign/kuwait.md)
- [Malaysia](sign/malaysia.md)
- [Mexico](sign/mexico.md)
- [Morocco](sign/morocco.md)
- [New Zealand](sign/new_zealand.md)
- [Nigeria](sign/nigeria.md)
- [Norway](sign/norway.md)
- [Oman](sign/oman.md)
- [Pakistan](sign/pakistan.md)
- [Peru](sign/peru.md)
- [Philippines](sign/philippines.md)
- [Qatar](sign/qatar.md)
- [Nga](sign/russia.md)
- [Ả Rập Xê Út](sign/saudi_arabia.md)
- [Singapore](sign/singapore.md)
- [Nam Phi](sign/south_africa.md)
- [Hàn Quốc](sign/south_korea.md)
- [Thuỵ Sĩ](sign/switzerland.md)
- [Thái Lan](sign/thailand.md)
- [Thổ Nhĩ Kỳ](sign/turkey.md)
- [Ukraine](sign/ukraine.md)
- [Các Tiểu Vương quốc Ả Rập Thống nhất](sign/united_arab_emirates.md)
- [Vương quốc Anh](sign/united_kingdom.md)
- [Uzbekistan](sign/uzbekistan.md)
- [Việt Nam](sign/vietnam.md)

## Send a document to sign

### Chữ ký một lần

You can click Upload a PDF to sign from your dashboard for a one-time signature. Select
your document, open it, and drag and drop the required [fields](#sign-fields) in your document.
You can modify the [role](#sign-role) assigned to a field by clicking on it and selecting the
one you want.

When ready, click Send, and fill in the required fields. Once sent, your document
remains available. Go to Documents ‣ All Documents to see your document
and the status of the signatures.

![Trạng thái chữ ký](../../_images/signature-status.png)

#### Validity dates and reminders

You can set **validity dates** on limited-duration agreement documents or send **automatic email
reminders** to obtain signatures on time. From your dashboard, click Send on your
document. On the new page, go to the Options section and fill in the Valid
Until and Reminder fields.

### Mẫu

You can create document templates when you have to send the same document several times. From your
dashboard, click Upload a PDF template. Select the document and add the required
[fields](#sign-fields). You can modify the [role](#sign-role) of a field by clicking on it
and selecting the one you want.

Click Template Properties to add Tags to your template, define a
Signed Document Workspace, add Signed Document Tags, set a
Redirect Link that will be available in the signature confirmation message received
after the signature, or define Authorized Users if you want to restrict the use of your
template to specific authorized users or groups.

Your templates are visible by default on your dashboard. You can click Send to quickly
send a document template to a signer or Sign Now if you are ready to sign your document
immediately.

<a id="sign-role"></a>

## Qui tắc

Each field in a Sign document is related to a role corresponding to a specific person. When a
document is being signed, the person assigned to the role must fill in their assigned fields and
sign it.

Roles are available by going to Sign ‣ Configuration ‣ Roles.

Có thể cập nhật các vai trò hiện có hoặc tạo các vai trò mới bằng cách nhấp vào Mới. Chọn Tên vai trò, thêm Bước xác thực bổ sung để xác nhận danh tính của người ký và nếu tài liệu có thể được chỉ định lại cho một liên hệ khác, hãy chọn Thay đổi được ủy quyền cho vai trò. Cũng có thể chọn Màu cho vai trò. Màu này có thể giúp hiểu vai trò nào chịu trách nhiệm cho trường nào khi cấu hình mẫu.

### Secured identification

As the owner of a document, you may request an Extra Authentication Step through
[SMS verification](#sign-sms) or via [Itsme®](#sign-itsme) (available in Belgium and the
Netherlands). Both authentication options require [credits](../essentials/in_app_purchase.md#iap-buying-credits). If you do not
have any credits left, the authentication steps will be skipped.

#### SEE ALSO
- [In-App Purchase (IAP)](../essentials/in_app_purchase.md)
- [SMS pricing and FAQ](../marketing/sms_marketing/pricing_and_faq.md)

<a id="sign-sms"></a>

#### Xác minh SMS

Go to Sign ‣ Configuration ‣ Roles. Click in the Extra
Authentication Step column for the role, and select Unique Code Via SMS.

#### NOTE
Before being able to send SMS Text Messages, you need to register your phone number. To do so, go
to Sign ‣ Configuration ‣ Settings and click Buy credits under
Authenticate by SMS.

Go to the document to sign, add the field for which the SMS verification is required, for example,
the Signature field, and click Send. On the new page, select the
customer and click Send.

The person signing the document fills in the Signature field, then Sign, and
clicks Validate & Send Completed Document. A Final Validation page pops up
where to add their phone number. One-time codes are sent by SMS.

![Add a hash to your document](../../_images/sms-verification.png)

#### NOTE
- This feature is enabled by default.
- As soon as the Extra Authentication Step applies to a role, this validation step is
  requested for any field assigned to this role.

<a id="sign-itsme"></a>

#### Itsme®

Itsme® authentication can be used to allow signatories to provide their identity using itsme®. This
feature is only available in **Belgium** and the **Netherlands**.

The feature can be enabled in Sign Settings and applies automatically to the
Customer (identified with itsme®) role. To enable it for other roles, go to
Sign ‣ Configuration ‣ Roles. Click in the Extra Authentication
Step column for the role, and select Via itsme®.

Go to the document that needs to be signed and add the Signature field. Switch to any
role configured to use the feature, and click Validate and Send.

![select customer identified with itsme®](../../_images/itsme-identification.png)

Upon signing the document, the signer completes the Signature field and proceeds by
clicking on Validate & Send Completed Document, triggering a
Final verification page where authentication via itsme® is required.

## Signatory hash

Each time someone signs a document, a **hash** - a unique digital signature of the operation - is
generated to ensure traceability, integrity, and inalterability. This process guarantees that any
changes made after a signature is affixed can be easily detected, maintaining the document's
authenticity and security throughout its lifecycle.

A visual security frame displaying the beginning of the hash is added to the signatures. Internal
users can hide or show it by turning the Frame option on or off when signing the
document.

![Adding the visual security frame to a signature.](../../_images/sign-hash.png)

<a id="sign-field-types"></a>

## Thẻ

Tags can be used to categorize and organize documents, allowing users to quickly search for and
filter documents based on specific criteria.

You can manage tags by going to Configuration ‣ Tags. To create a tag, click
New. On the new line, add the Tag Name and select a Color Index
for your tag.

To apply a tag to a document, use the dropdown list available in your document.

#### NOTE
You can modify the tags of a signed document by going to Documents ‣ All
Documents, clicking the vertical ellipsis (⋮) on your document, then
Details, and modifying your Tags.

## Thứ tự ký tên

When a document needs to be signed by different parties, the signing order lets you control the
order in which your recipients receive it for signature.

After uploading a PDF with at least two signature fields with two different roles and clicking
Send, toggle the Specify Signing Order switch and search for the signer's
name or email information to add them. You can decide on the signing order by typing **1** or **2**
in the first column.

![Toggle the switch to specify the signing order.](../../_images/specify-signing-order.png)

Each recipient receives the signature request notification only once the previous recipient has
completed their action.

<a id="sign-fields"></a>

## Field types

Fields are used in a document to indicate what information must be completed by the signers. You can
add fields to your document simply by dragging and dropping them for the left column into your
document.

Various field types can be used to sign documents (placeholder, autocompletion, etc.). By
configuring your own field types, also known as signature item types, the signing process can be
even faster for your customers, partners, and employees.

To create and edit field types, go to Sign ‣ Configuration ‣ Settings ‣
Edit field types.

You can select an existing field by clicking on it, or you can Create a new one. First,
edit the Field Name. Then, select a Field Type:

- Signature: users are asked to enter their signature either by drawing it, generating
  an automatic one based on their name, or uploading a local file (usually an image).
  Each subsequent Signature field type then reuses the data entered in the first field.
- Initial: users are asked to enter their initials, in a similar way to the
  Signature field.
- Text: users enter text on a single line.
- Multiline Text: users enter text on multiple lines.
- Checkbox: users can tick a box (e.g., to mark their approval or consent).
- Selection: users choose a single option from a variety of options.

The Auto-fill Partner Field setting is used to automatically fill in a field during the
signature process. It uses the value of one of the fields on the contact (`res.partner`) model of
the person signing the document. To do so, enter the contact model field's technical name.

#### NOTE
Auto-completed values are suggestions and can be modified as required by the person signing the
document.

Kích thước của các trường cũng có thể được thay đổi bằng cách chỉnh sửa Chiều rộng mặc định và Chiều cao mặc định. Cả hai kích thước đều được định nghĩa theo tỷ lệ phần trăm của toàn bộ trang biểu thị bằng số thập phân, trong đó 1 tương đương với chiều rộng hoặc chiều cao đầy đủ của trang. Theo mặc định, chiều rộng của các trường mới tạo được đặt ở mức 15% (0.150) chiều rộng trang đầy đủ, trong khi chiều cao được đặt ở mức 1.5% (0.015) chiều cao trang đầy đủ.

Next, write a Tip. Tips are displayed inside arrows on the left-hand side of the user's
screen during the signing process to help them understand what the step entails (e.g., "Sign here"
or “Fill in your birthdate”). You can also use a Placeholder text to be displayed inside
the field before it is completed.

![Tip and placeholder example in Odoo Sign](../../_images/tip-placeholder.png)
