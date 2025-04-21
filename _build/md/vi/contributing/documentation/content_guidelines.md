# Content guidelines

While we encourage you to adopt your own writing style, some rules still apply to maintain clarity
and ensure readers can easily understand the content.

#### IMPORTANT
We strongly recommend to read the [RST guidelines and cheat sheet](rst_guidelines.md) and the main [Documentation](../documentation.md)
pages before contributing.

<a id="contributing-content-organization"></a>

## Documentation organization

When writing documentation about a given topic, keep pages within the same folder organized.

For most topics, a single page should do the job. Place it in the appropriate section of the
documentation (e.g., content related to the CRM app goes under User Docs ‣ Sales
‣ CRM) and follow the [document structure](#contributing-content-structure) guidelines.

For more complex topics, several pages may be needed to cover all their aspects. Usually, you will
find yourself adding documentation to a topic that is already partially covered. In that case,
either create a new page and place it at the same level as other related pages or add new sections
to an existing page. When documenting a complex topic from scratch, organize the content across
several child pages that are referenced on that directory's parent page (the  page); whenever possible, write content on the parent page and not only on the child
pages. Make the parent page accessible from the navigation menu by using the
[show-content](rst_guidelines.md#contributing-rst-document-metadata) metadata directive.

#### NOTE
Avoid duplicating content whenever possible; if a topic is already documented on another page,
[reference](rst_guidelines.md#contributing-rst-hyperlinks) that existing information instead of repeating it.

#### IMPORTANT
When deleting or moving a `.rst` file, update the corresponding text file in the
`redirects` folder based on your branch's version (e.g., `17.0.txt`). To do so, add a
new line at the bottom of the relevant section (e.g., `# applications/sales`). On this line,
first, add the redirection entry point with the old file location, followed by a space, and then
add the exit point with the new or relevant file location. For example, if moving the file
`unsplash.rst` from `applications/websites/website/configuration` to
`applications/general/integrations`, add the following entry under the section
`# applications/websites`:

```text
applications/websites/website/configuration/unsplash.rst applications/general/integrations/unsplash.rst
```

<a id="contributing-content-structure"></a>

## Document structure

Use different **heading levels** to organize text by sections and sub-sections. Headings are not
only displayed in the document but also on the navigation menu (only the H1) and on the "On this
page" sidebar (all H2 to H6).

|    | **H1: Page title**<br/><br/><br/>The *page title* gives readers a quick and clear understanding of what the content<br/>is about.<br/><br/><br/><br/>The *content* in this section describes the upcoming content from a **business point<br/>of view**, and should not put the emphasis on Odoo, as this is documentation and not<br/>marketing.<br/><br/>Under the page title (H1), start with a **lead paragraph**, which helps the reader<br/>make sure that they've found the right page, then explain the **business aspects of<br/>this topic** in the following paragraphs.   |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | **H2: Section title (configuration)**<br/><br/><br/>This first H2 section is about the configuration of the feature, or the<br/>prerequisites to achieve a specific goal.<br/><br/>                                                                                                                                                                                                                                                                                                                                                                                                   |
|    | **H2: Section title (main sections)**<br/><br/><br/>Create as many main sections as you have actions or features to distinguish.<br/><br/>                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|    | **H2: Next Section**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

To write good titles and headings:

- **Be concise**: **avoid sentences**, questions, and titles starting with "how to".
- **Do not use pronouns** in your titles, especially 2nd person (*you/your*).
- Use **sentence case**. This means you capitalize only:
  - the first word of the title or heading;
  - the first word after a colon;
  - proper nouns (brands, product and service names, etc.).

#### NOTE
- Most titles and headings generally refer to a concept and do *not* represent the name of a
  feature or a model.
- Do not capitalize the words of an acronym if they do not entail a proper noun.
- Verbs in headings are fine since they often describe an action.

#### SEE ALSO
- [RST cheat sheet: headings](rst_guidelines.md#contributing-rst-headings)
- [RST cheat sheet: markups](rst_guidelines.md#contributing-rst-markups)

<a id="contributing-content-writing-style"></a>

## Writing style

Writing for documentation is not the same as writing for a blog or another medium. Readers are
more likely to skim through content to find the information they need. Keep in mind that the
documentation is a place to **inform and describe**, not to convince and promote.

<a id="contributing-content-spelling"></a>

### Spelling

Use American English spelling and grammar throughout the documentation.

<a id="contributing-content-consistency"></a>

### Consistency

*Consistency is key to everything.*

Make sure that the writing style remains **consistent**. When modifying existing content, try to
match the existing tone and presentation or rewrite it to match your own style.

<a id="contributing-content-capitalization"></a>

### Capitalization

- Use sentence case in [titles](#contributing-content-structure).
- Capitalize app names, e.g., **Odoo Sales**, the **Sales** app, etc.
- Capitalize labels (such as fields and buttons) as they appear in Odoo. If a label is in all caps,
  convert it to sentence case.
- Capitalize the first letter after a colon if it is a complete sentence.
- Avoid capitalizing common nouns, such as "sales order" and "bill of materials", unless you
  reference a label or a model.

<a id="contributing-content-grammatical-tenses"></a>

### Grammatical tenses

In English, descriptions and instructions usually require the use of the **present tense**, while
the *future tense* is appropriate only when a specific event is to happen ulteriorly.

<a id="contributing-content-lists"></a>

## Lists

Lists help organize information in a clear and concise manner and improve readability. They are
used to highlight important details, guide the reader through steps in a systematic way, etc.

Use numbered lists when the sequence matters, e.g., instructions, procedures, or steps that must be
performed in a particular order.

Use bulleted lists when the sequence of items does not matter, e.g., lists of features, fields,
options, etc.

#### SEE ALSO
[RST cheat sheet: lists](rst_guidelines.md#contributing-rst-lists)

## Icons

Use [icons](rst_guidelines.md#contributing-rst-icons) in instructions to help readers identify user interface
elements and reduce the need for lengthy explanations. Accompany every icon with a descriptor
in brackets.

#### SEE ALSO
[RST cheat sheet: icons](rst_guidelines.md#contributing-rst-icons)

<a id="contributing-content-images"></a>

## Images

Adding a few images to illustrate text helps the readers understand and memorize the content.
However, images should never replace text: written instructions should be complete and clear on
their own, without relying on visual aids. Use images sparingly, for example, to highlight a
particular point or clarify an example.

#### IMPORTANT
Do not forget to [compress your PNG files with pngquant](https://pngquant.org).

<a id="contributing-content-screenshots"></a>

### Screenshots

Screenshots are automatically resized to fit the content block's width. This implies that if they
are too wide, they are not readable on lower-resolution screens. We recommend avoiding full-screen
screenshots of the app unless absolutely necessary and making sure images are no wider than a range
of 768-933 pixels.

Here are a few tips to improve your screenshots:

1. **Resize** your browser's width, either by *resizing the window* itself or by opening the
   *browser's developer tools* and resizing the width.
2. **Select** the relevant area rather than keeping the entire window.
3. **Remove** unnecessary information and **resize** columns when applicable.

#### IMPORTANT
Do not use markups such as rectangles or arrows on screenshots. Instead, crop the image to
highlight the most relevant information, and ensure that text instructions are clear and
self-explanatory without relying on images.

<a id="contributing-content-media-files"></a>

### Media files

A **media filename**:

- is written in **lower-case letters**;
- is **relevant** to the media's content. (e.g., `screenshot-tips.gif`);
- separates its words with a **hyphen** `-` (e.g., `awesome-filename.png`).

Each RST file has its own folder for storing media files. The folder's name must be the same as the
RST file's name.

For example, the document `doc_filename.rst` refers to two images that are placed in the
folder `doc_filename`.

```default
├── section
│   └── doc_filename
│   │   └── screenshot-tips.gif
│   │   └── awesome-filename.png
│   └── doc_filename.rst
```

#### NOTE
Previously, image filenames would mostly be named with numbers (e.g., `feature01.png`) and
placed in a single `media` folder. While it is advised not to name your *new* images in
that fashion, it is also essential **not to rename unchanged files**, as doing this would double
the weight of renamed image files on the repository. They will eventually all be replaced as the
content referencing those images is updated.

<a id="contributing-content-alt-tags"></a>

### ALT tags

An **ALT tag** is a *text alternative* to an image. This text is displayed if the browser fails to
render the image. It is also helpful for users who are visually impaired. Finally, it helps
search engines, such as Google, to understand what the image is about and index it correctly, which
improves .

Good ALT tags are:

- **Short** (one line maximum);
- **Not a repetition** of a previous sentence or title;
- A **good description** of the action happening in the image;
- Easily **understandable** if read aloud.

#### SEE ALSO
[RST cheat sheet: images](rst_guidelines.md#contributing-rst-images)
