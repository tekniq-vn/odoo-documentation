# Chapter 14: A Brief History Of QWeb

So far the interface design of our real estate module has been rather limited. Building
a list view is straightforward since only the list of fields is necessary. The same holds true
for the form view: despite the use of a few tags such as `<group>` or `<page>`, there
is very little to do in terms of design.

However, if we want to give a unique look to our application, it is necessary to go a step
further and be able to design new views. Moreover, other features such as PDF reports or
website pages need another tool to be created with more flexibility: a [templating](https://en.wikipedia.org/wiki/Template_processor) engine.

You might already be familiar with existing engines such as Jinja (Python), ERB (Ruby) or
Twig (PHP). Odoo comes with its own built-in engine: [QWeb Templates](../../reference/frontend/qweb.md#reference-qweb).
QWeb is the primary templating engine used by Odoo. It is an XML templating engine and used
mostly to generate HTML fragments and pages.

You probably already have come across the [kanban board](https://en.wikipedia.org/wiki/Kanban_board) in Odoo where the records are
displayed in a card-like structure. We will build such a view for our real estate module.

## Concrete Example: A Kanban View

**Reference**: the documentation related to this topic can be found in
[Kanban](../../reference/user_interface/view_architectures.md#reference-view-architectures-kanban).

#### NOTE
**Goal**: at the end of this section a Kanban view of the properties should be created:

![Kanban view](../../../.gitbook/assets/kanban1.png)

In our estate application, we would like to add a Kanban view to display our properties. Kanban
views are a standard Odoo view (like the form and list views), but their structure is much more
flexible. In fact, the structure of each card is a mix of form elements (including basic HTML)
and QWeb. The definition of a Kanban view is similar to the definition of the list and form
views, except that their root element is `<kanban>`. In its simplest form, a Kanban view
looks like:

```xml
<kanban>
    <templates>
        <t t-name="kanban-box">
            <div class="oe_kanban_global_click">
                <field name="name"/>
            </div>
        </t>
    </templates>
</kanban>
```

Let's break down this example:

- `<templates>`: defines a list of [QWeb Templates](../../reference/frontend/qweb.md#reference-qweb) templates. Kanban views *must* define at
  least one root template `kanban-box`, which will be rendered once for each record.
- `<t t-name="kanban-box">`: `<t>` is a placeholder element for QWeb directives. In this case,
  it is used to set the `name` of the template to `kanban-box`
- `<div class="oe_kanban_global_click">`: the `oe_kanban_global_click` makes the `<div>`
  clickable to open the record.
- `<field name="name"/>`: this will add the `name` field to the view.

Once the Kanban view is working, we can start improving it. If we want to display an element
conditionally, we can use the `t-if` directive (see [Conditionals](../../reference/frontend/qweb.md#reference-qweb-conditionals)).

```xml
<kanban>
    <field name="state"/>
    <templates>
        <t t-name="kanban-box">
            <div class="oe_kanban_global_click">
                <field name="name"/>
                <div t-if="record.state.raw_value == 'new'">
                    This is new!
                </div>
            </div>
        </t>
    </templates>
</kanban>
```

We added a few things:

- `t-if`: the `<div>` element is rendered if the condition is true.
- `record`: an object with all the requested fields as its attributes. Each field has
  two attributes `value` and `raw_value`. The former is formatted according to current
  user parameters and the latter is the direct value from a `read()`.

In the above example, the field `name` was added in the `<templates>` element, but `state`
is outside of it. When we need the value of a field but don't want to display it in the view,
it is possible to add it outside of the `<templates>` element.

Let's give the final touch to our view: the properties must be grouped by type by default. You
might want to have a look at the various options described in
[Kanban](../../reference/user_interface/view_architectures.md#reference-view-architectures-kanban).

Kanban views are a typical example of how it is always a good idea to start from an existing
view and fine tune it instead of starting from scratch. There are many options and classes
available, so... read and learn!
