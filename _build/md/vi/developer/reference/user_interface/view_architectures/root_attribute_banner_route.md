### banner_route

The route to fetch HTML from and prepend it to the view.

If this attribute is set, the URL of the [controller route](developer/reference/backend/http.md#reference-controllers) is
fetched and the returned content is displayed above the view. The JSON response from the
controller must contain an `html` key.

If the HTML contains a `<link>` tag for a stylesheet, it is removed from its original location
and appended to the `<head>` section.

Use `<a type="action">` tags to interact with the backend, like with [action buttons](developer/reference/user_interface/view_architectures.md#reference-view-architectures-form-button).

* **Requirement:**
  Optional
* **Type:**
  [path](https://en.wikipedia.org/wiki/Path_(computing))
* **Default:**
  `''`
