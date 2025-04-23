# Models, modules, and apps

Models determine the logical structure of a database and how data is stored, organized, and\
manipulated. In other words, a model is a table of information that can be linked with other tables.\
A model usually represents a business concept, such as a _sales order_, _contact_, or _product_.

Modules and apps contain various elements, such as models, views, data files, web controllers, and\
static web data.

#### NOTE

All apps are modules. Larger, standalone modules are typically referred to as apps, whereas other\
modules usually serve as add-ons to said apps.

## Suggested features

Khi bạn tạo một mô hình hoặc ứng dụng mới bằng Studio, bạn có thể chọn thêm tối đa 14 tính năng để tăng tốc quá trình tạo. Các tính năng này kết hợp các trường, thiết lập mặc định và chế độ xem thường được sử dụng cùng nhau để cung cấp một số chức năng chuẩn. Hầu hết các tính năng này có thể được thêm vào sau, nhưng việc thêm chúng ngay từ đầu giúp quá trình tạo mô hình dễ dàng hơn nhiều. Hơn nữa, các tính năng này tương tác với nhau trong một số trường hợp để tăng tính hữu ích của chúng.

### Chi tiết liên hệ

Selecting Contact details adds to the [Form view](views.md#studio-views-general-form) a
[Many2One field](fields.md#studio-fields-relational-fields-many2one) linked to the *Contact* model and
two of its [Related Fields](fields.md#studio-fields-relational-fields-related-field): Phone
and Email. The Contact field is also added to the [List view](views.md#studio-views-multiple-records-list), and the [Map view](views.md#studio-views-multiple-records-map)
is activated.

### Phân công người dùng

Selecting User assignment adds to the [Form view](views.md#studio-views-general-form) a
[Many2One field](fields.md#studio-fields-relational-fields-many2one) linked to the *Contact* model, with
the following Domain: `Share User is not set` to only allow the selection of *Internal
Users*. In addition, the many2one_avatar_user widget is used to display the user's
avatar. The Responsible field is also added to the [List view](views.md#studio-views-multiple-records-list).

### Ngày & lịch

Selecting Date & Calendar adds to the [Form view](views.md#studio-views-general-form) a
[Date field](fields.md#studio-fields-simple-fields-date) and activates the [Calendar view](views.md#studio-views-timeline-calendar).

<a id="studio-models-modules-apps-suggested-features-date-range-gantt"></a>

### Phạm vi ngày & gantt

Selecting Date range & Gantt adds to the [Form view](views.md#studio-views-general-form)
two [Date fields](fields.md#studio-fields-simple-fields-date) next to each other: one to set a start
date, the other to set an end date, using the daterange widget, and activates the
[Gantt view](views.md#studio-views-timeline-gantt).

<a id="studio-models-modules-apps-suggested-features-pipeline-stages"></a>

### Giai đoạn chu trình

Selecting Pipeline stages activates the [Kanban view](views.md#studio-views-multiple-records-kanban), adds several fields such as [Priority](fields.md#studio-fields-simple-fields-priority) and Kanban State, and three stages:
New, In Progress, and Done. The Pipeline status bar
and the Kanban State field are added to the [Form view](views.md#studio-views-general-form). The Color field is added to the [List view](views.md#studio-views-multiple-records-list).

#### NOTE

The Pipeline stages feature can be added at a later stage.

### Thẻ

Selecting Tags adds to the [Biểu mẫu](views.md#studio-views-general-form) and
[Danh sách](views.md#studio-views-multiple-records-list) views a [Tags field](fields.md#studio-fields-relational-fields-tags), creating a *Tag* model with preconfigured access rights in
the process.

### Hình ảnh

Selecting Picture adds to the top-right of the [Form view](views.md#studio-views-general-form) an [Image field](fields.md#studio-fields-simple-fields-image).

#### NOTE

The Picture feature can be added at a later stage.

### Dòng

Selecting Lines: adds to the [Form view](views.md#studio-views-general-form) a [Lines
field](fields.md#studio-fields-relational-fields-lines) inside a Tab component.

### Ghi chú

Selecting Notes adds to the [Form view](views.md#studio-views-general-form) an [Html
field](fields.md#studio-fields-simple-fields-html) using the full width of the form.

### Giá trị tiền tệ

Selecting Monetary value adds to the [Biểu mẫu](views.md#studio-views-general-form) and
[Danh sách](views.md#studio-views-multiple-records-list) views a [Monetary field](fields.md#studio-fields-simple-fields-monetary). The [Biểu đồ](views.md#studio-views-reporting-graph) and
[Pivot](views.md#studio-views-reporting-pivot) views are also activated.

#### NOTE

A _Currency_ field is added and hidden from the view.

### Công ty

Selecting Company adds to the [Biểu mẫu](views.md#studio-views-general-form) and
[Danh sách](views.md#studio-views-multiple-records-list) views a [Many2One field](fields.md#studio-fields-relational-fields-many2one) linked to the *Company* model.

#### NOTE

This is only useful if you work in a multi-company environment.

### Sắp xếp tùy chỉnh

Selecting Custom Sorting adds to the [List view](views.md#studio-views-multiple-records-list) a drag handle icon to manually reorder records.

### Chatter

Selecting Chatter adds to the [Form view](views.md#studio-views-general-form) Chatter
functionalities (sending messages, logging notes, and scheduling activities).

#### NOTE

The Chatter feature can be added at a later stage.

### Đang lưu trữ

Selecting Archiving adds to the [Biểu mẫu](views.md#studio-views-general-form) and
[Danh sách](views.md#studio-views-multiple-records-list) views the Archive action and hides archived
records from searches and views by default.

## Export and import customizations

When you do any customization with Studio, a new module named Studio customizations is\
added to your database.

To export these customizations, go to Main dashboard ‣ Studio ‣ Customizations\
‣ Export to download a ZIP file containing all customizations.

To import and install these customizations in another database, connect to the destination database\
and go to Main dashboard ‣ Studio ‣ Customizations ‣ Import, then upload\
the exported ZIP file before clicking on the Import button.

#### WARNING

Before importing, make sure the destination database contains the same apps and modules as the\
source database. Studio does not add the underlying modules as dependencies of the exported\
module.
