# Tạo nhiệm vụ

Tasks in Odoo Project can be created manually or automatically, including from emails or website
forms.

## Manual task creation

Open the Project app and choose the desired project. Create a new task by doing one of the
following:

> - Clicking the <i class="fa fa-plus"></i> (plus) button in the upper left corner. This creates
>   a new task in the first stage of your Kanban view.
> - Pressing the <i class="fa fa-plus"></i> (plus) button next to the Kanban stage name. This
>   creates a new task in this Kanban stage.

Fill in the Task Title and add one or more Assignees, then click
Add.

<a id="task-creation-task-configuration"></a>

### Cấu hình nhiệm vụ

Click the task to open it. The task form includes the following fields that you can fill in:

> - Task Title: title of the task.
> - <i class="fa fa-star-o"></i> (Star): click the <i class="fa fa-star-o"></i> (star) icon to mark
>   the task as high priority. The icon will turn yellow. Click it again to remove the high priority.
> - Project: the project that this task belongs to.
> - Assignees: the person(s) in charge of handling the work on this task.
> - Tags: custom labels allowing to categorize and filter your tasks.
> - Customer: the person or company that will be billed for this task. This field only
>   appears in tasks that belong to billable projects.
> - Sales Order Item: this can be either the sales order that was used to create this
>   task, or a sales order that was linked to this task manually. This field only appears in tasks
>   linked to billable projects.
> - Allocated Time: the amount of time that the work on this task is expected to last,
>   tracked by timesheets.
> - Deadline: the expected end date of the task. Once this field is filled in, you can
>   also add a start date to designate the entire time frame of the tasks' duration.

<a id="task-creation-email-alias"></a>

## Creating tasks from an email alias

This feature allows for project tasks to be automatically created once an email is delivered to a
designated email address.

To configure it, open the Project app, then click the <i class="fa fa-ellipsis-v"></i> (vertical
ellipsis) icon next to the desired project's name. Select Settings, then open the
Settings tab.

Fill in the Create tasks by sending an email to field as follows:

> - **Section of the alias before the @ symbol**: type the name of the email alias, e.g. `contact`,
>   `help`, `jobs`.
> - **Domain**: in most cases, this is filled in by default with your [domain](../../../general/email_communication.md).
> - **Accept Emails From**: refine the senders whose emails will create tasks in the project.
![View of the email alias chosen on the dashboard view in Odoo Project](task_creation/email-configuration.png)

Once configured, the email alias can be seen under the name of your project on the Kanban dashboard.

When an email is sent to the alias, the email is automatically converted into a project task. The
following rules apply:

- The email sender is displayed in the Customer field.
- The email subject is displayed in the Task Title field.
- The email body is displayed in the Description field.
- The whole content of the email is additionally displayed in the **chatter**.
- All the recipients of the email (To/Cc/Bcc) that are Odoo users are automatically added as
  **followers** of the task.

## Creating tasks from a website form

If you have the Website app installed in your database, you can configure any form on your
website to trigger the creation of tasks in a project.

1. Go to the website page where you wish to add the the form and
   [add the Form building block](../../../websites/website/web_design/building_blocks.md#websites-website-web-design-building-blocks).
2. In the website editor, edit the following fields:
   - Action: select Create a Task.
   - Project: choose the project that you want the new tasks to be created in.
3. [Customize the form](../../../websites/website/web_design/building_blocks/dynamic_content.md#website-dynamic-content-form).

When the form is submitted, it automatically creates a project task. The task's content is defined
by the form's corresponding fields.

#### SEE ALSO
[Dynamic website content](../../../websites/website/web_design/building_blocks/dynamic_content.md)
