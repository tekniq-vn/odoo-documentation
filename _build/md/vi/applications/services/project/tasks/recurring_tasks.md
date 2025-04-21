# Nhiệm vụ định kỳ

When handling a project, the same task often needs to be performed several times: for example,
weekly meetings or status reports. The **recurring tasks** feature allows you to automate the
creation of those tasks.

#### SEE ALSO
[Odoo Tutorials: Recurring tasks](https://www.odoo.com/slides/slide/recurring-tasks-1946)

## Cấu hình

To enable recurring tasks, go to Project ‣ Configuration ‣ Settings, then
activate Recurring Tasks, and press Save.

### Set up task recurrence

In an existing task, click the <i class="fa fa-repeat"></i> (Recurrent) button next to the
Deadline field. Then, configure the Repeat Every field according to your
needs.

A new task in recurrence will be created once the status of the previous task is set to
Done or Canceled.

The new task is created on the project dashboard with the following configuration:

- Stage: is set to the first stage of the project dashboard (New or
  equivalent);
- Name, Description, Project, Assignees,
  Customer, Tags: are copied from the original task;
- Deadline: is updated based on the Repeat Every field (e.g., if the task is
  set to repeat once a week, 7 days will be added to the deadline);
- Milestones, Timesheets, Chatter,
  Activities, Subtasks: are **not** copied from the original task.

Once a recurrence is configured, a **smart button** on the task displays the total number of
existing recurrences.

### Edit or stop task recurrence

**To edit** the recurrence, open the last task in recurrence. Any changes made on the task will be
applied to the tasks that will be created in the future.

**To stop** the recurrence, open the last task in recurrence and press the Recurrent
button next to the Planned date.
