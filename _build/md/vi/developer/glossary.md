# Glossary

<a id="term-external-id"></a>

external id

<a id="term-external-identifier"></a>

external identifier

<a id="term-external-identifiers"></a>

external identifiers
: string identifier stored in `ir.model.data`, can be used to refer
  to a record regardless of its database identifier during data imports
  or export/import roundtrips.
  <br/>
  External identifiers are in the form `*module*.*id*` (e.g.
  `account.invoice_graph`). From within a module, the
  `*module*.` prefix can be left out.
  <br/>
  Sometimes referred to as "xml id" or `xml_id` as XML-based
  [Data Files](developer/reference/backend/data.md#reference-data) make extensive use of them.

<a id="term-format-string"></a>

format string
: inspired by [jinja variables](http://jinja.pocoo.org/docs/dev/templates/#variables), format strings allow more easily
  mixing literal content and computed content (expressions): content
  between `{{` and `}}` is interpreted as an expression and
  evaluated, other content is interpreted as literal strings and
  displayed as-is

<a id="term-GIS"></a>

GIS

<a id="term-Geographic-Information-System"></a>

Geographic Information System
: any computer system or subsystem to capture, store, manipulate,
  analyze, manage or present spatial and geographical data.

<a id="term-minified"></a>

minified

<a id="term-minification"></a>

minification
: process of removing extraneous/non-necessary sections of files
  (comments, whitespace) and possibly recompiling them using equivalent
  but shorter structures ([ternary operator](http://en.wikipedia.org/wiki/%3F:) instead of `if/else`) in
  order to reduce network traffic
