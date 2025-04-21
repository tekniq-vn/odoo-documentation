# Performance management

Odoo integrates a variety of tools to analyze and improve the performance of your eCommerce
website.

## Data monitoring

**Website** allows monitoring and analysis of the sales performance of your eCommerce. To access the
**reporting view**, go to Website ‣ Reporting ‣ eCommerce. This dashboard helps
you monitor everything related to sales, such as sales performance per product, category, day, etc.

![Performance reporting of eCommerce](applications/websites/ecommerce/performance/reporting.png)

By clicking Measures, you can select the type of measurement used, such as:

- Margin;
- SL đã lập hóa đơn
- Untaxed Total;
- Volume;
- ...

Other options include **multiple views (Pivot, etc.), comparison** by periods or years, and directly
insert in spreadsheet, etc.

## Phân tích

It is possible to link your Odoo website with [Plausible.io](../website/reporting/analytics.md#analytics-plausible) and
[Google Analytics](../website/reporting/analytics.md#analytics-google-analytics).

<a id="ecommerce-performance-email-queue"></a>

## Email queue optimization

For websites handling flash sales (e.g., event ticket sales) or experiencing high traffic spikes,
order confirmation emails can become a performance bottleneck, potentially slowing down the checkout
process for other customers.

To improve performance, these emails can be queued and processed separately from the order
confirmation flow. This is managed by the Sales: Send pending emails scheduled action,
which sends queued emails as soon as possible.

To enable asynchronous email sending:

1. Enable the [developer mode](../../general/developer_mode.md).
2. Go to Apps, remove the Apps filter, and install the Sales
   - Async Emails module.
3. Go to Settings ‣ Technical ‣ System Parameters and set the
   sale.async_emails system parameter to `True`.
4. Go to Settings ‣ Technical ‣ Scheduled Actions and ensure that the
   Sales: Send pending emails scheduled action is enabled.
