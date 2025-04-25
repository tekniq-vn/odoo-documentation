# Revenues report

The Odoo **Events** application creates custom reports, based on event-related data and analytics.
These reports can either be focused on *Attendees* or *Revenues*.

The following documentation focuses on the reporting options related to event *Revenues*.

## Revenues reporting page

To access the *Attendees* reporting page, navigate to Events app ‣ Reporting ‣
Revenues.

![The default view of the Revenues reporting page in the Odoo Events application.](../../../_images/default-view.png)

By default, the Revenues reporting page appears as a graph (a <i class="fa fa-line-chart"></i>
(Line Chart) with <i class="fa fa-database"></i> (Stacked) data). The default filters,
Non-free tickets and Event Start Date: (current year), are present in the
search bar.

The Revenues reporting page can also be viewed as a [pivot table](../../essentials/reporting.md#reporting-views-pivot), by clicking the <i class="oi oi-view-pivot"></i> (Pivot) icon in the
upper-right corner.

### Đơn vị tính

Choosing specific [Measures](../../essentials/reporting.md#reporting-choosing-measures) is a quick way to customize
reporting pages.

Regardless of the chosen view, the measures on the Revenues reporting page are as
follows: Revenues, Untaxed Revenues, and Count.

#### NOTE
In the default graph view of the Revenues reporting page, only the
Revenues option is set in the Measures drop-down menu.

In graph view, only one of the Measures can be selected at a time.

When the pivot option is selected, all Measures options are selected, by default.

- Revenues: shows the revenues generated from events.
- Untaxed Revenues: shows the untaxed revenues generated from events.
- Count: shows the total amount of registrants who attended events.

### Filters and grouping options

To reveal a drop-down menu of filter and grouping options to create custom reports, click the
<i class="fa fa-caret-down"></i> (down arrow) to the right of the search bar.

Doing so opens a drop-down mega menu of options organized into columns: [Filters](../../essentials/search.md#search-preconfigured-filters), [Group By](../../essentials/search.md#search-group), and [Favorites](../../essentials/search.md#search-favorites).

#### NOTE
If a time-related option has been selected from the Filters column (e.g. the default
Event Start Date: (year) filter), a Comparison column appears, with
comparison options for the corresponding time-related filter option selected.

Only **one** selection can be made from the Comparison column at a time.

#### SEE ALSO
[Tìm kiếm, lọc, và nhóm bản ghi](../../essentials/search.md)

#### Filter options

In the Filters column of the drop-down mega menu, there are various event-related
options that can be utilized to create custom reports, based on a number of specific criteria.

Multiple options in the Filters column can be selected at once.

The Filters column has the following options:

- Non-free tickets: event tickets/registrations that were **not** free.
- Free: event tickets/registrations that *were* free.
- Pending payment: event tickets/registrations that were purchased, but still have
  payment pending.
- Sold: event tickets/registrations that have been successfully sold (and paid for).
- Registration Date: Click the <i class="fa fa-caret-down"></i> (down arrow) icon to
  reveal a list of month, quarter, and year options. Select any number of these options to view a
  specific periods of time and see how many registrations happened during that time.
- Upcoming/Running: include revenue-related information for events that are either
  currently running or are going to happen in the future.
- Past Events: include revenue-related information for events that have already taken
  place.
- Event Start Date: Click the <i class="fa fa-caret-down"></i> (down arrow) icon to
  reveal a list of month, quarter, and year options. Select any number of these options to designate
  event start dates to use as filters for revenue-related event data.
- Event End Date: Click the <i class="fa fa-caret-down"></i> (down arrow) icon to
  reveal a list of month, quarter, and year options. Select any number of these options to designate
  event end dates to use as filters for revenue-related event data.
- Published Events: Select this option to show revenue-related data for published
  events.
- Add Custom Filter: Create a custom filter to analyze event-related revenue data. To
  learn more, refer to the documentation on [custom filters](../../essentials/search.md#search-custom-filters).

#### Group By options

In the Group By column of the drop-down mega menu, there are various event-related
options to create custom groupings of data.

Multiple Group By options can be selected at once.

The Group By column has the following options:

- Event Type: Group data based on the type of event.
- Event: Organize data into individual groups, separated by events.
- Product: Group data based on the event registration product.
- Ticket: Group data based on the type of event ticket purchased by attendees.
- Registration Status: Group data based on the status of registrations.
- Sale Order Status: Group data based on the status of event-related sales orders.
- Customer: Group data based on customer records.
- Add Custom Group: Click the <i class="fa fa-caret-down"></i> (down arrow) icon to
  reveal a drop-down of grouping options. To select one, click on the desired option, and Odoo adds
  it to the Group By column. Multiple selections can be made.

## Sample report: event ticket analysis (graph)

The following is an example of how various filters and grouping options can create a useful analytic
graph report related to event revenues. In this case, the configurations present data about sold or
free tickets to published events, with the metrics separated by ticket type and event.

![The event ticket analysis sample report with unique filters and groupings in place.](../../../_images/event-ticket-analysis.png)

To create such a report, navigate to Events app ‣ Reporting ‣ Revenues. Stay in
the default graph view, but remove the default filters from the search bar.

Then, click the <i class="fa fa-caret-down"></i> (down arrow) to the right of the search bar, to
reveal the drop-down mega menu of filter and grouping options.

From here, select Free and Sold from the Filters column.

Then, since it is desired to **only** view data related to already published events, select the
Published Events option in the Filters column, as well.

Next, in the Group By column, select the Event and Ticket
options, **in that sequential order**. Doing so first groups the data by event, *then* by ticket
type, which provides a more useful array of data to analyze.

#### IMPORTANT
The order in which the options are selected in the Group By column directly affects
how the data is presented on the report.

From there, additional configurations can be added for more detailed data, if desired.

If no additional filters or groupings are added, Odoo presents a graphical representation of data
related to all *free* or *sold* tickets for *published events*, grouped by *event*, and organized by
*ticket* type.

## Sample report: event type analysis (pivot table)

The following is an example of how various filters and grouping options can create a useful analytic
pivot table report related to event revenues. In this case, the configurations present data about
how much revenue different event types have generated, in order to gauge which events are the most
profitable.

![The event type analysis sample report with unique filters and groupings in place.](../../../_images/event-type-analysis.png)

First, navigate to Events app ‣ Reporting ‣ Revenues, and switch to the pivot
table view, by clicking the <i class="oi oi-view-pivot"></i> (Pivot) icon in the upper-right
corner.

Keep the default filters (Non-free tickets and Event Start Date: (year)) in
the search bar.

Next, open the Measures drop-down menu, and deselect the option for Count,
because this report is only going to focus on revenues.

Then, click <i class="fa fa-plus-square"></i> Total above the column titles, and select
Event Type from the resulting drop-down menu.

With these configurations in place, all the revenues generated from the events (and their
corresponding registrations) are displayed, organized by the event type (presented as expandable
columns).
