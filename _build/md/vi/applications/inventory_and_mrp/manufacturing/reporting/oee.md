# Overall equipment effectiveness

In Odoo's *Manufacturing* app, *overall equipment effectiveness* (OEE) represents the amount of time
a work center is fully productive.  is displayed as a percentage of the total time a work
center is active.

Fully productive time is considered to be time when the work center is operational **and**
processing work orders that have not exceeded their *expected duration*.

 helps manufacturing teams understand the efficiency of work centers, and the causes of
manufacturing downtime.

#### IMPORTANT
Since  tracks work center productivity, using it requires enabling the work centers feature
in the settings of the Manufacturing app.

To do so, navigate to Manufacturing app ‣ Configuration ‣ Settings, and tick
the checkbox next to Work Orders, under the Operations heading. Then,
click Save.

## Efficiency standards

For  to accurately reflect the percentage of fully productive time for a work center, the work
center **must** be properly configured with the correct productivity metrics. These include the work
center's *time efficiency*, *capacity*, and *OEE target*.

### Time efficiency

Hiệu suất thời gian thể hiện hiệu suất của khu vực sản xuất khi xử lý công đoạn và được biểu thị bằng tỷ lệ phần trăm. Giá trị hiệu suất thời gian 100% có nghĩa là khu vực sản xuất xử lý công đoạn với tốc độ đúng bằng thời gian dự kiến được liệt kê trong  của sản phẩm. Giá trị nhỏ hơn hoặc lớn hơn 100% lần lượt cho thấy khu vực sản xuất xử lý công đoạn chậm hơn hoặc nhanh hơn so với thời gian dự kiến của công đoạn.

To set the time efficiency for a work center, navigate to Manufacturing app ‣
Configuration ‣ Work Centers, and select a work center. On the General Information
tab, enter a numerical value in the Time Efficiency field.

### Sức chứa

Capacity represents how many units of a product can be produced in parallel at a work center. The
duration of work orders for multiple units increases or decreases, based on how many units the work
center can handle.

To set the capacity for a work center, navigate to Manufacturing app ‣
Configuration ‣ Work Centers, and select a work center. On the General Information
tab, enter a numerical value in the Capacity field.

### target

The  target is the goal for how much of a work center's operating time should be fully
productive time. It is displayed as a percentage, and should only be set as high as `100%`.

To set the  target for a work center, navigate to Manufacturing app ‣
Configuration ‣ Settings ‣ Work Centers, and select a work center. On the General
Information tab, enter a numerical value of `100.00` or less in the OEE Target field.

## Calculating

 được biểu thị bằng giá trị phần trăm từ 0 đến 100. Giá trị này thể hiện khoảng thời gian khu vực sản xuất hoạt động với năng suất tối đa. Phần còn lại biểu thị khoảng thời gian khu vực sản xuất hoạt động với hiệu suất thấp hơn mức tối đa. Tình trạng này có thể xảy ra do nhiều nguyên nhân bao gồm *giảm tốc độ*, *tình trạng còn hàng của nguyên vật liệu* và *hỏng hóc thiết bị*.

### Fully productive time

For a work center to be considered fully productive, it must be able to receive work orders, have
the components necessary to process work orders, and be operating within the expected duration of
the work order it is processing.

### Reduced speed

When a work center is operating at reduced speed, it means that it is processing a work order that
has exceeded its expected duration. While the work center may be operational, this is not considered
fully productive time.

### Material availability

Material availability refers to situations where a work center is able to accept a work order, but
the required components are not available. This can occur because the components are not in stock,
or are reserved for a different order.

### Equipment failure

Equipment failure signifies any period of time when a work center is unusable due to maintenance
issues with its equipment. This can be due to equipment breaking down, or when a work center is shut
down for scheduled maintenance. In these cases, a work center can be blocked using a
[maintenance request](../../maintenance/maintenance_requests.md).

## reporting

To view  reporting metrics for every work center, navigate to Manufacturing app
‣ Reporting ‣ Overall Equipment Effectiveness. This page shows the metrics for each work center
with  data.

Alternatively, to see  reporting metrics for a single work center, navigate to
Manufacturing app ‣ Configuration ‣ Work Centers, and select a work center. At
the top of the work center's form, click the <i class="fa fa-pie-chart"></i> OEE smart button.

By default, the main  reporting page shows data in a bar chart, while the page for a specific
work center shows it in a pie chart. To select a different chart type on either page, click the
<i class="fa fa-bar-chart"></i> (bar chart), <i class="fa fa-line-chart"></i> (line chart), or
<i class="fa fa-pie-chart"></i> (pie chart) button above the displayed chart.

It is also possible to see  data in a pivot view, or a list displaying each time entry, by
clicking the <i class="oi oi-view-pivot"></i> (pivot view) or <i class="oi oi-view-list"></i> (list
view) buttons at the top-right corner of the page.

![The dashboard of the OEE report.](../../../../_images/oee-report.png)
