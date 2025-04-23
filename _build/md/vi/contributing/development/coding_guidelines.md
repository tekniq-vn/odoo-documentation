# Coding guidelines

This page introduces the Odoo Coding Guidelines. Those aim to improve the\
quality of Odoo Apps code. Indeed proper code improves readability, eases\
maintenance, helps debugging, lowers complexity and promotes reliability.\
These guidelines should be applied to every new module and to all new development.

#### WARNING

When modifying existing files in **stable version** the original file style\
strictly supersedes any other style guidelines. In other words please never\
modify existing files in order to apply these guidelines. It avoids disrupting\
the revision history of code lines. Diff should be kept minimal. For more\
details, see our [pull request guide](https://odoo.com/submit-pr).

#### WARNING

When modifying existing files in **master (development) version** apply those\
guidelines to existing code only for modified code or if most of the file is\
under revision. In other words modify existing files structure only if it is\
going under major changes. In that case first do a **move** commit then apply\
the changes related to the feature.

## Module structure

### Directories

A module is organized in important directories. Those contain the business logic;\
having a look at them should make you understand the purpose of the module.

* _data/_ : demo and data xml
* _models/_ : models definition
* _controllers/_ : contains controllers (HTTP routes)
* _views/_ : contains the views and templates
* _static/_ : contains the web assets, separated into _css/, js/, img/, lib/, ..._

Other optional directories compose the module.

* _wizard/_ : regroups the transient models (`models.TransientModel`) and their views
* _report/_ : contains the printable reports and models based on SQL views. Python objects and XML views are included in this directory
* _tests/_ : contains the Python tests

### File naming

File naming is important to quickly find information through all odoo addons.\
This section explains how to name files in a standard odoo module. As an\
example we use a [plant nursery](https://github.com/tivisse/odoodays-2018/tree/master/plant_nursery) application.\
It holds two main models _plant.nursery_ and _plant.order_.

Concerning _models_, split the business logic by sets of models belonging to\
a same main model. Each set lies in a given file named based on its main model.\
If there is only one model, its name is the same as the module name. Each\
inherited model should be in its own file to help understanding of impacted\
models.

```
addons/plant_nursery/
|-- models/
|   |-- plant_nursery.py (first main model)
|   |-- plant_order.py (another main model)
|   |-- res_partner.py (inherited Odoo model)
```

Concerning _security_, three main files should be used:

* First one is the definition of access rights done in a `ir.model.access.csv` file.
* User groups are defined in `<module>_groups.xml`.
* Record rules are defined in `<model>_security.xml`.

```
addons/plant_nursery/
|-- security/
|   |-- ir.model.access.csv
|   |-- plant_nursery_groups.xml
|   |-- plant_nursery_security.xml
|   |-- plant_order_security.xml
```

Concerning _views_, backend views should be split like models and suffixed\
by `_views.xml`. Backend views are list, form, kanban, activity, graph, pivot, ..\
views. To ease split by model in views main menus not linked to specific actions\
may be extracted into an optional `<module>_menus.xml` file. Templates (QWeb\
pages used notably for portal / website display) are put in separate files named`<model>_templates.xml`.

```
addons/plant_nursery/
|-- views/
|   | -- plant_nursery_menus.xml (optional definition of main menus)
|   | -- plant_nursery_views.xml (backend views)
|   | -- plant_nursery_templates.xml (portal templates)
|   | -- plant_order_views.xml
|   | -- plant_order_templates.xml
|   | -- res_partner_views.xml
```

Concerning _data_, split them by purpose (demo or data) and main model. Filenames\
will be the main\_model name suffixed by `_demo.xml` or `_data.xml`. For instance\
for an application having demo and data for its main model as well as subtypes,\
activities and mail templates all related to mail module:

```
addons/plant_nursery/
|-- data/
|   |-- plant_nursery_data.xml
|   |-- plant_nursery_demo.xml
|   |-- mail_data.xml
```

Concerning _controllers_, generally all controllers belong to a single controller\
contained in a file named `<module_name>.py`. An old convention in Odoo is to\
name this file `main.py` but it is considered as outdated. If you need to inherit\
an existing controller from another module do it in `<inherited_module_name>.py`.\
For example adding portal controller in an application is done in `portal.py`.

```
addons/plant_nursery/
|-- controllers/
|   |-- plant_nursery.py
|   |-- portal.py (inheriting portal/controllers/portal.py)
|   |-- main.py (deprecated, replaced by plant_nursery.py)
```

Concerning _static files_, Javascript files follow globally the same logic as\
python models. Each component should be in its own file with a meaningful name.\
For instance, the activity widgets are located in `activity.js` of mail module.\
Subdirectories can also be created to structure the 'package' (see web module\
for more details). The same logic should be applied for the templates of JS\
widgets (static XML files) and for their styles (scss files). Don't link\
data (image, libraries) outside Odoo: do not use an URL to an image but copy\
it in the codebase instead.

Concerning _wizards_, naming convention is the same of for python models:`<transient>.py` and `<transient>_views.xml`. Both are put in the wizard\
directory. This naming comes from old odoo applications using the wizard\
keyword for transient models.

```
addons/plant_nursery/
|-- wizard/
|   |-- make_plant_order.py
|   |-- make_plant_order_views.xml
```

Concerning _statistics reports_ done with python / SQL views and classic views\
naming is the following :

```
addons/plant_nursery/
|-- report/
|   |-- plant_order_report.py
|   |-- plant_order_report_views.xml
```

Concerning _printable reports_ which contain mainly data preparation and Qweb\
templates naming is the following :

```
addons/plant_nursery/
|-- report/
|   |-- plant_order_reports.xml (report actions, paperformat, ...)
|   |-- plant_order_templates.xml (xml report templates)
```

The complete tree of our Odoo module therefore looks like

```
addons/plant_nursery/
|-- __init__.py
|-- __manifest__.py
|-- controllers/
|   |-- __init__.py
|   |-- plant_nursery.py
|   |-- portal.py
|-- data/
|   |-- plant_nursery_data.xml
|   |-- plant_nursery_demo.xml
|   |-- mail_data.xml
|-- models/
|   |-- __init__.py
|   |-- plant_nursery.py
|   |-- plant_order.py
|   |-- res_partner.py
|-- report/
|   |-- __init__.py
|   |-- plant_order_report.py
|   |-- plant_order_report_views.xml
|   |-- plant_order_reports.xml (report actions, paperformat, ...)
|   |-- plant_order_templates.xml (xml report templates)
|-- security/
|   |-- ir.model.access.csv
|   |-- plant_nursery_groups.xml
|   |-- plant_nursery_security.xml
|   |-- plant_order_security.xml
|-- static/
|   |-- img/
|   |   |-- my_little_kitten.png
|   |   |-- troll.jpg
|   |-- lib/
|   |   |-- external_lib/
|   |-- src/
|   |   |-- js/
|   |   |   |-- widget_a.js
|   |   |   |-- widget_b.js
|   |   |-- scss/
|   |   |   |-- widget_a.scss
|   |   |   |-- widget_b.scss
|   |   |-- xml/
|   |   |   |-- widget_a.xml
|   |   |   |-- widget_a.xml
|-- views/
|   |-- plant_nursery_menus.xml
|   |-- plant_nursery_views.xml
|   |-- plant_nursery_templates.xml
|   |-- plant_order_views.xml
|   |-- plant_order_templates.xml
|   |-- res_partner_views.xml
|-- wizard/
|   |--make_plant_order.py
|   |--make_plant_order_views.xml
```

#### NOTE

File names should only contain `[a-z0-9_]` (lowercase\
alphanumerics and `_`)

#### WARNING

Use correct file permissions : folder 755 and file 644.

## XML files

### Format

To declare a record in XML, the **record** notation (using ) is recommended:

* Place `id` attribute before `model`
* For field declaration, `name` attribute is first. Then place th&#x65;_&#x76;alue_ either in the `field` tag, either in the `eval`\
  attribute, and finally other attributes (widget, options, ...)\
  ordered by importance.
* Try to group the record by model. In case of dependencies between\
  action/menu/views, this convention may not be applicable.
* Use naming convention defined at the next point
* The tag is only used to set not-updatable data with `noupdate=1`.\
  If there is only not-updatable data in the file, the `noupdate=1` can be\
  set on the `<odoo>` tag and do not set a `<data>` tag.

```xml
<record id="view_id" model="ir.ui.view">
    <field name="name">view.name</field>
    <field name="model">object_name</field>
    <field name="priority" eval="16"/>
    <field name="arch" type="xml">
        <tree>
            <field name="my_field_1"/>
            <field name="my_field_2" string="My Label" widget="statusbar" statusbar_visible="draft,sent,progress,done" />
        </tree>
    </field>
</record>
```

Odoo supports custom tags acting as syntactic sugar:

* menuitem: use it as a shortcut to declare a `ir.ui.menu`
* template: use it to declare a QWeb View requiring only the `arch` section of the view.

These tags are preferred over the _record_ notation.

### XML IDs and naming

#### Security, View and Action

Use the following pattern :

* For a menu: `*<model_name>*_menu`, or `*<model_name>*_menu_*do_stuff*` for submenus.
* For a view: `*<model_name>*_view_ *<view_type>*`, where _view\_type_ is`kanban`, `form`, `tree`, `search`, ...
* For an action: the main action respects `*<model_name>*_action`.\
  Others are suffixed with `_ *<detail>*`, where _detail_ is a\
  lowercase string briefly explaining the action. This is used only if\
  multiple actions are declared for the model.
* For window actions: suffix the action name by the specific view information\
  like `*<model_name>*_action_view_ *<view_type>*`.
* For a group: `*<module_name>*_group_ *<group_name>*` where _group\_name_\
  is the name of the group, generally 'user', 'manager', ...
* For a rule: `*<model_name>*_rule_ *<concerned_group>*` wher&#x65;_&#x63;oncerned\_group_ is the short name of the concerned group ('user'\
  for the 'model\_name\_group\_user', 'public' for public user, 'company'\
  for multi-company rules, ...).

Name should be identical to xml id with dots replacing underscores. Actions\
should have a real naming as it is used as display name.

```xml
<!-- views  -->
<record id="model_name_view_form" model="ir.ui.view">
    <field name="name">model.name.view.form</field>
    ...
</record>

<record id="model_name_view_kanban" model="ir.ui.view">
    <field name="name">model.name.view.kanban</field>
    ...
</record>

<!-- actions -->
<record id="model_name_action" model="ir.act.window">
    <field name="name">Model Main Action</field>
    ...
</record>

<record id="model_name_action_child_list" model="ir.actions.act_window">
    <field name="name">Model Access Children</field>
</record>

<!-- menus and sub-menus -->
<menuitem
    id="model_name_menu_root"
    name="Main Menu"
    sequence="5"
/>
<menuitem
    id="model_name_menu_action"
    name="Sub Menu 1"
    parent="module_name.module_name_menu_root"
    action="model_name_action"
    sequence="10"
/>

<!-- security -->
<record id="module_name_group_user" model="res.groups">
    ...
</record>

<record id="model_name_rule_public" model="ir.rule">
    ...
</record>

<record id="model_name_rule_company" model="ir.rule">
    ...
</record>
```

#### Inheriting XML

Xml Ids of inheriting views should use the same ID as the original record.\
It helps finding all inheritance at a glance. As final Xml Ids are prefixed\
by the module that creates them there is no overlap.

Naming should contain an `.inherit.{details}` suffix to ease understanding\
the override purpose when looking at its name.

```xml
<record id="model_view_form" model="ir.ui.view">
    <field name="name">model.view.form.inherit.module2</field>
    <field name="inherit_id" ref="module1.model_view_form"/>
    ...
</record>
```

New primary views do not require the inherit suffix as those are new records\
based upon the first one.

```xml
<record id="module2.model_view_form" model="ir.ui.view">
    <field name="name">model.view.form.module2</field>
    <field name="inherit_id" ref="module1.model_view_form"/>
    <field name="mode">primary</field>
    ...
</record>
```

## Python

#### WARNING
Do not forget to read the [Security Pitfalls](../../developer/reference/backend/security.md#reference-security-pitfalls)
section as well to write secure code.

### PEP8 options

Using a linter can help show syntax and semantic warnings or errors. Odoo\
source code tries to respect Python standard, but some of them can be ignored.

* E501: line too long
* E301: expected 1 blank line, found 0
* E302: expected 2 blank lines, found 1

### Imports

The imports are ordered as

1. External libraries (one per line sorted and split in python stdlib)
2. Imports of `odoo`
3. Imports from Odoo modules (rarely, and only if necessary)

Inside these 3 groups, the imported lines are alphabetically sorted.

```python
# 1 : imports of python lib
import base64
import re
import time
from datetime import datetime
# 2 : imports of odoo
import odoo
from odoo import Command, _, api, fields, models # ASCIIbetically ordered
from odoo.tools.safe_eval import safe_eval as eval
# 3 : imports from odoo addons
from odoo.addons.web.controllers.main import login_redirect
from odoo.addons.website.models.website import slug
```

### Idiomatics of Programming (Python)

* Always favor _readability_ over _conciseness_ or using the language features or idioms.
* Don't use `.clone()`

```python
# bad
new_dict = my_dict.clone()
new_list = old_list.clone()
# good
new_dict = dict(my_dict)
new_list = list(old_list)
```

* Python dictionary : creation and update

```python
# -- creation empty dict
my_dict = {}
my_dict2 = dict()

# -- creation with values
# bad
my_dict = {}
my_dict['foo'] = 3
my_dict['bar'] = 4
# good
my_dict = {'foo': 3, 'bar': 4}

# -- update dict
# bad
my_dict['foo'] = 3
my_dict['bar'] = 4
my_dict['baz'] = 5
# good
my_dict.update(foo=3, bar=4, baz=5)
my_dict = dict(my_dict, **my_dict2)
```

* Use meaningful variable/class/method names
* Useless variable : Temporary variables can make the code clearer by giving\
  names to objects, but that doesn't mean you should create temporary variables\
  all the time:

```python
# pointless
schema = kw['schema']
params = {'schema': schema}
# simpler
params = {'schema': kw['schema']}
```

* Multiple return points are OK, when they're simpler

```python
# a bit complex and with a redundant temp variable
def axes(self, axis):
    axes = []
    if type(axis) == type([]):
        axes.extend(axis)
    else:
        axes.append(axis)
    return axes

 # clearer
def axes(self, axis):
    if type(axis) == type([]):
        return list(axis) # clone the axis
    else:
        return [axis] # single-element list
```

* Know your builtins : You should at least have a basic understanding of all\
  the Python builtins ([http://docs.python.org/library/functions.html](http://docs.python.org/library/functions.html))

```python
value = my_dict.get('key', None) # very very redundant
value = my_dict.get('key') # good
```

Also, `if 'key' in my_dict` and `if my_dict.get('key')` have very different\
meaning, be sure that you're using the right one.

* Learn list comprehensions : Use list comprehension, dict comprehension, and\
  basic manipulation using `map`, `filter`, `sum`, ... They make the code\
  easier to read.

```python
# not very good
cube = []
for i in res:
    cube.append((i['id'],i['name']))
# better
cube = [(i['id'], i['name']) for i in res]
```

* Collections are booleans too : In python, many objects have "boolean-ish" value\
  when evaluated in a boolean context (such as an if). Among these are collections\
  (lists, dicts, sets, ...) which are "falsy" when empty and "truthy" when containing\
  items:

```python
bool([]) is False
bool([1]) is True
bool([False]) is True
```

So, you can write `if some_collection:` instead of `if len(some_collection):`.

* Iterate on iterables

```python
# creates a temporary list and looks bar
for key in my_dict.keys():
    "do something..."
# better
for key in my_dict:
    "do something..."
# accessing the key,value pair
for key, value in my_dict.items():
    "do something..."
```

* Use dict.setdefault

```python
# longer.. harder to read
values = {}
for element in iterable:
    if element not in values:
        values[element] = []
    values[element].append(other_value)

# better.. use dict.setdefault method
values = {}
for element in iterable:
    values.setdefault(element, []).append(other_value)
```

* As a good developer, document your code (docstring on methods, simple\
  comments for tricky part of code)
* In additions to these guidelines, you may also find the following link\
  interesting: [https://david.goodger.org/projects/pycon/2007/idiomatic/handout.html](https://david.goodger.org/projects/pycon/2007/idiomatic/handout.html)\
  (a little bit outdated, but quite relevant)

### Programming in Odoo

* Avoid to create generators and decorators: only use the ones provided by\
  the Odoo API.
* As in python, use `filtered`, `mapped`, `sorted`, ... methods to\
  ease code reading and performance.

#### Propagate the context

The context is a `frozendict` that cannot be modified. To call a method with\
a different context, the `with_context` method should be used :

```python
records.with_context(new_context).do_stuff() # all the context is replaced
records.with_context(**additionnal_context).do_other_stuff() # additionnal_context values override native context ones
```

#### WARNING

Passing parameter in context can have dangerous side-effects.

Since the values are propagated automatically, some unexpected behavior may appear.\
Calling `create()` method of a model with _default\_my\_field_ key in context\
will set the default value of _my\_field_ for the concerned model.\
But if during this creation, other objects (such as sale.order.line, on sale.order creation)\
having a field name _my\_field_ are created, their default value will be set too.

If you need to create a key context influencing the behavior of some object,\
choose a good name, and eventually prefix it by the name of the module to\
isolate its impact. A good example are the keys of `mail` module :_mail\_create\_nosubscribe_, _mail\_notrack_, _mail\_notify\_user\_signature_, ...

#### Think extendable

Functions and methods should not contain too much logic: having a lot of small\
and simple methods is more advisable than having few large and complex methods.\
A good rule of thumb is to split a method as soon as it has more than one\
responsibility (see [http://en.wikipedia.org/wiki/Single\_responsibility\_principle](http://en.wikipedia.org/wiki/Single_responsibility_principle)).

Hardcoding a business logic in a method should be avoided as it prevents to be\
easily extended by a submodule.

```python
# do not do this
# modifying the domain or criteria implies overriding whole method
def action(self):
    ...  # long method
    partners = self.env['res.partner'].search(complex_domain)
    emails = partners.filtered(lambda r: arbitrary_criteria).mapped('email')

# better but do not do this either
# modifying the logic forces to duplicate some parts of the code
def action(self):
    ...
    partners = self._get_partners()
    emails = partners._get_emails()

# better
# minimum override
def action(self):
    ...
    partners = self.env['res.partner'].search(self._get_partner_domain())
    emails = partners.filtered(lambda r: r._filter_partners()).mapped('email')
```

The above code is over extendable for the sake of example but the readability\
must be taken into account and a tradeoff must be made.

Also, name your functions accordingly: small and properly named functions are\
the starting point of readable/maintainable code and tighter documentation.

This recommendation is also relevant for classes, files, modules and packages.\
(See also [http://en.wikipedia.org/wiki/Cyclomatic\_complexity](http://en.wikipedia.org/wiki/Cyclomatic_complexity))

#### Never commit the transaction

The Odoo framework is in charge of providing the transactional context for\
all RPC calls. The principle is that a new database cursor is opened at the\
beginning of each RPC call, and committed when the call has returned, just\
before transmitting the answer to the RPC client, approximately like this:

```python
def execute(self, db_name, uid, obj, method, *args, **kw):
    db, pool = pooler.get_db_and_pool(db_name)
    # create transaction cursor
    cr = db.cursor()
    try:
        res = pool.execute_cr(cr, uid, obj, method, *args, **kw)
        cr.commit() # all good, we commit
    except Exception:
        cr.rollback() # error, rollback everything atomically
        raise
    finally:
        cr.close() # always close cursor opened manually
    return res
```

If any error occurs during the execution of the RPC call, the transaction is\
rolled back atomically, preserving the state of the system.

Similarly, the system also provides a dedicated transaction during the execution\
of tests suites, so it can be rolled back or not depending on the server\
startup options.

The consequence is that if you manually call `cr.commit()` anywhere there is\
a very high chance that you will break the system in various ways, because you\
will cause partial commits, and thus partial and unclean rollbacks, causing\
among others:

1. inconsistent business data, usually data loss
2. workflow desynchronization, documents stuck permanently
3. tests that can't be rolled back cleanly, and will start polluting the\
   database, and triggering error (this is true even if no error occurs\
   during the transaction)

Here is the very simple rule:\
: You should **NEVER** call `cr.commit()` yourself, **UNLESS** you have\
created your own database cursor explicitly! And the situations where you\
need to do that are exceptional!\
And by the way if you did create your own cursor, then you need to handle\
error cases and proper rollback, as well as properly close the cursor when\
you're done with it.

And contrary to popular belief, you do not even need to call `cr.commit()`\
in the following situations:

* in the `_auto_init()` method of an _models.Model_ object: this is taken\
  care of by the addons initialization method, or by the ORM transaction when\
  creating custom models
* in reports: the `commit()` is handled by the framework too, so you can\
  update the database even from within a report
* within _models.Transient_ methods: these methods are called exactly like\
  regular _models.Model_ ones, within a transaction and with the corresponding`cr.commit()/rollback()` at the end
* etc. (see general rule above if you are in doubt!)

All `cr.commit()` calls outside of the server framework from now on must\
have an **explicit comment** explaining why they are absolutely necessary, why\
they are indeed correct, and why they do not break the transactions. Otherwise\
they can and will be removed !

#### Use translation method correctly

Odoo uses a GetText-like method named "underscore" `_( )` to indicate that\
a static string used in the code needs to be translated at runtime using the\
language of the context. This pseudo-method is accessed within your code by\
importing as follows:

```python
from odoo import _
```

A few very important rules must be followed when using it, in order for it to\
work and to avoid filling the translations with useless junk.

Basically, this method should only be used for static strings written manually\
in the code, it will not work to translate field values, such as Product names,\
etc. This must be done instead using the translate flag on the corresponding\
field.

The method accepts optional positional or named parameter\
The rule is very simple: calls to the underscore method should always be in\
the form `_('literal string')` and nothing else:

```python
# good: plain strings
error = _('This record is locked!')

# good: strings with formatting patterns included
error = _('Record %s cannot be modified!', record)

# ok too: multi-line literal strings
error = _("""This is a bad multiline example
             about record %s!""", record)
error = _('Record %s cannot be modified' \
          'after being validated!', record)

# bad: tries to translate after string formatting
#      (pay attention to brackets!)
# This does NOT work and messes up the translations!
error = _('Record %s cannot be modified!' % record)

# bad: formatting outside of translation
# This won't benefit from fallback mechanism in case of bad translation
error = _('Record %s cannot be modified!') % record

# bad: dynamic string, string concatenation, etc are forbidden!
# This does NOT work and messes up the translations!
error = _("'" + que_rec['question'] + "' \n")

# bad: field values are automatically translated by the framework
# This is useless and will not work the way you think:
error = _("Product %s is out of stock!") % _(product.name)
# and the following will of course not work as already explained:
error = _("Product %s is out of stock!" % product.name)

# Instead you can do the following and everything will be translated,
# including the product name if its field definition has the
# translate flag properly set:
error = _("Product %s is not available!", product.name)
```

Also, keep in mind that translators will have to work with the literal values\
that are passed to the underscore function, so please try to make them easy to\
understand and keep spurious characters and formatting to a minimum. Translators\
must be aware that formatting patterns such as `%s` or `%d`, newlines, etc.\
need to be preserved, but it's important to use these in a sensible and obvious\
manner:

```python
# Bad: makes the translations hard to work with
error = "'" + question + _("' \nPlease enter an integer value ")

# Ok (pay attention to position of the brackets too!)
error = _("Answer to question %s is not valid.\n" \
          "Please enter an integer value.", question)

# Better
error = _("Answer to question %(title)s is not valid.\n" \
          "Please enter an integer value.", title=question)
```

In general in Odoo, when manipulating strings, prefer `%` over `.format()`\
(when only one variable to replace in a string), and prefer `%(varname)` instead\
of position (when multiple variables have to be replaced). This makes the\
translation easier for the community translators.

### Symbols and Conventions

* Model name (using the dot notation, prefix by the module name) :\
  : - When defining an Odoo Model : use singular form of the name (_res.partner_\
  and _sale.order_ instead of _res.partnerS_ and _saleS.orderS_)
  * When defining an Odoo Transient (wizard) : use `<related_base_model>.<action>`\
    where _related\_base\_model_ is the base model (defined in _models/_) related\
    to the transient, and _action_ is the short name of what the transient do. Avoid the _wizard_ word.\
    For instance : `account.invoice.make`, `project.task.delegate.batch`, ...
  * When defining _report_ model (SQL views e.i.) : use`<related_base_model>.report.<action>`, based on the Transient convention.
* Odoo Python Class : use camelcase (Object-oriented style).

```python
class AccountInvoice(models.Model):
    ...
```

* Variable name :\
  : - use camelcase for model variable
  * use underscore lowercase notation for common variable.
  * suffix your variable name with _\_id_ or _\_ids_ if it contains a record id or list of id. Don't use `partner_id` to contain a record of res.partner

```python
Partner = self.env['res.partner']
partners = Partner.browse(ids)
partner_id = partners[0].id
```

* `One2Many` and `Many2Many` fields should always have _\_ids_ as suffix (example: sale\_order\_line\_ids)
* `Many2One` fields should have _\_id_ as suffix (example : partner\_id, user\_id, ...)
* Method conventions\
  : - Compute Field : the compute method pattern is _\_compute\_\<field\_name>_
  * Search method : the search method pattern is _\_search\_\<field\_name>_
  * Default method : the default method pattern is _\_default\_\<field\_name>_
  * Selection method: the selection method pattern is _\_selection\_\<field\_name>_
  * Onchange method : the onchange method pattern is _\_onchange\_\<field\_name>_
  * Constraint method : the constraint method pattern is _\_check\_\<constraint\_name>_
  * Action method : an object action method is prefix with _action\__.\
    Since it uses only one record, add `self.ensure_one()`\
    at the beginning of the method.
* In a Model attribute order should be\
  : 1. Private attributes (`_name`, `_description`, `_inherit`, `_sql_constraints`, ...)\
  2\. Default method and `default_get`\
  3\. Field declarations\
  4\. Compute, inverse and search methods in the same order as field declaration\
  5\. Selection method (methods used to return computed values for selection fields)\
  6\. Constrains methods (`@api.constrains`) and onchange methods (`@api.onchange`)\
  7\. CRUD methods (ORM overrides)\
  8\. Action methods\
  9\. And finally, other business methods.

```python
class Event(models.Model):
    # Private attributes
    _name = 'event.event'
    _description = 'Event'

    # Default methods
    def _default_name(self):
        ...

    # Fields declaration
    name = fields.Char(string='Name', default=_default_name)
    seats_reserved = fields.Integer(string='Reserved Seats', store=True
        readonly=True, compute='_compute_seats')
    seats_available = fields.Integer(string='Available Seats', store=True
        readonly=True, compute='_compute_seats')
    price = fields.Integer(string='Price')
    event_type = fields.Selection(string="Type", selection='_selection_type')

    # compute and search fields, in the same order of fields declaration
    @api.depends('seats_max', 'registration_ids.state', 'registration_ids.nb_register')
    def _compute_seats(self):
        ...

    @api.model
    def _selection_type(self):
        return []

    # Constraints and onchanges
    @api.constrains('seats_max', 'seats_available')
    def _check_seats_limit(self):
        ...

    @api.onchange('date_begin')
    def _onchange_date_begin(self):
        ...

    # CRUD methods (and name_search, _search, ...) overrides
    def create(self, values):
        ...

    # Action methods
    def action_validate(self):
        self.ensure_one()
        ...

    # Business methods
    def mail_user_confirm(self):
        ...
```

## Javascript

### Static files organization

Odoo addons have some conventions on how to structure various files. We explain\
here in more details how web assets are supposed to be organized.

The first thing to know is that the Odoo server will serve (statically) all files\
located in a _static/_ folder, but prefixed with the addon name. So, for example,\
if a file is located in _addons/web/static/src/js/some\_file.js_, then it will be\
statically available at the url _your-odoo-server.com/web/static/src/js/some\_file.js_

The convention is to organize the code according to the following structure:

* _static_: all static files in general
  * _static/lib_: this is the place where js libs should be located, in a sub folder.\
    So, for example, all files from the _jquery_ library are in _addons/web/static/lib/jquery_
  * _static/src_: the generic static source code folder
    * _static/src/css_: all css files
    * _static/fonts_
    * _static/img_
    * _static/src/js_
      * _static/src/js/tours_: end user tour files (tutorials, not tests)
    * _static/src/scss_: scss files
    * _static/src/xml_: all qweb templates that will be rendered in JS
  * _static/tests_: this is where we put all test related files.
    * _static/tests/tours_: this is where we put all tour test files (not tutorials).

### Javascript coding guidelines

* `use strict;` is recommended for all javascript files
* Use a linter (jshint, ...)
* Never add minified Javascript Libraries
* Use camelcase for class declaration

More precise JS guidelines are detailed in the [github wiki](https://github.com/odoo/odoo/wiki/Javascript-coding-guidelines).\
You may also have a look at existing API in Javascript by looking Javascript\
References.

## CSS and SCSS

### Syntax and Formatting

SCSS

```html
.o_foo, .o_foo_bar, .o_baz {
   height: $o-statusbar-height;

   .o_qux {
      height: $o-statusbar-height * 0.5;
   }
}

.o_corge {
   background: $o-list-footer-bg-color;
}
```

CSS

```css
.o_foo, .o_foo_bar, .o_baz {
   height: 32px;
}

.o_foo .o_quux, .o_foo_bar .o_quux, .o_baz .o_qux {
   height: 16px;
}

.o_corge {
   background: #EAEAEA;
}
```

* four (4) space indents, no tabs;
* columns of max. 80 characters wide;
* opening brace (`{`): empty space after the last selector;
* closing brace (`}`): on its own new line;
* one line for each declaration;
* meaningful use of whitespace.

### Properties order

Order properties from the "outside" in, starting from `position` and ending with decorative rules\
(`font`, `filter`, etc.).

[Scoped SCSS variables](coding_guidelines.md#contributing-coding-guidelines-scss-scoped-scss-variables) and[CSS variables](coding_guidelines.md#contributing-coding-guidelines-scss-css-variables) must be placed at the very\
top, followed by an empty line separating them from other declarations.

```html
.o_element {
   $-inner-gap: $border-width + $legend-margin-bottom;

   --element-margin: 1rem;
   --element-size: 3rem;

   @include o-position-absolute(1rem);
   display: block;
   margin: var(--element-margin);
   width: calc(var(--element-size) + #{$-inner-gap});
   border: 0;
   padding: 1rem;
   background: blue;
   font-size: 1rem;
   filter: blur(2px);
}
```

### Naming Conventions

Naming conventions in CSS are incredibly useful in making your code more strict, transparent and\
informative.

Avoid `id` selectors, and prefix your classes with `o_<module_name>`, where `<module_name>` is the\
technical name of the module (`sale`, `im_chat`, ...) or the main route reserved by the module\
(for website modules mainly, i.e. : `o_forum` for the `website_forum` module).\
The only exception for this rule is the webclient: it simply uses the `o_` prefix.\


Avoid creating hyper-specific classes and variable names. When naming nested elements, opt for the\
"Grandchild" approach.

Besides being more compact, this approach eases maintenance because it limits the need of renaming\
when changes occur at the DOM.

#### SCSS Variables

Our standard convention is `$o-[root]-[element]-[property]-[modifier]`, with:

* `$o-`\
  : The prefix.
* `[root]`\
  : Either the component **or** the module name (components take priority).
* `[element]`\
  : An optional identifier for inner elements.
* `[property]`\
  : The property/behavior defined by the variable.
* `[modifier]`\
  : An optional modifier.

#### SCSS Variables (scoped)

These variables are declared within blocks and are not accessible from the outside.\
Our standard convention is `$-[variable name]`.

#### SEE ALSO

[Variables scope on the SASS Documentation](https://sass-lang.com/documentation/variables#scope)

#### SCSS Mixins and Functions

Our standard convention is `o-[name]`. Use descriptive names. When naming functions, use verbs in\
the imperative form (e.g.: `get`, `make`, `apply`...).

Name optional arguments in the [scoped variables form](coding_guidelines.md#contributing-coding-guidelines-scss-scoped-scss-variables), so `$-[argument]`.

#### SEE ALSO

* [Mixins on the SASS Documentation](https://sass-lang.com/documentation/at-rules/mixin)
* [Functions on the SASS Documentation](https://sass-lang.com/documentation/at-rules/function)

#### CSS Variables

In Odoo, the use of CSS variables is strictly DOM-related. Use them to **contextually** adapt the\
design and layout.

Our standard convention is BEM, so `--[root]__[element]-[property]--[modifier]`, with:

* `[root]`\
  : Either the component **or** the module name (components take priority).
* `[element]`\
  : An optional identifier for inner elements.
* `[property]`\
  : The property/behavior defined by the variable.
* `[modifier]`\
  : An optional modifier.

### Use of CSS Variables

In Odoo, the use of CSS variables is strictly DOM-related, meaning that are used to **contextually**\
adapt the design and layout rather than to manage the global design-system. These are typically used\
when a component's properties can vary in specific contexts or in other circumstances.

We define these properties inside the component's main block, providing default fallbacks.

#### SEE ALSO

[CSS variables on MDN web docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

#### CSS and SCSS Variables

Despite being apparently similar, `CSS` and `SCSS` variables behave very differently. The main\
difference is that, while `SCSS` variables are **imperative** and compiled away, `CSS` variables are**declarative** and included in the final output.

#### SEE ALSO

[CSS/SCSS variables difference on the SASS Documentation](https://sass-lang.com/documentation/variables)

In Odoo, we take the best of both worlds: using the `SCSS` variables to define the design-system\
while opting for the `CSS` ones when it comes to contextual adaptations.

The implementation of the previous example should be improved by adding SCSS variables in order to\
gain control at the top-level and ensure consistency with other components.

#### The `:root` pseudo-class

Defining CSS variables on the `:root` pseudo-class is a technique we normally **don't use** in\
Odoo's UI. The practice is commonly used to access and modify CSS variables globally. We perform\
this using SCSS instead.

Exceptions to this rule should be fairly apparent, such as templates shared across bundles that\
require a certain level of contextual awareness in order to be rendered properly.
