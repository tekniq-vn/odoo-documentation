# Tài liệu

**Odoo Documents** allows you to store, view, and manage files within Odoo.

You can upload any file (max 64MB per file on Odoo Online) and organize them in various workspaces.

#### SEE ALSO
- [Odoo Documents: product page](https://www.odoo.com/app/documents)
- [Odoo Tutorials: Documents basics [video]](https://www.odoo.com/slides/slide/documents-basics-6841?fullscreen=1)
- [Odoo Tutorials: Using Documents with your Accounting App [video]](https://www.odoo.com/slides/slide/accounting-integration-and-workflow-actions-6853?fullscreen=1)

## Cấu hình

Bằng cách vào Tài liệu ‣ Cấu hình ‣ Cài đặt, bạn có thể kích hoạt tính năng tập trung hóa các tệp đính kèm vào một khu vực cụ thể trong hoạt động của mình. Ví dụ: bằng cách đánh dấu vào Nhân sự, các tài liệu nhân sự của bạn sẽ tự động khả dụng trong không gian làm việc Nhân sự, trong khi các tài liệu liên quan đến Bảng lương tự động khả dụng trong không gian làm việc phụ Bảng lương. Bạn có thể thay đổi không gian làm việc mặc định bằng menu thả xuống và chỉnh sửa thuộc tính của nó bằng cách nhấp vào biểu tượng <i class="fa fa-arrow-right"></i> (Liên kết nội bộ).

![Enable the centralization of files attached to a specific area of your activity.](applications/productivity/documents/files-centralization.png)

#### NOTE
- If you enable the centralization of your accounting files and documents, it is necessary to
  click on Journals and define each journal independently to allow automatic
  synchronization.
  ![Enable the centralization of files attached to your accounting.](applications/productivity/documents/accounting-files-centralization.png)
- If you select a new workspace, existing documents are not moved. Only newly created documents
  will be found under the new workspace.

<a id="documents-workspaces"></a>

## Workspaces

Workspaces are hierarchical folders having their own set of [tags](#documents-tags)
and [actions](#documents-workflow-actions). Default workspaces exist, but you can create your
own by going to Documents ‣ Configuration ‣ Workspaces and clicking
New. On the new page, fill in the following information:

- Tên
- Parent Workspace: if you want to create a sub-workspace, select its Parent
  Workspace.

Three tabs are available: [Tags](#documents-tags),
[Access Rights](#documents-access-rights), and [Description](#documents-description).

<a id="documents-tags"></a>

### Thẻ

Tags are used within workspaces to add a level of differentiation between documents. They are
organized per category, and filters can be used to sort them.

From the Tags tab, click Add a line, create the Tag Category,
and Name your tags.

#### NOTE
- The tags of a parent workspace apply to the child workspaces automatically;
- Tags can be created and modified by going to Documents ‣ Configuration ‣
  Tags;
- Tags can also be created or edited by clicking the <i class="fa fa-gear"></i> (gear) icon on
  the left panel;
- An [email alias](#documents-upload) can be used to automatically send received documents
  to a specific workspace based on the tag assigned.

<a id="documents-access-rights"></a>

### Quyền truy cập

To manage your workspace access rights, go to the Access Rights tab. You can add
Write Groups that can view, create, and edit the workspace's documents. You can also add
Read Groups that only view the workspace's documents.

<a id="documents-description"></a>

### Mô tả

You can add descriptive information to your workspace by going to the Description tab.

#### NOTE
Workspaces can also be created and edited by clicking the <i class="fa fa-gear"></i> (gear) icon
on the left panel.

<a id="documents-management"></a>

## Quản lý tài liệu

When selecting or opening a document, the right panel displays different options, including, for
example:

- <i class="fa fa-download"></i> (Tải xuống);
- <i class="fa fa-share-alt"></i> (Share this selection): a share URL is copied to your clipboard;
- <i class="fa fa-retweet"></i> (Replace): select a new file to replace the existing one. Scroll
  down to the bottom of the right panel to see the History and restore,
  download, or delete the document;
- <i class="fa fa-unlock"></i> (Khoá);
- <i class="fa fa-scissors"></i> ([Split](#documents-split)).

You can also <i class="fa fa-comments"></i> Open chatter or delete the document by clicking the
<i class="fa fa-trash"></i> (Move to trash) icon.

#### NOTE
Items moved to the trash are permanently deleted after 30 days.

To modify the name of your file, click on Name. A Contact or an
Owner can be assigned. The related Workspace can be modified and it is
possible to access the related Journal Entry or add Tags.

#### NOTE
- The Contact is a person related to the document who only has read
  [access rights](#documents-access-rights) to the document, e.g., an existing supplier in
  your database;
- The creator of a document is automatically assigned as its Owner and is granted
  full access rights to it. To replace the owner of a document, select the required user from the
  dropdown list in the Owner field.

Different [Actions](#documents-workflow-actions) are available at the bottom of the right
panel, depending on the workspace where your document is stored.

<a id="documents-split"></a>

### Split PDF documents

Select the PDF you want to split, and click the <i class="fa fa-scissors"></i> (scissors) icon. A
new view displays all the pages of the document.

By default, all pages are split when you click Split. To remove a split between two
pages, click the <i class="fa fa-scissors"></i> (scissors) icon.

![split your documents](applications/productivity/documents/split-pdf.png)

### Tính năng bổ sung

Select a workspace and click the <i class="fa fa-caret-down"></i> (down arrow) next to the
Upload button to access additional features:

#### Yêu cầu

You can request files and organize them as documents to remind users to download them.

Select the workspace where the file should be stored, click the <i class="fa fa-caret-down"></i>
(down arrow) next to the Upload button, then Request. Add the
Document Name and select the person you need it from in the Request To
field. You can also fill in the Due Date In, confirm the Workspace the
document should belong to, and add Tags and a Message. Then, click
Request. A placeholder for the missing document is created in the workspace.

When your document is available, click the placeholder to upload it.

You can see all missing documents by going to the **Activity** view and the Requested
Document column.

<a id="documents-add-a-link"></a>

#### Thêm một liên kết

To add a link to your documents dashboard, click Add a Link, enter the URL,
and Name it.

#### Chia sẻ

You can make a document or a workspace accessible to anyone by sharing a URL.

##### Share a document

To generate a **share link** to a document, select the document, click the <i class="fa fa-caret-down"></i>
(down arrow) next to the Upload button, and click Share.

In the pop-up, you can Name the share link, set a validity date by filling in the
Valid Until field, and if you own more than one site, select the Website you
want so the right domain name is reflected in the URL.

Click Copy or Share to send the URL to whomever you want.

##### Share a workspace

You can share a link to a workspace and allow users to Download its content or
Download and Upload files to it.

To do so, go to the left column of your dashboard. In the Workspace section, select the
workspace to share, and possibly one or several tags that will be automatically added to the
uploaded documents. Then, click the <i class="fa fa-caret-down"></i> (down arrow) next to the
Upload button and Share.

In the pop-up, a share URL you can Copy is displayed. You can
Name your share link, set a validity date by filling in the Valid Until
field, tick the Include Sub Folders box if you want to share the workspace's
sub-folders, and if you own more than one site, select the Website you
want so the share link reflects the right domain name.

Then, allow users to either Download files from your workspace, or to [Download and
Upload](#documents-upload) files to it.

#### NOTE
- The links added to your workspace using the [Add a Link](#documents-add-a-link) option
  cannot be shared and are, therefore, excluded;
- When tags are applied to a shared workspace, users can exclusively access the documents
  associated with those tags.

<a id="documents-upload"></a>

###### Tải lên bằng email

Select the Download and Upload option to enable users to upload their files to your
workspace using an Email Alias. To create the email alias, enter its name in the
Email Alias field. The [domain name](../general/email_communication.md) should be set
by default, but you can modify it by clicking it.

The documents sent to this email alias are uploaded to the workspace using the chosen
[tags](#documents-tags).

#### NOTE
- By default, the Document Owner is the person who uploads a file to a workspace, but
  you can select another user. You can also set a Contact, usually an external
  person, such as a partner.
- Enable Create a new activity to automatically create an activity when a document is
  uploaded. Select the Activity type from the dropdown list and set the
  Due Date In field. You can also add a Summary and a
  Responsible person assigned to the activity.

#### Bảng tính mới

To create a new [spreadsheet](spreadsheet.md), click New Spreadsheet. You can select
a Blank spreadsheet or an [existing template](spreadsheet/templates.md).

<a id="documents-workflow-actions"></a>

## Workflow actions

Workflow actions help manage documents and overall business operations. These are automated actions
that can be created and customized for each workspace. With a single click you can, for example,
create, move, sign, add tags to a document, and process bills.

When a document meets the set criteria, these workflow actions appear on the right panel.

### Create workflow actions

To update an existing workflow action or create a new one, go to Documents ‣
Configuration ‣ Actions and click New.

#### NOTE
An action applies to all **sub-workspaces** under the Related Workspace you selected.

### Set the conditions

Define the Action Name and then set the conditions that trigger the appearance of the
<i class="fa fa-play"></i> (play) icon on the right-side panel when selecting a file.

There are three basic types of conditions you can set:

1. Tags: you can use the Contains and Does not contain
   conditions, meaning the files *must have* or *must not have* the tags set here;
2. Contact: the files must be associated with the contact set here;
3. Owner: the files must be associated with the owner set here.

![Example of a workflow action's basic condition in Odoo Documents](applications/productivity/documents/basic-condition-example.png)

#### Advanced condition type: domain

#### IMPORTANT
It is recommended to have some knowledge of Odoo development to configure *Domain* filters
properly.

The [developer mode](../general/developer_mode.md#developer-mode) needs to be activated to access the Domain
condition from the Actions tab. Once done, select the Domain condition type
and click New Rule.

To create a rule, you typically select a field, an operator, and a
value. For example, if you want to add a workflow action to all the PDF files inside a
workspace, set the field to *Mime Type*, the operator to *contains*, and the
pdf value.

![Example of a workflow action's domain condition in Odoo Documents](applications/productivity/documents/domain-condition-example.png)

Click the <i class="fa fa-plus"></i> (Add New Rule) icon and the <i class="fa fa-sitemap"></i>
(Add branch) icon to add conditions and sub-conditions. You can then specify if your
rule should match all or any conditions. You can also edit the rule directly
using the Code editor.

### Configure the actions

Select the Actions tab to set up your action. You can simultaneously:

- **Move to Workspace**: move the file to any workspace;
- **Create**: create one of the following items attached to the file in your database:
  - **Link to record**: create a link between a document and a record from a specific model;
  - **Product template**: create a product you can edit directly;
  - **Task**: create a Project task you can edit directly;
  - **Signature PDF template**: create a new Sign template to send out;
  - **PDF to sign**: create a Sign template to sign directly;
  - **Applicant**: create a new HR application you can edit directly;
  - **Vendor bill**: create a vendor bill using OCR and AI to scrape information from the file
    content;
  - **Customer invoice**: create an invoice using OCR and AI to scrape information from the file;
  - **Vendor credit note**: create a vendor credit note using OCR and AI to scrape information
    from the file;
  - **Credit note**: create a customer credit note using OCR and AI to scrape information from the
    file;
  - **Miscellaneous Operations**: create an entry in the Miscellaneous Operations journal;
  - **Bank Statement**: import a bank statement;
  - **Purchase Receipt**: create a vendor receipt;
  - **Expense**: create an HR expense.
- **Set Contact**: add a contact to the file, or replace an existing contact with a new one;
- **Set Owner**: add an owner to the file, or replace an existing owner with a new one;
- **Set Tags**: add, remove, and replace any number of tags;
- **Activities - Mark all as Done**: mark all activities linked to the file as done;
- **Activities - Schedule Activity**: create a new activity linked to the file as configured in
  the action. You can choose to set the activity on the document owner.

![Example of a workflow action Odoo Documents](applications/productivity/documents/workflow-action-example.png)

## Digitize documents with AI and optical character recognition (OCR)

Documents available in the Finance workspace can be digitized. Select the document to digitize,
click Create Bill, Create Customer Invoice, or
Create credit note, and then click Send for Digitization.

#### SEE ALSO
[AI-powered document digitization](../finance/accounting/vendor_bills/invoice_digitization.md)
