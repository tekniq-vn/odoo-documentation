# Define module data

#### IMPORTANT
This tutorial is an extension of the [Server framework 101](server_framework_101.md) tutorial. Make sure you have
completed it and use the `estate` module you have built as a base for the exercises in this
tutorial.

## Data Types

### Master Data

Master data is usually part of the technical or business requirements for the module. In other
words, such data is often necessary for the module to work properly. This data will always be
installed when installing the module.

We already met technical data previously since we have defined [views](../reference/user_interface/view_records.md) and [actions](../reference/backend/actions.md). Those
are one kind of master data.

On top of technical data, business data can be defined, e.g. countries, currencies, units of measure,
as well as complete country localization (legal reports, tax definitions, chart of account), and much
more...

### Demo Data

In additional to master data, which are requirements for a module to work properly, we also like
having data for demonstration purposes:

* Help the sales representatives make their demos quickly.
* Have a set of working data for developers to test new features and see how these new features look
  with data they might not have added themselves.
* Test that the data is loaded correctly, without raising an error.
* Setup most of the features to be used quickly when creating a new database.

Demo data is automatically loaded when you start the server if you don't explicitly say you don't
want it. This can be done in the database manager or with the command line.

```console
$ ./odoo-bin -h
Usage: odoo-bin [options]

Options:
--version             show program's version number and exit
-h, --help            show this help message and exit

Common options:
  [...]
  --without-demo=WITHOUT_DEMO
                      disable loading demo data for modules to be installed
                      (comma-separated, use "all" for all modules). Requires
                      -d and -i. Default is none
[...]

$ ./odoo-bin --addons-path=... -d db -i account --without-demo=all
```

## Data Declaration

### Manifest

**Reference**: the documentation related to this topic can be found in
[Module Manifests](../reference/backend/module.md#reference-module-manifest).

Data is declared either in CSV or in XML.
Each file containing data must be added in the manifest for them to be loaded.

The keys to use in the manifest to add new data are `data` for the master data and `demo` for
the demo data. Both values should be a list of strings representing the relative paths to the files
declaring the data.

Usually, demo data is in a `demo` folder, views and actions are in a `views`
folder, security related data is in a `security` folder, and other data is in a
`data` folder.

If your work tree looks like this:

```bash
estate
├── data
│   └── master_data.xml
├── demo
│   └── demo_data.xml
├── models
│   ├── *.py
│   └── __init__.py
├── security
│   └── ir.model.access.csv
├── views
│   └── estate_property_offer_views.xml
├── __init__.py
└── __manifest__.py
```

Your manifest should look like this:

```python
# -*- coding: utf-8 -*-

{
    "name": "Real Estate",
    "depends": [
        ...
    ],
    "data": [
        "security/ir.model.access.csv",  # CSV and XML files are loaded at the same place
        "views/estate_property_offer_views.xml",  # Views are data too
        "data/master_data.xml",  # Split the data in multiple files depending on the model
    ],
    "demo": [
        "demo/demo_data.xml",
    ]
    "application": True,
}
```

### CSV

**Reference**: the documentation related to this topic can be found in
[CSV data files](../reference/backend/data.md#reference-data-csvdatafiles).

The easiest way to declare simple data is by using the CSV format. This is however limited in terms
of features: use it for long lists of simple models, but prefer XML otherwise.

```text
id,field_a,field_b,related_id:id
id1,valueA1,valueB1,module.relatedid
id2,valueA2,valueB2,module.relatedid
```

### XML

**Reference**: the documentation related to this topic can be found in
[Data Files](../reference/backend/data.md#reference-data).

When the data to create is more complex it can be useful, or even necessary, to do it in XML.

```xml
<odoo>
  <record id="id1" model="tutorial.example">
    <field name="field_a">valueA1</field>
    <field name="field_b">valueB1</field>
  </record>

  <record id="id2" model="tutorial.example">
    <field name="field_a">valueA2</field>
    <field name="field_b">valueB2</field>
  </record>
</odoo>
```

#### Data Extension

During the Core Training, we saw in the [Chapter 12: Inheritance](server_framework_101/12_inheritance.md) chapter we
could inherit (extend) an existing view. This was a special case of data extension: any data can be
extended in a module.

When you are adding new fields to an existing model in a new module, you might want to populate
those fields on the records created in the modules you are depending on. This is done by giving the
`xml_id` of the record you want to extend. It won't replace it, in this case we will set the
`field_c` to the given value for both records.

```xml
<odoo>
  <record id="id1" model="tutorial.example">
    <field name="field_c">valueC1</field>
  </record>

  <record id="id2" model="tutorial.example">
    <field name="field_c">valueC2</field>
  </record>
</odoo>
```

#### `ref`

Related fields can be set using the `ref` key. The value of that key is the `xml_id` of the
record you want to link. Remember the `xml_id` is composed of the name of the module where the
data is first declared, followed by a dot, followed by the `id` of the record (just the `id`
works too if you are in the module declaring it).

```xml
<odoo>
  <record id="id1" model="tutorial.example">
    <field name="related_id" ref="module.relatedid"/>
  </record>
</odoo>
```

#### `eval`

The value to assign to a field is not always a simple string and you might need to compute it.
It can also be used to optimize the insertion of related values, or because a constraint forces you
to add the related values in batch. See :[Add X2many fields](#tutorials-define-module-data-x2m).

```xml
<odoo>
  <record id="id1" model="tutorial.example">
    <field name="year" eval="datetime.now().year+1"/>
  </record>
</odoo>
```

#### `search`

Sometimes, you need to call the ORM to do a `search`. This is not feasible with the CSV format.

```xml
<odoo>
  <record id="id1" model="account.move.line">
    <field name="account_id" search="[
      ('user_type_id', '=', ref('account.data_account_type_direct_costs')),
      ('company_id', '=', obj().env.company.id)]
    "/>
  </record>
</odoo>
```

In this code snippet, it is needed because the master data depends on the localization
installed.

#### `function`

You might also need to execute python code when loading data.

```xml
<function model="tutorial.example" name="action_validate">
    <value eval="[ref('demo_invoice_1')]"/>
</function>
```

<a id="tutorials-define-module-data-x2m"></a>

### Add X2many fields

**Reference**: the documentation related to this topic can be found in
`Command`.

If you need to add related data in a One2many or a Many2many field, you can do so by using the
`Command` methods.

```xml
<odoo>
  <record id="id1" model="tutorial.example">
    <field name="related_ids" eval="[
        Command.create({
            'name': 'My name',
        }),
        Command.create({
            'name': 'Your name',
        }),
        Command.link(ref('model.xml_id')),
    ]"/>
  </record>
</odoo>
```

## Accessing the data

#### WARNING
You should never access demo data outside of the demo data declaration, not even in
tests.

There are multiple ways to access the master/demo data.

In python code, you can use the `env.ref(self, xml_id, raise_if_not_found=True)` method. It
returns the recordset linked to the `xml_id` you specify.

In XML, you can use the `ref` key like this

```xml
<odoo>
  <record id="id1" model="tutorial.example">
    <field name="related_id" ref="module.relatedid"/>
  </record>
</odoo>
```

It will call the ref method, and store the id of the record returned on the field `related_id` of
the record of type `tutorial.example` with id `id1`.

In CSV, the title of the column must be suffixed with `:id` or `/id`.

```text
id,parent_id:id,name
"child1","module.parent","Name1"
"child2","module.parent","Name2"
"child3","module.parent","Name3"
```

In SQL, it is more complicated, see [the advanced section](#tutorials-define-module-data-xml-id).

#### WARNING
Data can always be deleted by the user. Always code defensively, taking this into
account.

## Advanced

<a id="tutorials-define-module-data-xml-id"></a>

### What is the XML id?

Because we don't want a column `xml_id` in every single SQL table of the database, we need a
mechanism to store it. This is done with the `ir.model.data` model.

It contains the name of the record (the `xml_id`) along with the module in which it is defined,
the model defining it, and the id of it.

### No update

The records created with the `noupdate` flag won't be updated when upgrading the module that
created them, but it will be created if it didn't exist yet.

#### NOTE
`odoo-bin -i module` will bypass this setting and always load the data. But normally
one shouldn't do this on a production database.

```xml
<odoo noupdate="1">
  <record id="id1" model="model">
    <field name="fieldA" eval="True"/>
  </record>
</odoo>
```

### Import as SQL

In some cases, it makes sense to do the import directly in SQL. This is however discouraged as it
bypasses all the features of the ORM, computed fields (including metadata) and python constraints.

#### NOTE
Generally using raw SQL also bypasses ACLs and increases the risks of injections.

**Reference**: [Security in Odoo](../reference/backend/security.md#reference-security)

* It can help to speed the import time by a lot
  [with huge files](https://github.com/odoo/enterprise/blob/d46cceef8c594b9056d0115edb7169e207a5986f/product_unspsc/hooks.py#L19).
* For more complex imports like for the
  [translations](https://github.com/odoo/odoo/blob/e1f8d549895cd9c459e6350430f30d541d02838a/odoo/addons/base/models/ir_translation.py#L24).
* It can be necessary to
  [initialize the database](https://github.com/odoo/odoo/blob/e1f8d549895cd9c459e6350430f30d541d02838a/odoo/addons/base/data/base_data.sql).
