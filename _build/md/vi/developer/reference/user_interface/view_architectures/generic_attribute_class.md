### class

The [HTML class](https://en.wikipedia.org/wiki/HTML_attribute) to set on the generated element.

The styling uses the [Bootstrap](https://getbootstrap.com) framework and [UI icons](developer/reference/user_interface/icons.md#reference-user-interface-ui-icons). Common Odoo classes include:

- `oe_inline`: prevents the usual line break following fields, and limits their span;
- `oe_left`, `oe_right`: [floats](https://developer.mozilla.org/en-US/docs/Web/CSS/float) the
  element to the corresponding direction;
- `oe_read_only`, `oe_edit_only`: only displays the element in the corresponding form mode;
- `oe_avatar`: for image fields, displays images as an "avatar" (max 90x90 square);
- `oe_stat_button`: defines a particular rendering to dynamically display information while being
  clickable to target an action.

* **Requirement:**
  Optional
* **Type:**
  [str](https://docs.python.org/3/library/stdtypes.html#str)
* **Default:**
  `''`
