# RST guidelines and cheat sheet

#### IMPORTANT
We strongly recommend reading the [Content guidelines](content_guidelines.md) and main [Documentation](../documentation.md)
pages before contributing.

Follow the RST guidelines below when contributing to the documentation to help maintain consistency
with the rest of the documentation and facilitate the review process for the team:

- [Use formatting.](#contributing-rst-formatting)
- [Be consistent with indentation.](#contributing-rst-indentation)
- [Start a new line before the 100th character.](#contributing-rst-character-limit)

For hyperlinks:

- [Use relative links for internal URLs.](#contributing-rst-relative-links)
- [Do not break hyperlink targets when refactoring.](#contributing-rst-update-targets)
- [Do not use non-descriptive hyperlink labels.](#contributing-rst-descriptive-labels)

<a id="contributing-rst-formatting"></a>

## Formatting

Use specific formatting to improve clarity and readability. For example, apply
[Menu selection](#contributing-rst-menuselection) for menu paths, [GUI element](#contributing-rst-guilabel)
for other user interface elements, such as fields, buttons, and options, [Note](#contributing-rst-note)
for notes, [Example](#contributing-rst-example) for examples, etc.

#### NOTE
Add a blank line between different block elements, such as paragraphs, lists, and directives to
ensure proper rendering and formatting.

<a id="contributing-rst-hyperlinks-guidelines"></a>

## Hyperlinks

<a id="contributing-rst-relative-links"></a>

### Internal URLs: relative links

If you need to reference an [internal documentation page](#contributing-rst-doc-hyperlinks)
or a [file](#contributing-rst-file) that is not located in the same directory as the current
page, always use *relative file paths* instead of *absolute file paths*. This ensures that links
remain valid even with version updates, folder name changes, and directory structure
reorganizations.

An absolute file path indicates the target's location from the root directory. A relative file path
uses smart notations (such as `../` that redirects to the parent folder) to indicate the target's
location *relative* to that of the source document.

<a id="contributing-rst-update-targets"></a>

### Refactoring: hyperlink targets

When refactoring (improving without adding new content) section headings or hyperlink targets, take
care not to break any hyperlink reference to these targets or update them accordingly.

<a id="contributing-rst-descriptive-labels"></a>

### Hyperlink labels

Do not use non-descriptive labels for [hyperlinks](#contributing-rst-hyperlinks).

<a id="contributing-rst-indentation"></a>

## Indentation

Use only spaces (never tabs).

Use as many spaces at the beginning of an indented line as needed to align it with the first
character of the markup in the line above. This usually implies three spaces, but you only need two
for bulleted lists, for example.

<a id="contributing-rst-character-limit"></a>

## 100th-character limit

In RST, it is possible to break a line without forcing a line break on the rendered HTML. Make use
of this feature to write **lines of maximum 100 characters**. It is not necessary to leave a
trailing whitespace at the end of a line to separate words.

<a id="contributing-rst-headings"></a>

## Headings

For each formatting line (e.g., `===`), write as many symbols (`=`) as there are characters in the
header.

The symbols used for the formatting are, in fact, not important. Only the order in which they are
written matters, as it determines the size of the decorated heading. This means that you may
encounter different heading formatting and in a different order, in which case you should follow the
formatting in place in the document. In any other case, use the formatting shown below.

| Heading size   | Formatting                                          |
|----------------|-----------------------------------------------------|
| H1             | ```text<br/>=======<br/>Heading<br/>=======<br/>``` |
| H2             | ```text<br/>Heading<br/>=======<br/>```             |
| H3             | ```text<br/>Heading<br/>-------<br/>```             |
| H4             | ```text<br/>Heading<br/>~~~~~~~<br/>```             |
| H5             | ```text<br/>Heading<br/>*******<br/>```             |
| H6             | ```text<br/>Heading<br/>^^^^^^^<br/>```             |

#### IMPORTANT
Each document must have **exactly one H1 heading**.

<a id="contributing-rst-markups"></a>

## Markups

<a id="contributing-rst-italic"></a>

### Emphasis (italic)

To emphasize a part of the text. The text is rendered in italic.

| Fill out the information *before* saving the form.                     |
|------------------------------------------------------------------------|
| ```text<br/>Fill out the information *before* saving the form.<br/>``` |

<a id="contributing-rst-bold"></a>

### Strong emphasis (bold)

To emphasize a part of the text. The text is rendered in bold.

| A **subdomain** is a domain that is a part of another domain.                     |
|-----------------------------------------------------------------------------------|
| ```text<br/>A **subdomain** is a domain that is a part of another domain.<br/>``` |

<a id="contributing-rst-code-sample"></a>

### Technical term (literal)

To write a technical term or a specific value to insert. The text is rendered in literal.

| Insert the IP address of your printer, for example, `192.168.1.25`.                     |
|-----------------------------------------------------------------------------------------|
| ```text<br/>Insert the IP address of your printer, for example, `192.168.1.25`.<br/>``` |

<a id="contributing-rst-definitions"></a>

### Definitions

Use the `dfn` markup to define a term.

| The documentation is written in RST and needs to be built () to<br/>display nicely.                                             |
|---------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>The documentation is written in RST and needs to be built (:dfn:`converted to HTML`) to<br/>display nicely.<br/>``` |

<a id="contributing-rst-abbreviations"></a>

### Abbreviations

Use the `abbr` markup to write a self-defining abbreviation that is displayed as a tooltip.

| Odoo uses  and artificial intelligence<br/>technologies to recognize the content of the documents.                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>Odoo uses :abbr:`OCR (optical character recognition)` and artificial intelligence<br/>technologies to recognize the content of the documents.<br/>``` |

<a id="contributing-rst-guilabel"></a>

### element

Use the `guilabel` markup to identify any text of the interactive user interface (e.g., labels).

| Update your credentials, then click on Save.                                 |
|------------------------------------------------------------------------------|
| ```text<br/>Update your credentials, then click on :guilabel:`Save`.<br/>``` |

#### NOTE
Avoid using the `guilabel` markup when referring to a concept or general term.

<a id="contributing-rst-menuselection"></a>

### Menu selection

Use the `menuselection` markup to guide users through a sequence of menus, starting with the app's
name.

| To review sales performance, go to Sales ‣ Reporting ‣ Dashboard.                                          |
|------------------------------------------------------------------------------------------------------------|
| ```text<br/>To review sales performance, go to :menuselection:`Sales --> Reporting --> Dashboard`.<br/>``` |

#### NOTE
Only include actual menu items in the `menuselection` markup:

- Use the [GUI element](#contributing-rst-guilabel) markup for other user interface elements, such as
  buttons and section titles:
  ```text
  To configure the bill control policy, navigate to :menuselection:`Purchase --> Configuration
  --> Settings`, and scroll down to the :guilabel:`Invoicing` section. Under :guilabel:`Bill
  Control`, select either :guilabel:`Ordered quantities` or :guilabel:`Received quantities`.
  ```
- Do not include menu section names. For example, in the screenshot below, `Journals` should not
  be included in the menu path Accounting ‣ Accounting ‣ Journal Entries:
  ![Accounting menu showing the Journals menu section.](contributing/documentation/rst_guidelines/accounting-menu.png)

<a id="contributing-rst-file"></a>

### File

Use the `file` markup to indicate a file path or name.

| Create redirections using the `redirects.txt` file found at the root of the repository.                               |
|-----------------------------------------------------------------------------------------------------------------------|
| ```text<br/>Create redirections using the :file:`redirects.txt` file found at the root of the<br/>repository.<br/>``` |

<a id="contributing-rst-command"></a>

### Command

Use the `command` markup to highlight a command.

| Run the command **make clean html** to delete existing built files and build the<br/>documentation to HTML.                            |
|----------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>Run the command :command:`make clean html` to delete existing built files and build the<br/>documentation to HTML.<br/>``` |

<a id="contributing-rst-icons"></a>

### Icons

Use the `icon` markup to add the class name of an icon. There are two icon sets used in Odoo:
[FontAwesome4](https://fontawesome.com/v4/icons/) and [Odoo UI](../../developer/reference/user_interface/icons.md). Follow the icon with its name as a
[GUI element](#contributing-rst-guilabel) in brackets as a descriptor.

| The graph view is represented by the <i class="fa fa-area-chart"></i> (area chart) icon. The<br/>pivot view is represented by the <i class="oi oi-view-pivot"></i> icon.           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>The graph view is represented by the :icon:`fa-area-chart` :guilabel:`(area chart)` icon.<br/>The pivot view is represented by the :icon:`oi-view-pivot` icon.<br/>``` |

<a id="contributing-rst-lists"></a>

## Lists

<a id="contributing-rst-bulleted-list"></a>

### Bulleted list

| - This is a bulleted list.<br/>- It has two items, the second<br/>  item uses two lines.                     |
|--------------------------------------------------------------------------------------------------------------|
| ```text<br/>- This is a bulleted list.<br/>- It has two items, the second<br/>  item uses two lines.<br/>``` |

<a id="contributing-rst-numbered-list"></a>

### Numbered list

| 1. This is a numbered list.<br/>2. Numbering is automatic.                     |
|--------------------------------------------------------------------------------|
| ```text<br/>#. This is a numbered list.<br/>#. Numbering is automatic.<br/>``` |

| 1. Use this format to start the numbering<br/>   with a number other than one.<br/>2. The numbering is automatic from there.                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>6. Use this format to start the numbering<br/>   with a number other than one.<br/>#. The numbering is automatic from there.<br/>``` |

<a id="contributing-rst-nested-list"></a>

### Nested lists

| - This is the first item of a bulleted list.<br/>  1. It has a nested numbered list<br/>  2. with two items.                          |
|---------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>- This is the first item of a bulleted list.<br/><br/>  #. It has a nested numbered list<br/>  #. with two items.<br/>``` |

<a id="contributing-rst-hyperlinks"></a>

## Hyperlinks

<a id="contributing-rst-external-hyperlinks"></a>

### External hyperlinks

External hyperlinks are links to a URL with a custom label. They follow the syntax:
``label <URL>`_`.

#### NOTE
- Use [documentation page hyperlinks](#contributing-rst-doc-hyperlinks) when targeting
  another documentation page.
- Do not use [non-descriptive hyperlink labels](#contributing-rst-descriptive-labels).

| For instance, [this is an external hyperlink to Odoo's website](https://www.odoo.com).                       |
|--------------------------------------------------------------------------------------------------------------|
| ```text<br/>For instance, `this is an external hyperlink to Odoo's website <https://www.odoo.com>`_.<br/>``` |

<a id="contributing-rst-external-hyperlink-aliases"></a>

### External hyperlink aliases

External hyperlink aliases allow creating shortcuts for external hyperlinks. The definition syntax
is as follows: `.. _target: URL`. There are two ways to reference them, depending on the use case:

1. `target_` creates a hyperlink with the target name as label and the URL as reference. Note that
   the `_` moved after the target.
2. ``label <target_>`_` the label replaces the name of the target, and the target is replaced by
   the URL.

| A [proof-of-concept](https://en.wikipedia.org/wiki/Proof_of_concept) is a simplified<br/>version, a prototype of what is expected to agree on the main lines of expected changes. [PoC](https://en.wikipedia.org/wiki/Proof_of_concept) is a common abbreviation.                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. _proof-of-concept: https://en.wikipedia.org/wiki/Proof_of_concept<br/><br/>   A proof-of-concept_ is a simplified version, a prototype of what is expected to agree on<br/>   the main lines of expected changes. `PoC <proof-of-concept_>`_ is a common abbreviation.<br/>``` |

<a id="contributing-rst-custom-anchors"></a>

### Custom anchors

Custom anchors follow the same syntax as external hyperlink aliases but without any URL. They allow
referencing a specific part of a RST file by using the target as an anchor. When users click the
reference, they are taken to the part of the documentation page where the target is defined.

The definition syntax is: `.. _target:`. There are two ways to reference them, both using the `ref`
markup:

1. `:ref:`target`` creates a hyperlink to the anchor with the heading defined below as label.
2. `:ref:`label <target>`` creates a hyperlink to the anchor with the given label.

#### IMPORTANT
As targets are visible from the entire documentation when referenced with the `ref` markup,
prefix the target name with the **app/section name** and the **file name**, separated by slashes,
e.g., `accounting/taxes/configuration`.

#### NOTE
- Add custom anchors for all headings so they can be referenced from any documentation file or
  within Odoo using documentation links.
- Notice that there is no `_` at the end, contrary to what is done with [external hyperlinks](#contributing-rst-external-hyperlinks).

| Please refer to the [Hyperlinks](#contributing-rst-hyperlinks-guidelines) section to learn more<br/>about [relative links](#contributing-rst-relative-links).                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/> .. _contributing/rst/hyperlinks-guidelines:<br/><br/> Hyperlinks<br/> ==========<br/><br/>.. _contributing/rst/relative-links:<br/><br/>Use relative links for internal URLs<br/>------------------------------------<br/><br/>Please refer to the :ref:`contributing/rst/hyperlinks-guidelines` section to learn more<br/>about :ref:`relative links <contributing/rst/relative-links>`.<br/>``` |

<a id="contributing-rst-doc-hyperlinks"></a>

### Documentation page hyperlinks

The `doc` markup allows referencing a documentation page wherever it is in the file tree through a
relative file path. There are two ways to use the markup, both using the `doc` markup:

1. `:doc:`path_to_doc_page`` creates a hyperlink to the documentation page with the title of the
   page as label.
2. `:doc:`label <path_to_doc_page>`` creates a hyperlink to the documentation page with the given
   label.

| Please refer to the [Accounting documentation](../../applications/finance/accounting.md) to learn more about<br/>[Hóa đơn bán hàng](../../applications/finance/accounting/customer_invoices.md).              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>Please refer to the :doc:`Accounting documentation <../../../applications/finance/accounting>`<br/>to learn more about :doc:`../../../applications/finance/accounting/customer_invoices`.<br/>``` |

#### IMPORTANT
[Use relative links](#contributing-rst-relative-links) for documentation page hyperlinks.

<a id="contributing-rst-download"></a>

### File download hyperlinks

The `download` markup allows referencing files (that are not necessarily  documents) within the source tree to be downloaded.

| Download this [`module structure template`](rst_guidelines/my_module.zip) to start<br/>building your module.                          |
|---------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>Download this :download:`module structure template <rst_guidelines/my_module.zip>` to start building your module.<br/>``` |

#### NOTE
Store the file alongside other [media files](content_guidelines.md#contributing-content-media-files) and
reference it using a [relative link](#contributing-rst-relative-links).

<a id="contributing-rst-images"></a>

## Images

The `image` markup allows inserting images in a document.

| ![Create an invoice.](contributing/documentation/rst_guidelines/create-invoice.png)              |
|--------------------------------------------------------------------------------------------------|
| ```text<br/>.. image:: rst_guidelines/create-invoice.png<br/>   :alt: Create an invoice.<br/>``` |

#### SEE ALSO
[Content guidelines for images](content_guidelines.md#contributing-content-images)

<a id="contributing-rst-alert-blocks"></a>

## Alert blocks (admonitions)

<a id="contributing-rst-seealso"></a>

### See also

| #### SEE ALSO<br/>- [Accounting documentation](../../applications/finance/accounting.md)<br/>- [Hóa đơn chiếu lệ](../../applications/sales/sales/invoicing/proforma.md)<br/>- [Google documentation on setting up Analytics for a website](https://support.google.com/analytics/answer/1008015?hl=en/)               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. seealso::<br/>- :doc:`Accounting documentation <../../../applications/finance/accounting>`<br/>- :doc:`../../../applications/sales/sales/invoicing/proforma`<br/>- `Google documentation on setting up Analytics for a website <https://support.google.com/analytics/answer/1008015?hl=en/>`_<br/>``` |

<a id="contributing-rst-note"></a>

### Note

| #### NOTE<br/>Use this alert block to draw the reader's attention and highlight important additional<br/>information.                    |
|------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. note::<br/>   Use this alert block to draw the reader's attention and highlight important additional information.<br/>``` |

<a id="contributing-rst-tip"></a>

### Tip

|                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. tip::<br/>   Use this alert block to inform the reader about a useful trick that requires an action.<br/>``` |

<a id="contributing-rst-example"></a>

### Example

|                                                                                  |
|----------------------------------------------------------------------------------|
| ```text<br/>.. example::<br/>   Use this alert block to show an example.<br/>``` |

<a id="contributing-rst-exercise"></a>

### Exercise

|                                                                                                     |
|-----------------------------------------------------------------------------------------------------|
| ```text<br/>.. exercise::<br/>   Use this alert block to suggest an exercise to the reader.<br/>``` |

<a id="contributing-rst-important"></a>

### Important

| #### IMPORTANT<br/>Use this alert block to notify the reader about important information.                        |
|------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. important::<br/>   Use this alert block to notify the reader about important information.<br/>``` |

<a id="contributing-rst-warning"></a>

### Warning

| #### WARNING<br/>Use this alert block to require the reader to proceed with caution with what is described<br/>in the warning.                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. warning::<br/>   Use this alert block to require the reader to proceed with caution with what is described in the warning.<br/>``` |

<a id="contributing-rst-danger"></a>

### Danger

|                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. danger::<br/>   Use this alert block to bring the reader's attention to a serious threat.<br/>``` |

<a id="contributing-rst-custom-alert-blocks"></a>

### Custom

|                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. admonition:: Title<br/><br/>   Customize this alert block with a **Title** of your choice.<br/>``` |

<a id="contributing-rst-tables"></a>

## Tables

### List tables

List tables use two-level bulleted lists to convert data into a table. The first level represents
the rows and the second level represents the columns.

| | Name    | Country    | Favorite color   |<br/>|---------|------------|------------------|<br/>| Raúl    | Montenegro | Purple           |<br/>| Mélanie | France     | Red              |                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. list-table::<br/>   :header-rows: 1<br/>   :stub-columns: 1<br/><br/>   * - Name<br/>     - Country<br/>     - Favorite colour<br/>   * - Raúl<br/>     - Montenegro<br/>     - Purple<br/>   * - Mélanie<br/>     - France<br/>     - Turquoise<br/>``` |

### Grid tables

Grid tables represent the rendered table and are more visual to work with.

| |                       | Shirts       | T-shirts      |<br/>|-----------------------|--------------|---------------|<br/>| **Available colours** | Purple       | Green         |<br/>| Turquoise             | Orange       |               |<br/>| **Sleeves length**    | Long sleeves | Short sleeves |                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>+-----------------------+--------------+---------------+<br/>|                       | Shirts       | T-shirts      |<br/>+=======================+==============+===============+<br/>| **Available colours** | Purple       | Green         |<br/>|                       +--------------+---------------+<br/>|                       | Turquoise    | Orange        |<br/>+-----------------------+--------------+---------------+<br/>| **Sleeves length**    | Long sleeves | Short sleeves |<br/>+-----------------------+--------------+---------------+<br/>``` |

<a id="contributing-rst-code-blocks"></a>

## Code blocks

Use the `code-block` directive to show example code. Specify the language (e.g., python, xml, etc.)
to format the code according to the language's syntax rules.

| ```python<br/>def main():<br/>    print("Hello world!")<br/>```                                     |
|-----------------------------------------------------------------------------------------------------|
| ```text<br/>.. code-block:: python<br/><br/>   def main():<br/>       print("Hello world!")<br/>``` |

<a id="contributing-rst-spoilers"></a>

## Spoilers

|                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. spoiler:: Answer to the Ultimate Question of Life, the Universe, and Everything<br/><br/>   **42**<br/>``` |

<a id="contributing-rst-tabs"></a>

## Content tabs

#### WARNING
The `tabs` markup may not work well in some situations. In particular:

- The tabs' headers cannot be translated.
- A tab cannot contain [headings](#contributing-rst-headings).
- An [alert block](#contributing-rst-alert-blocks) cannot contain tabs.
- A tab cannot contain [custom anchors](#contributing-rst-custom-anchors).

<a id="contributing-rst-basic-tabs"></a>

### Basic tabs

Basic tabs are useful to split the content into multiple options. The `tabs` markup is used to
define sequence of tabs. Each tab is then defined with the `tab` markup followed by a label.

| Odoo Online<br/><br/>Content dedicated to Odoo Online users.<br/><br/>Odoo.sh<br/><br/>Alternative for Odoo.sh users.<br/><br/>On-premise<br/><br/>Third version for On-premise users.                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. tabs::<br/><br/>   .. tab:: Odoo Online<br/><br/>      Content dedicated to Odoo Online users.<br/><br/>   .. tab:: Odoo.sh<br/><br/>      Alternative for Odoo.sh users.<br/><br/>   .. tab:: On-premise<br/><br/>      Third version for On-premise users.<br/>``` |

<a id="contributing-rst-nested-tabs"></a>

### Nested tabs

Tabs can be nested inside one another.

| Stars<br/><br/>The Sun<br/><br/>The closest star to us.<br/><br/>Proxima Centauri<br/><br/>The second closest star to us.<br/><br/>Polaris<br/><br/>The North Star.<br/><br/>Moons<br/><br/>The Moon<br/><br/>Orbits the Earth.<br/><br/>Titan<br/><br/>Orbits Jupiter.                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. tabs::<br/><br/>   .. tab:: Stars<br/><br/>      .. tabs::<br/><br/>         .. tab:: The Sun<br/><br/>            The closest star to us.<br/><br/>         .. tab:: Proxima Centauri<br/><br/>            The second closest star to us.<br/><br/>         .. tab:: Polaris<br/><br/>            The North Star.<br/><br/>   .. tab:: Moons<br/><br/>      .. tabs::<br/><br/>         .. tab:: The Moon<br/><br/>            Orbits the Earth.<br/><br/>         .. tab:: Titan<br/><br/>            Orbits Jupiter.<br/>``` |

<a id="contributing-rst-group-tabs"></a>

### Group tabs

Group tabs are special tabs that synchronize based on a group label. The last selected group is
remembered and automatically selected when the user returns to the page or visits another page with
the tabs group. The `group-tab` markup is used to define group tabs.

| C++<br/><br/>C++<br/><br/>Python<br/><br/>Python<br/><br/>Java<br/><br/>Java<br/><br/>C++<br/><br/>```c++<br/>int main(const int argc, const char **argv) {<br/>    return 0;<br/>}<br/>```<br/><br/>Python<br/><br/>```python<br/>def main():<br/>    return<br/>```<br/><br/>Java<br/><br/>```java<br/>class Main {<br/>    public static void main(String[] args) {}<br/>}<br/>```                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. tabs::<br/><br/>   .. group-tab:: C++<br/><br/>      C++<br/><br/>   .. group-tab:: Python<br/><br/>      Python<br/><br/>   .. group-tab:: Java<br/><br/>      Java<br/><br/>.. tabs::<br/><br/>   .. group-tab:: C++<br/><br/>      .. code-block:: c++<br/><br/>         int main(const int argc, const char **argv) {<br/>             return 0;<br/>         }<br/><br/>   .. group-tab:: Python<br/><br/>      .. code-block:: python<br/><br/>         def main():<br/>             return<br/><br/>   .. group-tab:: Java<br/><br/>      .. code-block:: java<br/><br/>         class Main {<br/>             public static void main(String[] args) {}<br/>         }<br/>``` |

<a id="contributing-rst-code"></a>

### Code tabs

Use the `code-tab` markup to create code tabs, which are essentially [group tabs](#contributing-rst-group-tabs) that treat the tabs' content as a [code block](#contributing-rst-code-blocks). Specify the language to format the code according to the language's
syntax rules. If a label is set, it is used for grouping tabs instead of the language name.

| Hello C++<br/><br/>```c++<br/>#include <iostream><br/><br/>int main() {<br/>    std::cout << "Hello World";<br/>    return 0;<br/>}<br/>```<br/><br/>Hello Python<br/><br/>```python<br/>print("Hello World")<br/>```<br/><br/>Hello JavaScript<br/><br/>```javascript<br/>console.log("Hello World");<br/>```                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. tabs::<br/><br/>   .. code-tab:: c++ Hello C++<br/><br/>      #include <iostream><br/><br/>      int main() {<br/>          std::cout << "Hello World";<br/>          return 0;<br/>      }<br/><br/>   .. code-tab:: python Hello Python<br/><br/>      print("Hello World")<br/><br/>   .. code-tab:: javascript Hello JavaScript<br/><br/>      console.log("Hello World");<br/>``` |

<a id="contributing-rst-cards"></a>

## Cards

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>.. cards::<br/><br/>   .. card:: Documentation<br/>      :target: ../documentation<br/>      :tag: Step-by-step guide<br/>      :large:<br/><br/>      Use this guide to acquire the tools and knowledge you need to write documentation.<br/><br/>   .. card:: Content guidelines<br/>      :target: content_guidelines<br/><br/>      List of guidelines, tips, and tricks to help you create clear and effective content.<br/><br/>   .. card:: RST guidelines<br/>      :target: rst_guidelines<br/><br/>      List of technical guidelines to observe when writing with reStructuredText.<br/>``` |

<a id="contributing-rst-document-metadata"></a>

## Document metadata

[Sphinx](https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)) supports document-wide
metadata markups that specify a behavior for the entire page. They must be placed between colons
(`:`) at the top of the source file.

| **Metadata**    | **Purpose**                                                                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `show-content`  | Make a toctree page accessible from the navigation menu.                                                                                                                                                                                    |
| `show-toc`      | Show the table of content on a page that has the `show-content` metadata<br/>markup.                                                                                                                                                        |
| `hide-page-toc` | Hide the "On this page" sidebar and use full page width for the content.                                                                                                                                                                    |
| `nosearch`      | Exclude the document from search results.                                                                                                                                                                                                   |
| `orphan`        | Suppress the need to include the document in a toctree.                                                                                                                                                                                     |
| `code-column`   | Show a dynamic side column that can be used to display interactive<br/>tutorials or code excerpts.<br/><br/><br/>For example, see<br/>[Accounting cheat sheet](../../applications/finance/accounting/get_started/cheat_sheet.md).<br/><br/> |
| `custom-css`    | Link CSS files (comma-separated) to the file.                                                                                                                                                                                               |
| `custom-js`     | Link JS files (comma-separated) to the document.                                                                                                                                                                                            |
| `classes`       | Assign the specified classes to the `<main/>` element of the file.                                                                                                                                                                          |

<a id="contributing-rst-formatting-tips"></a>

## Formatting tips

<a id="contributing-rst-line-break"></a>

### Break the line but not the paragraph

| A first long line that you break in two<br/>-> here <- is rendered as a single line.<br/><br/><br/>A second line that follows a line break.<br/><br/>       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```text<br/>| A first long line that you break in two<br/>  -> here <- is rendered as a single line.<br/>| A second line that follows a line break.<br/>``` |

<a id="contributing-rst-escaping"></a>

### Escape markup symbols

Markup symbols escaped with backslashes (`\`) are rendered normally. For instance, `this
\*\*line of text\*\* with \*markup\* symbols` is rendered as “this \*\*line of text\*\* with
\*markup\* symbols”.

When it comes to backticks (```), which are used in many cases such as [external hyperlinks](#contributing-rst-external-hyperlinks), using backslashes for escaping is no longer
an option because the outer backticks interpret enclosed backslashes and thus prevent them from
escaping inner backticks. For instance, ``\`this formatting\``` produces an
`[UNKNOWN NODE title_reference]` error. Instead, ````this formatting```` should be used to
produce the following result: ``this formatting``.

#### SEE ALSO
[Docutils documentation on reStructuredText directives and roles](https://docutils.sourceforge.io/docs/ref/rst/directives.html)
