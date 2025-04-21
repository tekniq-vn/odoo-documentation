# Vehicle models

When adding a vehicle to the fleet, specify the vehicle model to maintain updated records, which
keeps track of specific details, like maintenance schedules and parts compatibility.

Odoo comes with preconfigured car models from four major auto manufacturers: Audi, BMW, Mercedes,
and Opel.

If a new vehicle model joins the fleet, and it is not one of the preconfigured models from these
manufacturers, the model (and/or manufacturer) **must** be [added to the
database](#fleet-add-model).

## Preconfigured models

The following models are preconfigured in Odoo, and do not need to be added to the database:

| AUDI   | BMW          | Mercedes   | Opel          |
|--------|--------------|------------|---------------|
| A1     | Sê-ri 1      | Hạng A     | Agilia        |
| A3     | Sê-ri 3      | Hạng B     | Ampera        |
| A4     | Sê-ri 5      | Hạng C     | Antara        |
| A5     | Sê-ri 6      | Hạng CL    | Astra         |
| A6     | Sê-ri 7      | Hạng CLS   | AstraGTC      |
| A7     | Sê-ri hybrid | Hạng E     | Combo Tour    |
| A8     | Sê-ri M      | Hạng GL    | Corsa         |
| Q3     | Sê-ri X      | Hạng GLK   | Insignia      |
| Q5     | Sê-ri Z4     | Hạng M     | Meriva        |
| Q7     |              | Hạng R     | Mokka         |
| TT     |              | Hạng S     | Zafira        |
|        |              | Hạng SLK   | Zafira Tourer |
|        |              | Hạng SLS   |               |

<a id="fleet-add-model"></a>

## Add a new model

To add a new vehicle model, navigate to Fleet app ‣ Configuration ‣ Models:
Models. Click New, and in a new vehicle model form, enter the following information on
the form.

#### NOTE
Be advised, some fields are specific to Belgian based companies, so not all fields or sections
may be visible depending on the location of the company.

- Model name: enter the model name in the field.
- Manufacturer: select the manufacturer from the drop-down menu. If the manufacturer is
  not configured, type in the manufacturer, and click Create or Create and
  edit...

  #### NOTE
  When the manufacturer is selected, if it is one of the default manufacturers in *Odoo*, the
  logo for the manufacturer automatically loads in the image box in the top-right corner.
- Vehicle Type: select one of two preconfigured vehicle types, either Car or
  Bike, from the drop-down menu. The vehicle types are hardcoded in Odoo, and are
  integrated with the *Payroll* application, since vehicles can be part of an employee's benefits.
  Adding additional vehicle types is *not* possible as it affects payroll.
- Category: select a category for the vehicle from the drop-down menu. To create a new
  category, type in the category and then click Create (new category).

### Tab thông tin

In the Information tab, specify details about the car model, such as the car size,
passenger capacity, cost settings (applicable to the Belgium localization only), and engine
information.

#### Model section

- Seats Number: enter how many passengers the vehicle can accommodate.
- Doors Number: enter the number of doors the vehicle has.
- Color: enter the color of the vehicle.
- Model Year: enter the year the vehicle was manufactured.
- Trailer Hitch: tick this checkbox if the vehicle has a trailer hitch installed.

#### Salary section

#### NOTE
The Salary section **only** appears for Belgian-based companies, and **only** if the
company has their localization setting set to Belgium. The cost values are all *monthly*, with
the exception of the Catalog Value (VAT Incl.).

- Can be requested: tick this checkbox if employees can request this model vehicle, if a
  vehicle is part of their employee contract.
- Catalog Value (VAT Incl.): enter the  for the vehicle at the time of purchase or lease.
- C02 fee: represents the carbon dioxide emission fee paid to the Belgian government.
  This value is automatically calculated, based on Belgian laws and regulations, and **cannot** be
  modified. The value is based on the figure entered in the CO2 Emissions field (in the
  Engine section of the Information tab) on the vehicle form.

#### IMPORTANT
Modifying the CO2 Emissions field adjusts the value in the CO2 fee field.

- Chi phí (Khấu hao): nhập chi phí hàng tháng cho xe, xuất hiện trong trình cấu hình lương cho nhân viên tương lai. Giá trị này ảnh hưởng đến tổng lương và lương thực nhận của nhân viên được phân công xe. Số liệu này được khấu hao theo thời gian dựa trên luật thuế địa phương. Chi phí (Khấu hao) **không** tự động khấu hao trên *mẫu xe*, mà chỉ khấu hao dựa trên *hợp đồng* liên kết với một xe cụ thể.
- Total Cost (Depreciated): this value is the combination of the Cost
  (Depreciated) and the C02 fee fields. It also depreciated over time.

#### Engine

- Fuel Type: select the type of fuel the vehicle uses from the drop-down menu. The
  options are Diesel, Gasoline, Hybrid Diesel, Hybrid
  Gasoline, Plug-in Hybrid Diesel, Plug-in Hybrid Gasoline,
  CNG, LPG, Hydrogen, or Electric.
- CO2 Emissions: enter the average carbon dioxide emissions the vehicle produces in
  grams per kilometer (g/km). This information is provided by the car manufacturer.
- CO2 Standard: enter the standard amount of carbon dioxide in grams per kilometer
  (g/km) for a similar-sized vehicle.
- Transmission: select Manual or Automatic transmission from the
  drop-down menu.
- Power: if the vehicle is electric or hybrid, enter the power the vehicle uses in
  kilowatts (kW).
- Horsepower: enter the vehicle's horsepower in this field.
- Horsepower Taxation: enter the amount that is taxed, based on the size of the
  vehicle's engine. This is determined by local taxes and regulations, and varies depending on the
  location. It is recommended to check with the accounting department to ensure this value is
  correct.
- Tax Deduction: this field auto-populates, according to the engine specifications, and
  **cannot** be modified. The percentage is based on the localization settings and local tax laws.

### Vendors tab

Specify the vendors a vehicle can be purchased from in this tab. With proper setup, requests for
quotations for vehicles can be easily created through Odoo's *Purchase* app.

To add a vendor, click Add, which opens an Add: Vendors pop-up window, with
a list of all the vendors currently in the database. Add a vendor by ticking the checkbox next to
the vendor name, then click Select. There is no limit to the number of vendors that can
be added to this list.

Nếu nhà cung cấp chưa có trong cơ sở dữ liệu, thêm nhà cung cấp bằng cách nhấp Mới ở góc dưới bên trái cửa sổ bật lên Thêm: Nhà cung cấp. Trong biểu mẫu Tạo nhà cung cấp hiện ra, nhập thông tin cần thiết, sau đó nhấp Lưu & đóng để thêm nhà cung cấp hoặc nhấp Lưu & mới để thêm nhà cung cấp hiện tại và tạo một nhà cung cấp mới khác.

![Vendor form to fill out when adding a new vendor.](models/vendor.png)

<a id="fleet-categories"></a>

## Model category

To best organize a fleet, it is recommended to have vehicle models housed under a specific category,
to easily see what kinds of vehicles are in the fleet. Model categories are set on the [vehicle
model form](#fleet-add-model).

Odoo does **not** come with any models preconfigured; all models **must** be added.

To view any models currently set up in the database, navigate to Fleet app ‣
Configuration ‣ Models: Categories. All models are displayed in a list view.

### Add a new model category

To add a new category, click the New button in the top-left corner of the
Categories page. A new entry line appears at the bottom of the list. Type in the new
category, then either click Save, or click anywhere on the screen, to save the entry.

To reorganize how the categories appear in the list, click on the <i class="oi oi-draggable"></i>
(draggable) icon to the left of any desired category name, and drag the line to the
desired position.

The order of the list does not affect the database in any way. However, it may be preferable to view
the vehicle categories in a specific order, for example, by size, or the numbers of passengers the
vehicle can carry.

![List view of the models in the fleet.](models/categories.png)
