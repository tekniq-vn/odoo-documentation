# Chapter 4: Security - A Brief Introduction

In the [previous chapter](developer/tutorials/server_framework_101/03_basicmodel.md), we created our first table
intended to store business data. In a business application such as Odoo, one of the first questions
to consider is who<sup>[1](#who)</sup> can access the data. Odoo provides a security mechanism to allow access
to the data for specific groups of users.

The topic of security is covered in more detail in [Restrict access to data](developer/tutorials/restrict_data_access.md). This chapter aims
to cover the minimum required for our new module.

## Data Files (CSV)

Odoo is a highly data driven system. Although behavior is customized using Python code, part of a
module's value is in the data it sets up when loaded. One way to load data is through a CSV
file. One example is the [list of country states](https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/res.country.state.csv) which is loaded at installation of the
`base` module.

```text
"id","country_id:id","name","code"
state_au_1,au,"Australian Capital Territory","ACT"
state_au_2,au,"New South Wales","NSW"
state_au_3,au,"Northern Territory","NT"
state_au_4,au,"Queensland","QLD"
...
```

- `id` is an [external identifier](developer/glossary.md#term-external-identifier). It can be used to refer to the record
  (without knowing its in-database identifier).
- `country_id:id` refers to the country by using its [external identifier](developer/glossary.md#term-external-identifier).
- `name` is the name of the state.
- `code` is the code of the state.

These three fields are
[defined](https://github.com/odoo/odoo/blob/2ad2f3d6567b6266fc42c6d2999d11f3066b282c/odoo/addons/base/models/res_country.py#L108-L111)
in the `res.country.state` model.

By convention, a file importing data is located in the `data` folder of a module. When the data
is related to security, it is located in the `security` folder. When the data is related to
views and actions (we will cover this later), it is located in the `views` folder.
Additionally, all of these files must be declared in the `data`
list within the `__manifest__.py` file. Our example file is defined
[in the manifest of the base module](https://github.com/odoo/odoo/blob/e8697f609372cd61b045c4ee2c7f0fcfb496f58a/odoo/addons/base/__manifest__.py#L29).

Also note that the content of the data files is only loaded when a module is installed or
updated.

#### WARNING
The data files are sequentially loaded following their order in the `__manifest__.py` file.
This means that if data `A` refers to data `B`, you must make sure that `B`
is loaded before `A`.

In the case of the country states, you will note that the
[list of countries](https://github.com/odoo/odoo/blob/e8697f609372cd61b045c4ee2c7f0fcfb496f58a/odoo/addons/base/__manifest__.py#L22)
is loaded **before** the
[list of country states](https://github.com/odoo/odoo/blob/e8697f609372cd61b045c4ee2c7f0fcfb496f58a/odoo/addons/base/__manifest__.py#L29).
This is because the states refer to the countries.

Why is all this important for security? Because all the security configuration of a model is loaded through
data files, as we'll see in the next section.

## Access Rights

**Reference**: the documentation related to this topic can be found in
[Access Rights](developer/reference/backend/security.md#reference-security-acl).

#### NOTE
**Goal**: at the end of this section, the following warning should not appear anymore:

```text
WARNING rd-demo odoo.modules.loading: The models ['estate.property'] have no access rules...
```

When no access rights are defined on a model, Odoo determines that no users can access the data.
It is even notified in the log:

```text
WARNING rd-demo odoo.modules.loading: The models ['estate.property'] have no access rules in module estate, consider adding some, like:
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
```

Access rights are defined as records of the model `ir.model.access`. Each
access right is associated with a model, a group (or no group for global
access) and a set of permissions: create, read, write and unlink<sup>[2](#unlink)</sup>. Such access
rights are usually defined in a CSV file named
`ir.model.access.csv`.

Here is an example for our previous `test_model`:

```text
id,name,model_id/id,group_id/id,perm_read,perm_write,perm_create,perm_unlink
access_test_model,access_test_model,model_test_model,base.group_user,1,0,0,0
```

- `id` is an [external identifier](developer/glossary.md#term-external-identifier).
- `name` is the name of the `ir.model.access`.
- `model_id/id` refers to the model which the access right applies to. The standard way to refer
  to the model is `model_<model_name>`, where `<model_name>` is the `_name` of the model
  with the `.` replaced by `_`. Seems cumbersome? Indeed it is...
- `group_id/id` refers to the group which the access right applies to.
- `perm_read,perm_write,perm_create,perm_unlink`: read, write, create and unlink permissions

Restart the server and the warning message should have disappeared!

It's now time to finally [interact with the UI](developer/tutorials/server_framework_101/05_firstui.md)!

* <a id='who'>**[1]**</a> meaning which Odoo user (or group of users)
* <a id='unlink'>**[2]**</a> 'unlink' is the equivalent of 'delete'
