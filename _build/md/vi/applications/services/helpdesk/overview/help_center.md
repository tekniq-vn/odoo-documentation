# Trung tâm hỗ trợ

Odoo *Helpdesk* integrates with the *Forum*, *eLearning*, and *Knowledge* apps to create the *Help
Center*. The *Help Center* is a centralized location where teams and customers can search for and
share detailed information about products and services.

![Overview of the settings page of a team emphasizing the Help Center features.](applications/services/helpdesk/overview/help_center/help-center-enable-features.png)

## Cấu hình

To activate any *Help Center* features (*Forums*, *eLearning*, or *Knowledge*) on a *Helpdesk* team,
go to Helpdesk app ‣ Configuration ‣ Helpdesk Teams and select a team, or
create a [new one](../../helpdesk.md). Verify the Visibility of the team is set to
Invited portal users and all internal users (public) in the Visibility &
Assignment section.

Additionally, the Website Form option on the *Helpdesk* team page **must** be enabled to
activate any of the *Help Center* features. When one or more of the *Help Center* features is
enabled, the Website Form is automatically enabled, as well.

#### SEE ALSO
[Helpdesk Overview](../../helpdesk.md)

## Kiến thức

Odoo's *Knowledge* application is a collaborative library, where users can store, edit, and share
information. The *Knowledge* app is accessible throughout the database by clicking on the
Knowledge (bookmark) icon.

![View of a message in Helpdesk focusing on the Knowledge bookmark icon.](applications/services/helpdesk/overview/help_center/help-center-knowledge-bookmark-icon.png)

### Enable Knowledge on a Helpdesk team

To enable the *Knowledge* feature on a *Helpdesk* team, go to Helpdesk app ‣
Configuration ‣ Helpdesk Teams and select a team, or create a [new one](../../helpdesk.md).

When a team has been selected or created, Odoo displays that team's detail form.

On the team's detail form, scroll down to the Help Center section. Then, click the box
next to Knowledge to activate the *Knowledge* feature. When clicked, a new field
labeled, Article appears.

Clicking the Article field reveals a drop-down menu. At first, there is only one option
in the drop-down menu titled Help, which Odoo provides by default. Select
Help from the drop-down menu to choose this article.

Once an article has been created and assigned to a *Helpdesk* team, content can be added and
organized through the *Knowledge* app.

#### SEE ALSO
[Editing Knowledge articles](../../../productivity/knowledge/articles_editing.md)

### Search articles from a Helpdesk ticket

When members of a *Helpdesk* team are trying to solve a ticket, they can search through the content
in the *Knowledge* app for more information on the issue.

To search *Knowledge* articles, open a ticket — either from the *Helpdesk* app dashboard, or by
going to Helpdesk app ‣ Tickets ‣ All Tickets, then select a ticket from the
list.

When a ticket is selected, Odoo reveals that ticket's detail form.

Click the Knowledge (bookmark) icon, located at the top-right of the page, to open a
pop-up search window.

![View of knowledge search window from a helpdesk ticket.](applications/services/helpdesk/overview/help_center/help-center-knowledge-search.png)

When Odoo reveals the desired article, click it, or highlight the Article title, and
press **Enter**. This will open the article in the Knowledge application.

To open the article in a new tab, press **Ctrl + Enter**.

#### Share an article to the Help Center

To make a *Knowledge* article available to customers and website visitors, it **must** be published.

#### IMPORTANT
Even though the *Help* article has been enabled on a team, Odoo does **not** share all the nested
articles to the web. Individual articles intended for customers **must** be published for them to
be viewable on the website.

To publish an article, navigate to the desired article, by following the above steps, and click the
Share icon in the upper-right corner. This reveals a menu. Slide the toggle button
labeled Share to Web to read Article Published.

![View of a knowledge article focused on sharing and publishing options.](applications/services/helpdesk/overview/help_center/help-center-knowledge-sharing.png)

### Solve tickets with a clipboard box

*Clipboard* boxes can be added to *Knowledge* articles to allow content to be reused, copied, sent
as messages, or added to the description on a ticket. This allows teams to maintain consistency when
answering customer tickets, and minimize the amount of time spent on responding to repeat questions.

#### Add clipboard boxes to articles

To create a clipboard box, go to Knowledge app ‣ Help. Click on an existing
nested article or create a new one by clicking the ➕ (plus sign) icon next to *Help*.

Type `/` to open the *powerbox*, and view a drop-down list of [commands](../../../productivity/knowledge/articles_editing.md). Select or type `clipboard`. A gray block is
then added to the page. Add any necessary content to this block.

![View of a clipboard in knowledge with focus on send and copy options.](applications/services/helpdesk/overview/help_center/help-center-knowledge-clipboard-options.png)

#### NOTE
Clipboard boxes only display the Use as description or Send as Message
options if they are accessed directly from the *Helpdesk*.

#### Use clipboard boxes in tickets

Clipboard boxes can be used to respond directly to a *Helpdesk* ticket as a message, or to add
information to the ticket's description.

To use clipboard boxes in a *Helpdesk* ticket, first, open a ticket, either from the
Helpdesk dashboard or by going to Helpdesk app ‣ Tickets ‣ All
Tickets and selecting a ticket from the list.

Click on the Knowledge (bookmark) icon in the top-right corner. This opens a search
window. In this search window, select, or search, for the desired article. Doing so reveals that
article page in the Odoo *Knowledge* application.

To use a clipboard box to respond to a ticket, click Send as message in the upper-right
corner of the clipboard box, located in the body of the article.

Doing so opens a Compose Email pop-up window. In this window, select the recipients,
make any necessary additions or edits to the clipboard content, then click Send.

<a id="helpdesk-forum"></a>

## Diễn đàn cộng đồng

A *Community Forum* provides a space for customers to answer each other's questions and share
information. By integrating a forum with a *Helpdesk* team, tickets submitted by customers can be
converted to posts and shared.

### Enable forums on a Helpdesk team

To enable Community Forums on a *Helpdesk* team, start by navigating to
Helpdesk app ‣ Configuration ‣ Helpdesk Teams and select a team, or create a
[new one](../../helpdesk.md).

Selecting or creating a team reveals that team's detail form. Scroll down to the Help
Center section of features, and enable Community Forum, by checking the box beside it.

When activated, a new field labeled Forums appears beneath.

Click the empty Forums field to reveal a drop-down menu. By default, there is only one
option to begin with, labeled Help. That is the option Odoo automatically created when
the Community Forums feature was enabled. Select Help from the drop-down
menu to enable that forum.

To create a new forum, type a name into the blank Forums field, then click the
Create and Edit option. Multiple forums can be selected in this field.

#### SEE ALSO
[Forum documentation](../../../websites/forum.md)

### Create a forum post from a Helpdesk ticket

When a *Helpdesk* team has a *Forum* enabled, tickets submitted to that team can be converted to
forum posts.

To do that, select a ticket, either from a team's pipeline or from Tickets ‣ All
Tickets in the Helpdesk application.

At the top of the ticket detail form, click the Share on Forum button.

![Overview of the Forums page of a website to show the available ones in Odoo Helpdesk.](applications/services/helpdesk/overview/help_center/help-center-share-on-forum.png)

When clicked, a pop-up window appears. Here, the Forum post and Title can be
edited to correct any typos, or modified to remove any proprietary or client information.

Tags can also be added to help organize the post in the forum, making it easier for
users to locate during a search. When all adjustments have been made, click Create and
View Post.

## Học trực tuyến

Odoo *eLearning* courses offer customers additional training and content in the form of videos,
presentations, and certifications/quizzes. Providing additional training enables customers to work
through issues and find solutions on their own. They can also develop a deeper understanding of the
services and products they are using.

### Enable eLearning courses on a Helpdesk team

To enable *eLearning* courses on a *Helpdesk* team, go to Helpdesk app ‣
Configuration ‣ Helpdesk Teams and select a team, or create a [new one](../../helpdesk.md).

On the team's settings page, scroll to the Help Center section, and check the box next
to eLearning. A new field appears below, labeled Courses.

Click the empty field next to Courses beneath the eLearning feature to
reveal a drop-down menu. Select an available course from the drop-down menu, or type a title into
the field, and click Create and edit to create a new course from this page. Multiple
courses can be assigned to a single team.

### Create an eLearning course

A new *eLearning* course can be created from the Helpdesk team's settings page, as in
the step above, or from the *eLearning* app.

To create a course directly through the *eLearning* application, navigate to
eLearning ‣ New. This reveals a blank course template that can be customized and
modified as needed.

On the course template page, add a Course Title, and below that, Tags.

Click on the Options tab.

Under Access Rights, select which users are able to view and enroll in the course.

The Show Course To field defines who can access the courses. The Enroll
Policy field specifies how they can register for the course.

Under Display, choose the preferred course Type.

#### Add content to an eLearning course

To add content to a course, click the Content tab and select Add Content.
Choose the Content Type from the drop-down menu and upload the file, or paste the link,
where instructed. Click Save when finished. Click Add Section to organize
the course in sections.

![View of a course being published for Odoo Helpdesk.](applications/services/helpdesk/overview/help_center/help-center-elearning-course-contents-page.png)

#### NOTE
In order to add a certification to a course, go to eLearning ‣ Configuration
‣ Settings, check the box labeled Certifications, and Save to activate
the setting.

#### SEE ALSO
[Odoo Tutorials: eLearning](https://www.odoo.com/slides/elearning-56)

### Publish an eLearning course

To allow customers to enroll in a course, both the course and the contents **must** be published.

To make the entire course available at once, each piece of course content must be published first,
then the course can be published.

To publish a course, choose a course from the *eLearning* dashboard. On the course template page,
click the Go to Website smart button.

This will reveal the front end of the course's web page. At the top of the course web page, move
the Unpublished toggle switch to Published.

#### Publish eLearning course contents from the back-end

To publish *eLearning* course content from the back-end, choose a course from the *eLearning*
dashboard. On the course template page, click the Published Contents smart button.

Doing so reveals a separate page displaying all the published content related to that course. Remove
the default Published filter from the search bar in the upper-right corner, to reveal
all the content related to the course - even the non-published content.

Click the ≣ (bars) icon in the upper-right corner, directly beneath the search bar to
switch to list view.

While in list view, there is a checkbox on the far-left of the screen, above the listed courses, to
the left of the Title column title. When that checkbox is clicked, all the course
contents are selected at once.

With all the course content selected, click any of the boxes in the Is Published column.
This reveals a pop-up window, asking for confirmation that all selected records are intended to be
published. Click Confirm to automatically publish all course content.

![View of a course contents being published in Odoo Helpdesk back-end.](applications/services/helpdesk/overview/help_center/help-center-elearning-publish-back-end.png)
