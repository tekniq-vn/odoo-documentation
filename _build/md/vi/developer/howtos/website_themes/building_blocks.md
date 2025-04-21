# Building blocks

Building blocks, also known as snippets, are how users design and layout pages. They are important
XML elements of your design.

The building blocks are classified into four categories:

1. **Structure blocks**: to give a basic structure to the website
2. **Feature blocks**: to describe the features of a product or service
3. **Dynamic Content blocks**: blocks that are animated or interact with the backend
4. **Inner Content blocks**: blocks used inside other building blocks

At the end of this chapter, you will be able to [create custom snippets](#website-themes-building-blocks-custom) and to add them into a dedicated category.

<a id="website-themes-building-blocks-file-structure"></a>

## File structure

The layout's file structure is the following.

```default
views
├── snippets
│   └── options.xml
│   └── s_snippet_name.xml
```

The styles' file structure is the following.

```default
static
├── src
│   └── snippets
│       └── s_snippet_name
│           └── 000.js
│           └── 000.scss
│           └── 000.xml
│           └── options.js
```

#### SEE ALSO
[XML templates of the different snippets](https://github.com/odoo/odoo/blob/ccb78f7af2a4413836a969ff8009dc3df6c2df33/addons/website/views/snippets/snippets.xml)

<a id="website-themes-building-blocks-layout"></a>

## Layout

Snippets are editable by the user using the Website Builder. Some Bootstrap classes are important as
**they trigger some Website Builder options**.

<a id="website-themes-building-blocks-layout-wrapper"></a>

### Wrapper

The standard main container of any snippet is a `section`. Any section element can be edited like a
block of content that you can move or duplicate.

```xml
<section class="s_snippet_name" data-name="..." data-snippet="...">
    <!-- Content -->
</section>
```

For inner content snippets, any other HTML tag can be used.

```xml
<div class="s_snippet_name" data-name="..." data-snippet="...">
    <!-- Content -->
</div>
```

| Attribute    | Description                                                                                              |
|--------------|----------------------------------------------------------------------------------------------------------|
| class        | Unique class name for this snippet                                                                       |
| data-name    | Displayed in the right panel as the name of the snippet. If not found, it will fall back to<br/>*Block*. |
| data-snippet | Used by the system to identify the snippet                                                               |

The system automatically adds the `data-name` and `data-snippet` attributes during the drag and
drop based on the template's name.

#### WARNING
Those attributes should be specifically added when a snippet is declared on a theme page.

#### WARNING
Avoid adding a `section` tag inside another `section` tag: this will trigger twice the Website
Builder's options. You can use inner content snippets instead.

<a id="website-themes-building-blocks-layout-elements"></a>

### Elements

There is a list of "features" we can enable/disable by using specific CSS classes.

<a id="website-themes-building-blocks-layout-elements-sizing"></a>

#### Sizing

Any large Bootstrap columns directly descending from a `.row` element (respecting Bootstrap
structure) will be triggered by the Website Builder to make them resizable.

```css
.row > .col-lg-*
```

Add padding on columns and `<section>`.

```xml
class="pt80 pb80"
```

#### NOTE
`pb*` and `pt*` are the Odoo classes used to control the handlers. Their values are
increased by **multiples of 8**, till a **max of 256** (0, 8, 16, 24, 32, 40, 48, ...).

Enable the columns selector.

```xml
<div class="container s_allow_columns">
```

Disable the columns amount option.

```xml
<div class="row s_nb_column_fixed">
```

Disable the size option for all child columns.

```xml
<div class="row s_col_no_resize">
```

Disable the size option for one specific column.

```xml
<div class="col-lg-* s_col_no_resize">
```

<a id="website-themes-building-blocks-layout-elements-colors"></a>

#### Colors

Add a background based on the color palette for columns and `<section>`.

```xml
class="o_cc o_cc*"
```

Disable the background color option for all columns.

```xml
<div class="row s_col_no_bgcolor">
```

Disable the background color option of one specific column.

```xml
<div class="col-lg-* s_col_no_bgcolor">
```

Add a black color filter with an opacity of 50%.

```xml
<section>
    <div class="o_we_bg_filter bg-black-50"/>
    <div class="container">
        <!-- Content -->
    </div>
</section>
```

Add a white color filter with an opacity of 85%.

```xml
<section>
    <div class="o_we_bg_filter bg-white-85"/>
    <div class="container">
        <!-- Content -->
    </div>
</section>
```

Add a custom color filter.

```xml
<section>
    <div class="o_we_bg_filter" style="background-color: rgba(39, 110, 114, 0.54) !important;"/>
    <div class="container">
        <!-- Content -->
    </div>
</section>
```

Add a custom gradient filter.

```xml
<section>
    <div class="o_we_bg_filter" style="background-image: linear-gradient(135deg, rgba(255, 204, 51, 0.5) 0%, rgba(226, 51, 255, 0.5) 100%) !important;"/>
    <div class="container">
        <!-- Content -->
    </div>
</section>
```

<a id="website-themes-building-blocks-layout-elements-features"></a>

#### Features

<a id="website-themes-building-blocks-layout-non-editable-areas"></a>

##### Non-editable areas

Make an element not editable.

```xml
<div class="o_not_editable">
```

Make an element not removable.

```xml
<div class="oe_unremovable">
```

<a id="website-themes-building-blocks-layout-background"></a>

##### Backgrounds

Add a background image and have it centered.

```xml
<div class="oe_img_bg o_bg_img_center" style="background-image: url('...')">
```

Add parallax effect.

```xml
<section class="parallax s_parallax_is_fixed s_parallax_no_overflow_hidden" data-scroll-background-ratio="1">
    <span class="s_parallax_bg oe_img_bg o_bg_img_center" style="background-image: url('...'); background-position: 50% 75%;"/>
    <div class="container">
        <!-- Content -->
    </div>
</section>
```

#### NOTE
A video background can be set on a section. Refer to the "[Media](media.md)" chapter of this documentation.

<a id="website-themes-building-blocks-layout-text-highlights"></a>

##### Text highlights

Text highlights are SVG files that can be incorporated onto specific words or phrases to emphasize them. Text highlights offer customizable options for colors and thickness.

![Example of text highlight](developer/howtos/website_themes/building_blocks/text-highlight.jpg)
```xml
<h2>
   Title with
   <span class="o_text_highlight o_text_highlight_fill" style="--text-highlight-width: 10px !important; --text-highlight-color: #FFFF00;">
      <span class="o_text_highlight_item">
         highlighted text
         <svg fill="none" class="o_text_highlight_svg o_content_no_merge position-absolute overflow-visible top-0 start-0 w-100 h-100 pe-none">
            <!-- SVG path -->
         </svg>
      </span>
   </span>
</h2>
```

| CSS custom property      | Description                  |
|--------------------------|------------------------------|
| `--text-highlight-width` | Thickness of the SVG borders |
| `--text-highlight-color` | Color of the SVG object      |

<a id="website-themes-building-blocks-layout-grid"></a>

### Grid layout

Grid Layout is a powerful and flexible layout system in CSS that enables users to design complex
building block layouts with ease.

<a id="website-themes-building-blocks-layout-grid-use"></a>

#### Use

Enable the Grid Layout by adding the `o_grid_mode` CSS class on the `row`. The number of rows in
your grid is defined by the `data-row-count` attribute. The grid always contains 12 columns. The
grid gap, specified in the `style` attribute, determines the gaps (or gutters) between rows and
columns.

```xml
<div class="row o_grid_mode" data-row-count="13" style="gap: 20px 10px">
   <!-- Content -->
</div>
```

<a id="website-themes-building-blocks-layout-grid-items"></a>

#### Items in a grid

Add items in the grid with the `o_grid_item` class. If the grid item contains an image, use the
`o_grid_item_image` class.

```xml
<div class="row o_grid_mode" data-row-count="13">
   <div class="o_grid_item g-height-* g-col-lg-*" style="grid-area: 2 / 1 / 7 / 8; z-index: 3;">
      <!-- Content -->
   </div>
   <div class="o_grid_item o_grid_item_image g-height-* g-col-lg-*" style="grid-area: 1 / 6 / 9 / 13; z-index: 2;">
      <img src="..." alt="..." >
   </div>
</div>
```

The dimensions and position of a grid item are defined by the grid-area that can be explicitly set
in the `style` attribute along with the z-index.

The `g-height-*` and `g-col-lg-*` classes are generated by the Website Builder for editing purposes.

<a id="website-themes-building-blocks-layout-grid-items-padding"></a>

#### Grid item padding

```xml
<div class="row o_grid_mode" data-row-count="13" style="gap: 20px 10px;">
   <div class="o_grid_item g-height-* g-col-lg-*" style="--grid-item-padding-y: 20px; --grid-item-padding-x: 15px; grid-area: 2 / 1 / 7 / 8; z-index: 3;">
      <!-- Content -->
   </div>
</div>
```

| CSS custom property     | Description                  |
|-------------------------|------------------------------|
| `--grid-item-padding-y` | Vertical paddings (Y axis)   |
| `--grid-item-padding-x` | Horizontal paddings (X axis) |

<a id="website-themes-building-blocks-compatibility"></a>

## Compatibility system

When a snippet has a `data-vcss`, `data-vjs` and/or `data-vxml` attribute, it means it is an updated
: version, not the original one.

```xml
<section class="s_snippet_name" data-vcss="001" data-vxml="001" data-js="001">
    <!-- Content -->
</section>
```

These data attributes indicate to the system which file version to load for that
snippet (e.g., `001.js`, `002.scss`).

<a id="website-themes-building-blocks-custom"></a>

## Custom snippet

To create a custom snippet, create first the snippet template. Then, add it to the list and make it
available via the Website Builder.

<a id="website-themes-building-blocks-custom-template"></a>

### Template

**Declaration**

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <template id="s_airproof_snippet" name="...">
        <section class="s_airproof_snippet">
            <!-- Content -->
        </section>
    </template>

</odoo>
```

#### WARNING
`data-name` and `data-snippet` attributes have to be specified when a snippet is declared on a
theme page. Otherwise, the snippet won't be recognised by the Website Builder and issues might
occur whenever a database upgrade is done. Additionally, remember that the name attribute is
shown as the name of your custom snippet in the Blocks section of the options panel.

Add your custom snippet to the list of standard snippets, so the user can drag and drop it on the
page, directly from the edit panel.

```xml
<template id="snippets" inherit_id="website.snippets" name="Airproof - Custom Snippets">
    <xpath expr="//*[@id='default_snippets']" position="before">
        <t id="x_theme_snippets">
            <div id="x_theme_snippets_category" class="o_panel">
                <div class="o_panel_header">Theme</div>
                <div class="o_panel_body">
                    <t t-snippet="website_airproof.s_airproof_snippet" t-thumbnail="/website_airproof/static/src/img/wbuilder/s_airproof_snippet.svg">
                        <keywords>Snippet</keywords>
                    </t>
                </div>
            </div>
        </t>
    </xpath>
</template>
```

| Attribute   | Description                                                            |
|-------------|------------------------------------------------------------------------|
| t-snippet   | The template to use                                                    |
| t-thumbnail | The path to the snippet thumbnail                                      |
| <keywords>  | Keywords entered by the user in the search field in the Snippets panel |

<a id="website-themes-building-blocks-custom-options"></a>

### Options

Options allow users to edit a snippet's appearance/behavior using the Website Builder. You can create
snippet options easily and automatically add them to the Website Builder.

#### SEE ALSO
[Standard snippet options](https://github.com/odoo/odoo/blob/ccb78f7af2a4413836a969ff8009dc3df6c2df33/addons/website/views/snippets/snippets.xml)

<a id="website-themes-building-blocks-custom-options-template"></a>

#### Template

There are a bunch of commands to set the options of a custom snippet. These options can be created
into `/website_airproof/views/snippets/s_airproof_snippet.xml`.

```xml
<template id="s_airproof_snippet_options" inherit_id="website.snippet_options" name="Airproof - Snippets Options">
   <xpath expr="." position="inside">
      <!-- Options -->
   </xpath>
</template>
```

Then insert the different available options:

```xml
<template id="s_airproof_snippet_options" inherit_id="website.snippet_options" name="Airproof - Snippets Options">
   <xpath expr="." position="inside">
      <div data-selector=".s_airproof_snippet">
         <we-select string="Layout">
            <we-button data-select-class="">Default</we-button>
            <we-button data-select-class="s_airproof_snippet_portrait">Portrait</we-button>
            <we-button data-select-class="s_airproof_snippet_square">Square</we-button>
            <we-button data-select-class="s_airproof_snippet_landscape">Landscape</we-button>
         </we-select>
         <we-title>Space</we-title>
         <we-button-group string="Before">
            <we-button data-select-class="mt-0">1</we-button>
            <we-button data-select-class="mt-3">2</we-button>
            <we-button data-select-class="mt-5">3</we-button>
         </we-button-group>
      </div>
   </xpath>
</template>
```

**Inner content**

Make a custom snippet "inner content" (droppable in an other building block) by extending the
`so_content_addition_selector` variable which contains all CSS selectors referring to the existing
inner content building blocks:

```xml
<template id="snippet_options" inherit_id="website.snippet_options" name="Airproof - Snippets Options">
   <xpath expr="//t[@t-set='so_content_addition_selector']" position="after">
      <t t-set="so_content_addition_selector"
         t-value="so_content_addition_selector + ', .s_airproof_snippet'" />
   </xpath>
</template>
```

#### SEE ALSO
[Standard "inner content" snippets declaration on Odoo's GitHub repository](https://github.com/odoo/odoo/blob/f922f09b83c68dff36c064d20709a6e6ba4541dc/addons/website/views/snippets/snippets.xml#L720)

<a id="website-themes-building-blocks-custom-options-binding"></a>

#### Binding

These options use CSS selectors (class, XML tag, id, etc).

<a id="website-themes-building-blocks-custom-options-binding-data-selector"></a>

##### data-selector

Options are wrapped in groups. Groups can have properties that define how the included options
interact with the user interface.

`data-selector` binds all the options included in the group to a particular element matching the
selector value (CSS class, ID, etc). The option will appear when the matching selector is selected.

```xml
<div data-selector="section, h1, .custom_class, #custom_id">
```

It can be used in combination with other attributes like `data-target`, `data-exclude` or
`data-apply-to`.

<a id="website-themes-building-blocks-custom-options-binding-data-target"></a>

##### data-target

`data-target=""` allows to apply the option to a child element of the `data-selector=""`.

```xml
<div
   data-selector=".s_airproof_snippet"
   data-target=".row">
```

<a id="website-themes-building-blocks-custom-options-binding-data-exclude"></a>

##### data-exclude

`data-exclude=""` allows to exclude some particular selectors from the rule.

```xml
<div
   data-selector="ul"
   data-exclude=".navbar-nav">
```

<a id="website-themes-building-blocks-custom-options-binding-data-drop-in"></a>

##### data-drop-in

`data-drop-in` defines the list of elements where the snippet can be dropped into.

```xml
<div data-selector=".s_airproof_snippet" data-drop-in=".x_custom_location">
```

<a id="website-themes-building-blocks-custom-options-binding-data-drop-near"></a>

##### data-drop-near

`data-drop-near` defines the list of elements where the snippet can be dropped beside.

```xml
<div data-selector=".s_airproof_snippet_card" data-drop-near=".card">
```

<a id="website-themes-building-blocks-custom-options-binding-data-js"></a>

##### data-js

`data-js` binds a custom JavaScript methods.

```xml
<div data-selector=".s_airproof_snippet" data-js="CustomMethodName">
```

<a id="website-themes-building-blocks-custom-options-layout-fields"></a>

#### Layout & fields

<a id="website-themes-building-blocks-custom-options-layout-fields-we-title"></a>

##### `<we-title>`

Add titles between options to categorize them.

```xml
<we-title>Option subtitle 1</we-title>
```

![Add a subtitle between custom options](developer/howtos/website_themes/building_blocks/we-title.jpg)

<a id="website-themes-building-blocks-custom-options-layout-fields-we-row"></a>

##### `<we-row>`

Create a row in which elements is displayed next to each other.

```xml
<we-row string="My option">
   <we-select>...</we-select>
   <we-button-group>...</we-button-group>
</we-row>
```

The perfect example for this case is the Animation row:

![Group different option fields into the same row.](developer/howtos/website_themes/building_blocks/we-row.png)

<a id="website-themes-building-blocks-custom-options-layout-fields-we-button"></a>

##### `<we-button>`

This tag is used inside `<we-select>` and `<we-button-group>`.

```xml
<we-button-group string="Before">
   <we-button data-select-class="mt-0">1</we-button>
   <we-button data-select-class="mt-3">2</we-button>
   <we-button data-select-class="mt-5">3</we-button>
</we-button-group>
```

Add `data-select-class=""` to indicate which class is added to the targeted element when this
choice is selected. Like any XML node, add other attributes allows to improve the style and/or the
user experience.

```xml
<we-button
   class="fa fa-fw fa-angle-double-right"
   title="Move to last"
   data-position="last" />
```

![Add option choices and style them with some icons](developer/howtos/website_themes/building_blocks/we-button.jpg)

<a id="website-themes-building-blocks-custom-options-layout-fields-we-select"></a>

##### `<we-select>`

Formats the option as a dropdown list. Add `string=""` to indicate the field name.

```xml
<we-select string="Layout">...</we-select>
```

![Add a dropddown list field](developer/howtos/website_themes/building_blocks/we-select.jpg)

<a id="website-themes-building-blocks-custom-options-layout-fields-we-button-group"></a>

##### `<we-button-group>`

Formats the option as buttons next to each other.

```xml
<we-button-group string="Before">...</we-button-group>
```

![Add a dropddown list field](developer/howtos/website_themes/building_blocks/we-button-group.jpg)

<a id="website-themes-building-blocks-custom-options-layout-fields-we-checkbox"></a>

##### `<we-checkbox>`

Formats the option as a toggle switch.

```xml
<we-checkbox
   string="Tooltip"
   data-select-class="s_airproof_snippet_tooltip" />
```

![Add a toggle switch.](developer/howtos/website_themes/building_blocks/we-checkbox.jpg)

<a id="website-themes-building-blocks-custom-options-layout-fields-we-range"></a>

##### `<we-range>`

Formats the option as a slider.

```xml
<we-range
   string="Images Spacing"
   data-select-class="o_spc-none|o_spc-small|o_spc-medium|o_spc-big" />
```

Each step of the range is separated by a `|`. Here, each class name corresponds to a step.

![Add a toggle switch.](developer/howtos/website_themes/building_blocks/we-range.jpg)

<a id="website-themes-building-blocks-custom-options-layout-fields-we-input"></a>

##### `<we-input>`

Formats the option as a text field.

```xml
<we-input
   string="Speed"
   data-unit="s"
   data-save-unit="ms"
   data-step="0.1" />
```

![Add a text field.](developer/howtos/website_themes/building_blocks/we-input.jpg)

`<we-input>` comes with optional attributes particularly useful in specific case:

| Attribute        | Description                                                                            |
|------------------|----------------------------------------------------------------------------------------|
| `data-unit`      | Shows the expected unit of measure.                                                    |
| `data-save-unit` | Set the unit of measure to which the value entered by the user is converted and saved. |
| `data-step`      | Set the numerical value by which the field can be incremented.                         |

<a id="website-themes-building-blocks-custom-options-layout-fields-we-colorpicker"></a>

##### `<we-colorpicker>`

Formats the option as a color/gradient to choose from.

```xml
<we-colorpicker
   string="Color filter"
   data-select-style="true"
   data-css-property="background-color"
   data-color-prefix="bg-"
   data-apply-to=".s_map_color_filter" />
```

![Add a colorpicker.](developer/howtos/website_themes/building_blocks/we-colorpicker.jpg)

| Attribute           | Description                                                                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `data-select-style` | Refers to `selectStyle` JavaScript method. Matchs the value of the `style=""` attribute<br/>applied on the target to thick the right option choice. |
| `data-css-property` | Define the CSS property targeted by the colorpicker.                                                                                                |
| `data-color-prefix` | Define the prefix applied to the CSS class returned.                                                                                                |
| `data-apply-to`     | Set the element on which the color is applied.                                                                                                      |

<a id="website-themes-building-blocks-custom-options-methods"></a>

#### Methods

Beside *binding options* allowing to select, target or exclude an element. Option fields have
several useful data attributes refering to standard JavaScript methods.

For example, `data-select-class` refers to the JavaScript method named `selectClass`.

<a id="website-themes-building-blocks-custom-options-methods-builtin"></a>

##### Built-in methods

<a id="website-themes-building-blocks-custom-options-methods-builtin-selection"></a>

###### Selection

There are several built-in methods available. They are callable by using the related data attribute
directly into the XML template.

| Data attributes                                      | Description                                                                                                                                            |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `data-select-class`                                  | Allows to select one and only one class in the option classes<br/>set and set it on the associated snippet.                                            |
| `data-select-data-attribute` + `data-attribute-name` | Allows to select a value and set it on the associated snippet as an attribute. The attribute<br/>name is given by the `data-attribute-name` attribute. |
| `data-select-property` + `data-property-name`        | Allows to select a value and set it on the associated snippet as a property. The attribute<br/>name is given by the `data-property-name` attribute.    |
| `data-select-style` + `data-css-property`            | Allows to select a value and set it on the associated snippet as a CSS style. The attribute<br/>name is given by the `data-css-property` attribute.    |
| `data-select-color-combination`                      | Enable the selection of a color palette.<br/>**Only for** `<we-colorpicker>`                                                                           |

<a id="website-themes-building-blocks-custom-options-methods-builtin-events"></a>

###### Events

There are also built-in methods directly linked to events the Website Builder listens to:

| Name         | Description                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| start        | Occurs when the publisher selects the snippet for the first time in an editing session or<br/>when the snippet is drag-and-dropped on the page.  |
| destroy      | Occurs after the publisher has saved the page.                                                                                                   |
| onFocus      | Occurs each time the snippet is selected by the user or when the snippet is drag-and-dropped<br/>on the page.                                    |
| onBlur       | Occurs when a snippet loses focus.                                                                                                               |
| onClone      | Occurs just after a snippet is duplicated.                                                                                                       |
| onRemove     | Occurs just before the snippet is removed.                                                                                                       |
| onBuilt      | Occurs just after the snippet is drag-and-dropped on a drop zone. When this event is<br/>triggered, the content is already inserted in the page. |
| cleanForSave | Occurs before the publisher saves the page.                                                                                                      |

#### SEE ALSO
- [Web Editor - JavaScript methods related to snippet options on GitHub](https://github.com/odoo/odoo/blob/380c9153b5fa9a0ea6d7ae485ef52a16ae999eda/addons/web_editor/static/src/js/editor/snippets.options.js#L3247)
- [XML templates of the different snippets](https://github.com/odoo/odoo/blob/ccb78f7af2a4413836a969ff8009dc3df6c2df33/addons/website/views/snippets/snippets.xml)

<a id="website-themes-building-blocks-custom-options-methods-custom"></a>

##### Custom methods

To create custom JavaScript methods, a link between the options group and the custom methods has to
be created. To do so, a JavaScript class has to be created and called in the XML template with
`data-js`.

Add the `data-js` attribute to your options group:

```xml
<template id="s_airproof_snippet_options" inherit_id="website.snippet_options" name="Airproof - Snippets Options">
   <xpath expr="." position="inside">
      <div data-selector=".s_airproof_snippet" data-js="airproofSnippet">
         // Options
      </div>
   </xpath>
</template>
```

Then, the class can be created in a JavaScript file:

```javascript
/** @odoo-module */

import options from 'web_editor.snippets.options';

const AirproofSnippet = options.Class.extend({
   // Built-in method example
   start: function() {
      //...
   }
   // Custom method example
   customMethodName: function() {
      //...
   }
});

options.registry.AirproofSnippet = AirproofSnippet;

export default AirproofSnippet;
```

Finally, the custom method can be called on your custom option through the XML template:

```xml
<template id="s_airproof_snippet_options" inherit_id="website.snippet_options" name="Airproof - Snippets Options">
   <xpath expr="." position="inside">
      <div data-selector=".s_airproof_snippet" data-js="airproofSnippet">
         <we-checkbox data-custom-method-name="" />
      </div>
   </xpath>
</template>
```

<a id="website-themes-building-blocks-custom-dynamic"></a>

### Dynamic Content templates

By default, Dynamic Content blocks have a selection of templates available in the Website Builder.
Custom templates can also be added to the list automatically by use the same naming convention for
the template id attribute.

<a id="website-themes-building-blocks-custom-dynamic-call"></a>

#### Call the template

The selected dynamic snippet replace the `<div class="dynamic_snippet_template"/>` placeholder by
the right template based on the `data-template-key` and the custom CSS class:

```xml
<section
   data-snippet="s_blog_posts"
   data-name="Blog Posts"
   class="s_blog_post_airproof s_dynamic_snippet_blog_posts s_blog_posts_effect_marley s_dynamic pb32 o_cc o_cc2 o_dynamic_empty"
   data-template-key="website_airproof.dynamic_filter_template_blog_post_airproof"
   data-filter-by-blog-id="-1"
   data-number-of-records="3"
   data-number-of-elements="3"
>
   <div class="container o_not_editable">
      <div class="css_non_editable_mode_hidden">
            <div class="missing_option_warning alert alert-info rounded-0 fade show d-none d-print-none">
               Your Dynamic Snippet will be displayed here... This message is displayed because you did not provided both a filter and a template to use.<br/>
            </div>
      </div>
      <div class="dynamic_snippet_template"/>
   </div>
</section>
```

<a id="website-themes-building-blocks-custom-dynamic-examples"></a>

#### Examples

Blog posts

```xml
<template id="dynamic_filter_template_blog_post_airproof" name="...">
   <div t-foreach="records" t-as="data" class="s_blog_posts_post">
      <t t-set="record" t-value="data['_record']"/>
      <!-- Content -->
   </div>
</template>
```

| Attribute   | Description                                                                    |
|-------------|--------------------------------------------------------------------------------|
| id          | The ID of the template. Has to start with `dynamic_filter_template_blog_post_` |
| name        | Human-readable name of the template                                            |

Products

```xml
<template id="dynamic_filter_template_product_product_airproof" name="...">
   <t t-foreach="records" t-as="data" data-number-of-elements="4" data-number-of-elements-sm="1" data-number-of-elements-fetch="8">
      <t t-set="record" t-value="data['_record']"/>
      <!-- Content -->
   </t>
</template>
```

| Attribute                     | Description                                                                          |
|-------------------------------|--------------------------------------------------------------------------------------|
| id                            | The ID of the template. Has to start with `dynamic_filter_template_product_product_` |
| name                          | Human-readable name of the template                                                  |
| data-number-of-elements       | Number of products per slide on desktop                                              |
| data-number-of-elements-sm    | Number of products per slide on mobile                                               |
| data-number-of-elements-fetch | The total amount of fetched products                                                 |

Events

```xml
<template id="dynamic_filter_template_event_event_airproof" name="...">
   <div t-foreach="records" t-as="data" class="s_events_event">
      <t t-set="record" t-value="data['_record']._set_tz_context()"/>
      <!-- Content -->
   </div>
</template>
```

| Attribute   | Description                                                                      |
|-------------|----------------------------------------------------------------------------------|
| id          | The ID of the template. Has to start with `dynamic_filter_template_event_event_` |
| name        | Human-readable name of the template                                              |
