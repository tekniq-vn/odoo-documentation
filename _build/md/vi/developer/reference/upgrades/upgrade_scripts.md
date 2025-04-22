# Upgrade scripts

An upgrade script is a Python file containing a function called [`migrate()`](#migrate), which the upgrade
process invokes during the update of a module.

### migrate(cr, version)

* **Tham số:**
  * **cr** (`Cursor`) -- current database cursor
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) -- installed version of the module

Typically, this function executes one or multiple SQL queries and can also access Odoo's ORM, as
well as the [Upgrade utils](developer/reference/upgrades/upgrade_utils.md).

## Writing upgrade scripts

Upgrade scripts follow a specific tree structure with a naming convention which determines when they
are executed.

The structure of an upgrade script path is `$module/migrations/$version/*pre,post,end*-*.py`,
where `$module` is the module for which the script will run, `$version` is the full version of the
module (including Odoo's major version and the module's minor version) and `{pre|post|end}-*.py` is
the file that needs to be executed. The file's name will determine the [phase](#upgrade-scripts-phases) and order in which it is executed for that module and version.

#### NOTE
From Odoo 13 the top-level directory for the upgrade scripts can also be named `upgrades`. This
naming is preferred since it has the correct meaning: *migrate* can be confused with *moving out
of Odoo*. Thus `$module/upgrades/$version/` is also valid.

#### NOTE
Upgrade scripts are only executed when the module is being updated. Therefore, the
module's minor version set in the `$version` directory needs to be higher than the module's
installed version and equal or lower to the updated version of the module.

<a id="upgrade-scripts-phases"></a>

## Phases of upgrade scripts

The upgrade process consists of three phases for each version of each module:

> 1. The pre-phase, before the module is loaded.
> 2. The post-phase, after the module and its dependencies are loaded and updated.
> 3. The end-phase, after all modules have been loaded and updated for that version.

Upgrade scripts are grouped according to the first part of their filenames into the corresponding
phase. Within each phase, the files are executed according to their lexical order.
