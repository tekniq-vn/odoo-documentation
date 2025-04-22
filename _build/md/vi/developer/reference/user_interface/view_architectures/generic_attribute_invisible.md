### invisible

Whether the element is visible (`False`) or hidden (`True`), as a Python expression that
evaluates to a bool.

#### NOTE
There are two uses for the `invisible` attribute:

- Usability: to avoid overloading the view and to make it easier for the user to read,
  depending on the content.
- Technical: a field must be present (invisible is enough) in the view to be used in a
  Python expression.

* **Requirement:**
  Optional
* **Type:**
  [Python expression](developer/reference/user_interface/view_architectures.md#reference-view-architectures-python-expression)
* **Default:**
  `False`
