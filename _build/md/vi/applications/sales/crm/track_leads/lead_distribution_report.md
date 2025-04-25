# Lead distribution report

A *lead distribution report* can be used to see if active leads are being assigned equitably
across sales members. It can also be used to view the distribution of good or [quality leads](quality_leads_report.md), and see how frequently each salesperson is receiving (and keeping) leads.

Lead distribution reports can be run each week to help keep salespeople on track, while
providing them with ample good leads. These reports can also be used to see whether sales members
are staying productive, if good leads are being lost too often by one salesperson, and what
percentage of good leads are being retained overall.

## Create lead distribution reports

To create a lead distribution report, first navigate to CRM app ‣ Reporting ‣
Pipeline, which reveals the Pipeline Analysis dashboard.

Remove all the default filters in the search bar at the top of the page. Doing so
displays data related to *all* leads.

[Custom filters](../../../essentials/search.md#search-custom-filters) can now be added by clicking the <i class="fa fa-caret-down"></i>
(down caret) icon, to the right of the search bar, to reveal a drop-down menu of search
and filter options.

Three columns are displayed: [Filters](../../../essentials/search.md#search-filters), [Group By](../../../essentials/search.md#search-group), and
[Favorites](../../../essentials/search.md#search-favorites). To begin, navigate to the bottom of the Filters
column, and click Add Custom Filter. This opens an Add Custom Filter pop-up
window, where the essential filters can be added one at a time.

<a id="crm-track-leads-essential-filters"></a>

### Essential filters

The following filter conditions are used to create a basic lead distribution report. Together they
gather all leads created within a certain timespan that have an associated contact method and have
been assigned to a sales team.

#### Lead creation date

Click the first field, under Match any of the following rules:, that has the value
Country in it. In the popover that appears, type `Created on` in the search bar, or
scroll to search through the list to locate and select it.

Then, in the second field of that row, select >= from the drop-down menu. This operator
**only** includes values greater than (or equal to) the value in the third, rightmost field.

The third field on the Add Custom Filter pop-up window should contain the earliest date
leads are selected from.

For example, setting `01/01/2024 00:00:00` only includes leads created from, and including, the
first day of 2024.

![Add a Created On rule for the start of the year onward.](../../../../.gitbook/assets/created-on2.png)

<a id="crm-track-leads-sales-team"></a>

#### Sales team

Click New rule to add another row to the form, and choose Sales Team for
this rule's parameter. Then, click the second field of the new rule, and select contains
from the drop-down menu. Selecting this operator filters for any records that contain the words in
the third, rightmost field.

In this third field, enter the name of the desired sales team(s) that are to be included in the
report. It is important for all contains argument values to be specific enough and
spelled correctly as they exist in Odoo, otherwise this risks returning multiple (or zero) values.

![Use Sales Team to filter the location the lead is associated with.](../../../../.gitbook/assets/sales-team-location.png)

#### IMPORTANT
By adding more than one rule to the form, a new option emerges at the top of the pop-up window
above all the filters, to specify whether any <i class="fa fa-caret-down"></i> or
all <i class="fa fa-caret-down"></i> of the conditions should match. This distinction is
important to set correctly, as it impacts the driving logic of how the filters return data.

Click the default any <i class="fa fa-caret-down"></i> menu item and be sure the all
<i class="fa fa-caret-down"></i> option is chosen instead. This setting will **only** show records that match
*all* the rules contained inside the form.

<a id="crm-track-leads-phone-number"></a>

#### Contact method

#### NOTE
The instruction below is not necessary, however, it's highly recommended to add a set contact
value to the report's search criteria. A lot of spam, duplicate, or low quality leads can easily
be screened out of the report simply by adding either a set Phone or
Email rule.

Add another New rule to the form and set the first field to the first field to
Phone. Then, select is set from the drop-down menu in the second field.
Selecting this operator **only** filters for records that have a phone number associated with the
lead.

Alternatively (or in addition to the above rule), click New rule and set the first field
to Email. Then, select is set from the drop-down menu in the second field.

These rules add only leads with an associated contact method to the report.

<a id="crm-track-leads-active-status"></a>

#### Active status

Click the <i class="fa fa-sitemap"></i> (Add branch) icon to the right of the `Phone is set` line,
to add a new rule that branches from the rules above.

Two horizontal sets of fields appear below a line showing any <i class="fa fa-caret-down"></i>
of: option. This setting filters for records that match **any** of the rules contained
inside. This uses the same logic as an OR (`|`) logical operator.

Set the first field to Active. Then, select is set in the next field.

Next, click the <i class="fa fa-plus"></i> (Add New Rule) button next to Active is set
to create a new line of fields beneath it.

Set the first field to Active. Then, select is not set in the next field.

![Use Active to include active status in the report.](../../../../.gitbook/assets/active-set.png)

This rule adds the activity status of the lead to the report.

#### NOTE
Active status is an important filter to include when creating a lead distribution report because
it includes **all** leads regardless of won/lost or active/inactive status in the report. This
provides a comprehensive view of all the leads assigned to each sales member.

#### Nhóm theo

Once all filters are set, click the Add button to add these filters to the search bar.
To have the report grouped appropriately, click the <i class="fa fa-caret-down"></i> (down caret)
icon, to the right of the search bar, and click Salesperson in the Group
By section. All results are now grouped by the salesperson assigned to each lead.

Once the rules for the filter are set, click the purple Confirm button at the bottom of
the pop-up menu to save the custom filter and close the pop-up menu.

The Pipeline Analysis dashboard is now displayed again with each filter rule in the
search bar.

Click the <i class="fa fa-area-chart"></i> (Graph) icon, to the right of the search bar, to view
the report as a bar chart. Alternatively, click the <i class="oi oi-view-list"></i> (List) icon to
view leads in a grouped list.

### Filter for quality leads

The following additional conditions are provided as an example of a *good*, but *not comprehensive*,
set of rules for finding quality leads. These filters should be applied on top of the
[Essential filters](#crm-track-leads-essential-filters) in the order specified to achieve a heavily-detailed
filter.

- **Referred-by:** Filter for referrals, such as by appointment or sales member.
- **Source:** Filter for specific source UTMs, such as Facebook or LinkedIn.
- **Notes:** Filter for internal notes.
- **Tags:** Filter for categorical tags.
- **Email:** Filter for specific email domains, such as gmail.com or yahoo.com.
- **Salesperson:** Filter for leads associated with certain sales members.

These conditions can be added, removed, or modified to best fit the desired information in the
report.

#### SEE ALSO
- [Add rules for quality leads](quality_leads_report.md#quality-leads-report-add-quality-rules)
- [Tìm kiếm, lọc, và nhóm bản ghi](../../../essentials/search.md)
