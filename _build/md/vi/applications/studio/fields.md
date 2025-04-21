# Fields and widgets

Trường cấu trúc các mô hình của cơ sở dữ liệu. Nếu hình dung một mô hình như một bảng hoặc bảng tính, thì các trường chính là những cột nơi dữ liệu được lưu trữ trong các bản ghi (tức là hàng). Trường cũng xác định loại dữ liệu được lưu trữ trong đó. Cách dữ liệu được trình bày và định dạng trên  được xác định bởi tiện ích của chúng.

From a technical point of view, there are 15 field types in Odoo. However, you can choose from 20
fields in Studio, as some field types are available more than once with a different default widget.

<a id="studio-fields-simple-fields"></a>

## Trường đơn giản

Simple fields contain basic values, such as text, numbers, files, etc.

#### NOTE
Non-default widgets, when available, are presented as bullet points or sub-headings below.

<a id="studio-fields-simple-fields-text"></a>

### Text (`char`)

The Text field is used for short text containing any character. One text line is
displayed when filling out the field.

- Badge: displays the value inside a rounded shape, similar to a tag. The value cannot
  be edited on the UI, but a default value can be set.
- Copy to Clipboard: users can copy the value by clicking a button.
- E-mail: the value becomes a clickable *mailto* link.
- Image: displays an image using a URL. The value cannot be edited manually, but a
  default value can be set.

  #### NOTE
  This works differently than selecting the [Image field](#studio-fields-simple-fields-image) directly, as the image is not stored in Odoo when using a
  Text field with the Image widget. For example, it can be useful if you
  want to save disk space.
- Phone: the value becomes a clickable *tel* link.
- URL: the value becomes a clickable URL.

<a id="studio-fields-simple-fields-multiline-text"></a>

### Multiline Text (`text`)

The Multiline Text field is used for longer text containing any type of character. Two
text lines are displayed on the UI when filling out the field.

- Copy to Clipboard: users can copy the value by clicking a button.

<a id="studio-fields-simple-fields-integer"></a>

### Integer (`integer`)

The Integer field is used for all integer numbers ().

- Percentage Pie: displays the value inside a percentage circle, usually for a computed
  value. The value cannot be edited on the UI, but a default value can be set.
- Progress Bar: displays the value next to a percentage bar, usually for a computed
  value. The field cannot be edited manually, but a default value can be set.
- Handle: displays a drag handle icon to order records manually in [List view](views.md#studio-views-multiple-records-list).

<a id="studio-fields-simple-fields-decimal"></a>

### Decimal (`float`)

The Decimal field is used for all decimal numbers ().

#### NOTE
Decimal numbers are displayed with two decimals after the decimal point on the UI, but they are
stored in the database with more precision.

- Monetary: it is similar to using the [Monetary field](#studio-fields-simple-fields-monetary). It is recommended to use the latter as it offers more
  functionalities.
- Percentage: displays a percent character `%` after the value.
- Percentage Pie: displays the value inside a percentage circle, usually for a computed
  value. The field cannot be edited manually, but a default value can be set.
- Progress Bar: displays the value next to a percentage bar, usually for a computed
  value. The field cannot be edited manually, but a default value can be set.
- Time: the value must follow the *hh:mm* format, with a maximum of 59 minutes.

<a id="studio-fields-simple-fields-monetary"></a>

### Monetary (`monetary`)

The Monetary field is used for all monetary values.

#### NOTE
When you first add a Monetary field, you are prompted to add a Currency
field if none exists already on the model. Odoo offers to add the Currency field for
you. Once it is added, add the Monetary field again.

<a id="studio-fields-simple-fields-html"></a>

### Html (`html`)

The Html field is used to add text that can be edited using the Odoo HTML editor.

- Multiline Text: disables the Odoo HTML editor to allow editing raw HTML.

<a id="studio-fields-simple-fields-date"></a>

### Date (`date`)

The Date field is used to select a date on a calendar.

- Remaining Days: the remaining number of days before the selected date is displayed
  (e.g., *In 5 days*), based on the current date. This field should be set to Read only.

<a id="studio-fields-simple-fields-date-time"></a>

### Date & Time (`datetime`)

The Date & Time field is used to select a date on a calendar and a time on a clock. The
user's current time is automatically used if no time is set.

#### Date Range (`daterange`)

The Date Range widget is used to display a period of time defined by a start date and an
end date in a single line. A date range can have a mandatory start and end date, e.g., for a
multi-day event, or allow an optional start or end date, e.g., for a field service intervention or a
project task.

Adding a date range requires two fields: a Date & Time field with the
Date Range widget set and another field that is selected as the start date *or* end
date. This underlying field can be an existing [Date](#studio-fields-simple-fields-date)
or Date & Time field, or one created specifically for this purpose.

To add a date range:

1. Identify an existing Date or Date & Time field that can be used as the
   underlying start/end date field, or add a new one. If the date range:
   - has a mandatory start date and end date, this field can be either the start date or end date;
     the outcome is the same.
   - allows an optional start or end date, this field is the start date or end date, respectively.
2. Add a Date & Time field and set the Widget field to
   Date Range.
3. Enter an appropriate Label.
4. Select the underlying start/end date field from the Start date field or
   End date field dropdown, as relevant.
5. If the date range should have a mandatory start and end date, enable Always range.
6. Update any other [general properties](#studio-fields-properties) or specific
   [properties for Date & Time fields](#studio-fields-properties-date-datetime) as needed, then
   click Close in the upper right corner of the screen.

#### Remaining Days (`remaining_days`)

The Remaining Days widget displays the remaining number of days before the selected date
(e.g., *In 5 days*), based on the current date and time. This field should be set to Read
only.

<a id="studio-fields-simple-fields-checkbox"></a>

### Hộp kiểm (`boolean`)

The Checkbox field is used when a value should only be true or false, indicated by
checking or unchecking a checkbox.

- Button: displays a radio button. The widget works without switching to the edit mode.
- Toggle: displays a toggle button. The widget works without switching to the edit mode.

<a id="studio-fields-simple-fields-selection"></a>

### Selection (`selection`)

The Selection field is used when users should select a single value from a group of
predefined values.

- Badge: displays the value inside a rounded shape, similar to a tag. The value cannot
  be edited on the UI, but a default value can be set.
- Badges: displays all selectable values simultaneously inside rectangular shapes,
  organized horizontally.
- Priority: displays star symbols instead of values, which can be used to indicate an
  importance or satisfaction level, for example. This has the same effect as selecting the
  [Priority field](#studio-fields-simple-fields-priority), although, for the latter, four
  priority values are already predefined.
- Radio: displays all selectable values at the same time as radio buttons.
- Status Bar: displays all selectable values at the same time as an arrow progress bar.

<a id="studio-fields-simple-fields-priority"></a>

### Priority (`selection`)

The Priority field is used to display a three-star rating system, which can be used to
indicate importance or satisfaction level. This field type is a [Selection field](#studio-fields-simple-fields-selection) with the Priority widget selected by default
and four priority values predefined. Consequently, the Badge, Badges,
Radio, and Selection widgets have the same effects as described under
[Selection](#studio-fields-simple-fields-selection).

<a id="studio-fields-simple-fields-file"></a>

### File (`binary`)

The File field is used to upload any type of file, or sign a form (Sign
widget).

- Image: users can upload an image file, which is then displayed in [Form view](views.md#studio-views-general-form). This has the same effect as using the [Image field](#studio-fields-simple-fields-image).
- PDF Viewer: users can upload a PDF file, which can be then browsed from the
  [Form view](views.md#studio-views-general-form).
- Sign: users can electronically sign the form. This has the same effect as selecting
  the [Sign field](#studio-fields-simple-fields-sign).

<a id="studio-fields-simple-fields-image"></a>

### Image (`binary`)

The Image field is used to upload an image and display it in [Form view](views.md#studio-views-general-form). This field type is a [File field](#studio-fields-simple-fields-file) with the Image widget selected by default.
Consequently, the File, PDF Viewer, and Sign widgets have the
same effects as described under [File](#studio-fields-simple-fields-file).

<a id="studio-fields-simple-fields-sign"></a>

### Sign (`binary`)

The Sign field is used to sign the form electronically. This field type is a [File
field](#studio-fields-simple-fields-file) with the Sign widget selected by default.
Consequently, the File, Image, and PDF Viewer widgets have the
same effects as described under [File](#studio-fields-simple-fields-file).

<a id="studio-fields-relational-fields"></a>

## Relational fields

Relational fields are used to link and display the data from records on another model.

#### NOTE
Non-default widgets, when available, are presented as bullet points below.

<a id="studio-fields-relational-fields-many2one"></a>

### Many2One (`many2one`)

The Many2One field is used to link another record (from another model) to the record
being edited. The record's name from the other model is then displayed on the record being edited.

- Badge: displays the value inside a rounded shape, similar to a tag. The value cannot
  be edited on the UI.
- Radio: displays all selectable values at the same time as radio buttons.

<a id="studio-fields-relational-fields-one2many"></a>

### One2Many (`one2many`)

The One2Many field is used to display the existing relations between a record on the
current model and multiple records from another model.

#### NOTE
To use a One2Many field, the two models must have been linked already using a
[Many2One field](#studio-fields-relational-fields-many2one). One2Many relations do not exist
independently: a reverse-search of existing Many2One relations is performed.

<a id="studio-fields-relational-fields-lines"></a>

### Lines (`one2many`)

The Lines field is used to create a table with rows and columns (e.g., the lines of
products on a sales order).

<a id="studio-fields-relational-fields-many2many"></a>

### Many2Many (`many2many`)

The Many2Many field is used to link multiple records from another model to multiple
records on the current model. Many2Many fields can use Disable creation,
Disable opening, Domain, just like [Many2One fields](#studio-fields-relational-fields-many2one).

- Checkboxes: users can select several values using checkboxes.
- Tags: users can select several values appearing in rounded shapes, also known as
  *tags*. This has the same effect as selecting the [Tags field](#studio-fields-relational-fields-tags).

<a id="studio-fields-relational-fields-tags"></a>

### Thẻ (`many2many`)

The Tags field is used to display several values from another model appearing in rounded
shapes, also known as *tags*. This field type is a [Many2Many field](#studio-fields-relational-fields-many2many) with the Tags widget selected by default.
Consequently, the Checkboxes and Many2Many widgets have the same effects as
described under [Many2Many](#studio-fields-relational-fields-many2many).

<a id="studio-fields-relational-fields-related-field"></a>

### Related Field (`related`)

A Related Field is not a relational field per se; no relationship is created between
models. It uses an existing relationship to fetch and display information from another record.

<a id="studio-fields-properties"></a>

## Thuộc tính

### General properties

- Invisible: Enable this property when it is not necessary for users to view a field on
  the UI. This helps declutter the UI by only showing the essential fields depending on a specific
  situation.

  The Invisible attribute also applies inside Studio. To view hidden fields in Studio,
  click on a view's View tab and enable Show Invisible Elements.
- Required: Enable this property if a field should always be completed by the user
  before being able to proceed.
- Readonly: Enable this property if users should not be able to modify a field.

#### NOTE
> You can choose to enable Invisible, Required and Readonly
> for specific records only by clicking on Conditional and creating a filter.

- Label: the field's name on the UI. This is not the name used in the PostgreSQL
  database. To view and change the latter, activate the [developer mode](../general/developer_mode.md#developer-mode) and
  edit the Technical Name.
- Help Tooltip: To explain the purpose of a field, add a description. The text is
  displayed inside a tooltip box when hovering with your mouse over the question mark beside the
  field's label.
- Widget: To change the default appearance or functionality of a field, select one of
  the available widgets.
- Placeholder: To provide an example of how a field should be completed, add placeholder
  text. The text appears in light gray until a value is entered.
- Default value: To display a default value in a field when a record is created, add a
  value.
- Allow visibility to groups: To limit which users can view the field, select one or
  more user access [groups](../general/users/access_rights.md#access-rights-groups).
- Forbid visibility to groups: To prevent certain users from seeing the field, select
  one or more user access [groups](../general/users/access_rights.md#access-rights-groups).

<a id="studio-fields-properties-date-datetime"></a>

### Properties for Date & Time fields

For Date & Time fields that have the Date & Time or Date Range
widget set, some specific properties are available:

- Time interval: Enter a value to determine the minute intervals shown in the time
  selector. For example, enter 15 to allow quarter-hour intervals. The default value is set to 5
  minutes.
- Warning for future dates: Enable this property to display a warning icon if a future
  date is selected.
- Show time: This property is enabled by default for Date & Time fields. On
  a read-only field, disable the property to show only the date. This can keep a list view less
  cluttered, for example.
- Earliest accepted date: Enter the earliest date that can be selected in the date
  selector in ISO-format, i.e., `YYYY-MM-DD`. If the current date is always the earliest accepted
  date, enter `today`. On the date selector, dates prior to the earliest accepted date are grayed
  out.
- Latest accepted date: Enter the latest date that can be selected in the date
  selector in ISO-format, i.e., `YYYY-MM-DD`. If the current date is always the latest accepted
  date, enter `today`. On the date selector, dates later than the latest accepted date are grayed
  out.
