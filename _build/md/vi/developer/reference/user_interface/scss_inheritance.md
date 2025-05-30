# SCSS inheritance

## Overview

Managing SCSS assets in Odoo is not as straightforward as it is in some other environments, but it's
highly efficient.

Modularity is key. The inheritance scheme described further allows Odoo to:

- customize the Bootstrap CSS framework;
- handle two different webclient designs (Community and Enterprise);
- handle backend and frontend bundles separately (including the user's website design);
- contextually load only necessary assets;
- handle multiple color-schemes (e.g.: dark-mode);

## SCSS's `!default` directive

"Direct variables’ overrides" are technically possible in SCSS but may lead to inconsistent results
in complex environments like Odoo.

Indeed, since the compilation process acts across different interdependent bundles, re-assigning
a variable in the "wrong spot" may lead to unexpected cascading results.

SCSS provides several techniques to overcome these issues
(e.g.: [shadowing](https://sass-lang.com/documentation/variables#shadowing)), but the most
critical procedure in Odoo is the use of the `!default` flag.

When using the `!default` flag, the compiler assigns a value **only** if that variable is not yet
defined.

As a result of this technique, the priority in which variables are assigned matches the assets'
loading order.

#### SEE ALSO
`!default` flag on the [SASS Documentation](https://sass-lang.com/documentation/variables#default-values)

## Odoo's SCSS inheritance system

The following diagram conceptually illustrates the compilation order in which the CSS and SCSS
variables are defined.

```text
↓ [Compilation starts]
⏐
↓ web.dark_mode_variables
⏐   ├─ Primary Variables
⏐   └─ Components Variables
⏐
↓ web._assets_primary_variables
⏐   ├─ Primary Variables (enterprise)
⏐   ├─ Components Variables (enterprise)
⏐   ├─ Primary Variables (community)
⏐   └─ Components Variables (community)
⏐
↓ web._assets_bootstrap
⏐
↓ web.assets_backend
⏐   ├─ ...
⏐   ├─ CSS variables definition
⏐   └─ CSS variables contextual adaptations
⏐
● [Visual result on screen]
```

#### IMPORTANT
This diagram is incomplete and does not match the current bundles' organization. Read more on
[asset bundles](../frontend/assets.md#reference-assets-bundle).
