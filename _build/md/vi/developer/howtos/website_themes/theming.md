# Theming

After your development environment is fully set up, you can start building the skeleton of your
theme module. In this chapter, you will discover how to:

- Enable/disable the Website Builder's standard options and templates.
- Define the colors and fonts to use for your design.
- Get the most out of Bootstrap variables.
- Add custom styles and JavaScript.

<a id="theming-module"></a>

## Theme module

Odoo comes with a default theme that provides minimal structure and layout. When you create a new
theme, you are extending the default theme.

Remember to add the directory containing your module to the `addons-path` command-line argument
when running Odoo in your development environment.

<a id="theming-module-naming"></a>

### Technical naming

The first step is to create a new directory.

```xml
website_airproof
```

#### NOTE
Prefix it with `website_` and use only lowercase ASCII alphanumeric characters and underscores.

In this documentation, we will use **Airproof** (a fictional project) as an example.

<a id="theming-module-structure"></a>

### File structure

Themes are packaged like any Odoo module. Even if you are designing a basic website, you need to
package its theme like a module.

```default
website_airproof
├── data
├── i18n
├── static
│   ├── description
│   ├── fonts
│   ├── lib
│   ├── shapes // Shapes for background
│   └── src
│       ├── img
│       │   ├── content // For those used in the pages of your website
│       │   └── wbuilder // For those used in the builder
│       ├── js
│       ├── scss // Theme specific styles
│       └── snippets // custom snippets
├── views
├── __init__.py
└── __manifest__.py
```

| Folder   | Description                                                                   |
|----------|-------------------------------------------------------------------------------|
| data     | Presets, menus, pages, images, shapes, … (`*.xml`)                            |
| i18n     | Translations (`*.po`, `*.pot`)                                                |
| lib      | External libraries (`*.js`)                                                   |
| static   | Custom assets (`*.jpg`, `*.gif`, `*.png`, `*.svg`, `*.pdf`, `*.scss`, `*.js`) |
| views    | Custom views and templates (`*.xml`)                                          |

<a id="theming-module-initialization"></a>

### Initialization

An Odoo module is also a Python package with a `__init__.py` file containing import
instructions for various Python files in the module. This file can remain empty for now.

<a id="theming-module-declaration"></a>

### Declaration

An Odoo module is declared by its manifest file. This file declares a Python package as an Odoo
module and specifies the module's metadata. It must at least contain the `name` field, which is
always required. It usually contains much more information.

```python
{
   'name': 'Airproof Theme',
   'description': '...',
   'category': 'Website/Theme',
   'version': '17.0.0',
   'author': '...',
   'license': '...',
   'depends': ['website'],
   'data': [
      # ...
   ],
   'assets': {
      # ...
   },
}
```

| Field       | Description                                                                                                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| name        | Human-readable name of the module (required)                                                                                                          |
| description | Extended description of the module, in [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText)                                             |
| category    | Classification category within Odoo                                                                                                                   |
| version     | Odoo version this module is addressing                                                                                                                |
| author      | Name of the module author                                                                                                                             |
| license     | By default, we use the `LGPL-3` license. More information in the [module manifest](../../reference/backend/module.md#reference-module-manifest) page. |
| depends     | Odoo modules must be loaded before this one, either because this module uses features<br/>they create or because it alters resources they define      |
| data        | List of XML files                                                                                                                                     |
| assets      | List of SCSS and JS files                                                                                                                             |

#### NOTE
> - The file structure above is just a suggestion.  We could add as many other folders as needed in
>   the project, such as `/controllers` to include controllers or `/views/backend` for backend
>   views, etc.
> - To create a website theme, you only need to install the Website app. If you need other apps
>   (Blogs, Events, eCommerce, ...), you can also add them.
> - Odoo version and major number are mandatory. However, patch number is optional. If you want
>   to specify the required version of Odoo to run your module, you should use a five arguments
>   structure, using the first two arguments to indicate your current Odoo version (`* = 17.0`).
![Module versioning](developer/howtos/website_themes/theming/versioning.png)

Example:
`17.0.1.0.0`
`odoo_major.odoo_minor.module_major.module_minor.module_patch`

#### WARNING
Automated file inclusion using wildcard notations `(ex.: /myfolder/*.scss)` doesn't work in
Odoo SaaS databases. In this case, include each file manually in the manifest.

<a id="theming-options"></a>

## Default options

First, try to construct your theme by using Odoo's default options. This ensures two things:

1. You do not re-invent something which already exists. For example, as Odoo provides an option to
   add a border on the footer, you shouldn't recode it yourself. Instead, enable the default option
   first, then extend it if needed.
2. The user can still use all of Odoo's features with your theme. For example, if you recode the
   border on the footer, you may break the default option or make it useless, giving the user a bad
   experience. Also, your recode might not work as well as the default option, as other Odoo
   features may rely on it.

#### SEE ALSO
[Odoo coding guidelines](../../../contributing/development/coding_guidelines.md)

<a id="theming-module-variables"></a>

### Odoo variables

Odoo declares many CSS rules, most entirely customizable by overriding the related SCSS variables.
To do so, create a `primary_variables.scss` file and add it to the `_assets_primary_variables`
bundle.

**Declaration**

```python
'assets': {
   'web._assets_primary_variables': [
      'website_airproof/static/src/scss/primary_variables.scss',
   ],
},
```

By reading the source code, variables related to options are easily noticeable.

```xml
<we-button title="..."
   data-name="..."
   data-customize-website-views="..."
   data-customize-website-variable="'Sidebar'"
   data-img="..."/>
```

These variables can be overridden through the `$o-website-value-palettes` map, for example.

<a id="theming-module-variables-global"></a>

#### Global

**Declaration**

```scss
$o-website-values-palettes: (
   (
      // Templates
      // Colors
      // Fonts
      // Buttons
      // ...
   ),
);
```

#### SEE ALSO
[Primary variables SCSS](https://github.com/odoo/odoo/blob/34c0c9c1ae00aba391932129d4cefd027a9c6bbd/addons/website/static/src/scss/primary_variables.scss#L1954)

<a id="theming-module-variables-fonts"></a>

#### Fonts

You can embed any font on your website. The Website Builder automatically makes them available in
the font selector.

**Declaration**

```scss
$o-theme-font-configs: (
   <font-name>: (
      'family': <css font family list>,
      'url' (optional): <related part of Google fonts URL>,
      'properties' (optional): (
         <font-alias>: (
            <website-value-key>: <value>,
            ...,
         ),
      ...,
   )
)
```

**Use**

```scss
$o-website-values-palettes: (
   (
      'font':                             '<font-name>',
      'headings-font':                    '<font-name>',
      'navbar-font':                      '<font-name>',
      'buttons-font':                     '<font-name>',
   ),
);
```

<a id="theming-module-variables-fonts-google"></a>

##### Google fonts

```scss
$o-theme-font-configs: (
   'Poppins': (
      'family':                         ('Poppins', sans-serif),
      'url':                            'Poppins:400,500',
      'properties' : (
         'base': (
            'font-size-base':           1rem,
         ),
      ),
   ),
);
```

<a id="theming-module-variables-fonts-custom"></a>

##### Custom fonts

First, create a specific SCSS file to declare your custom font(s).

```python
'assets': {
   'web.assets_frontend': [
      'website_airproof/static/src/scss/font.scss',
   ],
},
```

Then, use the `@font-face` rule to allow you custom font(s) to be loaded on your website.

```scss
@font-face {
   font-family: "My Custom Font", Helvetica, Helvetica Neue, Arial, sans-serif;
   font-weight: 400;
   font-style: normal;
   src: url('/fonts/my-custom-font.woff') format('woff'),
        url('/fonts/my-custom-font.woff2') format('woff2');
}
```

```scss
$o-theme-font-configs: (
   'Proxima Nova': (
      'family':                         ('Proxima Nova', sans-serif),
      'properties' : (
         'base': (
            'font-size-base':           1rem,
         ),
      ),
   ),
);
```

<a id="theming-module-variables-colors"></a>

#### Colors

The Website Builder relies on palettes composed of five named colors. Defining those in your theme
ensures it stays consistent.

| Color     | Description   |
|-----------|---------------|
| o-color-1 | Primary       |
| o-color-2 | Secondary     |
| o-color-3 | Extra (Light) |
| o-color-4 | Whitish       |
| o-color-5 | Blackish      |
![Theme colors](developer/howtos/website_themes/theming/theme-colors.png)

**Declaration**

```scss
$o-color-palettes: map-merge($o-color-palettes,
   (
      'airproof': (
         'o-color-1':                    #bedb39,
         'o-color-2':                    #2c3e50,
         'o-color-3':                    #f2f2f2,
         'o-color-4':                    #ffffff,
         'o-color-5':                    #000000,
      ),
   )
);
```

Add the created palette to the list of palettes offered by the Website Builder.

```scss
$o-selected-color-palettes-names: append($o-selected-color-palettes-names, 'airproof');
```

**Use**

```scss
$o-website-values-palettes: (
   (
      'color-palettes-name':              'airproof',
   ),
);
```

![Theme colors Airproof](developer/howtos/website_themes/theming/theme-colors-airproof.png)

**Color combinations**

Based on the previously defined five color palettes, the Website Builder automatically generates
five color combinations, each defining a color for the background, text, headings, links, primary
buttons, and secondary buttons. These colors can be customized later by the user.

![Theme colors](developer/howtos/website_themes/theming/theme-colors-big.png)

The colors used in a color combination are accessible and can be overridden through
`$o-color-palettes` using a specific prefix (`o-cc` for `color combination`).

```scss
$o-color-palettes: map-merge($o-color-palettes,
   (
      'airproof': (

         'o-cc*-bg':                     'o-color-*',
         'o-cc*-text':                   'o-color-*',
         'o-cc*-headings':               'o-color-*',
         'o-cc*-h2':                     'o-color-*',
         'o-cc*-h3':                     'o-color-*',
         'o-cc*-h4':                     'o-color-*',
         'o-cc*-h5':                     'o-color-*',
         'o-cc*-h6':                     'o-color-*',
         'o-cc*-link':                   'o-color-*',
         'o-cc*-btn-primary':            'o-color-*',
         'o-cc*-btn-primary-border':     'o-color-*',
         'o-cc*-btn-secondary':          'o-color-*',
         'o-cc*-btn-secondary-border':   'o-color-*',

      ),
   )
);
```

#### NOTE
For each `o-cc*`, replace the `*` with the digit (1 - 5) corresponding to the desired color
combination.

The default text color is `o-color-5`. If the background is too dark, it will automatically
change to the `o-color-4` color.

#### SEE ALSO
[Color combinations SCSS](https://github.com/odoo/odoo/blob/34c0c9c1ae00aba391932129d4cefd027a9c6bbd/addons/web_editor/static/src/scss/web_editor.common.scss#L711)

<a id="theming-module-variables-gradients"></a>

#### Gradients

You can also define gradients for the menu, header, footer and copyright bar, directly in your
`primary_variables.scss` file.

**Declaration**

```scss
$o-website-values-palettes: (
   (
      'menu-gradient': linear-gradient(135deg, rgb(203, 94, 238) 0%, rgb(75, 225, 236) 100%),
      'header-boxed-gradient': [your-gradient],
      'footer-gradient': [your-gradient],
      'copyright-gradient': [your-gradient],
   ),
);
```

<a id="theming-module-bootstrap"></a>

### Bootstrap variables

Odoo includes Bootstrap by default. You can use all variables and mixins of the framework.

If Odoo does not provide the variable you are looking for, there could be a Bootstrap variable that
allows it. Indeed all Odoo layouts respect Bootstrap structures and use Bootstrap components or
their extensions. If you customize a Bootstrap variable, you add a generic style for the whole user
website.

Use a dedicated file added to the `_assets_frontend_helpers` bundle to override Bootstrap
values and *not* the `primary_variables.scss` file.

**Declaration**

```python
'assets': {
   'web._assets_frontend_helpers': [
      ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
   ],
},
```

**Use**

```scss
// Typography
$h1-font-size:                 4rem !default;

// Navbar
$navbar-nav-link-padding-x:    1rem!default;

// Buttons + Forms
$input-placeholder-color:      o-color('o-color-1') !default;

// Cards
$card-border-width:            0 !default;
```

#### WARNING
Don't override Bootstrap variables that depend on Odoo variables. Otherwise, you might break the
possibility for the user to customize them using the Website Builder.

When an option is defined by a variable in `primary_variables.scss` and by a Boostrap variable,
you should always go for an override through the primary variables. Do it via
`bootstrap_overridden.scss` only if nothing exists in the primary variables.

#### SEE ALSO
[Bootstrap overridden SCSS](https://github.com/odoo/odoo/blob/17.0/addons/web/static/lib/bootstrap/scss/_variables.scss)

<a id="theming-module-bootstrap-fonts"></a>

#### Font sizes

Odoo has CSS font size classes to separate style (font sizes) and semantic (tag and styles in
general). Both logic can be combined to be more flexible.

#### SEE ALSO
[Bootstrap documentation about display headings](https://getbootstrap.com/docs/5.1/content/typography/#display-headings)

<a id="theming-module-bootstrap-fonts-text"></a>

##### Text style

Odoo's Website Builder allows to select a style for your text. Some are just tag related like the
`Header` with no extra CSS class. Other combine tag and style directly applied on them like the
`Header 1 Display`.

![Header styles](developer/howtos/website_themes/theming/header.png)
```xml
<!-- h1 with display heading sizes -->
<h1 class="display-1">Heading 1 with Display Heading 1 size</h1>
<h1 class="display-2">Heading 1 with Display Heading 2 size</h1>
<h1 class="display-3">Heading 1 with Display Heading 3 size</h1>
<h1 class="display-4">Heading 1 with Display Heading 4 size</h1>

<!-- Lead text - named "Light" in the dropdown -->
<p class="lead">A text typically used as an introduction.</p>

<!-- Small text -->
<p class="o_small">Body text with a smaller size.</p>
```

<a id="theming-module-bootstrap-fonts-sizing"></a>

##### Sizing classes

The sizing classes are added on a freshly created `span` tag inside the targeted element (See
examples below).

![Sizing classes](developer/howtos/website_themes/theming/sizing.png)

<a id="theming-module-bootstrap-fonts-sizing-headings-and-body"></a>

###### Heading and body text

Assuming these classes can be applied on any text element, take `h2` as an example below:

```xml
<!-- h2 sized like an h1 -->
<h2><span class="h1-fs">Heading</span></h2>

<!-- h2 sized with other heading sizes -->
<h2><span class="h2-fs">Heading</span></h2>
<h2><span class="h3-fs">Heading</span></h2>
<h2><span class="h4-fs">Heading</span></h2>
<h2><span class="h5-fs">Heading</span></h2>
<h2><span class="h6-fs">Heading</span></h2>

<!-- h2 sized like a normal paragraph (base size, 16px by default) -->
<h2><span class="base-fs">Heading</span></h2>

<!-- h2 sized like a small text (14px by default) -->
<h2><span class="o_small-fs">Heading</span></h2>
```

<a id="theming-module-bootstrap-fonts-sizing-display"></a>

###### Display headings

If larger titles are needed, Odoo uses Bootstrap's Display Headings classes, from `display-1` to `6`.

```xml
<h2><span class="display-1-fs">Heading</span></h2>
<h2><span class="display-2-fs">Heading</span></h2>
<h2><span class="display-3-fs">Heading</span></h2>
<h2><span class="display-4-fs">Heading</span></h2>
```

#### NOTE
The Website Builder allows the user to configure only sizes from `Display 1` to `Display 4`. You
can set the other sizes (`5` and `6`) to use them in your code but the user won't be able to
modify them directly within the Website Builder interface.

<a id="theming-module-website"></a>

### Website settings

Global options related to the website can be set through the website record by following the
structure below.

**Declaration**

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo noupdate="1">
   <record id="website.default_website" model="website">
      <field name="name">Airproof</field>
      <field name="logo" type="base64" file="website_airproof/static/src/img/content/logo_pred.png"/>
      <field name="favicon" type="base64" file="website_airproof/static/description/favicon.png" />
      <field name="shop_ppg">18</field>
      <field name="shop_ppr">3</field>
      <field name="cookies_bar" eval="True" />
      <field name="contact_us_button_url">/contact-us</field>
      <field name="social_facebook">https://www.facebook.com/Airproof</field>
      <field name="social_instagram">https://www.instagram.com/airproof</field>
      <field name="social_linkedin">https://www.linkedin.com/company/airproof</field>
      <field name="social_youtube">https://www.youtube.com/c/airproof</field>
   </record>
</odoo>
```

| Field                 | Description                                                                         |
|-----------------------|-------------------------------------------------------------------------------------|
| name                  | Name of the website (displayed in the browser)                                      |
| logo                  | Path to the logo (previously created into a record)                                 |
| favicon               | Path to the favicon (previously created into a record)                              |
| shop_ppg              | Number of products shown per page in the e-commerce                                 |
| shop_ppr              | Number of products shown per rows (in a page) in the e-commerce                     |
| cookies_bar           | Enable/disable the cookies bar                                                      |
| contact_us_button_url | URL of the `Contact us` page (For instance, used in the standard header templates). |
| social_facebook       | URL of a Facebook profile                                                           |
| social_instagram      | URL of a Instagram profile                                                          |
| social_linkedin       | URL of a LinkedIn company profile                                                   |
| social_youtube        | URL of a YouTube channel                                                            |

#### NOTE
`website.default_website` is the default reference whenever you work with only one website. If
there are several websites in your database, this record will refer to the default site (the
first one).

<a id="theming-module-views"></a>

### Views

For some options, in addition to the Website Builder variable, you also have to activate a specific
view.

By reading the source code, templates related to options are easily found.

```xml
<we-button title="..."
   data-name="..."
   data-customize-website-views="website.template_header_default"
   data-customize-website-variable="'...'"
   data-img="..."/>
```

```xml
<template id="..." inherit_id="..." name="..." active="True"/>
<template id="..." inherit_id="..." name="..." active="False"/>
```

<a id="theming-module-views-presets"></a>

#### Presets

In order to activate and deactivate views as presets, you should include those inside the
`presets.xml` file.

**Use**

```xml
<record id="module.view" model="ir.ui.view">
      <field name="active" eval="False"/>
</record>
```

<a id="theming-assets"></a>

## Assets

For this part, we will refer to the `assets_frontend` bundle located in the web module. This bundle
specifies the list of assets loaded by the Website Builder, and the goal is to add your SCSS and JS
files to the bundle.

This is a non-exhaustive list of the frequently used bundles for a website:

| Bundle                          | Description                                                                                                                           |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| web._assets_primary_variables   | Mainly used for the `primary_variables.scss` file                                                                                     |
| web._assets_secondary_variables | Mainly used for the `secondary_variables.scss` file                                                                                   |
| web._assets_frontend_helpers    | Mainly used for the `bootstrap_overridden.scss` file                                                                                  |
| web.assets_frontend             | You can add all your custom SCSS, JS or QWeb JS files                                                                                 |
| website.assets_wysiwyg          | Add your JS files related to the Website Builder options behaviors (for instance, a custom<br/>method for your custom building block) |
| website.assets_wysiwyg          | If you need to extend Boostrap through the Bootstrap Utilities API, for example                                                       |

<a id="theming-assets-styles"></a>

### Styles

The Website Builder together with Bootstrap are great for defining the basic styles of your website.
But to design something unique, you should go a step further. For this, you can easily add any SCSS
file to your theme.

**Declaration**

```python
'assets': {
   'web.assets_frontend': [
      'website_airproof/static/src/scss/theme.scss',
   ],
},
```

Feel free to reuse the variables from your Bootstrap file and the ones used by Odoo in your
`theme.scss` file.

<a id="theming-assets-interactivity"></a>

### Interactivity

Odoo supports three different kinds of JavaScript files:

- [plain JavaScript files](../../reference/frontend/javascript_modules.md#frontend-modules-plain-js) (no module system),
- [native JavaScript module](../../reference/frontend/javascript_modules.md#frontend-modules-native-js), and
- [Odoo modules](../../reference/frontend/javascript_modules.md#frontend-modules-odoo-module) (using a custom module system).

Most new Odoo JavaScript codes should use the native JavaScript module system. It's simpler and
brings the benefit of a better developer experience with better integration with the IDE.

#### IMPORTANT
Odoo needs to know which files should be translated into [Odoo modules](../../reference/frontend/javascript_modules.md#frontend-js-modules) and which files should not. It's an opt-in system: Odoo looks at the first
line of a JavaScript file and checks if it contains the string `@odoo-module`. If so,
it will automatically be converted to an Odoo module.

```javascript
/** @odoo-module **/
```

**Declaration**

```python
'assets': {
   'web.assets_frontend': [
      'website_airproof/static/src/js/theme.js',
   ],
},
```

#### NOTE
If you want to include files from an external library, you can add them to the `/lib`
folder of your module.

#### SEE ALSO
- [Odoo JavaScript coding guidelines](https://github.com/odoo/odoo/wiki/Javascript-coding-guidelines)
- [Overview of the Odoo JavaScript framework](../../reference/frontend/javascript_reference.md)
- [Odoo Experience Talk: 10 Tips to take your website design to the next level!](https://www.youtube.com/watch?v=vAgE_fPVXUQ&ab_channel=Odoo)
