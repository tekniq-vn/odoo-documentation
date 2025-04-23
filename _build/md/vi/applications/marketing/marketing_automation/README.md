# Tự động hóa marketing

Use the Odoo **Marketing Automation** application to create dynamic campaigns with actions that\
automatically occur within a defined duration, such as sending a series of timed mass emails or\
engaging with leads based on their interactions with marketing campaigns.

While the application is designed to be user-friendly for creating, launching, and reviewing\
marketing campaigns, it also provides advanced features to automate repetitive tasks throughout the\
database.

Get started by creating a [new campaign from scratch](./#marketing-automation-campaigns) or start\
with a [campaign template](./#marketing-automation-campaign-templates).

#### SEE ALSO

[Odoo Tutorials: Marketing](https://www.odoo.com/slides/marketing-27)

## Cấu hình

To begin, make sure the **Marketing Automation** application is [installed](applications/general/apps_modules.md#general-install).

#### IMPORTANT

Installing the **Marketing Automation** application also installs the [Email Marketing](applications/marketing/email_marketing.md) app, as most features of Odoo **Marketing Automation** are dependent on that\
specific application.

Additionally, install the [CRM](applications/sales/crm.md) and [SMS Marketing](applications/marketing/sms_marketing.md)\
applications to access _all_ of the features available in **Marketing Automation**.

The following documentation assumes that all three of these dependent applications are installed\
on the database.

## Chiến dịch

A _campaign_ refers to a workflow of activities that are automatically executed to a target\
audience, based on predefined filters, triggers, and durations of activities.

A new campaign can be created from scratch or from a [template](./#marketing-automation-campaign-templates).

To create a campaign, navigate to the Marketing Automation application and click\
the New button to reveal a new campaign form.

### Campaign templates

Odoo provides six campaign templates to help users get started. The campaign template cards **only**\
display when there are no existing campaigns in the database. Once a campaign has been created, the\
template cards on the _Campaigns_ dashboard are replaced with a Kanban view of the existing\
campaigns.

To get started with a template, navigate to the Marketing Automation application,\
from the main Odoo dashboard, to open the Campaigns dashboard, which displays six[campaign template](applications/marketing/marketing_automation/campaign_templates.md) cards:

* Tag Hot Contacts\
  Send a welcome email to contacts and tag them if they click it.\

* Welcome Flow\
  Send a welcome email to new subscribers, remove the address that bounced.\

* [Double Opt-in](applications/marketing/marketing_automation/campaign_templates/double_optin.md)\
  Send an email to new recipients to confirm their consent.\

* Commercial prospection\
  Send a free catalog and follow-up according to reactions.\

* Schedule Calls\
  If a lead is created for existing contact, schedule a call with their salesperson.\

* Prioritize Hot leads\
  Send an email to new leads and assign them a high priority if they open it.\


![Six campaign template cards on the Campaigns dashboard of the Marketing Automation app.](../../.gitbook/assets/campaigns-dashboard.png)

These templates are designed to be used as starting points for creating new campaigns. Click one of\
the template cards to open the campaign form.

## Targets and filters

On the campaign form, the Target and Filter section, also referred to as the\
domain, contains the fields used to define the target audience for the campaign's reach (i.e.,\
the unique contact records in the database).

The target audience specifies the type of records available for use in the campaign, such a&#x73;_&#x4C;ead/Opportunity_, _Event Registration_, _Contact_, and more.

### Bản ghi

The contacts in the system that fit the specified criteria for a campaign are referred to a&#x73;_&#x72;ecords_.

The number of records that are displayed next to the campaign Filter represent the total\
number of records the campaign is targeting.

### Người tham gia

The records that are engaged by the campaign are referred to as _participants_.

The number of participants engaged in a test run are shown in the _Tests_ smart button, which\
displays on the top of the campaign form after a test has been run.

The number of participants engaged in a running, or stopped, campaign are shown in th&#x65;_&#x50;articipants_ smart button at the top of the campaign form.

#### SEE ALSO

[Audience targeting](applications/marketing/marketing_automation/target_audience.md)

## Quy trình

A _workflow_ consists of an activity, many activities, or a sequence of activities organized in a\
campaign. A campaign's workflow is defined in the Workflow section of the campaign form.

### Hoạt động

_Activities_ are the methods of communication or server actions, organized in a workflow, that are\
executed within a campaign. Once running, each activity displays the number of participants that\
are engaged by the activity as _Success_ and _Rejected_ counts.

To create one of the following activities, click Add new activity in the\
Workflow section of the campaign form:

* [Email](applications/marketing/marketing_automation/workflow_activities.md#marketing-automation-email-activity-type): an email that is sent to the target\
  audience.
* [Server action](applications/marketing/marketing_automation/workflow_activities.md#marketing-automation-sa-activity-type): an internal action within the\
  database that is executed.
* [SMS](applications/marketing/marketing_automation/workflow_activities.md#marketing-automation-sms-activity-type): a text message that is sent to the target\
  audience.

#### SEE ALSO

[Campaign workflow activities](applications/marketing/marketing_automation/workflow_activities.md)

## Testing and running

Once a campaign has been created, it can be tested to ensure the workflow is functioning as\
expected, to check for errors, and correct any mistakes before it reaches its target audience.

After testing, the campaign can be launched to start engaging the target audience. The campaign can\
also be launched _without_ testing, if the user is confident in the workflow.

#### SEE ALSO

[Testing/running campaigns](applications/marketing/marketing_automation/testing_running.md)

## Báo cáo

A range of reporting metrics are available to measure the success of each campaign. Navigate to\
Marketing Automation app ‣ Reporting to access the following menu options:

* Link Tracker: displays the metrics of links to track the number of clicks.
* Traces: displays the results of all activities from all campaigns.
* Participants: displays an overview of the participants of all campaigns.

Additionally, each activity within the workflow of a campaign displays its engagement metrics.

#### SEE ALSO

[Campaign metrics](applications/marketing/marketing_automation/understanding_metrics.md)

* [Audience targeting](applications/marketing/marketing_automation/target_audience.md)
* [Campaign workflow activities](applications/marketing/marketing_automation/workflow_activities.md)
* [Testing/running campaigns](applications/marketing/marketing_automation/testing_running.md)
* [Campaign metrics](applications/marketing/marketing_automation/understanding_metrics.md)
* [Campaign templates](applications/marketing/marketing_automation/campaign_templates.md)
  * [Double Opt-in](applications/marketing/marketing_automation/campaign_templates/double_optin.md)
