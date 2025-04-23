# Continuous product improvement

*Continuous improvement* is a general philosophy intended to help individuals and organizations
constantly improve themselves and the work they produce.

There are a variety of different methodologies that fall under the umbrella of continuous
improvement. These include kaizen, six sigma, and lean, among others. While the specific steps of
each method differ, their goal remains the same: implement a process by which improvement is a
perpetual goal, rather than a one-time accomplishment.

The sections below contain details about how Odoo can be used to implement four general steps common
to many of the most popular continuous improvement strategies, with links to documentation about
configuring the necessary features. The final section details how a specific company might configure
these Odoo implementations within their organization.

1. [Identify problems](#manufacturing-workflows-ci-identify)
2. [Suggest improvements](#manufacturing-workflows-ci-suggest)
3. [Implement strategies](#manufacturing-workflows-ci-implement)
4. [Review actions](#manufacturing-workflows-ci-review)

#### IMPORTANT
Continuous improvement is not a one-size-fits-all methodology. While most strategies include
between four and six steps, proper implementation requires developing a system tailored to the
specific needs of each company.

This is not a limitation, but rather a benefit, as it makes the methodology flexible enough to
adapt to almost any use case. Odoo, in particular, adapts well to this flexibility, as it can be
configured to meet the needs of almost any workflow.

As such, it is important to remember the content below only provides *examples* of how Odoo
*might* be used. They should be viewed as more of a starting point, rather than a concrete
outline that every organization must follow.

<a id="manufacturing-workflows-ci-identify"></a>

## Identify problems

Before improvement can begin, it is necessary to determine where improvement is necessary. This is
where identifying problems comes into play. Two of the best Odoo apps for identifying problems with
products or processes are *Helpdesk* and *Quality*.

### Hỗ trợ

The *Helpdesk* app is useful for receiving feedback from outside of the organization, like from
clients or customers. This is accomplished by implementing one (or more) of the methods for
[receiving tickets](../../../services/helpdesk/overview/receiving_tickets.md), including email
aliases, live chat conversations, and website forms.

Using these methods, customers can submit feedback about problems, which is then reviewed by a
member of a [helpdesk team](../../../services/helpdesk.md). Depending on the outcome of the
review, the team member may decide to take further action to ensure the issue is addressed. This can
include creating a [quality alert](../../quality/quality_management/quality_alerts.md).

### Chất lượng

The *Quality* app is useful for receiving feedback from *within* the organization, like from
employees.

One method for accomplishing this is to set up a [quality control point](../../quality/quality_management/quality_control_points.md) (QCP). A  is used to automatically
create quality checks at regular intervals, prompting employees to inspect, and confirm, the quality
of a product.

Khi phát hiện vấn đề, nhân viên có thể tạo [cảnh báo chất lượng](../../quality/quality_management/quality_alerts.md) để thông báo cho bộ phận quản lý chất lượng. Cảnh báo chất lượng cũng có thể được tạo độc lập với  khi nhân viên phát hiện vấn đề mà không cần được yêu cầu kiểm tra trước. Đây là cách hiệu quả để nhân viên hỗ trợ khách hàng thông báo cho bộ phận chất lượng về các vấn đề được đề cập trong phiếu hỗ trợ khách hàng.

<a id="manufacturing-workflows-ci-suggest"></a>

## Suggest improvements

Once a problem is identified, the next step is to put forward ideas for how to address the problem.
As with identifying problems, the *Quality app* is also useful for suggesting improvements. In
addition, the *PLM* (*Product Lifecycle Management*) app can be used for this purpose, as well.

### Chất lượng

When creating a [quality alert](../../quality/quality_management/quality_alerts.md) to bring an
issue to the attention of a quality team, the Corrective Actions and
Preventive Actions tabs can be used to provide feedback about how the issue can be
addressed.

The Corrective Actions tab is used to suggest a method for fixing items affected by the
issue. For example, `Screw the bolts on tighter, so the seat stays in place`.

The Preventive Actions tab is used to suggest a method for preventing the issue from
occurring in the future. For example, `Do not tighten the screws too much, or they will be
stripped`.

The quality team that reviews the alert sees these suggested actions, and can take them into account
when deciding how to address the issue.

### QLVĐSP

The  app is used to manage the lifecycle of a product from its introduction through each
successive version. As such, it is useful for testing ideas for product improvements.

Using [engineering change orders](../../plm/manage_changes/engineering_change_orders.md), product
management teams can create new iterations of product , adding or removing specific components
or operations, as needed. The products created using these  are put through a review process
to confirm the effectiveness of the changes.

<a id="manufacturing-workflows-ci-implement"></a>

## Implement strategies

Implementing strategies involves putting the proposed solutions from the suggest improvements step
into action. The  app continues to be useful during this step, as it can be configured to make
 updates. The *Field Service* app can also be used by certain companies to make improvements to
products that have already been sold to customers.

### QLVĐSP

Once  changes have gone through the proper review process, they can be approved, and the
updated  put into use. This is accomplished by configuring one of the  review stages to
[apply the changes](../../plm/manage_changes/engineering_change_orders.md#plm-eco-apply-changes) made to the , at which point the updated 
becomes available for new .

Product  can continue to be updated, as needed. The [version control](../../plm/manage_changes/version_control.md) features of the  app allow for easy management of
all versions of a given .

### Dịch vụ hiện trường

The  app is a great way to make changes to product . However, these changes only affect
products produced using the new . If a defective product has already been sold to a customer,
it may be necessary to repair (or update) that product.

In such a case, the *Field Service* app can be used to schedule [onsite interventions](../../../services/field_service/creating_tasks.md). These interventions allow service
technicians (or other employees) to be sent to a customer's location to address an issue with a
product.

<a id="manufacturing-workflows-ci-review"></a>

## Review actions

Reviewing actions is where the "continuous" part of continuous improvement comes into play, as it
allows an organization to evaluate the decisions made in the previous steps. As such, this step is,
essentially, returning to the beginning of the process, so that additional problems can be
identified and addressed.

This means that the *Helpdesk* and *Quality* apps should be used again to receive customer and
employee feedback. Another app that may be useful at this stage is the *Surveys* app.

### Khảo sát

After implementing changes to a product or process, it may be wise to solicit customers for their
feedback directly, rather than waiting to hear from them of their own volition. This may bring to
light feedback that customers may have otherwise neglected to share.

One of the best ways to accomplish this is through the [Surveys](../../../marketing/surveys.md)
app. Creating a survey, and sending it to customers who receive an updated product, increases the
likelihood of receiving relevant feedback about the product.
