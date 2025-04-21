### type

The type of the button indicating how it behaves. It can have two different values:

### object

Call a method on the view's model. The button's `name` is the method that is called with the
current record ID and the current `context`.

### action

Load and execute an `ir.actions` action record. The button's `name` is the XMLID of the
action to load. The `context` is extended with the view's model (as `active_model`) and with
the current record (as `active_id`).

* **Requirement:**
  Mandatory if the `special` attribute is not set
* **Type:**
  [str](https://docs.python.org/3/library/stdtypes.html#str)
