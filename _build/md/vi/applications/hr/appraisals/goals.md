# Mục tiêu

The Odoo *Appraisals* application allows managers to set goals for their employees. That way,
employees know what to work toward before their next review.

To view all goals, navigate to Appraisals app ‣ Goals. This presents all the
goals for every employee, in a default Kanban view.

<a id="appraisals-goal-card"></a>

Each goal card contains the following information:

- Goal: the name of the goal.
- Employee: the employee the goal is assigned to.
- <i class="fa fa-clock-o"></i> (clock) icon: displays the corresponding [activity icon](../../essentials/activities.md) for the record. If no activities are scheduled, the default icon is
  the <i class="fa fa-clock-o"></i> (clock). If any activities have been scheduled, the icon
  represents the activity scheduled soonest.
- Deadline: the due date for the goal.
- Progress: the percentage of competency set for the goal. The options are
  0%, 25%, 50%, 75%, or 100%.
- Employee Icon: the profile icon of the employee the goal is assigned to.

If a goal is completed, a Done banner appears in the top-right corner of the goal card.

![The goals Kanban view, with nine goal cards.](applications/hr/appraisals/goals/goals.png)

#### NOTE
Every individual goal requires its own record for each employee. If multiple employees have the
same goal, a goal card for each employee appears on the list.

For example, if Bob and Sara have the same goal of `Typing`, two cards appear in the Kanban view:
one `Typing` goal for Bob, and another `Typing` goal for Sara.

## New goal

To create a new goal, navigate to Appraisals app ‣ Goals, and click
New top-left corner to open a blank goal form.

Input the Goal, Employee, Progress, and Deadline,
information on the goal card, as discussed in the [goal card](#appraisals-goal-card) section of
this document.

The information requested is all the same information that appears on the goal card in the Kanban
view, with the addition of a Tags field and a Description tab.

The current user populates the Employee field, by default, and the Manager
field populates with the manager set on the employee profile.

Make any necessary changes to the form, and add any notes that might be useful to clarify the goal
in the Description tab.

![A goal form filled out for a Python skill, set to 50% proficiency.](applications/hr/appraisals/goals/new-goal.png)

## Completed goals

When a goal has been met, it is important to update the record. A goal can be marked as `Done` in
one of two ways: from the main Goals dashboard, or from the individual goal card.

To mark a goal as `Done` from the main Goals dashboard, click on the
<i class="fa fa-ellipsis-v"></i> (vertical ellipsis) icon in the top-right of a goal card.

#### NOTE
The <i class="fa fa-ellipsis-v"></i> (vertical ellipsis) icon **only** appears when the mouse
hovers over the top-right corner of a goal card.

Then, click Mark as Done from the resulting drop-down menu. A green Done
banner appears in the top-right corner of the goal card.

To mark a goal as `Done` from the goal card itself, click on a goal card to open that goal's form.
Then, click the Mark as Done button in the top-left of the form. When clicked, a green
Done banner appears in the top-right corner of the goal form.
