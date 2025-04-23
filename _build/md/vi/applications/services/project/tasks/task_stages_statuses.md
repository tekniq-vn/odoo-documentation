# Task stages and statuses

## Giai đoạn nhiệm vụ

Task stages are displayed as columns in the project's Kanban view, and allow you to update the
progress of its tasks with a drag-and-drop. In most projects, the stages will be akin to **New**,
**In progress**, **Backlog**, etc.

By default, task stages are project-specific but can be shared across multiple projects that follow
the same workflow.

### Creating task stages

Odoo Project doesn’t provide default stages but instead allows you to create custom stages tailored
to your specific business needs. You are prompted to do so immediately after [creating a new
project](../project_management.md#project-management-configuration).

To create a stage, type its name into the Stage... field, then click Add.

### Editing task stages

To edit the task stage, click the <i class="fa fa-cog"></i> (cog) icon next to its name. From
there, click one of the following:

> - Fold: to hide the task stage and all of the tasks in this stage from the Kanban view.
> - Chỉnh sửa:
>   - Name: to change the name of the stage.
>   - SMS/Email Template: to automatically send an email or SMS notification to the
>     customer when a task reaches this stage.
>   - Folded in Kanban: to hide the task stage and all of the tasks in this stage from
>     the Kanban view.
>   - Projects: to share this task stage between several projects.
>   - Automations: to create [custom rules that trigger automatic actions](../../../studio/automated_actions.md) (e.g., creating activities, adding followers, or sending
>     webhook notifications). Note that this will activate Studio in your database, which may impact
>     your pricing plan.
> - Delete: to delete this stage.
> - Archive/Unarchive all: to archive or unarchive all of the tasks in this stage.

<a id="project-tasks-task-stages-statuses-statuses"></a>

## Trạng thái nhiệm vụ

Task statuses are used to track the status of tasks within the Kanban stage, as well as to close the
task when it’s done or canceled. Unlike Kanban stages, they cannot be customized; five task statuses
exist in Odoo and are used as follows:

> - In Progress: this is the default state of all tasks, meaning that work required for
>   the task to move to the next Kanban stage is ongoing.
> - Changes Requested: to highlight that changes, either requested by the customer or
>   internally, are needed before the task is moved to the next Kanban stage.
> - Approved: to highlight that the task is ready to be moved to the next stage.
> - Canceled: to cancel the task.
> - Done: to close the task once it's been completed.

#### NOTE
- The Changes Requested and Approved task statuses are cleared as soon as
  the task is moved to another Kanban stage. The task status reverts to the default In
  Progress status so that Changes Requested or Approved status can be
  applied again once the necessary work has been completed in this Kanban stage.
- The Done and Canceled statuses are independent from the Kanban stage.
  Once a task is marked as Done or Canceled, it is closed. If needed, it
  can be reopened by changing its status.
