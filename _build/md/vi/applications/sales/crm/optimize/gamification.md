# Trò chơi hóa CRM

In Odoo's *CRM* app, *gamification tools* provide the opportunity to evaluate and motivate users
through customizable challenges, goals, and rewards. Goals are created to target actions within the
*CRM* app, and can be tracked and rewarded automatically to participating sales teams.

## Cấu hình

To install the *CRM Gamification* module, navigate to the Apps application. Click
into the Search... bar at the top of the page and remove the Apps filter.
Type `CRM Gamification` to search.

On the CRM Gamification module, click Install. This module features goals
and challenges related to the *CRM* and *Sales* applications.

![View of the gamification module being installed in Odoo.](applications/sales/crm/optimize/gamification/gamification-module-install.png)

#### NOTE
If **both** the *CRM* and *Sales* apps are installed, the *CRM Gamification* module is
automatically installed on the database.

To access the *Gamification Tools* menu, first enable [Chế độ lập trình viên (chế độ gỡ lỗi)](../../../general/developer_mode.md#developer-mode).

Next, navigate to Settings app ‣ Gamification Tools.

![View if the gamification tools menu in Odoo Settings.](applications/sales/crm/optimize/gamification/gamification-tools-menu.png)

<a id="crm-create-rewards"></a>

## Create badges

*Badges* are awarded to users when they have completed a challenge. Different badges can be awarded
based on the type of task completed, and can be issued to more than one user, depending on the time
they accomplish the goal.

To view the existing badges, or create a new one, navigate to Settings ‣
Gamification Tools ‣ Badges.

![View of the badges page in Odoo.](applications/sales/crm/optimize/gamification/badges.png)

#### NOTE
Some badges can be awarded outside of challenges, as well. Select the Kanban card for the desired
badge, then click Grant. This opens a Grant Badge pop-up window. Select
a user from the Who would you like to reward? field.

Add any additional information regarding why the user is receiving the reward in the field below,
then click Grant Badge.

To create a new badge, click New at the top-left of the page to open a blank form.
Enter a name for the Badge, followed by a description.

The Allowance to Grant field determines when a badge can be granted, and by whom:

- Everyone: this badge can be manually granted by any user.
- A selected list of users: this badge can only be granted by a select group of users.
  If this option is selected, it generates a new field, Authorized Users. Choose the
  appropriate users from this drop-down list.
- People having some badges: this badge can only be granted by users who have already
  been awarded a specific badge. If this option is selected it generates a new field,
  Required Badges. Use this drop-down list to select the badge(s) a user must have
  before they can award this badge to others.
- No one, assigned through challenges: this badge cannot be manually granted, it can
  only be awarded through challenges.

To limit the number of badges a user can send, tick the Monthly Limited Spending
checkbox. This sets a limit on the number of times a user can grant this badge. In the
Limitation Number field, enter the maximum number of times this badge can be sent per
month, per person.

![The details page for a new badge.](applications/sales/crm/optimize/gamification/create-badge.png)

<a id="crm-create-challenge"></a>

## Create a challenge

To create a challenge, navigate to to Settings ‣ Gamification Tools ‣
Challenges. Click New in the top-left corner to open a blank challenge form.

At the top of the form, enter a Challenge Name.

### Create assignment rules

To assign the challenge to specific users, one or more assignment rules must be utilized.

Click into the first field under Assign Challenge to, and select a parameter from the
drop-down list to define the rule. Then, click into the next field to define the rule's operator. If
necessary, click into the third field to further define the parameter.

In the Periodicity field, select a time frame for goals to be automatically assessed.

### Add goals

Challenges can be based on a single goal, or can include multiple goals with different targets. To
add a goal to the challenge, click Add a line on the Goals tab.

In the Goal Definition field, choose a goal from the drop-down list. The
Condition field automatically updates to reflect the condition set on the goal
definition.

Enter a Target for the goal based on the Suffix.

Repeat these steps for each additional goal.

![The goals tab of a challenge form.](applications/sales/crm/optimize/gamification/challenge-goals.png)

### Thêm phần thưởng

Next, click the Reward tab. Choose the [badges](#crm-create-rewards) to be awarded
For 1st User and For Every Succeeding User by selecting them from the
drop-down lists.

#### NOTE
Badges are granted when a challenge is finished. This is either at the end of a running period,
at the end date of a challenge, or when the challenge is manually closed.

After setup is complete, click the Start Challenge button at the top-left of the page to
begin the challenge.
