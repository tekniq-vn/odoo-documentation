<a id="howto-base"></a>

<a id="howto-module"></a>

# Building a Module

#### WARNING
This tutorial requires [having installed Odoo](../../administration/on_premise/)

## Start/Stop the Odoo server

Odoo uses a client/server architecture in which clients are web browsers
accessing the Odoo server via RPC.

Business logic and extension is generally performed on the server side,
although supporting client features (e.g. new data representation such as
interactive maps) can be added to the client.

In order to start the server, simply invoke the command [odoo-bin](../reference/cli.md#reference-cmdline) in the shell, adding the full path to the file if
necessary:

```bash
odoo-bin
```

The server is stopped by hitting `Ctrl-C` twice from the terminal, or by
killing the corresponding OS process.

## Build an Odoo module

Both server and client extensions are packaged as *modules* which are
optionally loaded in a *database*.

Odoo modules can either add brand new business logic to an Odoo system, or
alter and extend existing business logic: a module can be created to add your
country's accounting rules to Odoo's generic accounting support, while the
next module adds support for real-time visualisation of a bus fleet.

Everything in Odoo thus starts and ends with modules.

### Composition of a module

An Odoo module can contain a number of elements:

Business objects
: Declared as Python classes, these resources are automatically persisted
  by Odoo based on their configuration

[Object views](../reference/user_interface/view_architectures.md)
: Definition of business objects UI display

[Data files](../reference/backend/data.md#reference-data)
: XML or CSV files declaring the model metadata :
  <br/>
  * [views](../reference/user_interface/view_architectures.md) or [reports](../reference/backend/reports.md#reference-reports),
  * configuration data (modules parametrization, [security rules](../reference/backend/security.md#reference-security)),
  * demonstration data
  * and more

[Web controllers](../reference/backend/http.md#reference-controllers)
: Handle requests from web browsers

Static web data
: Images, CSS or javascript files used by the web interface or website

### Module structure

Each module is a directory within a *module directory*. Module directories
are specified by using the [`--addons-path`](../reference/cli.md#cmdoption-odoo-bin-addons-path)
option.

An Odoo module is declared by its [manifest](../reference/backend/module.md#reference-module-manifest).

A module is also a
[Python package](http://docs.python.org/2/tutorial/modules.html#packages)
with a `__init__.py` file, containing import instructions for various Python
files in the module.

For instance, if the module has a single `mymodule.py` file `__init__.py`
might contain:

```default
from . import mymodule
```

Odoo provides a mechanism to help set up a new module, [odoo-bin](../reference/cli.md#reference-cmdline-server) has a subcommand [scaffold](../reference/cli.md#reference-cmdline-scaffold) to create an empty module:

```console
$ odoo-bin scaffold <module name> <where to put it>
```

The command creates a subdirectory for your module, and automatically creates a
bunch of standard files for a module. Most of them simply contain commented code
or XML. The usage of most of those files will be explained along this tutorial.

### Object-Relational Mapping

A key component of Odoo is the  layer.
This layer avoids having to write most 
by hand and provides extensibility and security services<sup>[2](#rawsql)</sup>.

Business objects are declared as Python classes extending
`Model` which integrates them into the automated
persistence system.

Models can be configured by setting a number of attributes at their
definition. The most important attribute is
`_name` which is required and defines the name for
the model in the Odoo system. Here is a minimally complete definition of a
model:

```default
from odoo import models
class MinimalModel(models.Model):
    _name = 'test.model'
```

### Model fields

Fields are used to define what the model can store and where. Fields are
defined as attributes on the model class:

```default
from odoo import models, fields

class LessMinimalModel(models.Model):
    _name = 'test.model2'

    name = fields.Char()
```

#### Common Attributes

Much like the model itself, its fields can be configured, by passing
configuration attributes as parameters:

```default
name = fields.Char(required=True)
```

Some attributes are available on all fields, here are the most common ones:

`string` (`unicode`, default: field's name)
: The label of the field in UI (visible by users).

`required` (`bool`, default: `False`)
: If `True`, the field can not be empty, it must either have a default
  value or always be given a value when creating a record.

`help` (`unicode`, default: `''`)
: Long-form, provides a help tooltip to users in the UI.

`index` (`bool`, default: `False`)
: Requests that Odoo create a [database index](https://use-the-index-luke.com/sql/preface) on the column.

#### Simple fields

There are two broad categories of fields: "simple" fields which are atomic
values stored directly in the model's table and "relational" fields linking
records (of the same model or of different models).

Example of simple fields are `Boolean`,
`Date`, `Char`.

#### Reserved fields

Odoo creates a few fields in all models<sup>[1](#autofields)</sup>. These fields are
managed by the system and shouldn't be written to. They can be read if
useful or necessary:

`id` (`Id`)
: The unique identifier for a record in its model.

`create_date` (`Datetime`)
: Creation date of the record.

`create_uid` (`Many2one`)
: User who created the record.

`write_date` (`Datetime`)
: Last modification date of the record.

`write_uid` (`Many2one`)
: user who last modified the record.

#### Special fields

By default, Odoo also requires a `name` field on all models for various
display and search behaviors. The field used for these purposes can be
overridden by setting `_rec_name`.

### Data files

Odoo is a highly data driven system. Although behavior is customized using
[Python](https://python.org) code part of a module's value is in the data it sets up when loaded.

Module data is declared via [data files](../reference/backend/data.md#reference-data), XML files with
`<record>` elements. Each `<record>` element creates or updates a database
record.

```xml
<odoo>

        <record model="{model name}" id="{record identifier}">
            <field name="{a field name}">{a value}</field>
        </record>

</odoo>
```

* `model` is the name of the Odoo model for the record.
* `id` is an [external identifier](../glossary.md#term-external-identifier), it allows referring to the record
  (without having to know its in-database identifier).
* `<field>` elements have a `name` which is the name of the field in the
  model (e.g. `description`). Their body is the field's value.

Data files have to be declared in the manifest file to be loaded, they can
be declared in the `'data'` list (always loaded) or in the `'demo'` list
(only loaded in demonstration mode).

<a id="howtos-module-actions"></a>

### Actions and Menus

Actions and menus are regular records in database, usually declared through
data files. Actions can be triggered in three ways:

1. by clicking on menu items (linked to specific actions)
2. by clicking on buttons in views (if these are connected to actions)
3. as contextual actions on object

Because menus are somewhat complex to declare there is a `<menuitem>`
shortcut to declare an `ir.ui.menu` and connect it to the corresponding
action more easily.

```xml
<record model="ir.actions.act_window" id="action_list_ideas">
    <field name="name">Ideas</field>
    <field name="res_model">idea.idea</field>
    <field name="view_mode">tree,form</field>
</record>
<menuitem id="menu_ideas" parent="menu_root" name="Ideas" sequence="10"
          action="action_list_ideas"/>
```

## Basic views

Views define the way the records of a model are displayed. Each type of view
represents a mode of visualization (a list of records, a graph of their
aggregation, …). Views can either be requested generically via their type
(e.g. *a list of partners*) or specifically via their id. For generic
requests, the view with the correct type and the lowest priority will be
used (so the lowest-priority view of each type is the default view for that
type).

[View inheritance](../reference/user_interface/view_records.md#reference-view-records-inheritance) allows altering views
declared elsewhere (adding or removing content).

### Generic view declaration

A view is declared as a record of the model `ir.ui.view`. The view type
is implied by the root element of the `arch` field:

```xml
<record model="ir.ui.view" id="view_id">
    <field name="name">view.name</field>
    <field name="model">object_name</field>
    <field name="priority" eval="16"/>
    <field name="arch" type="xml">
        <!-- view content: <form>, <tree>, <graph>, ... -->
    </field>
</record>
```

### Tree views

Tree views, also called list views, display records in a tabular form.

Their root element is `<tree>`. The simplest form of the tree view simply
lists all the fields to display in the table (each field as a column):

```xml
<tree string="Idea list">
    <field name="name"/>
    <field name="inventor_id"/>
</tree>
```

<a id="howtos-module-views-form"></a>

### Form views

Forms are used to create and edit single records.

Their root element is `<form>`. They are composed of high-level structure
elements (groups, notebooks) and interactive elements (buttons and fields):

```xml
<form string="Idea form">
    <group colspan="4">
        <group colspan="2" col="2">
            <separator string="General stuff" colspan="2"/>
            <field name="name"/>
            <field name="inventor_id"/>
        </group>

        <group colspan="2" col="2">
            <separator string="Dates" colspan="2"/>
            <field name="active"/>
            <field name="invent_date" readonly="1"/>
        </group>

        <notebook colspan="4">
            <page string="Description">
                <field name="description" nolabel="1"/>
            </page>
        </notebook>

        <field name="state"/>
    </group>
</form>
```

Form views can also use plain HTML for more flexible layouts:

```xml
<form string="Idea Form">
    <header>
        <button string="Confirm" type="object" name="action_confirm"
                invisible="state != 'draft'" class="oe_highlight" />
        <button string="Mark as done" type="object" name="action_done"
                invisible="state != 'confirmed'" class="oe_highlight"/>
        <button string="Reset to draft" type="object" name="action_draft"
                invisible="state not in ['confirmed', 'done']" />
        <field name="state" widget="statusbar"/>
    </header>
    <sheet>
        <div class="oe_title">
            <label for="name" class="oe_edit_only" string="Idea Name" />
            <h1><field name="name" /></h1>
        </div>
        <separator string="General" colspan="2" />
        <group colspan="2" col="2">
            <field name="description" placeholder="Idea description..." />
        </group>
    </sheet>
</form>
```

### Search views

Search views customize the search field associated with the list view (and
other aggregated views). Their root element is `<search>` and they're
composed of fields defining which fields can be searched on:

```xml
<search>
    <field name="name"/>
    <field name="inventor_id"/>
</search>
```

If no search view exists for the model, Odoo generates one which only allows
searching on the `name` field.

## Relations between models

A record from a model may be related to a record from another model. For
instance, a sale order record is related to a client record that contains the
client data; it is also related to its sale order line records.

### Relational fields

Relational fields link records, either of the same model (hierarchies) or
between different models.

Relational field types are:

`Many2one(other_model, ondelete='set null')`
: A simple link to an other object:
  <br/>
  ```default
  print(foo.other_id.name)
  ```
  <br/>
  #### SEE ALSO
  [foreign keys](http://www.postgresql.org/docs/12/static/tutorial-fk.html)

`One2many(other_model, related_field)`
: A virtual relationship, inverse of a `Many2one`.
  A `One2many` behaves as a container of records,
  accessing it results in a (possibly empty) set of records:
  <br/>
  ```default
  for other in foo.other_ids:
      print(other.name)
  ```

`Many2many(other_model)`
: Bidirectional multiple relationship, any record on one side can be related
  to any number of records on the other side. Behaves as a container of
  records, accessing it also results in a possibly empty set of records:
  <br/>
  ```default
  for other in foo.other_ids:
      print(other.name)
  ```

## Inheritance

### Model inheritance

Odoo provides two *inheritance* mechanisms to extend an existing model in a
modular way.

The first inheritance mechanism allows a module to modify the behavior of a
model defined in another module:

- add fields to a model,
- override the definition of fields on a model,
- add constraints to a model,
- add methods to a model,
- override existing methods on a model.

The second inheritance mechanism (delegation) allows to link every record of a
model to a record in a parent model, and provides transparent access to the
fields of the parent record.

![image](../../.gitbook/assets/inheritance_methods.png)

#### SEE ALSO
* `_inherit`
* `_inherits`

### View inheritance

Instead of modifying existing views in place (by overwriting them), Odoo
provides view inheritance where children "extension" views are applied on top of
root views, and can add or remove content from their parent.

An extension view references its parent using the `inherit_id` field, and
instead of a single view its `arch` field is composed of any number of
`xpath` elements selecting and altering the content of their parent view:

```xml
<!-- improved idea categories list -->
<record id="idea_category_list2" model="ir.ui.view">
    <field name="name">id.category.list2</field>
    <field name="model">idea.category</field>
    <field name="inherit_id" ref="id_category_list"/>
    <field name="arch" type="xml">
        <!-- find field description and add the field
             idea_ids after it -->
        <xpath expr="//field[@name='description']" position="after">
          <field name="idea_ids" string="Number of ideas"/>
        </xpath>
    </field>
</record>
```

`expr`
: An [XPath](https://w3.org/TR/xpath) expression selecting a single element in the parent view.
  Raises an error if it matches no element or more than one

`position`
: Operation to apply to the matched element:
  <br/>
  `inside`
  : appends `xpath`'s body at the end of the matched element
  <br/>
  `replace`
  : replaces the matched element with the `xpath`'s body, replacing any `$0` node occurrence
    in the new body with the original element
  <br/>
  `before`
  : inserts the `xpath`'s body as a sibling before the matched element
  <br/>
  `after`
  : inserts the `xpaths`'s body as a sibling after the matched element
  <br/>
  `attributes`
  : alters the attributes of the matched element using special
    `attribute` elements in the `xpath`'s body

#### Domains

In Odoo, [Search domains](../reference/backend/orm/#reference-orm-domains) are values that encode conditions on
records. A domain is a  list of criteria used to select a subset of a model's
records. Each criteria is a triple with a field name, an operator and a value.

For instance, when used on the *Product* model the following domain selects
all *services* with a unit price over *1000*:

```default
[('product_type', '=', 'service'), ('unit_price', '>', 1000)]
```

By default criteria are combined with an implicit AND. The logical operators
`&` (AND), `|` (OR) and `!` (NOT) can be used to explicitly combine
criteria. They are used in prefix position (the operator is inserted before
its arguments rather than between). For instance to select products "which are
services *OR* have a unit price which is *NOT* between 1000 and 2000":

```default
['|',
    ('product_type', '=', 'service'),
    '!', '&',
        ('unit_price', '>=', 1000),
        ('unit_price', '<', 2000)]
```

A `domain` parameter can be added to relational fields to limit valid
records for the relation when trying to select records in the client interface.

## Computed fields and default values

So far fields have been stored directly in and retrieved directly from the
database. Fields can also be *computed*. In that case, the field's value is not
retrieved from the database but computed on-the-fly by calling a method of the
model.

To create a computed field, create a field and set its attribute
`compute` to the name of a method. The computation
method should simply set the value of the field to compute on every record in
`self`.

```python
import random
from odoo import models, fields, api

class ComputedModel(models.Model):
    _name = 'test.computed'

    name = fields.Char(compute='_compute_name')

    def _compute_name(self):
        for record in self:
            record.name = str(random.randint(1, 1e6))
```

### Dependencies

The value of a computed field usually depends on the values of other fields on
the computed record. The ORM expects the developer to specify those dependencies
on the compute method with the decorator `depends()`.
The given dependencies are used by the ORM to trigger the recomputation of the
field whenever some of its dependencies have been modified:

```default
from odoo import models, fields, api

class ComputedModel(models.Model):
    _name = 'test.computed'

    name = fields.Char(compute='_compute_name')
    value = fields.Integer()

    @api.depends('value')
    def _compute_name(self):
        for record in self:
            record.name = "Record with value %s" % record.value
```

### Default values

Any field can be given a default value. In the field definition, add the option
`default=X` where `X` is either a Python literal value (boolean, integer,
float, string), or a function taking a recordset and returning a value:

```default
name = fields.Char(default="Unknown")
user_id = fields.Many2one('res.users', default=lambda self: self.env.user)
```

#### NOTE
The object `self.env` gives access to request parameters and other useful things:

> - `self.env.cr` or `self._cr` is the database *cursor* object; it is
>   used for querying the database
> - `self.env.uid` or `self._uid` is the current user's database id
> - `self.env.user` is the current user's record
> - `self.env.context` or `self._context` is the context dictionary
> - `self.env.ref(xml_id)` returns the record corresponding to an XML id
> - `self.env[model_name]` returns an instance of the given model

## Onchange

The "onchange" mechanism provides a way for the client interface to update a
form whenever the user has filled in a value in a field, without saving anything
to the database.

For instance, suppose a model has three fields `amount`, `unit_price` and
`price`, and you want to update the price on the form when any of the other
fields is modified. To achieve this, define a method where `self` represents
the record in the form view, and decorate it with `onchange()`
to specify on which field it has to be triggered. Any change you make on
`self` will be reflected on the form.

```xml
<!-- content of form view -->
<field name="amount"/>
<field name="unit_price"/>
<field name="price" readonly="1"/>
```

```python
# onchange handler
@api.onchange('amount', 'unit_price')
def _onchange_price(self):
    # set auto-changing field
    self.price = self.amount * self.unit_price
    # Can optionally return a warning and domains
    return {
        'warning': {
            'title': "Something bad happened",
            'message': "It was very bad indeed",
        }
    }
```

For computed fields, valued `onchange` behavior is built-in as can be seen by
playing with the *Session* form: change the number of seats or participants, and
the `taken_seats` progressbar is automatically updated.

## Model constraints

Odoo provides two ways to set up automatically verified invariants:
`Python constraints` and
`SQL constraints`.

A Python constraint is defined as a method decorated with
`constrains()`, and invoked on a recordset. The decorator
specifies which fields are involved in the constraint, so that the constraint is
automatically evaluated when one of them is modified. The method is expected to
raise an exception if its invariant is not satisfied:

```default
from odoo.exceptions import ValidationError

@api.constrains('age')
def _check_something(self):
    for record in self:
        if record.age > 20:
            raise ValidationError("Your record is too old: %s" % record.age)
    # all records passed the test, don't return anything
```

SQL constraints are defined through the model attribute
`_sql_constraints`. The latter is assigned to a list
of triples of strings `(name, sql_definition, message)`, where `name` is a
valid SQL constraint name, `sql_definition` is a [table_constraint](https://www.postgresql.org/docs/12/static/ddl-constraints.html) expression,
and `message` is the error message.

## Advanced Views

### Tree views

Tree views can take supplementary attributes to further customize their
behavior:

`decoration-{$name}`
: allow changing the style of a row's text based on the corresponding
  record's attributes.
  <br/>
  Values are Python expressions. For each record, the expression is evaluated
  with the record's attributes as context values and if `true`, the
  corresponding style is applied to the row. Here are some of the other values
  available in the context:
  <br/>
  * `uid`: the id of the current user,
  * `today`: the current local date as a string of the form `YYYY-MM-DD`,
  * `now`: same as `today` with the addition of the current time.
    This value is formatted as `YYYY-MM-DD hh:mm:ss`.
  <br/>
  `{$name}` can be `bf` (`font-weight: bold`), `it`
  (`font-style: italic`), or any [bootstrap contextual color](https://getbootstrap.com/docs/3.3/components/#available-variations) (`danger`,
  `info`, `muted`, `primary`, `success` or `warning`).
  <br/>
  ```xml
  <tree string="Idea Categories" decoration-info="state=='draft'"
      decoration-danger="state=='trashed'">
      <field name="name"/>
      <field name="state"/>
  </tree>
  ```

`editable`
: Either `"top"` or `"bottom"`. Makes the tree view editable in-place
  (rather than having to go through the form view), the value is the
  position where new rows appear.

### Calendars

Displays records as calendar events. Their root element is `<calendar>` and
their most common attributes are:

`color`
: The name of the field used for *color segmentation*. Colors are
  automatically distributed to events, but events in the same color segment
  (records which have the same value for their `@color` field) will be
  given the same color.

`date_start`
: record's field holding the start date/time for the event

`date_stop` (optional)
: record's field holding the end date/time for the event

`string`
: record's field to define the label for each calendar event

```xml
<calendar string="Ideas" date_start="invent_date" color="inventor_id">
    <field name="name"/>
</calendar>
```

### Search views

Search view `<field>` elements can have a `@filter_domain` that overrides
the domain generated for searching on the given field. In the given domain,
`self` represents the value entered by the user. In the example below, it is
used to search on both fields `name` and `description`.

Search views can also contain `<filter>` elements, which act as toggles for
predefined searches. Filters must have one of the following attributes:

`domain`
: add the given domain to the current search

`context`
: add some context to the current search; use the key `group_by` to group
  results on the given field name

```xml
<search string="Ideas">
    <field name="name"/>
    <field name="description" string="Name and description"
           filter_domain="['|', ('name', 'ilike', self), ('description', 'ilike', self)]"/>
    <field name="inventor_id"/>
    <field name="country_id" widget="selection"/>

    <filter name="my_ideas" string="My Ideas"
            domain="[('inventor_id', '=', uid)]"/>
    <group string="Group By">
        <filter name="group_by_inventor" string="Inventor"
                context="{'group_by': 'inventor_id'}"/>
    </group>
</search>
```

To use a non-default search view in an action, it should be linked using the
`search_view_id` field of the action record.

The action can also set default values for search fields through its
`context` field: context keys of the form
`search_default_*field_name*` will initialize *field_name* with the
provided value. Search filters must have an optional `@name` to have a
default and behave as booleans (they can only be enabled by default).

### Gantt

#### WARNING
The gantt view requires the web_gantt module which is present in the [enterprise edition](../../administration/#install-editions) version.

Horizontal bar charts typically used to show project planning and advancement,
their root element is `<gantt>`.

```xml
<gantt string="Ideas"
       date_start="invent_date"
       date_stop="date_finished"
       progress="progress"
       default_group_by="inventor_id" />
```

### Graph views

Graph views allow aggregated overview and analysis of models, their root
element is `<graph>`.

#### NOTE
Pivot views (element `<pivot>`) a multidimensional table, allows the selection of filers and
dimensions to get the right aggregated dataset before moving to a more graphical overview. The
pivot view shares the same content definition as graph views.

Graph views have 4 display modes, the default mode is selected using the
`@type` attribute.

Bar (default)
: a bar chart, the first dimension is used to define groups on the
  horizontal axis, other dimensions define aggregated bars within each group.
  <br/>
  By default bars are side-by-side, they can be stacked by using
  `@stacked="True"` on the `<graph>`

Line
: 2-dimensional line chart

Pie
: 2-dimensional pie

Graph views contain `<field>` with a mandatory `@type` attribute taking
the values:

`row` (default)
: the field should be aggregated by default

`measure`
: the field should be aggregated rather than grouped on

```xml
<graph string="Total idea score by Inventor">
    <field name="inventor_id"/>
    <field name="score" type="measure"/>
</graph>
```

#### WARNING
Graph views perform aggregations on database values, they do not work with non-stored computed
fields.

### Kanban

Used to organize tasks, production processes, etc… their root element is
`<kanban>`.

A kanban view shows a set of cards possibly grouped in columns. Each card
represents a record, and each column the values of an aggregation field.

For instance, project tasks may be organized by stage (each column is a
stage), or by responsible (each column is a user), and so on.

Kanban views define the structure of each card as a mix of form elements
(including basic HTML) and [QWeb Templates](../reference/frontend/qweb.md#reference-qweb).

## Security

Access control mechanisms must be configured to achieve a coherent security
policy.

### Group-based access control mechanisms

Groups are created as normal records on the model `res.groups`, and granted
menu access via menu definitions. However even without a menu, objects may
still be accessible indirectly, so actual object-level permissions (read,
write, create, unlink) must be defined for groups. They are usually inserted
via CSV files inside modules. It is also possible to restrict access to
specific fields on a view or object using the field's groups attribute.

### Access rights

Access rights are defined as records of the model `ir.model.access`. Each
access right is associated to a model, a group (or no group for global
access), and a set of permissions: read, write, create, unlink. Such access
rights are usually created by a CSV file named after its model:
`ir.model.access.csv`.

```text
id,name,model_id/id,group_id/id,perm_read,perm_write,perm_create,perm_unlink
access_idea_idea,idea.idea,model_idea_idea,base.group_user,1,1,1,0
access_idea_vote,idea.vote,model_idea_vote,base.group_user,1,1,1,0
```

### Record rules

A record rule restricts the access rights to a subset of records of the given
model. A rule is a record of the model `ir.rule`, and is associated to a
model, a number of groups (many2many field), permissions to which the
restriction applies, and a domain. The domain specifies to which records the
access rights are limited.

Here is an example of a rule that prevents the deletion of leads that are not
in state `cancel`. Notice that the value of the field `groups` must follow
the same convention as the method `write()` of the ORM.

```xml
<record id="delete_cancelled_only" model="ir.rule">
    <field name="name">Only cancelled leads may be deleted</field>
    <field name="model_id" ref="crm.model_crm_lead"/>
    <field name="groups" eval="[(4, ref('sales_team.group_sale_manager'))]"/>
    <field name="perm_read" eval="0"/>
    <field name="perm_write" eval="0"/>
    <field name="perm_create" eval="0"/>
    <field name="perm_unlink" eval="1" />
    <field name="domain_force">[('state','=','cancel')]</field>
</record>
```

<a id="howto-module-wizard"></a>

## Wizards

Wizards describe interactive sessions with the user (or dialog boxes) through
dynamic forms. A wizard is simply a model that extends the class
`TransientModel` instead of
`Model`. The class
`TransientModel` extends `Model`
and reuse all its existing mechanisms, with the following particularities:

- Wizard records are not meant to be persistent; they are automatically deleted
  from the database after a certain time. This is why they are called
  *transient*.
- Wizard records may refer to regular records or wizard records through relational
  fields(many2one or many2many), but regular records *cannot* refer to wizard records through a
  many2one field.

We want to create a wizard that allow users to create attendees for a particular
session, or for a list of sessions at once.

### Launching wizards

Wizards are simply [window actions](#howtos-module-actions) with a `target`
field set to the value `new`, which opens the view
(usually [a form](#howtos-module-views-form)) in a separate dialog. The
action may be triggered via a menu item, but is more generally triggered by a
button.

An other way to launch wizards is through the Action menu of
a tree or form view. This is done through the `binding_model_id` field of the
action. Setting this field will make the action appear on the views of the model
the action is "bound" to.

```xml
<record id="launch_the_wizard" model="ir.actions.act_window">
    <field name="name">Launch the Wizard</field>
    <field name="res_model">wizard.model.name</field>
    <field name="view_mode">form</field>
    <field name="target">new</field>
    <field name="binding_model_id" ref="model_context_model_ref"/>
</record>
```

## Internationalization

Each module can provide its own translations within the i18n directory, by
having files named LANG.po where LANG is the locale code for the language, or
the language and country combination when they differ (e.g. pt.po or
pt_BR.po). Translations will be loaded automatically by Odoo for all
enabled languages. Developers always use English when creating a module, then
export the module terms using Odoo's gettext POT export feature
(Settings ‣ Translations ‣ Import/Export ‣ Export
Translation without specifying a language), to create the module template POT
file, and then derive the translated PO files. Many IDE's have plugins or modes
for editing and merging PO/POT files.

```text
|- idea/ # The module directory
   |- i18n/ # Translation files
      | - idea.pot # Translation Template (exported from Odoo)
      | - fr.po # French translation
      | - pt_BR.po # Brazilian Portuguese translation
      | (...)
```

## Reporting

### Printed reports

Odoo uses a report engine based on [QWeb Templates](../reference/frontend/qweb.md#reference-qweb),
[Twitter Bootstrap](https://getbootstrap.com) and [Wkhtmltopdf](https://wkhtmltopdf.org).

A report is a combination two elements:

* an `ir.actions.report` which configures various basic parameters for the
  report (default type, whether the report should be saved to the database
  after generation,…)
  ```xml
  <record id="account_invoices" model="ir.actions.report">
      <field name="name">Invoices</field>
      <field name="model">account.invoice</field>
      <field name="report_type">qweb-pdf</field>
      <field name="report_name">account.report_invoice</field>
      <field name="report_file">account.report_invoice</field>
      <field name="attachment_use" eval="True"/>
      <field name="attachment">(object.state in ('open','paid')) and
          ('INV'+(object.number or '').replace('/','')+'.pdf')</field>
      <field name="binding_model_id" ref="model_account_invoice"/>
      <field name="binding_type">report</field>
  </record>
  ```
* A standard [QWeb view](../reference/user_interface/view_architectures.md#reference-view-architectures-qweb) for the actual report:
  ```xml
  <t t-call="web.html_container">
      <t t-foreach="docs" t-as="o">
          <t t-call="web.external_layout">
              <div class="page">
                  <h2>Report title</h2>
              </div>
          </t>
      </t>
  </t>
  ```

  the standard rendering context provides a number of elements, the most
  important being:

  `docs`
  : the records for which the report is printed

  `user`
  : the user printing the report

Because reports are standard web pages, they are available through a URL and
output parameters can be manipulated through this URL, for instance the HTML
version of the *Invoice* report is available through
[http://localhost:8069/report/html/account.report_invoice/1](http://localhost:8069/report/html/account.report_invoice/1) (if `account` is
installed) and the PDF version through
[http://localhost:8069/report/pdf/account.report_invoice/1](http://localhost:8069/report/pdf/account.report_invoice/1).

<a id="reference-backend-reporting-printed-reports-pdf-without-styles"></a>

### Dashboards

* <a id='autofields'>**[1]**</a> it is possible to [disable the automatic creation of some fields](../reference/backend/orm/#reference-fields-automatic-log-access)
* <a id='rawsql'>**[2]**</a> writing raw SQL queries is possible, but requires care as it bypasses all Odoo authentication and security mechanisms.

<a id="postgresql-s-documentation"></a>
