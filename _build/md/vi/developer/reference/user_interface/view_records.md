# View records

Views are what define how records should be displayed to end-users. They are specified in XML and
stored as records themselves, meaning they can be edited independently from the models that they
represent. They are flexible and allow a high level of customization of the screens that they
control. There exist various [types of views](#reference-view-records-types). Each represents a
visualization mode: *form*, *list*, *kanban*, etc.

<a id="reference-view-records-structure"></a>

## Generic structure

Basic views generally share the common minimal structure defined below. Placeholders are denoted in
all caps.

```xml
<record id="ADDON.MODEL_view_TYPE" model="ir.ui.view">
  <field name="name">NAME</field>
  <field name="model">MODEL</field>
  <field name="arch" type="xml">
    <VIEW_TYPE>
      <views/>
    </VIEW_TYPE>
  </field>
</record>
```

<a id="reference-view-records-types"></a>

## View types

[Form](developer/reference/user_interface/view_architectures.md#reference-view-architectures-form)
: Display and edit the data from a single record.

[List](developer/reference/user_interface/view_architectures.md#reference-view-architectures-list)
: View and edit multiple records.

[Search](developer/reference/user_interface/view_architectures.md#reference-view-architectures-search)
: Apply filters and perform searches. The results are displayed in the current list, kanban... view.

[Kanban](developer/reference/user_interface/view_architectures.md#reference-view-architectures-kanban)
: Display records as "cards", configurable as a small template.

[Qweb](developer/reference/user_interface/view_architectures.md#reference-view-architectures-qweb)
: Templating of reporting, website...

[Graph](developer/reference/user_interface/view_architectures.md#reference-view-architectures-graph)
: Visualize aggregations over a number of records or record groups.

[Pivot](developer/reference/user_interface/view_architectures.md#reference-view-architectures-pivot)
: Display aggregations as a [pivot table](https://en.wikipedia.org/wiki/Pivot_table).

[Calendar](developer/reference/user_interface/view_architectures.md#reference-view-architectures-calendar)
: Display records as events in a daily, weekly, monthly, or yearly calendar.

[Cohort](developer/reference/user_interface/view_architectures.md#reference-view-architectures-cohort) <span class="badge" style="background-color:#714B67">Enterprise feature</span>
: Display and understand the way some data changes over a period of time.

[Gantt](developer/reference/user_interface/view_architectures.md#reference-view-architectures-gantt) <span class="badge" style="background-color:#714B67">Enterprise feature</span>
: Display records as a Gantt chart.

[Grid](developer/reference/user_interface/view_architectures.md#reference-view-architectures-grid) <span class="badge" style="background-color:#714B67">Enterprise feature</span>
: Display computed information in numerical cells; are hardly configurable.

[Map](developer/reference/user_interface/view_architectures.md#reference-view-architectures-map) <span class="badge" style="background-color:#714B67">Enterprise feature</span>
: Display records on a map, and the routes between them.

<a id="reference-view-records-fields"></a>

## Fields

View records expose a number of fields.

#### NOTE
The current context and user access rights may also impact the view abilities.

<a id="reference-view-records-inheritance"></a>

## Inheritance

Inheritance allows for customizing delivered views. It makes it possible, for example, to add
content as modules are installed, or to deliver different displays according to the action.

Inherit views generally share the common structure defined below. Placeholders are denoted in all
caps. This synthetic view will update a node targeted by an XPath, and another targeted by its name
and attributes.

```xml
<record id="ADDON.MODEL_view_TYPE" model="ir.ui.view">
    <field name="model">MODEL</field>
    <field name="inherit_id" ref="VIEW_REFERENCE"/>
    <field name="mode">MODE</field>
    <field name="arch" type="xml">
        <xpath expr="XPATH" position="POSITION">
            <CONTENT/>
        </xpath>
        <NODE ATTRIBUTES="VALUES" position="POSITION">
            <CONTENT/>
        </NODE>
    </field>
</record>
```

The `inherit_id` and `mode` fields determine the [view resolution](#reference-view-records-inheritance-resolution). The `xpath` or `NODE` elements indicate the
[inheritance specs](#reference-view-records-inheritance-specs). The `expr` and `position`
attributes specify the [inheritance position](#reference-view-records-inheritance-position).

<a id="reference-view-records-inheritance-resolution"></a>

### View resolution

Resolution generates the final `arch` for a requested/matched `primary` view as follow:

1. if the view has a parent, the parent is fully resolved, then the current view's inheritance specs
   are applied;
2. if the view has no parent, its `arch` is used as-is;
3. the current view's children with mode `extension` are looked up, and their inheritance specs are
   applied depth-first (a child view is applied, then its children, then its siblings).

The inheritance is applied according to the `inherit_id` field. If several view records inherit the
same view, the order is determined by the `priority`.

The result of applying children views yields the final `arch`.

<a id="reference-view-records-inheritance-specs"></a>

### Inheritance specs

Inheritance specs are applied sequentially and are comprised of:

1. an element locator to match the inherited element in the parent view;
2. children element to modify the inherited element.

There are three types of element locators:

- An `xpath` element with an `expr` attribute. `expr` is an [XPath](https://en.wikipedia.org/wiki/XPath) expression<sup>[1](#hasclass)</sup> applied to the current `arch`,
  matching the first node it finds;
- A `field` element with a `name` attribute, matching the first field with the same `name`.

  #### NOTE
  All other attributes are ignored.
- Any other element, matching the first element with the same `name` and identical attributes.

  #### NOTE
  The attributes `position` and `version` are ignored.

* <a id='hasclass'>**[1]**</a> An extension function is added for simpler matching in QWeb views: `hasclass(*classes)` matches if the context node has all the specified classes.

<a id="reference-view-records-inheritance-position"></a>

### Inheritance position

The inheritance specs accept an optional `position` attribute, defaulting to `inside`, that
specifies how the matched node should be modified.

### inside

The content of the inheritance spec is appended to the matched node.

### after

The content of the inheritance spec is appended to the matched node's parent after the matched
node.

### before

The content of the inheritance spec is appended to the matched node's parent before the matched
node.

### replace

The content of the inheritance spec replaces the matched node. Any text node containing only `$0`
within the contents of the spec is replaced by a copy of the matched node, effectively wrapping
the matched node.

### attributes

The content of the inheritance spec should be made of only `attribute` elements, each with a
`name` attribute and an optional body.

- If the `attribute` element has a body, a new attributed named after its `name` is added to the
  matched node with the `attribute` element's text as value.
- If the `attribute` element has no body, the attribute named after its `name` is removed from the
  matched node.
- If the `attribute` element has an `add` attribute, a `remove` attribute, or both, the value of
  the matched node's attribute named after `name` is recomputed to account for the value(s) of
  `add`, `remove`, and an optional `separator` attribute defaulting to `,`. `add` includes its
  value(s), separated by `separator`. `remove` removes its value(s), separated by `separator`.

### move

The attribute `position="move"` is set on the content of the inheritance spec to specify how nodes
are moved relatively to the inheritance spec's element locator, on which the attribute `position`
must also be set, with values `inside`, `replace`, `after`, or `before`.

<a id="reference-view-records-model-commons"></a>

## Model commons
