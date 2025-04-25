# Event booths

The Odoo _Events_ application provides users with the ability to create event booths, sell their\
availability, and manage their reservations.

## Cấu hình

In order to create, sell, and manage booths for events, the _Booth Management_ feature must be\
activated.

To do that, navigate to Events app ‣ Configuration ‣ Settings, and tick the\
Booth Management checkbox. Then, click Save.

![The Booth Management setting in the Odoo Events application.](../../../_images/booth-management-setting.png)

#### IMPORTANT

When the Booth Management setting is activated, a new [Product Type](../../inventory_and_mrp/inventory/product_management/configure/type.md) becomes available on all\
product forms: _Event Booth_.

This is important because every created booth **must** be assigned a _Booth Category_ on their\
respective booth form, and every booth category **must** have an _Event Booth_ product assigned\
to it.

## Booth categories

With the _Booth Management_ setting activated in the _Events_ app, the _Booth Categories_ option\
appears in the Configuration menu.

To access the Booth Category dashboard, go to Events app ‣\
Configuration ‣ Booth Categories, which reveals a list of all created booth categories.

![The Booth Category page in the Odoo Events application.](../../../_images/booth-category-page.png)

On the Booth Category page, the following information for each booth category is listed:

* Name: the name of the booth category.
* Create Sponsor: if checked, booking this booth category creates a sponsor for the\
  user.
* Product: the _Event Booth_ product associated with that specific booth category.
* Price: the price of a booth in that booth category.

When the (settings) icon, located to the far-right of the\
column titles, is clicked, a drop-down menu of additional column options appears. From the resulting\
drop-down menu, tick the checkbox beside Sponsor Level and/or Sponsor Type\
to reveal those columns on the Booth Category page.

To edit an existing booth category, select it from the list, and proceed to make any desired\
modifications from the event category form.

### Create booth category

To create a booth category from the Booth Category page, click the New\
button in the upper-left corner to reveal a blank booth category form.

![A typical booth category form in the Odoo Events application.](../../../_images/booth-category-form.png)

Start by entering a name for the booth category in the top Booth Category field. This is\
a **requried** field.

Để thêm hình ảnh minh họa cho danh mục gian hàng (VD: ảnh mẫu về cách bố trí gian hàng), hãy nhấp vào biểu tượng (bút chì) xuất hiện khi di chuột qua vị trí hình máy ảnh ở góc trên bên phải của biểu mẫu danh mục gian hàng. Khi nhấp vào, tiến hành tải lên hình ảnh mong muốn cho biểu mẫu danh mục gian hàng nếu cần.

In the Booth Details section, users **must** assign a Product to the\
category, and it **must** have _Event Booth_ set as the _Product Type_ on the product form.

And, regardless of the listed price on the _Event Booth_ product chosen, the user can input a custom\
Price to be applied for this booth category in the field below.

In the Sponsorship section, there is a Create Sponsor checkbox option. With\
that checkbox ticked, whenever a booth belonging to this category is booked, the user is created as\
an official _Sponsor_ of the event.

When the Create Sponsor checkbox is ticked, two additional fields appear beneath it:\
Sponsor Level and Sponsor Type.

#### NOTE

Cấp độ nhà tài trợ và Loại nhà tài trợ chỉ dùng để phân biệt các cấp bậc khác nhau của nhà tài trợ. Ví dụ, nếu một nhà tài trợ đã gắn bó với công ty trong nhiều năm, họ sẽ được cấp một cấp độ cao hơn (VD: _Vàng_), giúp họ có ngay uy tín và vị thế. Ngược lại, một nhà tài trợ mới hơn sẽ được cấp một cấp độ thấp hơn VD: _Đồng_), tương ứng với mức độ uy tín và vị thế của họ.

Select a desired level of sponsorship from the Sponsor Level drop-down field.

Users can also create a new Sponsor Level, by typing in the name of the new level, and\
clicking Create and edit... from the resulting drop-down menu.

#### NOTE

Clicking Create from the resulting drop-down menu in this instance creates the\
sponsor level, but doesn't immediately prompt the user to further configure it, via a\
Create Sponsor Level pop-up window.

Doing so reveals a Create Sponsor Level pop-up window.

![The Create Sponsor Level pop-up window that appears in the Odoo Events application.](../../../_images/create-sponsor-level-popup.png)

From this pop-up window, confirm the newly-created Sponsor Level, and decide what kind\
of Ribbon Style should be applied, if any. The Ribbon Style options\
available in that drop-down field are: No Ribbon, Gold, Silver,\
and Bronze.

If one is selected, that Ribbon Style appears with the sponsor's name on the event\
website.

On the booth category form, beneath those sections (Booth Details and\
Sponsorship), there is the Description tab. In this tab, proceed to enter\
any vital information related to the booth category that would be important for any potential\
booth-buyer to know about (e.g., the square footage, any amenities, size of display screen, etc.).

## Add booth to an event

In order to add a booth to an event, navigate to an existing event form, via Events\
app ‣ Events, and select the desired event from the Events dashboard. Or, click\
New to open a blank event form.

From the event form, to access the _Booths_ for that specific event, click the Booths\
smart button at the top of the page.

The Booths page is displayed in a Kanban view, by default, with two different stages:\
Available and Unavailable.

#### NOTE

The Booths page of an event is also viewable in a List view, Graph view, and Pivot view. All of which are accessible, via their icons, in the upper-right corner\
of the Booths page.

The booths present in the Available stage are still available for people to purchase for\
the event. The booths present in the Unavailable stage have already been purchased, and\
are no longer available.

To modify any existing booth, simply click the desired booth from the Booths page, and\
proceed to make any necessary changes from the booth form. Or, create a new one, by clicking the\
New button in the upper-left corner to reveal a blank booth form.

### Booth form

The booth form in Odoo _Events_ lets users customize and configure event booths in a number of\
different ways.

![Typical booth form in the Odoo Events application.](../../../_images/booth-form.png)

Start by typing in a Name for the booth. This is a **required** field.

Then, apply a Booth Category to the booth. This is a **required** field.

Upon selecting a pre-existing Booth Category, two additional, non-modifiable fields\
appear: Product and Price. Both fields represent their respective selections\
for that specific booth category.

When a person purchases a booth rental through the event website, the subsequent renter-related\
fields on the form auto-populate, based on the information provided by the purchaser during the\
online transaction. The booth also automatically changes its status from _Available_ t&#x6F;_&#x55;navailable_.

However, if the rental of a booth is conducted in any other way (e.g., in person, via sales order,\
etc.), the Renter, Renter Name, Renter Email, and\
Renter Phone fields can be entered in manually.

The status of the booth (Available or Unavailable) can also be changed\
manually, either by clicking the appropriate status from the status bar present on the booth form,\
or by dragging-and-dropping the desired booth into the appropriate stage, via the _Booths_ page\
Kanban view.

## Sell event booths

With event booths configured on the event form, via the event-specific _Booths_ pages, Odoo presents\
them on the event website, via the _Get A Booth_ event subheader link.

To access the _Get A Booth_ page on the event website, open the Events app, and\
select the desired event from the Events dashboard. From the event form, click the\
Go to Website smart button to be taken to the Odoo-built event website.

If the event subheader menu (with the Get A Booth option) is _not_ showing up on the\
event website, there are two ways to make it appear.

While on the event website, enter the edit mode by clicking the Edit button in the\
upper-right corner. Then, click into the Customize tab of the resulting sidebar of web\
design tools.

In the Customize tab, click the toggle switch for Sub-Menu (Specific), and\
click Save. Doing so reveals the event subheader menu with various options.

Alternatively, enter [Debug mode](../../general/developer_mode.md), and open the specific event\
form in the the _Events_ application.

On the event form, with _Debug mode_ on, an array of subheader menu options appears. Tick the\
checkbox for Website Submenu, in order for the submenu to appear on the event website.\
Doing so also ticks every other submenu-related checkbox automatically.

At this point, proceed to choose which options to keep on the event subheader menu. In this case,\
make sure the Booth Register checkbox is ticked.

From there, click the Get A Booth event subheader menu option. Doing so reveals the\
Get A Booth page, showcasing all the configured event booths that were created on the\
event form.

![Typical Get A Booth page on the event website via the Odoo Events app.](../../../_images/get-a-booth-page.png)

From here, the visitor can select their desired booth option, then Location. Next, they\
would click the Book my Booth(s) button, located at the bottom of the Get A\
Booth page.

Doing so reveals a Contact Details page, wherein they fill out either _Contact Details_\
or _Sponsor Details_, depending on how the booth was configured on the event form. The fields\
present on this form vary, depending on whether its meant for a basic contact or an event sponsor.

#### NOTE

If the selected booth has the _Create Sponsor_ checkbox ticked, this page reads as _Sponsor_\
_Details_.

The information provided on this details page is used to auto-populate the renter-related\
information on the booth form on the event form in the _Events_ application.

Once the necessary information has been entered, the visitor then clicks the Go to\
Payment at the bottom of the page, and proceeds to complete the typical checkout process.

Upon a successful payment confirmation, that selected booth automatically moves to the _Unavailable_\
stage on the event-specific _Booths_ page in the _Events_ application (accessible via the _Booths_\
smart button on the event form).

Also, the provided _Sponsor_ information (if applicable) and _Sales Order_ information are\
accessible from the specific event form, via their respective smart buttons that appear at the top\
of the form.

#### NOTE

Click the _Sponsors_ smart button to modify any information about the sponsor, if necessary.

#### SEE ALSO

* [Create events](create_events.md)
* [Sell event tickets](sell_tickets.md)
