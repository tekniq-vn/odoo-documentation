# Procurement expenses report

With the *Purchase* application, users can monitor procurement expenses over time. This report helps
companies track and analyze spending, identify cost-saving opportunities, and ensure efficient
budget management.

## Create procurement expenses report

To create a procurement expenses report, first navigate to Purchase app ‣ Reporting ‣ Purchase to
open the Purchase Analysis dashboard.

By default, the dashboard displays a line chart overview of the Untaxed Total of
Purchase Orders (POs) with a Confirmation Date for the current month, or of
Requests for Quotation (RFQs) with a status of *Draft*, *Sent*, or *Cancelled*.

### Add filters and groups

On the top-right, click the <i class="oi oi-view-pivot"></i> (pivot) icon to switch to pivot view.

Remove any default filters from the Search... bar. Then, click the <i class="fa fa-caret-down"></i> (down) icon to open the
drop-down menu that contains the Filters, Group By, and
Favorites columns.

#### NOTE
Unless otherwise specified, the report displays data from both  and . This can be
changed by selecting either Requests for Quotation or Purchase Orders
under the Filters column.

Under the Filters column, select a time frame to use for comparison. The report can be
filtered by either Order Date or Confirmation Date. Choose one from the
list, and click the <i class="fa fa-caret-down"></i> (down) icon to specify the date range, either by month, quarter, or year.

Next, under the Group by column, select Vendor. Then, select
Product Category, which is also located in the Group By column.

#### NOTE
The selections under the Group By heading can be altered, depending on the needs of
the individual company. For example, selecting Product, instead of Product
Category, provides a more in depth look at the performance of specific items, in place of an
entire category.

Tiếp theo, chọn một tùy chọn dưới tiêu đề So sánh. Các tùy chọn này chỉ khả dụng sau khi chọn phạm vi ngày trong cột Bộ lọc và thay đổi tùy theo phạm vi đó. Giai đoạn trước thêm so sánh với giai đoạn trước, như tháng hoặc quý trước. Năm trước so sánh cùng khoảng thời gian với năm trước.

#### NOTE
While multiple time-based filters can be added at once, only one comparison can be selected at a
time.

![The drop-down menu of filters, group by and comparison options for the procurement expenses
report.](applications/inventory_and_mrp/purchase/advanced/procurement_expenses_report/filters-groups.png)

### Add measures

After selecting the Filters, Group by, and Comparison settings,
click out of the drop-down menu.

By default, the report displays data with the following measures: Order,
Total, Untaxed Total, and Count. Click Measures at
the top-left to open the drop-down list of available measures.

Click the following specific measures to include additional columns for the procurement expenses
report:

- Total and Untaxed Total: can include one or both measures. These are
  included for overall spending analysis.
- Average Cost: included to evaluate cost efficiency.
- Days to Confirm and Days to Receive: used to assess supplier performance.
- Qty Ordered and Qty Received: used to understand order efficiency.
- Qty Billed and Qty to be Billed: used to track order accuracy.

After selecting all necessary measures, click out of the drop-down menu.

<a id="purchase-view-results"></a>

## Xem kết quả

After all of the filters and measures have been selected, the report generates in the selected view.

![A sample version of the procurement expenses report.](applications/inventory_and_mrp/purchase/advanced/procurement_expenses_report/sample-per-report.png)

Click Insert in Spreadsheet to add the pivot view into an editable spreadsheet format
within the *Documents* app.

#### IMPORTANT
The Insert in Spreadsheet option is **only** available if the *Documents Spreadsheet*
module is installed.

#### NOTE
The procurement expenses report is also available in graph view. Click the <i class="fa fa-area-chart"></i> (area
chart) icon to change to graph view. Click the corresponding icon at the top of the report to
switch to a <i class="fa fa-bar-chart"></i> (bar chart), <i class="fa fa-line-chart"></i> (line
chart), or <i class="fa fa-pie-chart"></i> (pie chart).

#### SEE ALSO
To save this report as a *favorite*, see [Yêu thích](../../../essentials/search.md#search-favorites).
