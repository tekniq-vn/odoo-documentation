# View architectures

## Generic architecture

The architecture of a view is defined by XML data interpreted by the JavaScript framework.

For most views, there is a `*.rng` file defining the attributes and possible architectures.\
Some views are not ruled by such a file either because they accept HTML content, or for performance\
reasons.

#### NOTE

The current context and user access rights may impact the view abilities.

#### SEE ALSO
[View records](view_records.md)

[View records](developer/reference/user_interface/view_records.md)

## Python expression

When evaluating node attributes, e.g. the `readonly` modifier, it is possible to provide a **Python**\
**expression** that will be executed in an environment that has access to the following variables:

* The names of all fields present in the current view, containing the value of the current record,\
  except for `column_invisible` in [list view](./#reference-view-architectures-list-field);\
  relational fields are given as a list of IDs;
- The ID of the current record;
- `parent`: the record that refers to the container; only inside sub-views of [relational
  fields](../../../applications/studio/fields.md#studio-fields-relational-fields);
- `context (dict)`: the current view's context;
- `uid (int)`: the id of the current user;
- `today (str)`: the current local date in the `YYYY-MM-DD` format;
- `now (str)`: the current local datetime in the `YYYY-MM-DD hh:mm:ss` format.

<a id="reference-view-architectures-form"></a>

## Form

Form views are used to display the data from a single record. They are composed of regular [HTML](https://en.wikipedia.org/wiki/HTML)\
with additional semantic and structural components.

The root element of form views is `form`.

```xml
<form>
    ...
</form>
```

### Root attributes

Optional attributes can be added to the root element `form` to customize the view.

### string

The view title. It is displayed only if you open an action that has no name and whose target is`new` (opening a dialog).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### create

Disable/enable record creation on the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### edit

Disable/enable record edition on the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### duplicate

Disable/enable record duplication on the view through the **Action** dropdown.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### delete

Disable/enable record deletion on the view through the Action dropdown.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### js\_class

The name of the JavaScript component the webclient will instantiate instead of the form view.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### disable\_autofocus

Disable automatic focusing on the first field in the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

### banner\_route

The route to fetch HTML from and prepend it to the view.

If this attribute is set, the URL of the [controller route](../backend/http.md#reference-controllers) is
fetched and the returned content is displayed above the view. The JSON response from the
controller must contain an `html` key.

If the HTML contains a `<link>` tag for a stylesheet, it is removed from its original location\
and appended to the `<head>` section.

Use `<a type="action">` tags to interact with the backend, like with [action buttons](./#reference-view-architectures-form-button).

* **Requirement:**\
  Optional
* **Type:**[path](https://en.wikipedia.org/wiki/Path_\(computing\))
* **Default:**`''`

### Semantic components

Semantic components tie into the Odoo system and allow interaction with it.

Form views accept the following children semantic components: [field](./#reference-view-architectures-form-field), [label](./#reference-view-architectures-form-label),[button](./#reference-view-architectures-form-button),[Chatter widget](./#reference-view-architectures-form-chatter), and[Attachments preview widget](./#reference-view-architectures-form-attachment).

Placeholders are denoted in all caps.

#### `field`: display field values

The `field` element renders (and allows editing of, possibly) a single field of the current record.

Using the same field multiple times in a form view is supported, and the fields can receive\
different values for the `invisible` and `readonly` attributes. These fields may have the same\
values but can be displayed differently. However, the behavior is not guaranteed when several fields\
exist with different values for the `required` attribute.

```xml
<form>
    <field name="FIELD_NAME"/>
</form>
```

The `field` element can have the following attributes:

### name

The name of the field to render.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### id

The node id. Useful when there are several occurrences of the same field in the view (see[label: display field labels](./#reference-view-architectures-form-label)).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**\
  The field name

### string

The label of the field.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**\
  The `string` attribute of the model's field

### help

The tooltip displayed when hovering the field or its label.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### widget

The rendering method and context to use in place of the default one assigned to the field's type
(e.g., `Char`, `Many2one`). See
[Fields](../frontend/javascript_reference.md#reference-js-widgets).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### options

The configuration options for the field's widget (including default widgets), as a Python\
expression that evaluates to a dict.

For relation fields, the following options are available: `no_create`, `no_quick_create`,`no_open`, and `no_create_edit`.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`{}`

### readonly

Whether the field can be modified by the user (`False`) or is read-only (`True`), as a Python\
expression that evaluates to a bool.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### required

Whether the field can be left empty (`False`) or must be set (`True`), as a Python expression\
that evaluates to a bool.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### domain

The filters to apply when displaying existing records for selection, as a Python expression that
evaluates to a [domain](../backend/orm.md#reference-orm-domains).

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`[]`
* **Scope:**\
  Relational fields

### context

The context to use when fetching possible values and creating or searching records, as a Python\
expression that evaluates to a dict.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`{}`
* **Scope:**\
  Relational fields

### nolabel

Whether the field label should be hidden.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`
* **Scope:**\
  Fields that are a direct child of a `group` element

### placeholder

The help message to display on _empty_ fields. It can replace field labels in complex forms.\
However, it _should not_ be an example of data, as users may confuse placeholder text with filled\
fields.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### mode

The comma-separated list of display modes (view types) to use for the field's linked records.\
Allowed modes are: `tree`, `form`, `kanban`, and `graph`.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`tree`
* **Scope:**`One2many` and `Many2many` fields

### class

The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](icons.md#reference-user-interface-ui-icons). Common Odoo classes include:

* `oe_inline`: prevents the usual line break following fields, and limits their span;
* `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the\
  element to the corresponding direction;
* `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
* `oe_avatar`: for image fields, displays images as an "avatar" (max 90x90 square);
* `oe_stat_button`: defines a particular rendering to dynamically display information while being\
  clickable to target an action.
* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### filename

The name of the related field providing the name of the file.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`
* **Scope:**`Binary` fields

### password

Whether the field stores a password and thus its data should not be displayed.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`
* **Scope:**`Char` fields

### kanban\_view\_ref

The XMLID of the specific Kanban [view record](view_records.md) that should be used when
selecting records in a mobile environment.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`
* **Scope:**\
  Relational fields

### default\_focus

Whether the field is focused when the view opens. It can be applied to only one field of a view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

#### NOTE
[Relational fields](../../../applications/studio/fields.md#studio-fields-relational-fields) nodes can contain specific subviews.

[Relational fields](applications/studio/fields.md#studio-fields-relational-fields) nodes can contain specific subviews.

#### `label`: display field labels

When a [field](./#reference-view-architectures-form-field) component is not placed directly\
inside a [group](./#reference-view-architectures-form-group), or when its `nolabel` attribute is\
set, the field's label is not automatically displayed alongside its value. The `label` component is\
the manual alternative of displaying the label of a field.

```xml
<form>
    <div class="col col-md-auto">
        <label for="FIELD_NAME" string="LABEL"/>
        <div>
            <field name="FIELD_NAME" class="oe_inline"/>
        </div>
    </div>
</form>
```

The `label` element can have the following attributes:

### for

The reference to the field associated with the label. It can be either the name of the field, or\
its id (the `id` attribute set on the [field](./#reference-view-architectures-form-field)).

When there are several occurrences of the same field in the view, and there are several `label`\
components associated with these field nodes, these labels must have unique `for` attribute; in\
this case, referencing the `id` attribute of the corresponding field nodes.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### string

The label to display.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**\
  The field's label coming from the field definition on the model

### class

The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](icons.md#reference-user-interface-ui-icons). Common Odoo classes include:

* `oe_inline`: prevents the usual line break following fields, and limits their span;
* `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the\
  element to the corresponding direction;
* `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
* `oe_avatar`: for image fields, displays images as an "avatar" (max 90x90 square);
* `oe_stat_button`: defines a particular rendering to dynamically display information while being\
  clickable to target an action.
* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

#### `button`: display action buttons

```xml
<form>
    <button type="object" name="ACTION" string="LABEL"/>
    <button type="object" name="ACTION" icon="FONT_AWESOME"/>
</form>
```

The `button` element can have the following attributes:

### type

The type of the button indicating how it behaves. It can have two different values:

### object

Call a method on the view's model. The button's `name` is the method that is called with the\
current record ID and the current `context`.

### action

Load and execute an `ir.actions` action record. The button's `name` is the XMLID of the\
action to load. The `context` is extended with the view's model (as `active_model`) and with\
the current record (as `active_id`).

* **Requirement:**\
  Mandatory if the `special` attribute is not set
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### name

The method to call if the `type` is `object`. The [XMLID](../../glossary.md#term-external-identifier) of the
action to load if the `type` is `action`, either in raw format or in `%(XMLID)d` format.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### string

The button's text if there is no `icon`, the `alt` text for the icon otherwise.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### icon

The icon to use to display the button. See [icons](icons.md#reference-user-interface-ui-icons) for
the reference list.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### help

The tooltip message shown when hovering with the mouse cursor.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### context

The context that is merged into the view's context when performing the button's call, as a Python\
expression that evaluates to a dict.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`{}`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### class

The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](icons.md#reference-user-interface-ui-icons). Common Odoo classes include:

* `oe_inline`: prevents the usual line break following fields, and limits their span;
* `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the\
  element to the corresponding direction;
* `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
* `oe_avatar`: for image fields, displays images as an "avatar" (max 90x90 square);
* `oe_stat_button`: defines a particular rendering to dynamically display information while being\
  clickable to target an action.
* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### special

The behavior of the button for form views opened in dialog. It can have two different values:

### save

Save the record and close the dialog.

### cancel

Close the dialog without saving.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### confirm

The confirmation message to display (and for the user to accept) before performing the button's\
action.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### data-hotkey

The hotkey ([keyboard\_shortcut](https://en.wikipedia.org/wiki/Keyboard_shortcut), similar to an [accesskey](https://www.w3.org/TR/html5/editing.html#the-accesskey-attribute)) that is bound to the button. It is\
enabled when the `alt` key is pressed together with the selected character, or together with the`shift` key and the selected character when `shift+` is prepended to the value.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

#### Chatter widget

The [chatter widget](../backend/mixins.md#reference-mixins-mail-chatter) is the communication and log tool allowing
to email colleagues and customers directly from a record (task, order, invoice, event, note...).

It is added with a `div` element with the class `oe_chatter` when the model inherits the`mail.thread` mixin.

#### Attachments preview widget

The attachment preview widget is added with an _empty_ `div` element with the class`o_attachment_preview`.

### Structural components

Structural components provide structure or "visual" features with little logic. They are used as\
elements or sets of elements in form views.

Form views accept the following children structural components: [group](./#reference-view-architectures-form-group), [sheet](./#reference-view-architectures-form-sheet),[notebook](./#reference-view-architectures-form-notebook),[notebook](./#reference-view-architectures-form-notebook),[newline](./#reference-view-architectures-form-newline),[separator](./#reference-view-architectures-form-separator),[header](./#reference-view-architectures-form-header),[footer](./#reference-view-architectures-form-footer),[Buttons container](./#reference-view-architectures-form-button-container), and[Title container](./#reference-view-architectures-form-title-container).

Placeholders are denoted in all caps.

#### `group`: define columns layouts

The `group` element is used to define column layouts in forms. By default, groups define 2 columns,\
and most direct children of groups take a single column.

[field](./#reference-view-architectures-form-field) elements that are direct children of groups\
display a `label` by default, and the label and the field itself have a `colspan` of `1` each.

Children are laid out horizontally (they try to fill the next column before changing row).

```xml
 <form>
     <group>
         ...
     </group>
</form>
```

The `group` element can have the following attributes:

### string

The title displayed for the group.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### col

The number of columns in a `group`.

* **Requirement:**\
  Optional
* **Type:**[int](https://docs.python.org/3/library/functions.html#int)
* **Default:**`2`

### colspan

The number of columns taken by a child element.

* **Requirement:**\
  Optional
* **Type:**[int](https://docs.python.org/3/library/functions.html#int)
* **Default:**`1`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

#### `sheet`: make the layout responsive

The `sheet` element can be used as a direct child of the [form](./#reference-view-architectures-form) root element for a narrower and more responsive form layout\
(centered page, margin...). It usually contains [group](./#reference-view-architectures-form-group) elements.

```xml
<form>
    <sheet>
        ...
    </sheet>
</form>
```

#### `notebook` & `page`: add tabbed sections

The `notebook` element defines a tabbed section. Each tab is defined through a `page` child element.

The `notebook` element should not be placed within `group` elements.

```xml
<form>
    <notebook>
        <page string="LABEL">
            ...
        </page>
    </notebook>
</form>
```

The `page` element can have the following attributes:

### string

The title of the tab.

* **Requirement:**\
  Optional
* **Type:**`str`
* **Default:**`''`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

#### `newline`: start new group rows

The `newline` element is used within [group](./#reference-view-architectures-form-group)\
elements to end the current row early and immediately switch to a new row, without filling any\
remaining column beforehand.

```xml
<form>
    <group>
        ...
        <newline/>
        ...
    </group>
</form>
```

#### `separator`: add horizontal spacing

The `separator` element adds vertical spacing between elements within a group.

```xml
<form>
    ...
    <separator/>
    ...
</form>
```

The `<separator>` element can have the following attributes:

### string

The title as a section title.

* **Requirement:**\
  Optional
* **Type:**`str`
* **Default:**`''`

#### `header`: display workflow buttons and a status

The `header` element combined with the [sheet](./#reference-view-architectures-form-sheet)\
element provides a full-width location above the sheet itself generally used to display workflow[button](./#reference-view-architectures-form-button) elements and a [field](./#reference-view-architectures-form-field) element rendered as status widget.

```xml
<form>
    <header>
        <BUTTONS/>
    </header>
    <sheet>
        ...
    </sheet>
</form>
```

#### `footer`: display dialog buttons

The `footer` element is used to display [buttons](./#reference-view-architectures-form-button)\
elements at the end of dialogs.

```xml
<form>
    <sheet>
        ...
    </sheet>
    <footer>
        <BUTTONS/>
    </footer>
</form>
```

#### Buttons container

A [button](./#reference-view-architectures-form-button) elements container can be created with a`div` element with the class `button_box`.

```xml
<form>
    <div name="button_box">
        <BUTTONS/>
    </div>
<form>
```

#### Title container

A title [field](./#reference-view-architectures-form-field) element container can be created with\
a `div` element with the class `oe_title`.

```xml
<form>
    <sheet>
        <div class="oe_title">
            <h1><FIELD/></h1>
        </div>
    </sheet>
<form>
```

## Settings

Settings views are a customization of the [form](./#reference-view-architectures-form) view. They\
are used to display settings in a centralized place. They differ from generic form views in that\
they have a search bar and a sidebar.

### Components

Settings views accept the [field](./#reference-view-architectures-form-field), [label](./#reference-view-architectures-form-label) and [button](./#reference-view-architectures-form-button) elements of [form](./#reference-view-architectures-form) views, as well as three additional children elements:[app](./#reference-view-architectures-settings-app), [block](./#reference-view-architectures-settings-block), and [setting](./#reference-view-architectures-settings-setting).

Placeholders are denoted in all caps.

#### `app`: declare the application

The `app` element is used to declare the application on the settings view. It creates an entry with\
the logo of the application on the sidebar of the view. It also acts as delimiter when searching.

```xml
<form>
    <app string="NAME" name="TECHNICAL_NAME">
    ...
    </app>
</form>
```

The `app` element can have the following attributes:

### string

The name of the application.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### name

The technical name of the application (the name of the module).

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### logo

The [relative path](https://en.wikipedia.org/wiki/URL) to the logo.

* **Requirement:**\
  Optional
* **Type:**[path](https://en.wikipedia.org/wiki/Path_\(computing\))
* **Default:**\
  A path computed with the `name` attribute: `/*name*/static/description/icon.png`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

#### `block`: declare a group of settings

The `block` element is used to declare a group of settings. This group can have a title and a\
description.

```xml
 <form>
     <app string="NAME" name="TECHNICAL_NAME">
         ...
         <block title="TITLE">
             ...
         </block>
         ...
     </app>
</form>
```

The `block` element can have the following attributes:

### title

The title of the block of settings. One can search on its value.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### help

The description of the block of settings. One can search on its value.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

#### `setting`: declare the setting

The `setting` element is used to declare the setting itself.

The first [field](./#reference-view-architectures-form-field) element in the setting is used as\
the main field. It is placed on the left panel if it is a boolean field, and on the top of the right\
panel otherwise. The field is also used to create the setting label if a `string` attribute is not\
defined.

The `setting` element can also contain additional elements (e.g., HTML). All of those elements are\
rendered in the right panel.

```xml
<form>
    <app string="NAME" name="TECHNICAL_NAME">
        <block title="TITLE">
            ...
            <setting string="SETTING_NAME">
                ...
                <field name="FIELD_NAME"/>
                ...
            </setting>
            ...
        </block>
    </app>
</form>
```

The `<setting>` element can have the following attributes:

### type

By default, a setting is visually separated on two panels (left and right), and is used to edit a\
given [field](./#reference-view-architectures-form-field). By defining `type="header"`, a\
special kind of setting is rendered instead. This setting is used to modify the scope of the\
other settings. For example, on the Website application, this setting is used to indicate to\
which website the other settings apply. The header setting is visually represented as a banner on\
top of the screen.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### string

The text used as the label of the setting.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**\
  The first field's label

### title

The text used as a tooltip.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### help

The description of the setting. This text is displayed just below the setting label (with the\
class `text-muted`).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### company\_dependent

Whether the setting is company-specific. If set, an icon is displayed next to the setting label.

It accepts only the value `'1'`.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### documentation

The [path](https://en.wikipedia.org/wiki/Path_\(computing\)) to the documentation on the setting. If set, a clickable icon is displayed next to\
the setting label. The path can be both an absolute or a [relative path](https://en.wikipedia.org/wiki/URL). In the latter case, it\
is relative to `https://www.odoo.com/documentation/<version>`.

* **Requirement:**\
  Optional
* **Type:**`path_`
* **Default:**`''`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

## List

The root element of list views is `tree`[<sup>1</sup>](./#treehistory).

### Root attributes

Optional attributes can be added to the root element `tree` to customize the view.

### string

The view title. It is displayed only if you open an action that has no name and whose target is`new` (opening a dialog).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### create

Disable/enable record creation on the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### edit

Disable/enable record edition on the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### delete

Disable/enable record deletion on the view through the Action dropdown.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### import

Disable/enable record import from data on the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### export\_xlsx

Disable/enable record export to data on the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### editable

Make the view's records editable in-place, and allow creating new records from a row of the list.\
It can have two different values:

### top

New records are created from the top of the list.

### bottom

New records are created from the bottom of the list.

The architecture for the inline [form](./#reference-view-architectures-form) view is derived\
from the list view. Most attributes valid on a form view's fields and buttons are thus accepted\
by list views, although they may not have any meaning if the list view is non-editable.

#### IMPORTANT

This behavior is disabled if the `edit` attribute is set to `False`.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### multi\_edit

Activate the multi-editing feature that allows updating a field to the same value for multiple\
records at once.

It accepts only the value `'1'`.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### open\_form\_view

Display a button at the end of each row to open the record in a form view.

It has no effect if the view is non-editable.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

### default\_group\_by

The name of the field on which the records should be grouped by default if no grouping is\
specified via the action or the current [search](./#reference-view-architectures-search).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### default\_order

A comma-separated list of fields names that overrides the ordering defined on the model through\
the `_order` attribute.

To inverse the sorting order of a field, postfix it with `desc`, separated by a space.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### decoration-The style that should be applied to matching records' rows, as a Python expression that evaluates to a bool.`<style>` must be replaced by one of `bf` (bold), `it` (italic), `info`, `warning`, `danger`,`muted`, `primary`, and `success`.**Requirement:** Optional**Type:**[Python expression](./#reference-view-architectures-python-expression)**Default:**`False`

### limit

The default size of a page. It must be strictly positive.

* **Requirement:**\
  Optional
* **Type:**[int](https://docs.python.org/3/library/functions.html#int)
* **Default:**`80` for list views, `40` for X2many lists in form views

### groups\_limit

The default number of groups on a page when the list view is grouped. It must be strictly\
positive.

* **Requirement:**\
  Optional
* **Type:**[int](https://docs.python.org/3/library/functions.html#int)
* **Default:**`80` for list views, `40` for X2many lists in form views

### expand

Whether the first level of groups should be opened by default when the list view is grouped.

#### WARNING

It may be slow, depending on the number of groups.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

### sample

Whether the view should be populated with a set of sample records if none are found for the\
current model.

These fake records have heuristics for certain field names/models. For example, a field`display_name` on the model `res.users` will be populated with sample people names, while an`email` field will be in the form `firstname.lastname@sample.demo`.

The user is unable to interact with these data, and they will be discarded as soon as an action\
is performed (record created, column added, etc.).

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

### banner\_route

The route to fetch HTML from and prepend it to the view.

If this attribute is set, the URL of the [controller route](../backend/http.md#reference-controllers) is
fetched and the returned content is displayed above the view. The JSON response from the
controller must contain an `html` key.

If the HTML contains a `<link>` tag for a stylesheet, it is removed from its original location\
and appended to the `<head>` section.

Use `<a type="action">` tags to interact with the backend, like with [action buttons](./#reference-view-architectures-form-button).

* **Requirement:**\
  Optional
* **Type:**[path](https://en.wikipedia.org/wiki/Path_\(computing\))
* **Default:**`''`

### Components

List views accept the following children elements: [field](./#reference-view-architectures-list-field), [button](./#reference-view-architectures-list-button), [groupby](./#reference-view-architectures-list-groupby), [header](./#reference-view-architectures-list-header), [control, and create](./#reference-view-architectures-list-control).

Placeholders are denoted in all caps.

#### `field`: display field values

The `field` element renders (and allows editing of, possibly) a single field of all current records\
as a column.

Using the same field multiple times in a list view is not supported

```xml
<tree>
    <field name="FIELD_NAME"/>
</tree>
```

The `field` element can have the following attributes:

### name

The name of the field to render.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### string

The label of the field.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**\
  The `string` attribute of the model's field

### optional

Make the visibility of the field optional. The field's column can be hidden or shown through a\
button on the view's header.

It can have two different values:

### show

The field is shown by default.

### hide

The field is hidden by default.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### readonly

Whether the field can be modified by the user (`False`) or is read-only (`True`), as a Python\
expression that evaluates to a bool.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### required

Whether the field can be left empty (`False`) or must be set (`True`), as a Python expression\
that evaluates to a bool.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### column\_invisible

Whether the column is visible (`False`) or hidden (`True`), as a Python expression that evaluates\
to a bool.

Unlike `invisible`, it affects the entire column, and is evaluated without the subtree values.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### decoration-The style that should be applied to matching records' field, as a Python expression that evaluates to a bool.`<style>` must be replaced by one of `bf` (bold), `it` (italic), `info`, `warning`, `danger`,`muted`, `primary`, and `success`.**Requirement:** Optional**Type:**[Python expression](./#reference-view-architectures-python-expression)**Default:**`False`

### widget

The rendering method and context to use in place of the default one assigned to the field's type
(e.g., `Char`, `Many2one`). See
[Fields](../frontend/javascript_reference.md#reference-js-widgets).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### sum, avg

The aggregate to display at the bottom of the column. The aggregation is computed on only\
records that are currently displayed. The aggregation operation must match the corresponding\
field's `group_operator`.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### width

The width to apply to the field's column when there are no records in the list, as an absolute\
width (e.g., `100px`).

#### IMPORTANT

The width is set by the webclient when there are records in the list.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### nolabel

Whether the field's column header should remain empty. If set, the column will not be sortable.

It accepts only the value `'1'`

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

#### NOTE

When a list view is grouped, numeric fields are aggregated and displayed for each group. Also, if\
there are too many records in a group, a pager appears on the right of the group row. For this\
reason, it is a bad practice to have a numeric field in the last column when the list view is in\
a situation where it can be grouped. However, it does not pose a problem for X2many fields in a\
form view, as they cannot be grouped.

#### `button`: display action buttons

```xml
<tree>
    <button type="object" name="ACTION" string="LABEL"/>
    <button type="object" name="ACTION" icon="FONT_AWESOME"/>
</tree>
```

The `button` element can have the following attributes:

### type

The type of the button indicating how it behaves. It can have two different values:

### object

Call a method on the view's model. The button's `name` is the method that is called with the\
current record ID and the current `context`.

### action

Load and execute an `ir.actions` action record. The button's `name` is the XMLID of the\
action to load. The `context` is extended with the view's model (as `active_model`) and with\
the current record (as `active_id`).

* **Requirement:**\
  Mandatory if the `special` attribute is not set
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### name

The method to call if the `type` is `object`. The [XMLID](../../glossary.md#term-external-identifier) of the
action to load if the `type` is `action`, either in raw format or in `%(XMLID)d` format.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### string

The button's text if there is no `icon`, the `alt` text for the icon otherwise.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### icon

The icon to use to display the button. See [icons](icons.md#reference-user-interface-ui-icons) for
the reference list.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### help

The tooltip message shown when hovering with the mouse cursor.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### context

The context that is merged into the view's context when performing the button's call, as a Python\
expression that evaluates to a dict.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`{}`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### column\_invisible

Whether the column is visible (`False`) or hidden (`True`), as a Python expression that evaluates\
to a bool.

Unlike `invisible`, it affects the entire column, and is evaluated without the subtree values.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### class

The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](icons.md#reference-user-interface-ui-icons). Common Odoo classes include:

* `oe_inline`: prevents the usual line break following fields, and limits their span;
* `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the\
  element to the corresponding direction;
* `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
* `oe_avatar`: for image fields, displays images as an "avatar" (max 90x90 square);
* `oe_stat_button`: defines a particular rendering to dynamically display information while being\
  clickable to target an action.
* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

#### `groupby`: define group headers

The `groupby` element is used to define group headers with [button](./#reference-view-architectures-list-button) elements when grouping records on`Many2one` fields. It also accepts [field](./#reference-view-architectures-list-field) elements, which can be used for modifiers. These fields\
thus belong on the Many2one co-model. These extra fields are fetched in batch.

```xml
<tree>
    ...
    <groupby name="FIELD_NAME">
        <BUTTONS/>
        <FIELDS/>
    </groupby>
</tree>
```

The `groupby` element can have the following attributes:

### name

The name of the a `Many2one` field to use as header.

A special [button](./#reference-view-architectures-list-button) element with `type="edit"` can\
be defined to open the Many2one field's form view.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

#### NOTE

Fields inside the `groupby` element are used only to fetch and store the value, but they are\
never displayed.

#### `header`: display workflow buttons

```xml
<tree>
    <header>
        <BUTTONS/>
    </header>
    ...
</tree>
```

The `header` element accepts the following children elements:

### button

The `button` element allows defining buttons in the control panel. It is the same element as the[button element in list views](./#reference-view-architectures-list-button), but it accepts\
one more attribute when placed inside a `header` element:

### display

Make the button available at all time, without having to select records.

It accepts only the value `always`.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

#### `control` & `create`: add inline create buttons

The `control` element defines a control row that accepts create buttons. Each create button is\
defined through a `create` element.

```xml
<tree>
   <control>
       <create string="LABEL"/>
       <BUTTONS/>
    </control>
    ...
</tree>
```

The `control` element takes no attributes.

The `create` element can have the following attributes:

### string

The button's text.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### context

The context that is merged into the view's context when performing the button's call, as a Python\
expression that evaluates to a dict.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`{}`

#### NOTE

Using the `control` element makes sense only if the list view is inside a`One2many` or `Many2many` field. If any `create` element\
is defined, it overwrites the default add a line button.

* **\[1]** For historical reasons, it has its origin in tree-type views later repurposed to a more table/list-type display

## Search

Search views are different from other view types in that they are not used to display content.\
Although they apply to a specific model, they are used to filter another view's content (usually\
aggregated views; e.g., [List](./#reference-view-architectures-list) and[Graph](./#reference-view-architectures-graph)).

The root element of search views is `search`.

It takes no attributes.

### Components

Search views accept the following children elements: [field](./#reference-view-architectures-search-field), [filter](./#reference-view-architectures-search-filter), [separator](./#reference-view-architectures-search-separator), [group](./#reference-view-architectures-search-group), and [searchpanel](./#reference-view-architectures-search-searchpanel).

Placeholders are denoted in all caps.

#### `field`: filter based on field values

The `field` element defines domains or contexts with user-provided values. When search domains are\
generated, field domains are joined with each other and with filters using the **AND** operator.

```xml
<search>
    <field name="FIELD_NAME"/>
</search>
```

The `field` element can have the following attributes:

### name

The name of the field to filter on.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### string

The label of the field.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**\
  The `string` attribute of the model's field

### operator

By default, fields generate domains of the form `[(name, *operator*, value)]`, where `name`\
is the field's name and `value` is the value provided by the user, possibly filtered or\
transformed (e.g., a user is expected to provide the _label_ of a selection field's value, not\
the value itself).

The `operator` attribute allows overriding the default operator, which depends on the field's\
type (e.g., `=` for float fields, but `ilike` for char fields and `child_of` for many2one).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`=`

### filter\_domain

The domain to use as the field's search domain, as a Python expression that evaluates to a
[domain](../backend/orm.md#reference-orm-domains).

It can use the `self` variable to inject the provided value in the custom domain. It can be used\
to generate significantly more flexible domains than with the `operator` attribute alone (e.g.,\
search on multiple fields at once).

If both the `operator` and `filter_domain` attributes are provided, `filter_domain` takes\
precedence.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`[]`

### context

The context to merge into the context of the view that the search view is targeting, as a Python\
expression that evaluates to a dict.

It can contain user-provided values, which are available under the `self` variable.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`{}`

### domain

The filters to apply to the completion results for fields that allow for auto-completion (e.g.,`Many2one`).

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`[]`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

#### `filter`: create pre-defined filters

The `filter` element is used to create pre-defined filters that can be toggled in the search view.\
It allows adding data to the search context , or appending new sections to the search filter.

```xml
<search>
    <filter string="LABEL" domain="DOMAIN"/>
</search>
```

The `filter` element can have the following attributes:

### name

The technical name of the filter. It can be used to [enable it by default](#reference-view-architectures-search-defaults) or as an [inheritance hook](view_records.md#reference-view-records-inheritance).

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### string

The label of the filter.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### help

The tooltip displayed when hovering the filter.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### domain

The domain to append to the action's domain as part of the search domain.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`[]`

### date

The name of the `date` or `datetime` field to filter on.

When used, this attribute creates a set of filters available in a sub-menu of the\
Filters menu. The available filters are time-dependent but not dynamic in the sense\
that their domains are evaluated at the time of the control panel instantiation.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### default\_period

The default period of the time-based filter (with a `date` attribute). It must be one of, or a\
comma-separated list of, `today`, `this_week`, `this_month`, `last_month`,`antepenultimate_month`, `fourth_quarter`, `third_quarter`, `second_quarter`, `first_quarter`,`this_year`, `last_year` or `antepenultimate_year`.

The filter must be in the default set of filters activated at the view initialization.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`this_month`
* **Scope:**\
  Filters with a non-empty `date` attribute

### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that\
evaluates to a bool.

#### NOTE

There are two uses for the `invisible` attribute:

* Usability: to avoid overloading the view and to make it easier for the user to read,\
  depending on the content.
* Technical: a field must be present (invisible is enough) in the view to be used in a\
  Python expression.
* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`False`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### context

The context merged into the action's domain to generate the search domain

The context key `group_by` set with a field as value can be used to define a group available in\
the Group By menu. When the field is of type `date` or `datetime`, the filter\
generates a submenu of the Group By menu with the following interval options\
available: Year, Quarter, Month, Week, and\
Day. When the filter is in the default set of filters activated at the view\
initialization, the records are grouped by month by default. This can be changed by using the\
syntax `date_field:interval`.

#### NOTE

The results of `read_groups` grouped on a field may be influenced by its `group_expand`\
attribute, allowing to display empty groups when needed. For more information, please refer to`Field`.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`{}`

#### `separator`: separate groups of filters

The `separator` element is used to separates groups of [filters](./#reference-view-architectures-search-filter) in simple search views. For more complex search views,\
the [group](./#reference-view-architectures-search-group) element is recommended.

```xml
<search>
    <FILTERS/>
    <separator/>
    <FILTERS/>
</search>
```

The `separator` element takes no attributes.

#### `group`: separate groups of filters

The `group` element is used to separate groups of [filters](./#reference-view-architectures-search-filter) in cluttered search views. In simpler search views, it\
can be substituted for the [separator](./#reference-view-architectures-search-group) element.

```xml
<search>
    <group>
        <FILTERS/>
    </group>
</search>
```

The `group` element takes no attributes.

#### `searchpanel`: display search panels

The `searchpanel` element displays a search panel to the left of multi-records views. It allows for\
quickly filtering data on the basis of given fields.

```xml
<search>
    <searchpanel>
        <FIELDS/>
    </searchpanel>
</search>
```

The `searchpanel` element accepts only `field` children elements.

The `field` element used as a child element of a `searchpanel` element can have the following\
attributes:

### name

The name of the field to filter on.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### string

The label of the field.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**\
  The `string` attribute of the model's field

### select

The behavior and display of the field. It can have two different values:

### one

At most one value can be selected. Supported field types are `many2one` and `selection`.

### multi

Several values can be selected. Supported field types are `many2one`, `many2many` and`selection`.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`one`

### groups

The comma-separated list of user groups to whom the element is displayed. Users who do not belong\
to at least one of these groups are unable to see the element. Groups can be prefixed with the\
negative `!` operator to exclude them.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### icon

The icon of the field.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### color

The color of the field.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

When the `field` element has the `select=one` attribute set, it can have the following additional\
attributes:

### hierarchize

Whether child categories should appear under their parent category, or at the same hierarchy\
level.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`
* **Scope:**`Many2one` fields

When the `field` element has the `select=multi` attribute set, it can have the following additional\
attributes:

### enable\_counters

Whether the record counters is computed and displayed if non-zero.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

### expand

Whether categories and filters with no records should be shown.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

### limit

The maximal number of values to fetch for the field. If the limit is reached, no values are\
displayed on the search panel, and an error message is shown instead. If set to 0, all values are\
fetched.

* **Requirement:**\
  Optional
* **Type:**[int](https://docs.python.org/3/library/functions.html#int)
* **Default:**`200`

### domain

The conditions that the records have to satisfy.

* **Requirement:**\
  Optional
* **Type:**[Python expression](./#reference-view-architectures-python-expression)
* **Default:**`[]`

### groupby

The name of the field name on which values should be grouped.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`
* **Scope:**`Many2one` and `Many2many` fields

### Search defaults

Search fields and filters can be configured through the action's `context` using`search_default_*name*` keys. For fields, the value must be the value to set to the field. For\
filters, it must be a boolean value or a number.

A numeric value (between 1 and 99) can be used to define the order of default _groupby_ filters.

## Kanban

Kanban views are a used as a [kanban board](https://en.wikipedia.org/wiki/Kanban_board)\
visualisation: they display records as "cards", halfway between a [list](./#reference-view-architectures-list) view and a non-editable [form](./#reference-view-architectures-form) view.

Records may be grouped in columns for use in workflow visualisation or manipulation (e.g., tasks or\
work-progress management), or ungrouped (used simply to visualize records).

The root element of Kanban views is `kanban`.

#### NOTE

Kanban views load and display a maximum of ten columns. Any column after that is closed but can\
still be opened by the user.

### Root attributes

Optional attributes can be added to the root element `kanban` to customize the view.

### string

The view title. It is displayed only if you open an action that has no name and whose target is`new` (opening a dialog).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### create

Disable/enable record creation on the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### edit

Disable/enable record edition on the view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### delete

Disable/enable record deletion on the view through the Action dropdown.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### default\_group\_by

The name of the field on which the records should be grouped by default if no grouping is\
specified via the action or the current [search](./#reference-view-architectures-search).

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### default\_order

A comma-separated list of fields names that overrides the ordering defined on the model through\
the `_order` attribute.

To inverse the sorting order of a field, postfix it with `desc`, separated by a space.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### class

Add HTML classes to the root HTML element of the view.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### examples

The key in the `KanbanExamplesRegistry` of the examples than can be browsed when creating a new\
column in the grouped kanban view.

#### SEE ALSO

[Use of the examples attribute in the utm module](https://github.com/odoo/odoo/blob/17.0/addons/utm/static/src/js/utm_campaign_kanban_examples.js)

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### group\_create

Whether the Add a new column bar is visible.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### group\_delete

Whether columns can be deleted via the cog menu.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### group\_edit

Whether columns can be edited via the cog menu.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### groups\_draggable

Whether columns can be reordered.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### records\_draggable

Whether records can be dragged when the kanban view is grouped.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### archivable

Whether records belonging to a column can be archived and unarchived when the `active` field is\
defined on the model.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True`

### quick\_create

Whether it should be possible to create records without switching to the form view.

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`True` when the kanban view is grouped by many2one, selection, char, or boolean fields,\
  otherwise `False`

### quick\_create\_view

The reference of the [form](./#reference-view-architectures-form) view to open when using the\
quick creation of records.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### on\_create

The custom action to call when clicking on Create.

If set to `'quick_create'`, the quick creation of records is used instead. If the quick creation\
is disabled, the standard create action is called.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

### sample

Whether the view should be populated with a set of sample records if none are found for the\
current model.

These fake records have heuristics for certain field names/models. For example, a field`display_name` on the model `res.users` will be populated with sample people names, while an`email` field will be in the form `firstname.lastname@sample.demo`.

The user is unable to interact with these data, and they will be discarded as soon as an action\
is performed (record created, column added, etc.).

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

### banner\_route

The route to fetch HTML from and prepend it to the view.

If this attribute is set, the URL of the [controller route](../backend/http.md#reference-controllers) is
fetched and the returned content is displayed above the view. The JSON response from the
controller must contain an `html` key.

If the HTML contains a `<link>` tag for a stylesheet, it is removed from its original location\
and appended to the `<head>` section.

Use `<a type="action">` tags to interact with the backend, like with [action buttons](./#reference-view-architectures-form-button).

* **Requirement:**\
  Optional
* **Type:**[path](https://en.wikipedia.org/wiki/Path_\(computing\))
* **Default:**`''`

### Components

Kanban views accept the following children elements: [field](./#reference-view-architectures-kanban-field), [header](./#reference-view-architectures-kanban-header), [progressbar](./#reference-view-architectures-kanban-progressbar), and [templates](./#reference-view-architectures-kanban-templates).

Placeholders are denoted in all caps.

#### `field`: display field values

The `field` element declares fields to use in the [templates](./#reference-view-architectures-kanban-templates). If the field is simply displayed, it does not need\
to be pre-declared.

```xml
<kanban>
    <field name="FIELD_NAME"/>
    ...
</kanban>
```

The `field` element can have the following attributes:

### name

The name of the field to render.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

#### `header`: display buttons in the control panel

The `header` element is used to insert custom buttons in the control panel.

```xml
<kanban>
    <header>
        <BUTTONS/>
    </header>
    ...
</kanban>
```

The `header` element accepts only `button` children elements, similar to [list views' button](./#reference-view-architectures-list-button) elements.

The `button` element used as a child element of the `header` element can have the following\
additional attributes:

### display

The display mode of the button. It can have two different values:

### display

The button is displayed only when some records are selected; their action applies to the\
selected records.

### always

The button is displayed at all times, even if no records are selected.

#### IMPORTANT

Only the `always` display mode is available because it is not yet possible to select records\
in a kanban view.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`display`

#### `progressbar`: show progress bars on top of columns

The `progressbar` element is used to define a progress bar to display on top of kanban columns.

```xml
<kanban>
    <progressbar field="FIELD_NAME"/>
    ...
</kanban>
```

The `progressbar` element can have the following attributes:

### field

The name of the field on which the progress bar's sub-groups\
are based.

* **Requirement:**\
  Mandatory
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### colors

The mapping of the progress bar's field values to the color values `muted`, `success`, `warning`,\
and `danger`.

* **Requirement:**\
  Mandatory
* **Type:**[JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

### sum\_field

The name of the field to use in a sum displayed next to the progress bar. If not set, the total\
number of records is displayed instead.

* **Requirement:**\
  Optional
* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**`''`

#### `templates`: define cards structure

The `templates` elements is used to define the [QWeb templates](../frontend/qweb.md#reference-qweb) that structure
the kanban cards.

Cards structure definition can be split into multiple templates for clarity, but at least one root\
template `kanban-box` must be defined.

Two additional templates can be defined: `kanban-menu` and `kanban-tooltip`. If defined, the`kanban-menu` template is rendered inside a dropdown that can be toggled with a vertical ellipsis\
(⋮) on the top right of the card. The `kanban-tooltip` template is rendered inside a\
tooltip when hovering kanban cards.

The templates are written in [JavaScript QWeb](../frontend/qweb.md#reference-qweb-javascript)

```xml
<kanban>
    ...
    <templates>
        <t t-name="kanban-box">
            <div>
                <field name="name"/>
            </div>
        </t>
    </templates>
</kanban>
```

The following variables are available in the rendering context:

### widget

The current `KanbanRecord()`. It can be used to fetch some meta-information. The methods\
are also available directly in the template context and don't need to be accessed via `widget`.

* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### record

An object with all the requested fields as its attributes. Each field has two attributes: `value`\
and `raw_value`. The former is formatted according to current user parameters while the latter is\
the raw value from a `read()` (except for the `date` and `datetime` fields\
that are [formatted according to the user locale](https://github.com/odoo/odoo/blob/a678bd4e/addons/web_kanban/static/src/js/kanban_record.js#L102)).

* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### context

The current context propagated from either the action that opens the kanban view, or the one2many\
or many2many field that embeds the kanban view in a form view.

* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### read\_only\_mode

* **Type:**[str](https://docs.python.org/3/library/stdtypes.html#str)

### selection\_mode

Whether the kanban view is opened when selecting a many2one or many2many field in mobile\
environment.

* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)

While most of the kanban templates are standard [QWeb templates](../frontend/qweb.md#reference-qweb), the kanban
view processes `field`, `button` and `a` elements is a special way:

*   By default, fields are replaced by their formatted value, unless the `widget` attribute is\
    specified, in which case their rendering and behavior depends on the corresponding widget. The`widget` attribute can have different values including:

    #### handle

    Allow reordering records with a drag and drop when their are sorted based on `sequence` (or`integer`) fields.
*   Buttons and links with a `type` attribute perform different operations than their standard HTML\
    function. The `type` attribute can have the values `action` and `object` of [regular buttons](./#reference-view-architectures-list-button), or the following values:

    #### open

    Clicking the element opens the card's record in form view in read-only mode.

    #### edit

    Clicking the element opens the card's record in form view in editable mode.

    #### delete

    Clicking the element deletes the card's record and removes the card.

## QWeb

QWeb views are standard [QWeb Templates](../frontend/qweb.md#reference-qweb) templates inside a view's
`arch`. They don't have a specific root element. Because QWeb views don't
have a specific root element, their type must be specified explicitly (it can
not be inferred from the root element of the `arch` field).

QWeb views have two use cases:

* they can be used as frontend templates, in which case
  [template](../backend/data.md#reference-data-template) should be used as a shortcut.
* they can be used as actual qweb views (opened inside an action), in which
  case they should be defined as regular view with an explicit `type` (it
  can not be inferred) and a model.

The main additions of qweb-as-view to the basic qweb-as-template are:

* qweb-as-view has a special case for a `<nav>` element bearing the CSS\
  class `o_qweb_cp_buttons`: its contents should be buttons and will be\
  extracted and moved to the control panel's button area, the `<nav>` itself\
  will be removed, this is a work-around to control panel views not existing\
  yet
*   qweb-as-view rendering adds several items to the standard qweb rendering\
    context:

    `model`\
    : the model to which the qweb view is bound

    `domain`\
    : the domain provided by the search view

    `context`\
    : the context provided by the search view

    `records`\
    : a lazy proxy to `model.search(domain)`, this can be used if you just\
    want to iterate the records and not perform more complex operations\
    (e.g. grouping)
* qweb-as-view also provides additional rendering hooks:
  * `_qweb_prepare_context(view_id, domain)` prepares the rendering context\
    specific to qweb-as-view
  * `qweb_render_view(view_id, domain)` is the method called by the client\
    and will call the context-preparation methods and ultimately`env['ir.qweb'].render()`.

## Graph

The graph view is used to visualize aggregations over a number of records or\
record groups. Its root element is `<graph>` which can take the following\
attributes:

`type` (optional)\
: one of `bar` (default), `pie` and `line`, the type of graph to use

`stacked` (optional)\
: only used for `bar` charts. Set to `0` to prevent the bars within a group\
to be stacked initially.

`disable_linking` (optional)\
: set to `1` to prevent from redirecting clicks on graph to list view

`order` (optional)\
: if set, x-axis values will be sorted by default according their measure with\
respect to the given order (`asc` or `desc`). Only used for `bar` and`pie` charts.

`string` (optional)\
: string displayed in the breadcrumbs when redirecting to list view.

### sample

Whether the view should be populated with a set of sample records if none are found for the\
current model.

These fake records have heuristics for certain field names/models. For example, a field`display_name` on the model `res.users` will be populated with sample people names, while an`email` field will be in the form `firstname.lastname@sample.demo`.

The user is unable to interact with these data, and they will be discarded as soon as an action\
is performed (record created, column added, etc.).

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

The only allowed element within a graph view is `field` which can have the\
following attributes:

`name` (mandatory)\
: the name of a field to use in the view. If used for grouping (rather\
than aggregating)

`invisible` (optional)\
: if true, the field will not appear either in the active measures nor in the\
selectable measures.

`type` (optional)\
: if set to `measure`, the field will be used as an aggregated value within a\
group instead of a grouping criteria. It only works for the last field\
with that attribute but it is useful for other fields with string attribute\
(see below).

`interval` (optional)\
: on date and datetime fields, groups by the specified interval (`day`,`week`, `month`, `quarter` or `year`) instead of grouping on the\
specific datetime (fixed second resolution) or date (fixed day resolution).\
Default is `month`.

`string` (optional)\
: only used for field with `type="measure"`. The name that will be used to\
display the field in the graph view, overrides the default python String\
attribute of the field.

The measures are automatically generated from the model fields; only the\
aggregatable fields are used. Those measures are also alphabetically\
sorted on the string of the field.

#### WARNING

graph view aggregations are performed on database content, non-stored\
function fields can not be used in graph views

In Graph views, a `field` can have a `widget` attribute to dictate its format.\
The widget should be a field formatter, of which the most interesting are`float_time`, and `monetary`.

```xml
<field name="working_hours_close" widget="float_time"/>
```

## Pivot

The pivot view is used to visualize aggregations as a [pivot table](https://en.wikipedia.org/wiki/Pivot_table). Its root\
element is `<pivot>` which can take the following attributes:

`disable_linking` (optional)\
: Set to `1` to remove table cell's links to list view.

`display_quantity` (optional)\
: Set to `1` to display the Quantity column by default.

`default_order` (optional)\
: The name of the measure and the order (asc or desc) to use as default order\
in the view.\


```xml
<pivot default_order="foo asc">
   <field name="foo" type="measure"/>
</pivot>
```

The only allowed element within a pivot view is `field` which can have the\
following attributes:

`name` (mandatory)\
: the name of a field to use in the view. If used for grouping (rather\
than aggregating)

`string` (optional)\
: the name that will be used to display the field in the pivot view,\
overrides the default python String attribute of the field.

`type` (optional)\
: indicates whether the field should be used as a grouping criteria or as an\
aggregated value within a group. Possible values are:\
`row` (default)\
: groups by the specified field, each group gets its own row.\
`col`\
: creates column-wise groups\
`measure`\
: field to aggregate within a group\
`interval`\
: on date and datetime fields, groups by the specified interval (`day`,`week`, `month`, `quarter` or `year`) instead of grouping on the\
specific datetime (fixed second resolution) or date (fixed day resolution).

`invisible` (optional)\
: if true, the field will not appear either in the active measures nor\
in the selectable measures (useful for fields that do not make sense aggregated,\
such as fields in different units, e.g. € and $).

### sample

Whether the view should be populated with a set of sample records if none are found for the\
current model.

These fake records have heuristics for certain field names/models. For example, a field`display_name` on the model `res.users` will be populated with sample people names, while an`email` field will be in the form `firstname.lastname@sample.demo`.

The user is unable to interact with these data, and they will be discarded as soon as an action\
is performed (record created, column added, etc.).

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

The measures are automatically generated from the model fields; only the\
aggregatable fields are used. Those measures are also alphabetically\
sorted on the string of the field.

#### WARNING

like the graph view, the pivot aggregates data on database content\
which means that non-stored function fields can not be used in pivot views

In Pivot view a `field` can have a `widget` attribute to dictate its format.\
The widget should be a field formatter, of which the most interesting are`date`, `datetime`, `float_time`, and `monetary`.

For instance a timesheet pivot view could be defined as:

```default
<pivot string="Timesheet">
    <field name="employee_id" type="row"/>
    <field name="date" interval="month" type="col"/>
    <field name="unit_amount" type="measure" widget="float_time"/>
</pivot>
```

## Calendar

Calendar views display records as events in a daily, weekly, monthly or yearly\
calendar.

#### NOTE

By default the calendar view will be centered around the current date\
(today). You can pass a specific initial date to the context of the action in\
order to set the initial focus of the calendar on the period (see `mode`) around\
this date (the context key to use being `initial_date`)

Their root element is `<calendar>`. Available attributes on the\
calendar view are:

*   **string:**\
    string (default: `''`)

    This view title is displayed only if you open an action that has no name and\
    whose target is 'new' (opening a dialog)
*   **create:**\
    bool (default: `True`)

    Disable/enable record creation on the view.
*   **edit:**\
    bool (default: `True`)

    Disable/enable record edition on the view.
*   **delete:**\
    bool (default: `True`)

    Disable/enable record deletion on the view through the **Action** dropdown.

`date_start` (required)\
: name of the record's field holding the start date for the event

`date_stop`\
: name of the record's field holding the end date for the event, if`date_stop` is provided records become movable (via drag and drop)\
directly in the calendar

`date_delay`\
: alternative to `date_stop`, provides the duration of the event instead of\
its end date (unit: day)

`color`\
: name of a record field to use for _color segmentation_. Records in the\
same color segment are allocated the same highlight color in the calendar,\
colors are allocated semi-randomly.\
Displayed the display\_name/avatar of the visible record in the sidebar

`form_view_id`\
: view to open when the user create or edit an event. Note that if this attribute\
is not set, the calendar view will fall back to the id of the form view in the\
current action, if any.

`event_open_popup`\
: If the option 'event\_open\_popup' is set to true, then the calendar view will\
open events (or records) in a FormViewDialog. Otherwise, it will open events\
in a new form view (with a do\_action)

`quick_create`\
: enables quick-event creation on click: only asks the user for a `name`\
(the field to which this values is saved can be controlled through`rec_name`) and tries to create a new event with just that and the clicked\
event time. Falls back to a full form dialog if the quick creation fails

`quick_create_view_id`\
: View to open when the attribute `quick_create` is set and the user creates\
an event instead of the default dialog.

`create_name_field`\
: name of the record's field holding the textual representation of the record,\
this is used when creating records through the 'quick create' mechanism

`all_day`\
: name of a boolean field on the record indicating whether the corresponding\
event is flagged as day-long (and duration is irrelevant)

`mode`\
: Default display mode when loading the calendar.\
Possible attributes are: `day`, `week`, `month`, `year`

`scales`\
: Comma-separated list of scales to provide. By default, all scales are\
available. See mode for possible scale values.

`create`, `delete`\
: allows disabling the corresponding action in the view by setting the\
corresponding attribute to `false`

`<field>`\
: declares fields to aggregate or to use in kanban _logic_. If the field is\
simply displayed in the calendar cards.\
Fields can have additional attributes:\
`invisible`\
: use "True" to hide the value in the cards\
`avatar_field`\
: only for x2many field, to display the avatar instead of the display\_name\
in the cards\
`write_model` and `write_field` and `filter_field`\
: you can add a filter and save the result in the defined model, the\
filter is added in the sidebar. The `filter_field` is optional and allows\
you to specify the field that will hold the status of the filter.\
`filters` and `color`\
: use "True" to add this field in filter in the sidebar. You can specify\
a `color` field used to colorize the checkbox.

### Model Commons

## Activity

The Activity view is used to display the activities linked to the records. The\
data are displayed in a chart with the records forming the rows and the activity\
types the columns. The first cell of each row displays a (customizable, see`templates`, quite similarly to [Kanban](./#reference-view-architectures-kanban)) card representing\
the corresponding record. When clicking on others cells, a detailed description\
of all activities of the same type for the record is displayed.

#### WARNING

The Activity view is only available when the `mail` module is installed,\
and for the models that inherit from the `mail.activity.mixin`.

The root element of the Activity view is `<activity>`, it accepts the following\
attributes:

`string` (mandatory)\
: A title, which should describe the view

Possible children of the view element are:

`field`\
: declares fields to use in activity _logic_. If the field is simply displayed\
in the activity view, it does not need to be pre-declared.\
Possible attributes are:\
`name` (required)\
: the name of the field to fetch

`templates`
: defines the [QWeb Templates](../frontend/qweb.md#reference-qweb) templates. Cards definition may be
  split into multiple templates for clarity, but activity views *must* define at
  least one root template `activity-box`, which will be rendered once for each
  record.
  <br/>
  The activity view uses mostly-standard [javascript qweb](../frontend/qweb.md#reference-qweb-javascript) and provides the following context variables
  (see [Kanban](#reference-view-architectures-kanban) for more details):
  <br/>
  `widget`
  : the current `ActivityRecord()`, can be used to fetch some
    meta-information. These methods are also available directly in the
    template context and don't need to be accessed via `widget`
  <br/>
  `record`
  : an object with all the requested fields as its attributes. Each field has
    two attributes `value` and `raw_value`

<a id="reference-view-architectures-cohort"></a>

## Cohort

Enterprise feature

The cohort view is used to display and understand the way some data changes over\
a period of time. For example, imagine that for a given business, clients can\
subscribe to some service. The cohort view can then display the total number\
of subscriptions each month, and study the rate at which client leave the service\
(churn). When clicking on a cell, the cohort view will redirect you to a new action\
in which you will only see the records contained in the cell's time interval;\
this action contains a list view and a form view.

#### NOTE

By default the cohort view will use the same list and form views as those\
defined on the action. You can pass a list view and a form view\
to the context of the action in order to set/override the views that will be\
used (the context keys to use being `form_view_id` and `list_view_id`)

For example, here is a very simple cohort view:

```xml
<cohort string="Subscription" date_start="date_start" date_stop="date" interval="month"/>
```

The root element of the Cohort view is , it accepts the following\
attributes:

`string` (mandatory)\
: A title, which should describe the view

`date_start` (mandatory)\
: A valid date or datetime field. This field is understood by the view as the\
beginning date of a record

`date_stop` (mandatory)\
: A valid date or datetime field. This field is understood by the view as the\
end date of a record. This is the field that will determine the churn.

`disable_linking` (optional)\
: Set to `1` to prevent from redirecting clicks on cohort cells to list view.

`mode` (optional)\
: A string to describe the mode. It should be either 'churn' or\
'retention' (default). Churn mode will start at 0% and accumulate over time\
whereas retention will start at 100% and decrease over time.

`timeline` (optional)\
: A string to describe the timeline. It should be either 'backward' or 'forward' (default).\
Forward timeline will display data from date\_start to date\_stop, whereas backward timeline\
will display data from date\_stop to date\_start (when the date\_start is in future / greater\
than date\_stop).

`interval` (optional)\
: A string to describe a time interval. It should be 'day', 'week', 'month''\
(default) or 'year'.

`measure` (optional)\
: A field that can be aggregated. This field will be used to compute the values\
for each cell. If not set, the cohort view will count the number of occurrences.

`<field>` (optional)\
: allows to specify a particular field in order to manage it from the available measures, it's\
main use is for hiding a field from the selectable measures:\
`name` (mandatory)\
: the name of the field to use in the view.\
`string` (optional)\
: the name that would be used to display the field in the cohort view, overrides the\
default python String attribute of the field.\
`invisible` (optional)\
: if true, the field will not appear either in the active measures nor in the selectable\
measures (useful for fields that do not make sense aggregated, such as fields in different\
units, e.g. € and $).\
If the value is a domain, the domain is evaluated in the context of the current row's\
record, if `True` the corresponding attribute is set on the cell.

### odoo.addons.base.models.ir\_ui\_view.sample

Whether the view should be populated with a set of sample records if none are found for the\
current model.

These fake records have heuristics for certain field names/models. For example, a field`display_name` on the model `res.users` will be populated with sample people names, while an`email` field will be in the form `firstname.lastname@sample.demo`.

The user is unable to interact with these data, and they will be discarded as soon as an action\
is performed (record created, column added, etc.).

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

## Grid

Enterprise feature

### Limitations

This view is a work in progress and may have to be expanded or altered.

* only `date` column fields have been tested, `selection` and `many2one`\
  are nominally implemented and supported but have not been tested,`datetime` is not implemented at all.
* column cells are hardly configurable and must be numerical
* cell adjustment is disabled by default and must be configured to be enabled
* `create`, `edit` and `delete` ACL metadata doesn't get automatically\
  set on the view root due to limitations in `fields_view_get`\
  post-processing (there's a fixed explicit list of the view types getting\
  those attributes)

### Schema

The grid view has its own schema and additional validation in this module. The\
view architecture is:

`<grid>` (1)\
: architecture root element\


* mandatory `string` attribute
* optional `create`, `edit` and `delete` attributes
* optional `adjustment` and `adjust_name` attributes\
  \`adjustment\` can be either \`object\` or \`action\` to indicate\
  whether a cell's adjustment should be performed through a method call\
  or an action execution. \`adjust\_name\` provides respectively the method\
  name and the action id.

\
In both cases, the adjustment parameters are provided as a\
\`grid\_adjust\` context member, in the \`object\` case, the parameters\
are also provided as positional function parameters (next to an empty\
list of ids):\
\`row\_domain\`\
: the domain matching the entire row of the adjusted cell\
\`column\_field\`\
: the name of the column for the adjusted cell\
\`column\_value\`\
: the value of the column for the adjusted cell\
\`cell\_field\`\
: the measure field of the adjusted cell\
\`change\`\
: the difference between the old value of the cell and the adjusted one,\
may be positive or negative\
\* optional \`hide\_line\_total\` and \`hide\_column\_total\` attributes\
\`hide\_line\_total\`\
: set to true to hide total line (default false)\
\`hide\_column\_total\`\
: set to true to hide total column (default false)\
\* optional \`barchart\_total\` attribute\
\`barchart\_total\`\
: set to \`true\` in order to display a bar chart at the bottom of the grid, based on\
the totals of the columns (default false).\
\* optional \`create\_inline\` and \`display\_empty\` attributes\
\`create\_inline\`\
: set to \`true\` in order to display an additional row at bottom of the grid with an\
\`Add a line\` button (default false). When this option is set to \`true\`, the \`Add a line\` button\
from the control panel is hidden. When no data is available and when \`display\_empty\` is\
not set (so when the help content is displayed), the the \`Add a line\` button from the\
control panel is shown in order to let the user create a first record.\
\`display\_empty\`\
: set to \`true\` in order to keep displaying the grid when there is no data (default false). This can\
be useful when you want the user to be able to keep track of the current period (as dates\
are displayed in the columns headers). As a reminder, when no data are present and when this\
attribute is no set, the help content is displayed instead of the grid.

`<button>` (0+)\
: Regular Odoo action buttons, displayed in the view header\


* mandatory `string` attribute (the button label)
* mandatory `type` attribute, either `object` or `action`\
  \#### NOTE\
  workflow buttons are not supported
* mandatory `name` attribute, either the name of the method to call, or\
  the ID of the action to execute
* optional `context`\


The server callback is provided with all the record ids displayed in the\
view, either as the ids passed to the method (`object` button) or as\
the context's `active_ids` (`action` buttons)

`<field type="row">` (1+)\
: Row grouping fields, will be replaced by the search view's groupby filter\
if any.\
The order of `row` fields in the view provides their grouping depth:\
if the first field is `school` and the second is `age` the records\
will be grouped by `school` first and by `age` within each school.

`<field type="col">` (1)\
: Column grouping field.\
The col field can contain 0+ `<range>` elements which specify\
customisable column ranges. `range` elements have the following\
mandatory attributes\
`name`\
: can be used to override the default range (the first one by default)\
through the `grid_range` context value\
`string`\
: the range button's label (user-visible)\
`span`\
: symbolic name of the span of all columns to display at once in the\
view, may trigger pagination.\
For `date` fields, valid spans are currently `week` and `month`.\
`step`\
: symbolic name of the step between one column and the previous/next\
For `date` fields, the only valid span is currently `day`.

`<field type="measure">` (1)\
: Cell field, automatically accumulated (by `read_group`).\
The measure field can take a `widget` attribute to customise its\
display.

### Server interactions

Aside from optional buttons, the grid view currently calls two methods:

* `read_grid` (provided on all models by the module) returns almost the\
  entirety of the grid's content as a dict:
  *   the row titles is a list of dictionaries with the following keys:

      `values` (required)\
      : this maps to a dictionary with a key per `row` field, the values ar&#x65;_&#x61;lways_ of the form `[value, label]`.

      `domain` (required)\
      : the domain of any record at the source of this row, in case it's\
      necessary to copy a record during cell adjustment
  *   the column titles is a list of dictionaries with at least one key:

      `values` (required)\
      : see row title values

      `domain` (required)\
      : see column domain value

      `current` (optional)\
      : boolean, marks/highlights a column
  *   the grid data as a list (of rows) of list (of cells) of cell dicts each\
      with the following keys:

      `value`\
      : the numeric value associated with the cell

      `domain`\
      : the domain matching the cell's records (should be assumed opaque)

      `size`\
      : the number of records grouped in the cell

      `readonly` (optional)\
      : a boolean indicating that this specific cell should not be\
      client-editable

      `classes` (optional)\
      : a list of classes (as strings) to add on the cell's container (between\
      the cell's TD and the cell's potentially-editable element).\
      In case of conflicts between this list and the base classes (prefixed\
      with `o_grid_cell_`), the classes in this list are ignored.

      Note that the grid data is _dense_, if querying the database yields no\
      group matching a cell a cell will generate an "empty" cell with default\
      values for required keys.
  * `prev` and `next` which can be either falsy (no pagination) or a\
    context item to merge into the view's own context to `read_grid` the\
    previous or next page, it should be assumed to be opaque
* `read_grid_domain(field, range)` (provided on al models by the module)\
  returns the domain matching the current configured "span" of the grid. This\
  is also done internally by `read_grid`, but can be useful or necessary to\
  call independently to use with separate e.g. `search_count` or`read_group`.
* `adjust_grid`, for which there currently isn't a blanket implementation\
  and whose semantics are likely to evolve with time and use cases

### Server Hooks

`read_grid` calls a number of hooks allowing the customisation of its\
operations from within without having to override the entire method:

`_grid_format_cell(group, cell_field)`\
: converts the output of a read\_group (group-by-group) into cells in the\
format described above (as part of "the grid data")

`_grid_make_empty_cell(row_domain, column_domain, view_domain)`\
: generates an empty version of a cell (if there is no corresponding group)

`_grid_column_info(name, range)`\
: generates a ColumnMetadata object based on the column type, storing values\
either returned directly (as part of `read_grid`) or used query and\
reformat `read_group` into `read_grid`:\
`grouping`\
: the actual grouping field/query for the columns\
`domain`\
: domain to apply to `read_group` in case the column field is\
paginated, can be an empty list\
`prev` and `next`\
: context segments which will be sent to `read_grid` for pages before\
and after the current one. If `False`, disables pagination in that\
direction\
`values`\
: column values to display on the "current page", each value is a\
dictionary with the following keys:\
`values`\
: dictionary mapping field names to values for the entire column,\
usually just `name` -> a value\
`domain`\
: domain matching this specific column\
`is_current`\
: `True` if the current column should be specifically outlined in\
the grid, `False` otherwise\
`format`\
: how to format the values of that column/type from `read_group`\
formatting to `read_grid` formatting (matching `values` in\
ColumnInfo)

### ACL

* if the view is not editable, individual cells won't be editable
* if the view is not creatable, the `Add a Line` button will not be\
  displayed (it currently creates a new empty record)

### Context Keys

`grid_range`\
: selects which range should be used by default if the view has multiple\
ranges

`grid_anchor`\
: if applicable, used as the default anchor of column ranges instead of\
whatever `read_grid` defines as its default.\
For date fields, the reference date around which the initial span will be\
computed. The default date anchor is "today" (in the user's timezone)

## Gantt

Enterprise feature

Gantt views appropriately display Gantt charts (for scheduling).

The root element of gantt views is `<gantt/>`, it has no children but can\
take the following attributes:

*   **string:**\
    string (default: `''`)

    This view title is displayed only if you open an action that has no name and\
    whose target is 'new' (opening a dialog)
*   **create:**\
    bool (default: `True`)

    Disable/enable record creation on the view.
*   **edit:**\
    bool (default: `True`)

    Disable/enable record edition on the view.
*   **delete:**\
    bool (default: `True`)

    Disable/enable record deletion on the view through the **Action** dropdown.

`date_start` (required)\
: name of the field providing the start datetime of the event for each\
record.

`date_stop` (required)\
: name of the field providing the end duration of the event for each\
record.

`dependency_field`\
: name of the `many2many` field that provides the dependency relation between two records.\
If B depends on A, `dependency_field` is the field that allows getting A\
from B. Both this field and `dependency_inverted_field` field are used to\
draw dependency arrows between pills and reschedule them.

`dependency_inverted_field` (required if `dependency_field` is provided)\
: name of the `many2many` field that provides the invert dependency relation than`dependency_field`. If B depends on A, `dependency_inverted_field` is\
the field that allows getting B from A.

`color`\
: name of the field used to color the pills according to its value

`decoration-{$name}`\
: [python expression](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) that evaluates to a bool\
allow changing the style of a cell's text based on the corresponding\
record's attributes.\
`{$name}` can be one of the following [bootstrap contextual color](https://getbootstrap.com/docs/3.3/components/#available-variations) (`danger`,`info`, `secondary`, `success` or `warning`).\
Define a conditional display of a record in the style of a row's text based on the corresponding\
record's attributes.\
Values are Python expressions. For each record, the expression is evaluated\
with the record's attributes as context values and if `true`, the\
corresponding style is applied to the row. Here are some of the other values\
available in the context:\


* `uid`: the id of the current user,
* `today`: the current local date as a string of the form `YYYY-MM-DD`,
* `now`: same as `today` with the addition of the current time.\
  This value is formatted as `YYYY-MM-DD hh:mm:ss`.\


```xml
<gantt decoration-info="state == 'draft'"
      decoration-danger="state == 'help_needed'"
      decoration-bf="state == 'busy'">
  ...
</gantt>
```

`default_group_by`\
: name of a field to group tasks by

`disable_drag_drop`\
: if set to true, the gantt view will not have any drag\&drop support

`consolidation`\
: field name to display consolidation value in record cell

`consolidation_max`\
: dictionary with the "group by" field as key and the maximum consolidation\
value that can be reached before displaying the cell in red\
(e.g. `{"user_id": 100}`)

`consolidation_exclude`\
: name of the field that describes if the task has to be excluded\
from the consolidation\
if set to true it displays a striped zone in the consolidation line

`create`, `cell_create`, `edit`, `delete`, `plan`\
: allows _di&#x73;_&#x61;bling the corresponding action in the view by setting the\
corresponding attribute to `false` (default: `true`).\


* `create`: If enabled, an `Add` button will be available in the control\
  panel to create records.
* `cell_create`: If enabled and `create` enabled, a "**+**" button will be\
  displayed while hovering on a time slot cell to create a new record on that slot.
* `edit`: If enabled, the opened records will be in edit mode (thus editable).
* `plan`: If enabled and `edit` enabled, a "magnifying glass" button will be displayed\
  on time slots to plan unassigned records into that time slot.

`offset`\
: Depending on the scale, the number of units to add to today to compute the\
default period. Examples: An offset of +1 in default\_scale week will open the\
gantt view for next week, and an offset of -2 in default\_scale month will open\
the gantt view of 2 months ago.

`progress`\
: name of a field providing the completion percentage for the record's event,\
between 0 and 100

`string`\
: title of the gantt view

`precision`\
: JSON object specifying snapping precisions for the pills in each scale.\
Possible values for scale `day` are (default: `hour`):\


* `hour`: records times snap to full hours (ex: 7:12 becomes 8:00)
* `hour:half`: records times snap to half hours (ex: 7:12 becomes 7:30)
* `hour:quarter`: records times snap to half hours (ex: 7:12 becomes 7:15)\


Possible values for scale `week` are (default: `day:half`):\


`templates`
: defines the [QWeb Templates](../frontend/qweb.md#reference-qweb) template `gantt-popover` which is used
  when the user hovers over one of the records in the gantt view.
  <br/>
  The gantt view uses mostly-standard [javascript qweb](../frontend/qweb.md#reference-qweb-javascript) and provides the following context variables:
  <br/>
  `widget`
  : the current `GanttRow()`, can be used to fetch some
    meta-information. The `getColor` method to convert in a color integer is
    also available directly in the template context without using `widget`.
  <br/>
  `on_create`
  : If specified when clicking the add button on the view, instead of opening a generic dialog, launch a client action.
    this should hold the xmlid of the action (eg: `on_create="%(my_module.my_wizard)d"`


Possible values for scale `month` are (default: `day:half`):\


* `day`: records times snap to full days (ex: 7:28 AM becomes 11:59:59 PM of the previous day, 10:32 PM becomes 12:00 PM of the current day)
* `day:half`: records times snap to half hours (ex: 7:28 AM becomes 12:00 PM)\


Scale `year` always snap to full day.\
Example of precision attribute: `{"day": "hour:quarter", "week": "day:half", "month": "day"}`

`total_row`\
: boolean to control whether the row containing the total count of records should\
be displayed. (default: `false`)

`collapse_first_level`\
: boolean to control whether it is possible to collapse each row if grouped by\
one field. (default: `false`, the collapse starts when grouping by two fields)

`display_unavailability`\
: boolean to mark the dates returned by the `gantt_unavailability` function of\
the model as available inside the gantt view. Records can still be scheduled\
in them, but their unavailability is visually displayed. (default: `false`)

`default_scale`\
: default scale when rendering the view. Possible values are (default: `month`):\


* `day`
* `week`
* `month`
* `year`

`scales`\
: comma-separated list of allowed scales for this view. By default, all scales\
are allowed. For possible scale values to use in this list, see `default_scale`.

`templates`\
: defines the [QWeb Templates](developer/reference/frontend/qweb.md#reference-qweb) template `gantt-popover` which is used\
when the user hovers over one of the records in the gantt view.\
The gantt view uses mostly-standard [javascript qweb](developer/reference/frontend/qweb.md#reference-qweb-javascript) and provides the following context variables:\
`widget`\
: the current `GanttRow()`, can be used to fetch some\
meta-information. The `getColor` method to convert in a color integer is\
also available directly in the template context without using `widget`.\
`on_create`\
: If specified when clicking the add button on the view, instead of opening a generic dialog, launch a client action.\
this should hold the xmlid of the action (eg: `on_create="%(my_module.my_wizard)d"`

`form_view_id`\
: view to open when the user create or edit a record. Note that if this attribute\
is not set, the gantt view will fall back to the id of the form view in the\
current action, if any.

`dynamic_range`\
: if set to true, the gantt view will start at the first record,\
instead of starting at the beginning of the year/month/day.

`pill_label`\
: If set to true, the time appears in the pill label when the scale is set on week or month. (e.g.`7:00 AM - 11:00 AM (4h) - DST Task 1`)

`thumbnails`\
: This allows to display a thumbnail next to groups name if the group is a relationnal field.\
This expects a python dict which keys are the name of the field on the active model.\
Values are the names of the field holding the thumbnail on the related model.\
Example: tasks have a field user\_id that reference res.users. The res.users model has a field image that holds the avatar,\
then:\


```xml
<gantt
   date_start="date_start"
   date_stop="date_stop"
   thumbnails="{'user_id': 'image_128'}"
 >
 </gantt>
```

\
will display the users avatars next to their names when grouped by user\_id.

### odoo.addons.base.models.ir\_ui\_view.sample

Whether the view should be populated with a set of sample records if none are found for the\
current model.

These fake records have heuristics for certain field names/models. For example, a field`display_name` on the model `res.users` will be populated with sample people names, while an`email` field will be in the form `firstname.lastname@sample.demo`.

The user is unable to interact with these data, and they will be discarded as soon as an action\
is performed (record created, column added, etc.).

* **Requirement:**\
  Optional
* **Type:**[bool](https://docs.python.org/3/library/functions.html#bool)
* **Default:**`False`

## Map

Enterprise feature

This view is able to display records on a map and the routes between them. The records are represented by pins. It also allows the visualization of fields from the model in a popup tied to the record's pin.

#### NOTE

The model on which the view is applied should contain a `res.partner` many2one since the view relies on the `res.partner`'s address and coordinates fields to localize the records.

### API

The view uses location data platforms' API to fetch the tiles (the map's background), do the geoforwarding (converting addresses to a set of coordinates) and fetch the routes.\
The view implements two API, OpenStreetMap and MapBox. OpenStreetMap is used by default and is able to fetch [tiles](https://wiki.openstreetmap.org/wiki/Tile_data_server) and do [geoforwarding](https://nominatim.org/release-docs/develop/). This API does not require a token.\
As soon as a valid [MapBox](https://docs.mapbox.com/api/) token is provided in the general settings the view switches to the MapBox API. This API is faster and allows the computation of routes. A token can be obtained by [signing up](https://account.mapbox.com/auth/signup/) to MapBox.

### Structural components

The view's root element is `<map>`. It can have the following attributes:

`res_partner`\
: Contains the `res.partner` many2one. If not provided the view resorts to create an empty map.

`default_order`\
: If a field is provided the view overrides the model's default order. The field must be part of the model on which the view is applied, not from `res.partner`.

`routing`\
: if `1` display the routes between the records. The view needs a valid MapBox token and at least two located records (i.e the records have a `res.partner` many2one and the partner has an address or valid coordinates).

`hide_name`\
: if `1` hide the name from the pin's popup (default: `0`).

`hide_address`\
: if `1` hide the address from the pin's popup (default: `0`).

`hide_title`\
: if `1` hide the title from the pin list (default: `0`).

`panel_title`\
: String to display as title of the pin list. If not provided, the title is the action's name or "Items" if the view is not in an action.

`limit`\
: Maximum number of records to fetch (default: `80`). It must be a positive integer.

The `<map>` element can contain multiple `<field>` elements. Each `<field>` element is interpreted as a line in the pin's popup. The field's attributes are the following:

`name`\
: The field to display.

`string`\
: String to display before the field's content. It can be used as a description.

For example here is a map:\
: \`\`\`xml

```
```
