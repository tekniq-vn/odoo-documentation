# Write lean easy-to-maintain CSS

There are many ways to lean and simplify SCSS. The first step is to establish if custom code is
needed at all.

Odoo's webclient has been designed to be modular, meaning that (potentially all) classes can be
shared across views. Check the code before creating a new class. Chances are that there is already a
class or an HTML tag doing exactly what you're looking for.

On top of that, Odoo relies on [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) (BS), one of the most complete
CSS frameworks available. The framework has been customized in order to match Odoo's design (both
community and enterprise versions), meaning that you can use any BS class directly in Odoo and
achieve a visual result that is consistent with our UI.

#### WARNING
- The fact that a class achieves the desired visual result doesn't necessarily mean that it's the
  right one for the job. Be aware of classes triggering JS behaviors, for example.
- Be careful about class semantics. Applying a **button class** to a **title** is not only
  semantically wrong, it may also lead to migration issues and visual inconsistencies.

The following sections describe tips to strip-down SCSS lines **when custom-code is the only way to
go**.

<a id="tutorials-scss-tips-browser-defaults"></a>

## Browser defaults

By default, each browser renders content using a *user agent stylesheet*. To overcome
inconsistencies between browsers, some of these rules are overridden by [Bootstrap Reboot](https://getbootstrap.com/docs/5.1/content/reboot/).

At this stage all "browser-specific-decoration" rules have been stripped away, but a big chunk of
rules defining basic layout information is maintained (or reinforced by *Reboot* for consistency
reasons).

You can rely on these rules.

Here's a non-comprehensive list of default rules:

| Tag / Attribute                                     | Defaults                                                                                 |
|-----------------------------------------------------|------------------------------------------------------------------------------------------|
| `<div/>`, `<section/>`, `<header/>`, `<footer/>`... | `display: block`                                                                         |
| `<span/>`, `<a/>`, `<em/>`, `<b/>`...               | `display: inline`                                                                        |
| `<button/>`, `<label/>`, `<output/>`...             | `display: inline-block`                                                                  |
| `<img/>`, `<svg/>`                                  | `vertical-align: middle`                                                                 |
| `<summary/>`, `[role="button"]`                     | `cursor: pointer;`                                                                       |
| `<q/>`                                              | `:before {content: open-quote}`<br/><br/><br/>`:after  {content: close-quote}`<br/><br/> |
| ...                                                 | ...                                                                                      |

#### SEE ALSO
[Bootstrap Reboot on GitHub](https://github.com/twbs/bootstrap/blob/1a6fdfae6b/scss/_reboot.scss)

<a id="tutorials-scss-tips-html-tags"></a>

## HTML tags

It may seem obvious, but the simplest and most **consistent** way of making text look like a title
is to use a header tag (`<h1>`, `<h2>`, ...). Besides reboot rules, mostly all tags carry decorative
styles defined by Odoo.

#### NOTE
Besides reducing the amount of code, a modular-design approach (use classes, tags, mixins...)
keeps the visual result consistent and easily **maintainable**.

Following the last example, if Odoo titles' design changes, these changes will be applied in the
`o_module_custom_title` element too since it's using an `<h5>` tag.

<a id="tutorials-scss-tips-utility-classes"></a>

## Utility classes

Our framework defines a multitude of utility classes designed to cover almost all
layout/design/interaction needs. The simple fact that a class already exists justifies its use over
custom CSS whenever possible.

Take the example of `position-relative`.

```css
position-relative {
   position: relative !important;
}
```

Since a utility-class is defined, any CSS line with the declaration `position: relative` is
**potentially** redundant.

Odoo relies on the default [Bootstrap utility-classes](https://getbootstrap.com/docs/5.1/utilities/background/) stack and defines its own using
[Bootstrap API](https://getbootstrap.com/docs/5.1/utilities/api/).

#### SEE ALSO
- [Bootstrap utility classes](https://getbootstrap.com/docs/5.1/utilities/api/)
- [Odoo custom utilities on github](https://github.com/odoo/odoo/blob/17.0/addons/web/static/src/scss/utilities_custom.scss)

<a id="tutorials-scss-tips-utility-classes-downside"></a>

### Handling utility-classes verbosity

The downside of utility-classes is the potential lack of readability.

To overcome the issue you may combine different approaches:

- in Qweb attributes, only use classes to be toggled *on-the-fly*;
- use new lines for each attribute;
- order classes using the convention `[odoo component] [bootstrap component] [css declaration order]`.

#### SEE ALSO
[Odoo CSS properties order](contributing/development/coding_guidelines.md#contributing-coding-guidelines-scss-properties-order)
