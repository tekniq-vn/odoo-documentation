# Diễn đàn

**Odoo Forum** is a question-and-answer forum designed with providing customer support in mind.
Adding a forum to a website enables you to build a community, encourage engagement, and share
knowledge.

<a id="forum-create"></a>

## Create a forum

To create or edit a forum, go to Website ‣ Configuration ‣ Forum: Forums. Click
New or select an existing forum and configure the following elements.

Forum Name: add the name of the forum.

Mode: select Questions to enable marking an answer as best, meaning
questions then appear as *solved*, or Discussions if the feature is not needed.

#### NOTE
Regardless of the selected mode, only **one answer** per user is allowed on a single post.
Commenting multiple times is allowed, however.

Default Sort: choose how questions are sorted by default.

> - Newest: by latest question posting date
> - Last Updated: by latest posting activity date (answers and comments included)
> - Most Voted: by highest vote tally
> - Relevance: by post relevancy (determined by a formula)
> - Answered: by likelihood to be answered (determined by a formula)

#### NOTE
Users have several sorting options (total replies, total views, last activity) on the forum
front end.

Privacy: select Public to let anyone view the forum, Signed In
to make it visible only for signed-in users, or Some users to make it visible only for a
specific user access group by selecting one Authorized Group.

Next, configure the [karma gains](#forum-karma-gains) and the [karma-related rights](#forum-karma-related-rights).

<a id="forum-karma"></a>

### Điểm karma

Karma points can be given to users based on different forum interactions. They can be used to
determine which forum functionalities users can access, from being able to vote on posts to
having moderator rights. They are also used to set user [ranks](#forum-ranks).

#### IMPORTANT
- A user's karma points are shared across all forums, courses, etc., of a single Odoo website.
- eLearning users can earn karma points through different [course interactions](elearning.md#elearning-karma) and by [completing quizzes](elearning.md#elearning-quiz).

<a id="forum-karma-gains"></a>

#### Karma gains

Several forum interactions can give or remove karma points.

| Tương tác           | Mô tả                                                                           |   Default karma gain |
|---------------------|---------------------------------------------------------------------------------|----------------------|
| Asking a question   | You post a question.                                                            |                    2 |
| Question upvoted    | Another user votes for a question you posted.                                   |                    5 |
| Question downvoted  | Another user votes against a question you posted.                               |                   -2 |
| Answer upvoted      | Another user votes for an answer you posted.                                    |                   10 |
| Answer downvoted    | Another user votes against an answer you posted.                                |                   -2 |
| Accepting an answer | You mark an answer posted by another user as best.                              |                    2 |
| Answer accepted     | Another user marks an answer you posted as best.                                |                   15 |
| Answer flagged      | A question or an answer you posted is [marked as offensive](#forum-moderation). |                 -100 |

#### NOTE
New users receive **three points** upon validating their email address.

To modify the default values, go to Website ‣ Configuration ‣ Forum: Forums,
select the forum, and go to the Karma Gains tab. Select a value to edit it.

If the value is positive (e.g., `5`), the number of points will be added to the user's tally each
time the interaction happens on the selected forum. Conversely, if the value is negative (e.g.,
`-5`), the number of points will be deducted. Use `0` if an interaction should not impact a user's
tally.

<a id="forum-karma-related-rights"></a>

#### Karma-related rights

To configure how many karma points are required to access the different forum functionalities, go
to Website ‣ Configuration ‣ Forum: Forums, select the forum, and go to the
Karma Related Rights tab. Select a value to edit it.

#### WARNING
Some functionalities, such as Edit all posts, Close all posts,
Delete all posts, Moderate posts, and Unlink all comments,
are rather sensitive. Make sure to understand the consequences of giving *any* user reaching the
set karma requirements access to such functionalities.

| Functionality                                  | Mô tả                                                                                                                                                                 |   Default karma requirement |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Ask questions                                  | Post questions.                                                                                                                                                       |                           3 |
| Answer questions                               | Post answers to questions.                                                                                                                                            |                           3 |
| Upvote                                         | Vote for questions or answers.                                                                                                                                        |                           5 |
| Downvote                                       | Vote against questions or answers.                                                                                                                                    |                          50 |
| Edit own posts                                 | Edit questions or answers you posted.                                                                                                                                 |                           1 |
| Edit all posts                                 | Edit any question or answer.                                                                                                                                          |                         300 |
| Close own posts                                | Close questions or answers you posted.                                                                                                                                |                         100 |
| Close all posts                                | Close any question or answer.                                                                                                                                         |                         500 |
| Delete own posts                               | Delete questions or answers you posted.                                                                                                                               |                         500 |
| Delete all posts                               | Delete any question or answer.                                                                                                                                        |                           1 |
| Nofollow links                                 | If you are under the karma threshold, a *nofollow* attribute tells search engines to ignore<br/>links you post.                                                       |                         500 |
| Accept an answer on own questions              | Mark an answer as best on questions you posted.                                                                                                                       |                          20 |
| Accept an answer to all questions              | Mark an answer as best on any question.                                                                                                                               |                         500 |
| Editor Features: image and links               | Add links and images to your posts.                                                                                                                                   |                          30 |
| Comment own posts                              | Post comments under questions or answers you created.                                                                                                                 |                           1 |
| Comment all posts                              | Post comments under any question or answer.                                                                                                                           |                           1 |
| Convert own answers to comments and vice versa | Convert comments you posted as answers.                                                                                                                               |                          50 |
| Convert all answers to comments and vice versa | Convert any comment as answer.                                                                                                                                        |                         500 |
| Unlink own comments                            | Delete comments you posted.                                                                                                                                           |                          50 |
| Unlink all comments                            | Delete any comment.                                                                                                                                                   |                         500 |
| Ask questions without validation               | Questions you post do not require to be [validated](#forum-moderation) first.                                                                                         |                         100 |
| Flag a post as offensive                       | Flag a question or answer as offensive.                                                                                                                               |                         500 |
| Moderate posts                                 | Access all [moderation tools](#forum-moderation).                                                                                                                     |                           1 |
| Change question tags                           | Change posted questions' [tags](#forum-tags) (if you have the right to edit them).                                                                                    |                          75 |
| Create new tags                                | Create new [tags](#forum-tags) when posting questions.                                                                                                                |                          30 |
| Display detailed user biography                | When a user hovers their mouse on your avatar or username, a popover box showcases your<br/>karma points, biography, and number of [badges](#forum-badges) per level. |                         750 |

<a id="forum-gamification"></a>

### Trò chơi hóa

Ranks and badges can be used to encourage participation. Ranks are based on the total [karma
points](#forum-karma), while badges can be granted manually or automatically by completing
challenges.

<a id="forum-ranks"></a>

#### Ranks

To create new ranks or modify the default ones, go to Website ‣ Configuration ‣
Forum: Ranks and click New or select an existing rank.

Add the Rank Name, the Required Karma points to reach it, its
Description, a Motivational message to encourage users to reach it, and an
image.

![Default forum ranks](applications/websites/forum/ranks.png)

<a id="forum-badges"></a>

#### Huy hiệu

To create new badges or modify the default ones, go to Website ‣ Configuration ‣
Forum: Badges and click New or select an existing badge.

Enter the badge name and description, add an image, and configure it.

##### Assign manually

If the badge should be granted manually, select which users can grant them by selecting one of the
following Allowance to Grant options:

- Everyone: all non-portal users (since badges are granted from the backend).
- A selected list of users: users selected under Authorized Users.
- People having some badges: users who have been granted the badges selected under
  Required Badges.

It is possible to restrict how many times per month each user can grant the badge by enabling
Monthly Limited Sending and entering a Limitation Number.

##### Assign automatically

If the badge should be granted **automatically** when certain conditions are met, select
No one, assigned through challenges under Allowance to Grant.

Next, determine how the badge should be granted by clicking Add under the
Rewards for challenges section. Select a challenge to add it or create one by clicking
New.

![Default forum badges](applications/websites/forum/badges.png)

<a id="forum-tags"></a>

### Thẻ

Users can use tags to filter forum posts.

To manage tags, go to Website ‣ Configuration ‣ Forum: Tags. Click
New to create a tag and select the related Forum.

<a id="forum-use"></a>

## Use a forum

#### NOTE
Access to many functionalities depends on a user's [karma points](#forum-karma-related-rights).

<a id="forum-post"></a>

### Post questions

To create a new post, access the forum's front end, click New Post, and fill in the
following:

- Title: add the question or the topic of the post.
- Description: add a description for the question.
- Tags: add up to five [tags](#forum-tags).

Click Post Your Question.

<a id="forum-interact"></a>

### Interact with posts

Different actions are possible on a post.

- Mark a question as **favorite** by clicking the star button (☆).
- Follow a post and get **notifications** (by email or within Odoo) when it is answered by clicking
  the bell button (🔔).
- **Vote** *for* (up arrow ▲) or *against* (down arrow ▼) a question or
  answer.
- Mark an answer as **best** by clicking the check mark button (✔). This option is only
  available if the Forum Mode is set to Questions.
- Answer a question.
- **Comment** on a question or answer by clicking the speech bubble button (💬).
- **Share** a question on Facebook, Twitter, or LinkedIn by clicking the *share nodes* button.

Click the ellipsis button (...) to:

> - Edit a question or answer.
> - Close a question.
> - Delete a question, answer, or comment. It is possible to Undelete
>   questions afterward.
> - Flag a question or answer as offensive.
> - Convert a comment into an answer.
> - View the related [Helpdesk ticket](../services/helpdesk/overview/help_center.md#helpdesk-forum), if any.
![Posts actions](applications/websites/forum/post-actions.png)

#### NOTE
By default, 150 karma points are required to view another user's profile. This value can be
configured when creating a new website.

<a id="forum-moderation"></a>

## Moderate a forum

On the forum's front end, the sidebar's Moderation tools section gathers the essential
moderator functionalities.

![Forum sidebar moderation tools](applications/websites/forum/moderation-tools.png)

To Validate: access all questions and answers waiting for validation before being
displayed to non-moderator users.

![Question to validate](applications/websites/forum/to-validate.png)

#### NOTE
A question is pending if a user does not have the required karma. The user is not able to post
questions or answers while awaiting validation. Only one pending question per user is allowed per
forum.

Flagged: access all questions and answers that have been flagged as offensive. Click
Accept to remove the offensive flag or Offensive to confirm it, then select
a reason and click Mark as offensive. The post is then hidden from users without
moderation rights, and 100 karma points are deducted from the offending user's tally.

![Offensive reason selection](applications/websites/forum/offensive-reason.png)

Closed: access all questions that have been closed. It is possible to Delete
or Reopen them. To close a question, open it, click the ellipsis button
(...), then Close, select a Close Reason, and click
Close post. The post is then hidden from users without moderation rights.

#### NOTE
When selecting Spam or advertising or Contains offensive or malicious
remarks as the reason, 100 karma points are deducted from the poster's tally.
