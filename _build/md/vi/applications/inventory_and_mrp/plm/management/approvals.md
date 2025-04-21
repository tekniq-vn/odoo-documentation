# Phê duyệt

<a id="plm-approvals"></a>

Notify stakeholders and managers automatically by assigning approvers to stages of [engineering
change orders](../manage_changes/engineering_change_orders.md#plm-eco) (ECOs) under review. Changes can only be applied after the assigned
approver accepts them. Approvals ensure reviews by team members, which prevents mistakes and
premature actions.

#### SEE ALSO
[Stage configuration](../manage_changes/eco_type.md#plm-eco-stage-config)

## Add approver

To add an approver, first go to the PLM app, and click on the project card of an
ECO type to open the Gantt view of the .

On the Engineering Change Orders page, hover over the intended stage, and select the
⚙️ (gear) icon. Then, click Edit to open a pop-up window.

#### NOTE
Approvers can be added to any stage, but it's strongly recommended to assign them to the
*verification* stage, which comes before the *closing* stage, where  are applied, and the
 version is updated.

See the documentation about [stage types](../manage_changes/eco_type.md#plm-eco-stage-config) for more information.

<a id="plm-approvals-approval-type"></a>

In the Edit stage pop-up window, click the Add a line button, located under
Approvals. Then, type in the approver's position (or title) under Role (e.g.
`Engineering Manager`, `Quality Team`, etc.), and select the relevant User from the
drop-down menu.

Next, set the Approval Type to Is required to approve, Approves,
but the approval is optional, or Comments only.

## Manage approvals

Approvers can easily track their to-do approvals by navigating to the PLM app, and
looking at the card for an ECO type, which shows the count of open tasks assigned to them.

Here's what each button on an ECO project card does:

1. The # Engineering Changes button displays a count of in-progress  of this ECO
   type. Clicking the button opens the Gantt view of the Engineering Change Orders page.
2. My Validations displays a count of  the approver must accept or reject.
   Clicking on this button displays  pending approval or rejected (marked with the red
   Blocked state).
3. The All Validations button shows the count of  awaiting approval or rejected by
   any approver. Clicking it reveals these pending .
4. To Apply displays a count of  to which the user needs to apply changes.
   Clicking on the button displays all the  to approve, and apply changes to, in the
   verification stage.

    marked with the green Done stage have already been approved, and the user just
   needs to click on the  to enter the form view, and click the Apply Changes
   button.

![Display count of validations to-do and buttons to open filtered list of ECOs.](applications/inventory_and_mrp/plm/management/approvals/validation-overview.png)

### Phê duyệt ECO

Navigate to an  in a verification stage, while logged in as the assigned approver, to see the
Approve, Reject, and Apply Changes buttons.

To approve the , and apply the changes onto the production ,
click Approve, and then Apply Changes.

Note that the Apply Changes button will **not** work unless the Approve
button was clicked first. Additionally, the chatter logs the history of the clicked buttons.

#### WARNING
When the Approval Type is **not** set to Is required to approve, approval
from the associated user is not needed before applying changes with the Apply Changes
button. Thus, the Apply Changes button **will work** without requiring the
Approve button to be clicked first.

### Hoạt động tự động

When an  is moved to a verification stage, a planned activity is automatically created for
assigned approvers to review the . Approvers receive a notification in their activities inbox,
accessible through the 🕘 (clock) icon at the top of the page.

In the to-do task list, the Engineering Change Order (ECO) notification displays the
number of activities marked Late, Today, and Future. Clicking on
each of these buttons shows a filtered Gantt view of the respective .

By clicking a pending , a *planned activity* for ECO Approval is recorded in the
chatter. Click on the i (Info) icon to view additional information, including the
approval's Created date, the approver Assigned to it, and the due date.

![Show additional details of the planned ECO approval.](applications/inventory_and_mrp/plm/management/approvals/planned-activity.png)

#### Hoạt động follow-up

When  are rejected, tasks need to be assigned to project members for required modifications
before  approval. To create tasks with deadlines, navigate to the rejected  form, and go
to the chatter.

Select the Mark Done button in the Planned Activities section of the chatter
to close the activity, and open a pop-up window for creating tasks.

![Show *Mark Done* window to show *Done & Schedule Next*, *Done*, and *Discard* buttons to
close the planned activity.](applications/inventory_and_mrp/plm/management/approvals/mark-as-done.png)

In the Mark Done window, click Done & Schedule Next to open a new
Schedule an Activity window. Next, set the Assigned to team member and the
Due Date for completing the changes. Provide task details in the Summary
field and the text box. Click the Schedule button to close the window.

After closing the window, on the  form, move the  back one stage. Doing so ensures that
when the team member completes the changes, and returns the  to the verification stage, a new
ECO Approval task is created for the approver.
