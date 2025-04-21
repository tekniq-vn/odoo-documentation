# Báo cáo đăng ký

The Odoo **Subscriptions** app provides a series of reporting pages to help companies analyze how
subscriptions are performing.

On the *Subscriptions Analysis* reporting page, users can view specific data related to recurring
subscriptions, quantity of subscriptions, in-progress or paused subscriptions, and more.

The *Retention Analysis* reporting page provides an organized table of subscription retention
percentages over any period of time.

The *MRR Breakdown* reporting page clearly divides  and  metrics for subscriptions into
various graphs, lists, and charts.

And the *MRR Analysis* reporting page offers a time-based collection of analytics showcasing how
subscription  and  have changed over the course of any given period of time.

## Reporting page elements

All subscriptions-based reporting pages can be accessed via the Reporting header menu in
the **Subscriptions** app.

The following sections describe elements found on each reporting page.

### Filters and Group By

*Filters* are used to narrow down metrics to show specific analytics, whereas groupings (via the
*Group By* option) are used to gather the data from specific sections into groups for more
organized analysis.

This section refers to both filters and groupings, as a combination of the two can be saved in the
*Favorites* section.

To modify the results being shown on any reporting page, click the <i class="fa fa-caret-down"></i>
(down arrow) icon to the right of the search bar. Doing so reveals a drop-down menu of
detailed filter and grouping options.

If desired, a filter or grouping (or combination of filters and/or groupings) can be saved in the
Favorites section of that drop-down menu. To do so, click the <i class="fa fa-caret-down"></i>
(down arrow) icon beside Save current search, located beneath the
Favorites section.

This reveals a field to assign a title to the favorite filter. Two options are also found beneath
the title field: Default filter and Shared.

Ticking the checkbox beside Default filter makes the newly-favorited filter the default
option for that reporting page.

Ticking the checkbox beside Shared makes the newly-favorited filter available to other
users in the database.

#### NOTE
The Default filter and Shared options are **not** required, and only
*one* of these options can be selected at a time.

To save the filter, click Save in the Favorites section of the drop-down
filter menu.

When clicked, that saved filter appears beneath the Favorites column of the drop-down
filter menu, and a <i class="fa fa-star"></i> (gold star) icon appears beside the favorite filter's
name in the search bar.

### Lượt xem

On the Subscription Analysis, MRR Breakdown, and MRR Analysis
reporting pages, three different view options are located in the upper-right corner.

#### NOTE
There are *no* other view options available on the Retention Analysis reporting page.

The available view options, from left to right, are:

- Biểu đồ
- Danh sách
- Pivot

![The different view options available on the Subscriptions Analysis page.](applications/sales/subscriptions/reports/subscriptions-analysis-page-view-options.png)

Each view has its own series of related view-specific visual options.

#### Chế độ xem biểu đồ

With the graph view selected, the following options appear between the search bar and visual
representation of the data. These graph-specific options are located to the right of the
Measures and Insert in Spreadsheet buttons.

![The different graph view options in the Odoo Subscriptions app.](applications/sales/subscriptions/reports/subscriptions-graph-specific-options.png)

The first three options, from left to right, represent different graph-related views. The remaining
options represent different ways to organize and visualize that specific graph-related data.

From left to right, the specific graph-related view options are:

- <i class="fa fa-bar-chart"></i> Bar Chart: showcases the data in a bar chart format.
- <i class="fa fa-line-chart"></i> Line Chart: showcases the data in a line chart format.
- <i class="fa fa-pie-chart"></i> Pie Chart: showcases the data in a pie chart format.

Each graph view option has its own series of specific visual options, which are represented by the
available buttons that appear to the right of the selected graph-related view option.

When the <i class="fa fa-bar-chart"></i> Bar Chart graph view is selected, the following visual
options are available:

- <i class="fa fa-database"></i> Stacked: showcases the data in a stacked visual format.
- <i class="fa fa-sort-amount-desc"></i> Descending: showcases the data in descending order.
- <i class="fa fa-sort-amount-asc"></i> Ascending: showcases the data in ascending order.

When the Line Chart graph view is selected, the following visual options are available:

- <i class="fa fa-database"></i> Stacked: showcases the data in a stacked visual format.
- <i class="fa fa-signal"></i> Cumulative: showcases the data in accumulated, increasing format.
- <i class="fa fa-sort-amount-desc"></i> Descending: showcases the data in descending order.
- <i class="fa fa-sort-amount-asc"></i> Ascending: showcases the data in ascending order.

When the Pie Chart graph view is selected, there are no additional visual options.

#### Xem danh sách

With the list view selected, the subscription metrics being analyzed are displayed in a simple list,
which can be fully customized by using any of the available filters or groupings in the drop-down
filter menu (accessible via the <i class="fa fa-caret-down"></i> (down arrow) icon to the right of
the search bar).

#### NOTE
With list view selected, the Measures drop-down menu and Insert in
Spreadsheet button are *not* available.

#### Chế độ xem pivot

With the pivot view selected, the subscription metrics are displayed in a data table, which can be
fully customized.

The pivot data table can be customized using the options available in the Measures
drop-down menu, and/or the filter grouping options available in the filter drop-down menu
(accessible via the <i class="fa fa-caret-down"></i> (down arrow) icon to the right of the search
bar).

Three pivot-specific options are available, located to the right of the Measures
drop-down menu and Insert in Spreadsheet button.

![The pivot-specific view options available in the Odoo Subscriptions app.](applications/sales/subscriptions/reports/subscriptions-pivot-view-options.png)

From left to right, those pivot-specific view options are:

- <i class="fa fa-exchange"></i> Flip axis: the `x` and `y` axis of the pivot data table flip.
- <i class="fa fa-arrows"></i> Expand all: all the available rows and columns of the pivot data
  table expand fully.
- <i class="fa fa-download"></i> Download .xlsx: the pivot data table is downloaded as an
  `.xlsx` file.

### Đơn vị tính

The graph and pivot reporting pages have their own metric-specific Measures drop-down
menu of data-related options to choose from, located in the upper-left corner, above the visual
representation of metrics.

![The standard measures drop-down menu in the Odoo Subscriptions app.](applications/sales/subscriptions/reports/subscriptions-measures-drop-down.png)

When the Measures button is clicked, a series of selectable measures becomes available,
via a drop-down menu. When any of the options are selected from the Measures drop-down
menu, the chosen metrics related to that specific measure appear on the reporting page.

#### NOTE
For more information on the different measures that can be utilized on each reporting page, refer
to the [specific reporting page breakdowns](#subscriptions-reports-reporting) found below in
this documentation.

### Chèn vào bảng tính

Beside the Measures drop-down menu, there is an Insert in Spreadsheet
button.

When clicked, the ability to add the configured data currently being showcased on the reporting page
into a new or pre-existing spreadsheet or dashboard becomes available, via a pop-up window.

![The spreadsheet pop-up window of the Subscriptions Analysis page.](applications/sales/subscriptions/reports/subscriptions-analysis-spreadsheet-popup.png)

Select the desired option from this pop-up window, then click Confirm.

<a id="subscriptions-reports-reporting"></a>

## Reporting pages

In the Odoo **Subscriptions** app, there are four different reporting pages available.

To access, analyze, and customize various reports related to subscriptions, navigate to
Subscriptions app, and click the Reporting drop-down menu in the
header to reveal the following reporting pages:

- Đăng ký
- Retention
- MRR Breakdown
- MRR Timeline

Clicking any of those options reveals a separate, fully-customizable reporting page focusing on that
particular aspect of subscription data.

The following is a breakdown of those four specific reporting pages.

### Phân tích đăng ký

To access the Subscriptions Analysis reporting page, navigate to
Subscriptions app ‣ Reporting ‣ Subscriptions.

By default, the Bar Chart option, in the Graph view, is selected on the
Subscriptions Analysis reporting page.

The following filters are also present in the search bar: In Progress or Paused and
Recurring.

![The default view of the Subscriptions Analysis reporting page in Odoo Subscriptions.](applications/sales/subscriptions/reports/subscriptions-analysis-page-default.png)

When the Measures button on the Subscriptions Analysis page is
clicked, a series of metric-related options becomes available as a drop-down menu.

![The measures drop-down menu of the Subscriptions Analysis page.](applications/sales/subscriptions/reports/subscriptions-analysis-measures.png)

The metric-related options in the Measures drop-down menu on the
Subscriptions Analysis page are:

- Monthly Recurring
- Số lượng
- Recurring Revenue
- Untaxed Total
- Yearly Recurring
- Số

#### NOTE
The Monthly Recurring measure option is selected by default.

When any of those available measures are clicked, Odoo displays that selected data on the reporting
page for further analysis.

### Retention analysis

To access the Retention Analysis reporting page, navigate to
Subscriptions app ‣ Reporting ‣ Retention.

The Retention Analysis reporting page differs from the other **Subscriptions** app
reporting pages, in that it does **not** provide any additional view options. The data on this page
is only presented in a customizable data chart.

![The default view of the Retention Analysis reporting page in Odoo Subscriptions.](applications/sales/subscriptions/reports/subscriptions-retention-analysis-page-default.png)

When the Measures drop-down menu on the Retention Analysis reporting page is
clicked, a series of metric-related options become available.

![The measures drop-down menu of the Retention Analysis page.](applications/sales/subscriptions/reports/subscriptions-retention-analysis-measures.png)

The metric-related options in the Measures drop-down menu on the Retention
Analysis reporting page are:

- Amount to invoice
- Margin
- Biên lợi nhuận (%)
- Prepayment percentage
- Shipping Weight
- Số tiền chưa thanh toán
- Số

#### NOTE
The Count measure option is selected by default.

To the right of the Measures drop-down menu on the Retention Analysis page
is an additional drop-down menu containing different time periods. The default time period is
Month.

When clicked, a drop-down menu of various time period options become available.

![The time period drop-down menu of the Retention Analysis page.](applications/sales/subscriptions/reports/subscriptions-retention-analysis-time-periods.png)

The time period options are:

- Ngày
- Tuần
- Tháng
- Năm

When a time period option from this drop-down menu is selected, the Retention Analysis
reporting page showcases data for the configured measures and filters within that time period.

To the right of the time period drop-down menu, there is a download button, which allows the user to
download the data presented on the Retention Analysis page as an Excel file.

### MRR breakdown

To access the MRR Breakdown reporting page, navigate to Subscriptions
app ‣ Reporting ‣ MRR Breakdown.

By default, the data displayed on the MRR Breakdown reporting page is in graph view,
with the Bar Chart option and Stacked option selected.

A default filter is also available in the search bar for Event Date: Month > Event Type.

![The default appearance of the MRR Breakdown reporting page in Odoo Subscriptions.](applications/sales/subscriptions/reports/subscriptions-mrr-breakdown-default.png)

When the Measures drop-down menu on the MRR Breakdown reporting page is
clicked, a series of metric-related options become available.

![The default appearance of the MRR Breakdown reporting page in Odoo Subscriptions.](applications/sales/subscriptions/reports/subscriptions-mrr-breakdown-measures.png)

The metric-related options in the Measures drop-down menu on the MRR
Breakdown reporting page are:

- Active Subscriptions Change
- ARR Change
- MRR Change
- Số

#### NOTE
The MRR Change measure option is selected by default.

### Phân tích MRR

To access the MRR Analysis reporting page, navigate to Subscriptions
app ‣ Reporting ‣ MRR Timeline.

By default, the data displayed on the MRR Analysis reporting page is in graph view, with
the Line Chart option, Stacked option, and Cumulative option
selected.

A default filter is also found in the search bar for Event Date: Month.

![The default appearance of the MRR Analysis reporting page in Odoo Subscriptions.](applications/sales/subscriptions/reports/subscriptions-mrr-analysis-default.png)

When the Measures drop-down menu on the MRR Analysis reporting page is
clicked, a series of metric-related options become available.

![The default appearance of the MRR Analysis reporting page in Odoo Subscriptions.](applications/sales/subscriptions/reports/subscriptions-mrr-analysis-measures.png)

The metric-related options in the Measures drop-down menu on the MRR
Analysis reporting page are:

- Active Subscriptions Change
- ARR Change
- MRR Change
- Số

#### NOTE
The MRR Change measure option is selected by default.

#### SEE ALSO
- [Đăng ký](../subscriptions.md)
- [Gói cước đăng ký](plans.md)
