# Layout

In this chapter, you will learn how to:

- Create a custom header.
- Create a custom footer.
- Modify a standard template.
- Add a copyright section.
- Improve your website's responsiveness.

<a id="website-themes-layout-default"></a>

## Default

An Odoo page combines cross-page and unique elements. Cross-page elements are the same on every
page, while unique elements are only related to a specific page. By default, a page has two
cross-page elements, the header and the footer, and a unique main element that contains the specific
content of that page.

```xml
<div id="wrapwrap">
   <header/>
      <main>
         <div id="wrap" class="oe_structure">
            <!-- Page Content -->
         </div>
      </main>
   <footer/>
</div>
```

Any Odoo XML file starts with encoding specifications. After that, you must write your code inside
an `<odoo>` tag.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<odoo>
   ...
</odoo>
```

#### NOTE
Using precise template names is important to find information through all modules quickly.
Template names should only contain lowercase alphanumerics and underscores.

Always add an empty line at the end of your file. This can be done automatically by configuring
your IDE.

<a id="website-themes-layout-xpath"></a>

## XPath

XPath (XML Path Language) is an expression language that enables you to navigate through elements
and attributes in an XML document easily. XPath is used to extend standard Odoo templates.

A view is coded the following way.

```xml
<template id="..." inherit_id="..." name="...">
   <!-- Content -->
</template>
```

| Attribute    | Description                                                              |
|--------------|--------------------------------------------------------------------------|
| id           | ID of the modified view                                                  |
| inherited_id | ID of the standard view (using the following pattern: `module.template`) |
| name         | Human-readable name of the modified view                                 |

For each XPath, you modify two attributes: **expression** and **position**.

#### WARNING
Be careful when replacing default elements' attributes. As your theme extends the default one,
your changes will take priority over any future Odoo update.

#### NOTE
- You should update your module every time you create a new template or record.
- *XML IDs* of inheriting views should use the same *ID* as the original record. It helps to find
  all inheritance at a glance. As final *XML IDs* are prefixed by the module that creates them,
  there is no overlap.

<a id="website-themes-layout-xpath-expressions"></a>

### Expressions

XPath uses path expressions to select nodes in an XML document. Selectors are used inside the
expression to target the right element. The most useful ones are listed below.

| Descendent selectors   | Description                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------------------|
| /                      | Selects from the root node.                                                                                  |
| //                     | Selects nodes in the document from the current node that matches the selection no matter<br/>where they are. |

| Attribute selectors   | Description                                                                                               |
|-----------------------|-----------------------------------------------------------------------------------------------------------|
| \*                    | Selects any XML tag. `*` can be replaced by a specific tag if the selection needs to be<br/>more precise. |
| \*[@id="id"]          | Selects a specific ID.                                                                                    |
| \*[hasclass("class")] | Selects a specific class.                                                                                 |
| \*[@name="name"]      | Selects a tag with a specific name.                                                                       |
| \*[@t-call="t-call"]  | Selects a specific t-call.                                                                                |

<a id="website-themes-layout-xpath-position"></a>

### Position

The position defines where the code is placed inside the template. The possible values are listed
below:

| Position   | Description                                        |
|------------|----------------------------------------------------|
| replace    | Replaces the targeted node with the XPath content. |
| inside     | Adds the XPath content inside the targeted node.   |
| before     | Adds the XPath content before the targeted node.   |
| after      | Adds the XPath content after the targeted node.    |
| attributes | Adds the XPath content inside an attribute.        |

#### SEE ALSO
You can find more information about XPath in this [cheat sheet](https://devhints.io/xpath).

<a id="website-themes-layout-qweb"></a>

## QWeb

QWeb is the primary templating engine used by Odoo. It is an XML templating engine mainly used to
generate HTML fragments and pages.

#### SEE ALSO
[QWeb templates documentation](../../reference/frontend/qweb.md).

<a id="website-themes-layout-custom-fields"></a>

## Custom fields

Depending on your needs, you can create custom fields to save data in the database.

<a id="website-themes-layout-custom-fields-declaration"></a>

### Declaration

First, create a record to declare the field. This field has to be linked to an existing model.

```xml
<record id="x_post_category" model="ir.model.fields">
   <field name="name">x_post_category</field>
   <field name="field_description">...</field>
   <field name="ttype">html</field>
   <field name="state">manual</field>
   <field name="index">0</field>
   <field name="model_id" ref="website_blog.model_blog_post"/>
</record>
```

#### NOTE
Fields creation is also possible (and recommended) through [a model using Python](/developer/tutorials/backend).

<a id="website-themes-layout-custom-fields-backend"></a>

### Back-end

Add the field to the relevant view through an XPath. Therefore, the user can see the field in the
interface and fill it afterwards.

```xml
<record id="view_blog_post_form_category" model="ir.ui.view">
   <field name="name">view_blog_post_form_category</field>
   <field name="model">blog.post</field>
   <field name="inherit_id" ref="website_blog.view_blog_post_form"/>
   <field name="arch" type="xml">
      <xpath expr="//field[@name='blog_id']" position="before">
         <field name="x_post_category" string="..." placeholder="..."/>
      </xpath>
   </field>
</record>
```

<a id="website-themes-layout-custom-fields-frontend"></a>

### Front-end

The field value can be shown somewhere in a page by calling `model_name.field_name` like this:

```xml
<h1 t-field="blog_post.x_post_category"/>
```

<a id="website-themes-layout-background"></a>

## Background

You can define a color or an image as the background of your website.

<a id="website-themes-layout-background-colors"></a>

### Colors

```scss
$o-color-palettes: map-merge($o-color-palettes,
   (
      'airproof': (
         'o-cc1-bg':                     'o-color-5',
         'o-cc5-bg':                     'o-color-1',
      ),
    )
);
```

<a id="website-themes-layout-background-image-pattern"></a>

### Image/pattern

```scss
$o-website-values-palettes: (
   (
      'body-image': '/website_airproof/static/src/img/background-lines.svg',
      'body-image-type': 'image' or 'pattern'
   )
);
```

<a id="website-themes-layout-header"></a>

## Header

By default, the header contains two distinct templates (desktop and mobile) which display the  main
navigation, the company's logo and other optional elements (call-to-action, language selector, etc).
Depending on the situation, choose between enabling/disabling existing elements with a standard
template or building a brand new custom template.

<a id="website-themes-layout-header-standard"></a>

### Standard

The Odoo Website Builder distinguishes between desktop templates and the mobile template in order to
facilitate the adaptation of the user experience according to the device.

<a id="website-themes-layout-header-standard-desktop"></a>

#### Desktop template

Enable one of the header default templates.

#### IMPORTANT
Don't forget that you may need to disable the active header template first.

Explicitly set the desired template in the `primary_variables.scss` file.

```scss
$o-website-values-palettes: (
   (
      'header-template': 'Contact',
   ),
);
```

```xml
<record id="website.template_header_contact" model="ir.ui.view">
   <field name="active" eval="True"/>
</record>
```

<a id="website-themes-layout-header-standard-mobile"></a>

#### Mobile template

Each header template comes with the `template_header_mobile` template ensuring a seamless user
experience accross every devices.

#### SEE ALSO
[Mobile header template on Odoo's Git repository](https://github.com/odoo/odoo/blob/d053ea84d45f2ba50a31c2773f2d3ded9fd1ee6b/addons/website/views/website_templates.xml#L343)

<a id="website-themes-layout-header-custom"></a>

### Custom

Create your own template and add it to the list.

#### IMPORTANT
Don't forget that you may need to disable the active header template first.

**Option**

Use the following code to add an option for your new custom header on the Website Builder.

```xml
<template id="template_footer_opt" inherit_id="website.snippet_options" name="Footer Template - Option">
   <xpath expr="//we-select[@data-variable='footer-template']" position="inside">
      <we-button title="airproof"
         data-customize-website-views="website_airproof.footer"
         data-customize-website-variable="'airproof'"  data-img="/website_airproof/static/src/img/wbuilder/template_footer_opt.svg"/>
   </xpath>
</template>
```

| Attribute                       | Description                                                                                  |
|---------------------------------|----------------------------------------------------------------------------------------------|
| data-customize-website-views    | The template to enable                                                                       |
| data-customize-website-variable | The name given to the variable                                                               |
| data-img                        | The thumbnail of the custom template shown in the templates selection on the Website Builder |

Now you have to explicitly define that you want to use your custom template in the Odoo SASS
variables.

```scss
$o-website-values-palettes: (
   (
      'header-template': 'airproof',
   ),
);
```

**Template**

```xml
<record id="header" model="ir.ui.view">
   <field name="name">Airproof Header</field>
   <field name="type">qweb</field>
   <field name="key">website_airproof.header</field>
   <field name="inherit_id" ref="website.layout"/>
   <field name="mode">extension</field>
   <field name="arch" type="xml">
      <xpath expr="//header//nav" position="replace">
         <!-- Static Content -->
         <!-- Components -->
         <!-- Editable areas -->
      </xpath>
   </field>
</record>
```

Don't forget to adapt the `template_header_mobile` accordingly to keep consistency between desktop
and mobile:

```xml
<template id="template_header_mobile" inherit_id="website.template_header_mobile" name="Airproof - Template Header Mobile">
   <!-- Xpaths -->
</template>
```

<a id="website-themes-layout-header-components"></a>

### Components

In your custom header, you can call several sub-templates using the `t-call` directive from QWeb:

<a id="website-themes-layout-header-components-logo"></a>

#### Logo

```xml
<t t-call="website.placeholder_header_brand">
   <t t-set="_link_class" t-valuef="..."/>
</t>
```

#### IMPORTANT
Don't forget to [create a record of the website logo](media.md#website-themes-media-images-use-logo)
logo in the database.

<a id="website-themes-layout-headers-components-menu"></a>

#### Menu

```xml
<t t-foreach="website.menu_id.child_id" t-as="submenu">
   <t t-call="website.submenu">
      <t t-set="item_class" t-valuef="nav-item"/>
      <t t-set="link_class" t-valuef="nav-link"/>
   </t>
</t>
```

<a id="website-themes-layout-header-components-signin"></a>

#### Sign in

```xml
<t t-call="portal.placeholder_user_sign_in">
   <t t-set="_item_class" t-valuef="nav-item"/>
   <t t-set="_link_class" t-valuef="nav-link"/>
</t>
```

<a id="website-themes-layout-header-components-user-dropdown"></a>

#### User dropdown

```xml
<t t-call="portal.user_dropdown">
   <t t-set="_user_name" t-value="true"/>
   <t t-set="_icon" t-value="false"/>
   <t t-set="_avatar" t-value="false"/>
   <t t-set="_item_class" t-valuef="nav-item dropdown"/>
   <t t-set="_link_class" t-valuef="nav-link"/>
   <t t-set="_dropdown_menu_class" t-valuef="..."/>
</t>
```

<a id="website-themes-layout-header-components-language-selector"></a>

#### Language selector

```xml
<t t-call="website.placeholder_header_language_selector">
   <t t-set="_div_classes" t-valuef="..."/>
</t>
```

<a id="website-themes-layout-header-components-cta"></a>

#### Call to action

```xml
<t t-call="website.placeholder_header_call_to_action">
   <t t-set="_div_classes" t-valuef="..."/>
</t>
```

<a id="website-themes-layout-header-components-navbar-toggler"></a>

#### Navbar toggler

```xml
<t t-call="website.navbar_toggler">
   <t t-set="_toggler_class" t-valuef="..."/>
</t>
```

#### SEE ALSO
You can add a [header overlay](pages.md#website-themes-pages-theme-pages-header-overlay) to position your header over the content of
your page. It has to be done on each page individually.

<a id="website-themes-layout-footer"></a>

## Footer

By default, the footer contains a section with some static content. You can easily add new elements
or create your own template.

<a id="website-themes-layout-footer-standard"></a>

### Standard

Enable one of the default footer templates. Don't forget that you may need to disable the active
footer template first.

#### IMPORTANT
Don't forget that you may need to disable the active footer template first.

```scss
$o-website-values-palettes: (
   (
      'footer-template': 'Links',
   ),
);
```

```xml
<record id="website.template_footer_links" model="ir.ui.view">
   <field name="active" eval="True"/>
</record>
```

<a id="website-themes-layout-footer-custom"></a>

### Custom

Create your own template and add it to the list. Don't forget that you may need to disable the
active footer template first.

**Option**

```xml
<template id="template_header_opt" inherit_id="website.snippet_options" name="Footer Template - Option">
   <xpath expr="//we-select[@data-variable='footer-template']" position="inside">
      <we-button title="airproof"
         data-customize-website-views="website_airproof.footer"
         data-customize-website-variable="'airproof'"
         data-img="/website_airproof/static/src/img/wbuilder/template_header_opt.svg"/>
   </xpath>
</template>
```

**Declaration**

```scss
$o-website-values-palettes: (
   (
      'footer-template': 'airproof',
   ),
);
```

**Template**

```xml
<record id="footer" model="ir.ui.view">
   <field name="name">Airproof Footer</field>
   <field name="type">qweb</field>
   <field name="key">website_airproof.footer</field>
   <field name="inherit_id" ref="website.layout"/>
   <field name="mode">extension</field>
   <field name="arch" type="xml">
      <xpath expr="//div[@id='footer']" position="replace">
         <div id="footer" class="oe_structure oe_structure_solo" t-ignore="true" t-if="not no_footer">
            <!-- Content -->
         </div>
      </xpath>
   </field>
</record>
```

<a id="website-themes-layout-copyright"></a>

## Copyright

There is only one template available at the moment for the copyright bar.

To replace the content or modify its structure, you can add your own code to the following XPath.

```xml
<template id="copyright" inherit_id="website.layout">
   <xpath expr="//div[hasclass('o_footer_copyright')]" position="replace">
      <div class="o_footer_copyright" data-name="Copyright">
         <!-- Content -->
      </div>
   </xpath>
</template>
```

<a id="website-themes-layout-dropzone"></a>

## Drop zone

Instead of defining the complete layout of a page, you can create building blocks (snippets) and
let the user choose where to drag and drop them, creating the page layout on their own. We call
this *modular design*.

You can define an empty area that the user can fill with snippets.

```xml
<div id="oe_structure_layout_01" class="oe_structure"/>
```

| Class                    | Description                                                                                                                    |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| oe_structure             | Define a drag-and-drop area for the user.                                                                                      |
| oe_structure_solo        | Only one snippet can be dropped in this area.                                                                                  |
| oe_structure_not_nearest | If a building block is dropped outside of a Drop zone having this class, the block will be<br/>moved in the nearest Drop Zone. |

You can also populate an existing drop zone with your content.

```xml
<template id="oe_structure_layout_01" inherit_id="..." name="...">
   <xpath expr="//*[@id='oe_structure_layout_01']" position="replace">
      <div id="oe_structure_layout_01" class="oe_structure oe_structure_solo">
         <!-- Content -->
      </div>
   </xpath>
</template>
```

<a id="website-themes-layout-responsive"></a>

## Responsive

Odoo in general relies on the Bootstrap framework which eases the responsiveness of your website on
: desktop and mobile. On Odoo 16, you can mainly take action on 3 aspects:

1. Automatic computed font sizes depending on the device
2. Column sizes on desktop (the columns are automatically stacked on mobile)
3. Visibility conditions (Show/Hide something on desktop/mobile)

#### SEE ALSO
- [Bootstrap documentation on display property](https://getbootstrap.com/docs/5.1/utilities/display/)

<a id="website-themes-layout-reponsive-font-sizes"></a>

### Font sizes

In Bootstrap 5, responsive font sizes are enabled by default, allowing text to scale more naturally
across device and viewport sizes (relying on the `$enable-rfs` variable).

#### SEE ALSO
- [Bootstrap documentation about responsive font sizes](https://getbootstrap.com/docs/5.1/getting-started/rfs/)

<a id="website-themes-layout-reponsive-column-sizes"></a>

### Column sizes

Bootstrap uses a grid made of rows and columns to layout a page. Thanks to this structure, columns
can be sized differently on mobile and desktop. In this version, the Website Builder allows to set
mobile sizes (`col-12` for example) and desktop ones (`col-lg-4` for example) but not the
medium breakpoints (`col-md-4` for example).

#### WARNING
The medium sizes can be set but the end-user is not able to edit them within the Website Builder.

#### SEE ALSO
- [Bootstrap documentation on responsive breakpoints](https://getbootstrap.com/docs/5.1/layout/breakpoints/)
- [Bootstrap documentation about the grid](https://getbootstrap.com/docs/5.1/layout/grid/)

<a id="website-themes-layout-reponsive-visibility-conditions"></a>

### Visibility conditions

In the Odoo Website Builder, entire sections or specific columns can be hidden on mobile or desktop.
: This functionality leverages Bootstrap along with Odoo-specific classes:

- `o_snippet_mobile_invisible`
- `o_snippet_desktop_invisible`

Hide a section on desktop:

```xml
<section class="s_text_block o_cc o_cc1 o_colored_level pt16 pb16 d-lg-none o_snippet_desktop_invisible" data-snippet="s_text_block" name="Text">
    <!-- Content -->
</section>
```

Hide a column on mobile:

```xml
<section class="s_text_block o_cc o_cc1 o_colored_level pt16 pb16" data-snippet="s_text_block" name="Text">
   <div class="container s_allow_columns">
      <div class="row">
         <div class="col-12 col-lg-6 d-none d-lg-block o_snippet_mobile_invisible">
            Column 1
         </div>
         <div class="col-12 col-lg-6">
            Column 2
         </div>
      </div>
   </div>
</section>
```

| Class                       | Description                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| o_snippet_mobile_invisible  | It tells the Website Builder that the element is hidden and is using visibility conditions<br/>option.                |
| o_snippet_desktop_invisible | It tells the Website Builder that the element is hidden **on desktop and** is using visibility<br/>conditions option. |
| d-none                      | Hide the element in every situations.                                                                                 |
| d-lg-block                  | Show the element from the "large" breakpoint (on desktop).                                                            |

#### IMPORTANT
`o_snippet_mobile_invisible` / `o_snippet_desktop_invisible` classes have to be specified to keep
: the visibility conditions option functional. Even if an element is hidden on desktop, the
  Website Builder displays a list of these elements allowing the end-user to force show the
  element and edit it without switching between mobile and desktop mode.

![Force show a hidden element on the current device.](developer/howtos/website_themes/layout/screenshot-visibility.png)
