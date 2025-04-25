<a id="reference-orm-changelog"></a>

# Changelog

## Odoo version 17.0

- Introduce an `SQL` wrapper object to make SQL composition
  easier and safer with respect to SQL injections. Methods of the ORM now use it
  internally. Introduced by [#134677](https://github.com/odoo/odoo/pull/134677).

## Odoo Online version 16.4

- Method `name_get()` has been deprecated with
  [#122085](https://github.com/odoo/odoo/pull/122085).
  Read field `display_name` instead.

## Odoo Online version 16.3

- Method `_read_group()` has a new signature with
  [#110737](https://github.com/odoo/odoo/pull/110737)

## Odoo Online version 16.2

- Refactor the implementation of searching and reading methods to be able to
  combine both in a minimal number of SQL queries. We introduce two new methods
  `search_fetch()` and `fetch()`
  that take advantage of the combination. More details can be found on the pull
  request [#112126](https://github.com/odoo/odoo/pull/112126).

## Odoo version 16.0

- Translations for translated fields are stored as JSONB values with
  [#97692](https://github.com/odoo/odoo/pull/97692)
  and [#101115](https://github.com/odoo/odoo/pull/101115).
  Code translations are no longer stored into the database.
  They become static and are extracted from the PO files when needed.
- `search_count()` takes the `limit` argument into account with [#95589](https://github.com/odoo/odoo/pull/95589).
  It limits the number of records to count, improving performance when a partial result is acceptable.

## Odoo Online version 15.4

- New API for flushing to the database and invalidating the cache with
  [#87527](https://github.com/odoo/odoo/pull/87527).
  New methods have been added to `odoo.models.Model` and `odoo.api.Environment`,
  and are less confusing about what is actually done in each case.
  See the section [SQL Execution](./#reference-orm-sql).

## Odoo Online version 15.3

- The argument `args` is renamed to `domain` for `search()`, `search_count()`
  and `_search()`. [#83687](https://github.com/odoo/odoo/pull/83687)
- `filtered_domain()` conserves the order of the current recordset. [#83687](https://github.com/odoo/odoo/pull/83687)
- `browse()` does not accept [`str`](https://docs.python.org/3/library/stdtypes.html#str) as `ids`. [#83687](https://github.com/odoo/odoo/pull/83687)
- The methods `fields_get_keys()` and `get_xml_id()` on `Model` are deprecated. [#83687](https://github.com/odoo/odoo/pull/83687)
- The method `_mapped_cache()` is removed. [#83687](https://github.com/odoo/odoo/pull/83687)
- Remove the `limit` attribute of `One2many` and `Many2many`. [#83687](https://github.com/odoo/odoo/pull/83687)

## Odoo Online version 15.2

- Specific index types on fields:  With [#83274](https://github.com/odoo/odoo/pull/83274) and
  [#83015](https://github.com/odoo/odoo/pull/83015), developers can now define what type of
  indexes can be used on fields by PostgreSQL. See the [index property](./#reference-fields) of
  `odoo.fields.Field`.
- The `_sequence` attribute of `Model` is removed. Odoo lets PostgreSQL use the default sequence of the primary key. [#82727](https://github.com/odoo/odoo/pull/82727)
- The method `_write()` does not raise an error for non-existing records. [#82727](https://github.com/odoo/odoo/pull/82727)
- The `column_format` and `deprecated` attributes of `Field` are removed. [#82727](https://github.com/odoo/odoo/pull/82727)
