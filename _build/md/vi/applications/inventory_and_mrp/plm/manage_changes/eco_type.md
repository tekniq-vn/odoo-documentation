# Loại ECO

An *ECO type* is assigned to *engineering change orders* (ECOs) to organize and track changes to
products and bills of materials (BoMs). Each  type separates  into a project in Gantt
view, ensuring collaborators and stakeholders **only** view and assist with relevant 
improvements.

For example, an electronic chip manufacturer might use 'New Product Introduction', 'Product
Improvement', 'Component Change', and 'Firmware Update'  types. Then, designers and engineers
can focus on  in the 'New Product Introduction' and 'Product Improvement' projects, avoiding
unrelated supplier change or firmware update .

## Create ECO type

To access and manage ECO types, navigate to PLM app ‣ Configuration ‣ ECO
Types.

Create a new ECO type by clicking New. On the new ECO Types form, fill in
the following information:

- Name: the name of the  type, which will organize all of the  of this *type*
  in a project.
- Email Alias: if this optional field is filled, emails submitted to this email address
  automatically generate  in the left-most stage of this  type.

## Edit ECO type

Modify existing  type names and email aliases by navigating to the PLM app ‣
Configuration ‣ ECO Types page. There, click on the desired  type from the list.

On the form for each  type, proceed to edit the Name and Email Alias
fields.

<a id="plm-eco-stage-config"></a>

## Giai đoạn

Within an  type project, *stages* are like milestones and are used to identify the progress of
the  before the changes are ready to be applied. (e.g. 'Feedback', 'In Progress', 'Approved',
'Complete')

Additionally, required approvers can be added to each stage, ensuring that changes to the production
 cannot proceed until the approver reviews and approves the . Doing so prevents errors on
the production  by enforcing at least one review of suggested changes before they're applied on
a production .

For best practice, there should be at least one *verification* stage, which is a stage with a
required approver, and one *closing* stage, which stores  that have been either canceled or
approved for use as the next production .

### Create stage

To add a stage, go to the PLM app and select the intended project for an  type
from the PLM Overview dashboard.

Then, on the Engineering Change Orders project pipeline for the  type, click the
+ Stage button. Doing so reveals a text box to fill in the name of the stage. After
filling it in, click the Add button to finish adding the stage.

### Verification stage

Click an ECO type from PLM app ‣ Overview to open a kanban view of  of this
type.

To configure a verification stage, hover over the intended stage, and select the ⚙️
(gear) icon. Then, click Edit to open a pop-up window.

Configure the verification stage in the edit stage pop-up window, by checking the box for
Allow to apply changes.

Then, add an approver in the Approvers section, by clicking Add a line, and
specifying the Role of the reviewer, their User, and Approval
Type.

Make sure at least one approver is configured with the Approval Type: Is
required to approve.

The approver listed is automatically notified when  are dropped in the stage specified in the
pop-up window. Once finished, click Save & Close.

### Closing stage

Configure a closing stage by opening the Edit: [stage] pop-up window. To do so, hover
over the intended stage and click the ⚙️ (gear) icon that appears in the top-right
corner. Then, click Edit from the drop-down menu.

On the Edit: [stage] pop-up window, select the check boxes for Folded in
kanban view, Allow to apply changes and Final Stage.

![Show configurations of the closing stage.](../../../../_images/closing-stage.png)
