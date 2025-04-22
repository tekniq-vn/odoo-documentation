<a id="frontend-hooks"></a>

# Hooks

[Owl hooks](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md) are a
way to factorize code, even if it depends on some component lifecycle. Most hooks
provided by Owl are related to the lifecycle of a component, but some of them (such as
[useComponent](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#usecomponent))
provide a way to build specific hooks.

Using these hooks, it is possible to build many customized hooks that help solve
a specific problem, or make some common tasks easier. The rest of this page
documents the list of hooks provided by the Odoo web framework.

| Name                                           | Short Description                                      |
|------------------------------------------------|--------------------------------------------------------|
| [useAssets](#frontend-hooks-useassets)         | load assets                                            |
| [useAutofocus](#frontend-hooks-useautofocus)   | focus automatically an element referenced by autofocus |
| [useBus](#frontend-hooks-usebus)               | subscribe and unsubscribe to a bus                     |
| [usePager](#frontend-hooks-usepager)           | Display the pager of the control panel of a view.      |
| [usePosition](#frontend-hooks-useposition)     | position an element relative to a target               |
| [useSpellCheck](#frontend-hooks-usespellcheck) | activate spellcheck on focus for input or textarea     |

<a id="frontend-hooks-useassets"></a>

## useAssets

### Location

`@web/core/assets`

### Description

See the section on [lazy loading assets](developer/reference/frontend/assets.md#frontend-assets-lazy-loading) for
more details.

<a id="frontend-hooks-useautofocus"></a>

## useAutofocus

### Location

`@web/core/utils/hooks`

### Description

Focus an element referenced by a t-ref="autofocus" in the current component as
soon as it appears in the DOM and if it was not displayed before.

```javascript
import { useAutofocus } from "@web/core/utils/hooks";

class Comp {
  setup() {
    this.inputRef = useAutofocus();
  }
  static template = "Comp";
}
```

```xml
<t t-name="Comp">
  <input t-ref="autofocus" type="text"/>
</t>
```

### API

### useAutofocus()

* **Trả về:**
  the element reference.

<a id="frontend-hooks-usebus"></a>

## useBus

### Location

`@web/core/utils/hooks`

### Description

Add and clear an event listener to a bus. This hook ensures that
the listener is properly cleared when the component is unmounted.

```javascript
import { useBus } from "@web/core/utils/hooks";

class MyComponent {
  setup() {
    useBus(this.env.bus, "some-event", event => {
      console.log(event);
    });
  }
}
```

### API

### useBus(bus, eventName, callback)

* **Đối số:**
  * **bus** (`EventBus()`) -- the target event bus
  * **eventName** (`string()`) -- the name of the event that we want to listen to
  * **callback** (`function()`) -- listener callback

<a id="frontend-hooks-usepager"></a>

## usePager

### Location

`@web/search/pager_hook`

### Description

Display the [Pager](developer/reference/frontend/owl_components.md#frontend-pager) of the control panel of a view. This hooks correctly sets `env.config` to provide the props to the pager.

```javascript
import { usePager } from "@web/search/pager_hook";

class CustomView {
  setup() {
    const state = owl.hooks.useState({
      offset: 0,
      limit: 80,
      total: 50,
    });
    usePager(() => {
      return {
        offset: this.state.offset,
        limit: this.state.limit,
        total: this.state.total,
        onUpdate: (newState) => {
          Object.assign(this.state, newState);
        },
      };
    });
  }
}
```

### API

### usePager(getPagerProps)

* **Đối số:**
  * **getPagerProps** (`function()`) -- function that returns the pager props.

<a id="frontend-hooks-useposition"></a>

## usePosition

### Location

`@web/core/position_hook`

### Description

Helps positioning an HTMLElement (the `popper`) relatively to another
HTMLElement (the `reference`). This hook ensures the positioning is updated when
the window is resized/scrolled.

```javascript
import { usePosition } from "@web/core/position_hook";

class MyPopover extends owl.Component {
  setup() {
    // Here, the reference is the target props, which is an HTMLElement
    usePosition(this.props.target);
  }
}
MyPopover.template = owl.tags.xml`
  <div t-ref="popper">
    I am positioned through a wonderful hook!
  </div>
`;
```

#### IMPORTANT
You should indicate your `popper` element using a [t-ref directive](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref).

### API

### usePosition(reference)

* **Đối số:**
  * **reference** (`HTMLElement or ()=>HTMLElement()`) -- the target HTMLElement to be positioned from
  * **options** (`Options()`) -- the positioning options (see table below)

| Option         | Type                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `popper`       | string                                                   | this is a [useRef reference](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref) for the element that will get positioned.<br/>Default is `"popper"`.                                                                                                                                                                                                                                                                                                                                                                                                |
| `container`    | HTMLElement                                              | the container from which the popper is expected not to overflow. If<br/>overflowing occurs, other popper positions are tried until a not<br/>overflowing one is found. (default: the `<html/>` node)                                                                                                                                                                                                                                                                                                                                                                    |
| `margin`       | number                                                   | added margin between popper and reference elements (default: `0`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `position`     | Direction[-Variant]                                      | the desired position. It is a string composed of one `Direction` and one<br/>`Variant` separated by a dash character.<br/>`Direction` could be: `top`, `bottom`, `right`, `left`.<br/>`Variant` could be: `start`, `middle`, `end`, `fit`.<br/>The variant can be omitted (default variant is `middle`).<br/>The `fit` variant means that the popper would have the exact same width or height,<br/>depending on the chosen direction.<br/>Examples of valid positions: `right-end`, `top-start`, `left-middle`,<br/>`left`, `bottom-fit`. (default position: `bottom`) |
| `onPositioned` | (el: HTMLElement, position: PositioningSolution) => void | a callback that will be called everytime a positioning occurs<br/>(e.g. on component mounted/patched, document scroll, window resize...).<br/>Can be used i.e. for dynamic styling regarding the current position.<br/>The `PositioningSolution` is an object having the following type:<br/>`{ direction: Direction, variant: Variant, top: number, left: number }`.                                                                                                                                                                                                   |

<a id="frontend-hooks-usespellcheck"></a>

## useSpellCheck

### Location

`@web/core/utils/hooks`

### Description

Activate the spellcheck state to an input or textarea on focus by a `t-ref="spellcheck"` in
the current component. This state is then removed on blur, as well as the red outline, which
improves readability of the content.

The hook can also be used on any HTML element with the `contenteditable` attribute. To disable
spellcheck completely on elements that might be enabled by the hook, set explicitly the
`spellcheck` attribute as `false` on the element.

### API

### useSpellCheck()

* **Đối số:**
  * **options** (`Options()`) -- the spellcheck options (see table below)

| Option    | Type   | Description                                                                                                                                              |
|-----------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `refName` | string | this is a [useRef reference](https://github.com/odoo/owl/blob/master/doc/reference/hooks.md#useref) for the element that will be<br/>spellcheck enabled. |
