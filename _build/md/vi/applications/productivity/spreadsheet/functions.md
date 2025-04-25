# Hàm

Hàm bảng tính được phân chia thành các loại sau:

- [Array](#functions-array)
- [Cơ sở dữ liệu](#functions-database)
- [Ngày](#functions-date)
- [Kỹ thuật](#functions-engineering)
- [Bộ lọc](#functions-filter)
- [Tài chính](#functions-financial)
- [Thông tin](#functions-info)
- [Logic](#functions-logical)
- [Tìm kiếm](#functions-lookup)
- [Toán](#functions-math)
- [Khác](#functions-misc)
- [Odoo](#functions-odoo)
- [Toán tử](#functions-operators)
- [Thống kê](#functions-statistical)
- [Văn bản](#functions-text)
- [Web](#functions-web)

#### NOTE
Những công thức chứa các hàm không tương thích với Excel sẽ được thay thế bằng kết quả đã được đánh giá khi xuất bảng tính.

<a id="functions-array"></a>

## Mảng

| Tên và đối số                               | Mô tả hoặc liên kết                                                                                                               |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ARRAY.CONSTRAIN(input_range, rows, columns) | Trả về một mảng kết quả bị giới hạn ở chiều rộng và chiều cao cụ thể (không tương thích với Excel)                                |
| CHOOSECOLS(array, col_num, [col_num2, ...]) | [Bài viết về hàm Excel CHOOSECOLS](https://support.microsoft.com/office/choosecols-function-bf117976-2722-4466-9b9a-1c01ed9aebff) |
| CHOOSEROWS(array, row_num, [row_num2, ...]) | [Bài viết về hàm Excel CHOOSEROWS](https://support.microsoft.com/office/chooserows-function-51ace882-9bab-4a44-9625-7274ef7507a3) |
| EXPAND(array, rows, [columns], [pad_with])  | [Bài viết về hàm Excel EXPAND](https://support.microsoft.com/office/expand-function-7433fba5-4ad1-41da-a904-d5d95808bc38)         |
| FLATTEN(range, [range2, ...])               | Làm phẳng tất cả giá trị từ một hoặc nhiều dải ô thành một cột duy nhất (không tương thích với Excel)                             |
| FREQUENCY(data, classes)                    | [Bài viết về hàm Excel FREQUENCY](https://support.microsoft.com/office/frequency-function-44e3be2b-eca0-42cd-a3f7-fd9ea898fdb9)   |
| HSTACK(range1, [range2, ...])               | [Bài viết về hàm Excel HSTACK](https://support.microsoft.com/office/hstack-function-98c4ab76-10fe-4b4f-8d5f-af1c125fe8c2)         |
| MDETERM(square_matrix)                      | [Bài viết về hàm Excel MDETERM](https://support.microsoft.com/office/mdeterm-function-e7bfa857-3834-422b-b871-0ffd03717020)       |
| MINVERSE(square_matrix)                     | [Bài viết về hàm Excel MINVERSE](https://support.microsoft.com/office/minverse-function-11f55086-adde-4c9f-8eb9-59da2d72efc6)     |
| MMULT(matrix1, matrix2)                     | [Bài viết về hàm Excel MMULT](https://support.microsoft.com/office/mmult-function-40593ed7-a3cd-4b6b-b9a3-e4ad3c7245eb)           |
| SUMPRODUCT(range1, [range2, ...])           | [Bài viết về hàm Excel SUMPRODUCT](https://support.microsoft.com/office/sumproduct-function-16753e75-9f68-4874-94ac-4d2145a2fd2e) |
| SUMX2MY2(array_x, array_y)                  | [Bài viết về hàm Excel SUMX2MY2](https://support.microsoft.com/office/sumx2my2-function-9e599cc5-5399-48e9-a5e0-e37812dfa3e9)     |
| SUMX2PY2(array_x, array_y)                  | [Bài viết về hàm Excel SUMX2PY2](https://support.microsoft.com/office/sumx2py2-function-826b60b4-0aa2-4e5e-81d2-be704d3d786f)     |
| SUMXMY2(array_x, array_y)                   | [Bài viết về hàm Excel SUMXMY2](https://support.microsoft.com/office/sumxmy2-function-9d144ac1-4d79-43de-b524-e2ecee23b299)       |
| TOCOL(array, [ignore], [scan_by_column])    | [Bài viết về hàm Excel TOCOL](https://support.microsoft.com/office/tocol-function-22839d9b-0b55-4fc1-b4e6-2761f8f122ed)           |
| TOROW(array, [ignore], [scan_by_column])    | [Bài viết về hàm Excel TOROW](https://support.microsoft.com/office/torow-function-b90d0964-a7d9-44b7-816b-ffa5c2fe2289)           |
| TRANSPOSE(range)                            | [Bài viết về hàm Excel TRANSPOSE](https://support.microsoft.com/office/transpose-function-ed039415-ed8a-4a81-93e9-4b6dfac76027)   |
| VSTACK(range1, [range2, ...])               | [Bài viết về hàm Excel VSTACK](https://support.microsoft.com/office/vstack-function-a4b86897-be0f-48fc-adca-fcc10d795a9c)         |
| WRAPCOLS(range, wrap_count, [pad_with])     | [Bài viết về hàm Excel WRAPCOLS](https://support.microsoft.com/office/wrapcols-function-d038b05a-57b7-4ee0-be94-ded0792511e2)     |
| WRAPROWS(range, wrap_count, [pad_with])     | [Bài viết về hàm Excel WRAPROWS](https://support.microsoft.com/office/wraprows-function-796825f3-975a-4cee-9c84-1bbddf60ade0)     |

<a id="functions-database"></a>

## Cơ sở dữ liệu

| Tên và đối số                       | Mô tả hoặc liên kết                                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| DAVERAGE(database, field, criteria) | [Bài viết về hàm Excel DAVERAGE](https://support.microsoft.com/office/daverage-function-a6a2d5ac-4b4b-48cd-a1d8-7b37834e5aee) |
| DCOUNT(database, field, criteria)   | [Bài viết về hàm Excel DCOUNT](https://support.microsoft.com/office/dcount-function-c1fc7b93-fb0d-4d8d-97db-8d5f076eaeb1)     |
| DCOUNTA(database, field, criteria)  | [Bài viết về hàm Excel DCOUNTA](https://support.microsoft.com/office/dcounta-function-00232a6d-5a66-4a01-a25b-c1653fda1244)   |
| DGET(database, field, criteria)     | [Bài viết về hàm Excel DGET](https://support.microsoft.com/office/dget-function-455568bf-4eef-45f7-90f0-ec250d00892e)         |
| DMAX(database, field, criteria)     | [Bài viết về hàm Excel DMAX](https://support.microsoft.com/office/dmax-function-f4e8209d-8958-4c3d-a1ee-6351665d41c2)         |
| DMIN(database, field, criteria)     | [Bài viết về hàm Excel DMIN](https://support.microsoft.com/office/dmin-function-4ae6f1d9-1f26-40f1-a783-6dc3680192a3)         |
| DPRODUCT(database, field, criteria) | [Bài viết về hàm Excel DPRODUCT](https://support.microsoft.com/office/dproduct-function-4f96b13e-d49c-47a7-b769-22f6d017cb31) |
| DSTDEV(database, field, criteria)   | [Bài viết về hàm Excel DSTDEV](https://support.microsoft.com/office/dstdev-function-026b8c73-616d-4b5e-b072-241871c4ab96)     |
| DSTDEVP(database, field, criteria)  | [Bài viết về hàm Excel DSTDEVP](https://support.microsoft.com/office/dstdevp-function-04b78995-da03-4813-bbd9-d74fd0f5d94b)   |
| DSUM(database, field, criteria)     | [Bài viết về hàm Excel DSUM](https://support.microsoft.com/office/dsum-function-53181285-0c4b-4f5a-aaa3-529a322be41b)         |
| DVAR(database, field, criteria)     | [Bài viết về hàm Excel DVAR](https://support.microsoft.com/office/dvar-function-d6747ca9-99c7-48bb-996e-9d7af00f3ed1)         |
| DVARP(database, field, criteria)    | [Bài viết về hàm Excel DVARP](https://support.microsoft.com/office/dvarp-function-eb0ba387-9cb7-45c8-81e9-0394912502fc)       |

<a id="functions-date"></a>

## Ngày

| Tên và đối số                                                 | Mô tả hoặc liên kết                                                                                                                           |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| DATE(year, month, day)                                        | [Bài viết về hàm Excel DATE](https://support.microsoft.com/office/date-function-e36c0c8c-4104-49da-ab83-82328b832349)                         |
| DATEDIF(start_date, end_date, unit)                           | [Bài viết về hàm Excel DATEDIF](https://support.microsoft.com/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c)                   |
| DATEVALUE(date_string)                                        | [Bài viết về hàm Excel DATEVALUE](https://support.microsoft.com/office/datevalue-function-df8b07d4-7761-4a93-bc33-b7471bbff252)               |
| DAY(date)                                                     | [Bài viết về hàm Excel DAY](https://support.microsoft.com/office/day-function-8a7d1cbb-6c7d-4ba1-8aea-25c134d03101)                           |
| DAYS(end_date, start_date)                                    | [Bài viết về hàm Excel DAYS](https://support.microsoft.com/office/days-function-57740535-d549-4395-8728-0f07bff0b9df)                         |
| DAYS360(start_date, end_date, [method])                       | [Bài viết về hàm Excel DAYS360](https://support.microsoft.com/office/days360-function-b9a509fd-49ef-407e-94df-0cbda5718c2a)                   |
| EDATE(start_date, months)                                     | [Bài viết về hàm Excel EDATE](https://support.microsoft.com/office/edate-function-3c920eb2-6e66-44e7-a1f5-753ae47ee4f5)                       |
| EOMONTH(start_date, months)                                   | [Bài viết về hàm Excel EOMONTH](https://support.microsoft.com/office/eomonth-function-7314ffa1-2bc9-4005-9d66-f49db127d628)                   |
| HOUR(time)                                                    | [Bài viết về hàm Excel HOUR](https://support.microsoft.com/office/hour-function-a3afa879-86cb-4339-b1b5-2dd2d7310ac7)                         |
| ISOWEEKNUM(date)                                              | [Bài viết về hàm Excel ISOWEEKNUM](https://support.microsoft.com/office/isoweeknum-function-1c2d0afe-d25b-4ab1-8894-8d0520e90e0e)             |
| MINUTE(time)                                                  | [Bài viết về hàm Excel MINUTE](https://support.microsoft.com/office/minute-function-af728df0-05c4-4b07-9eed-a84801a60589)                     |
| MONTH(date)                                                   | [Bài viết về hàm Excel MONTH](https://support.microsoft.com/office/month-function-579a2881-199b-48b2-ab90-ddba0eba86e8)                       |
| NETWORKDAYS(start_date, end_date, [holidays])                 | [Bài viết về hàm Excel NETWORKDAYS](https://support.microsoft.com/office/networkdays-function-48e717bf-a7a3-495f-969e-5005e3eb18e7)           |
| NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays]) | [Bài viết về hàm Excel NETWORKDAYS.INTL](https://support.microsoft.com/office/networkdays-intl-function-a9b26239-4f20-46a1-9ab8-4e925bfd5e28) |
| NOW()                                                         | [Bài viết về hàm Excel NOW](https://support.microsoft.com/office/now-function-3337fd29-145a-4347-b2e6-20c904739c46)                           |
| SECOND(time)                                                  | [Bài viết về hàm Excel SECOND](https://support.microsoft.com/office/second-function-740d1cfc-553c-4099-b668-80eaa24e8af1)                     |
| TIME(hour, minute, second)                                    | [Bài viết về hàm Excel TIME](https://support.microsoft.com/office/time-function-9a5aff99-8f7d-4611-845e-747d0b8d5457)                         |
| TIMEVALUE(time_string)                                        | [Bài viết về hàm Excel TIMEVALUE](https://support.microsoft.com/office/timevalue-function-0b615c12-33d8-4431-bf3d-f3eb6d186645)               |
| TODAY()                                                       | [Bài viết về hàm Excel TODAY](https://support.microsoft.com/office/today-function-5eb3078d-a82c-4736-8930-2f51a028fdd9)                       |
| WEEKDAY(date, [type])                                         | [Bài viết về hàm Excel WEEKDAY](https://support.microsoft.com/office/weekday-function-60e44483-2ed1-439f-8bd0-e404c190949a)                   |
| WEEKNUM(date, [type])                                         | [Bài viết về hàm Excel WEEKNUM](https://support.microsoft.com/office/weeknum-function-e5c43a03-b4ab-426c-b411-b18c13c75340)                   |
| WORKDAY(start_date, num_days, [holidays])                     | [Bài viết về hàm Excel WORKDAY](https://support.microsoft.com/office/workday-function-f764a5b7-05fc-4494-9486-60d494efbf33)                   |
| WORKDAY.INTL(start_date, num_days, [weekend], [holidays])     | [Bài viết về hàm Excel WORKDAY.INTL](https://support.microsoft.com/office/workday-intl-function-a378391c-9ba7-4678-8a39-39611a9bf81d)         |
| YEAR(date)                                                    | [Bài viết về hàm Excel YEAR](https://support.microsoft.com/office/year-function-c64f017a-1354-490d-981f-578e8ec8d3b9)                         |
| YEARFRAC(start_date, end_date, [day_count_convention])        | Số năm chính xác giữa hai ngày (không tương thích với Excel)                                                                                  |
| MONTH.START(date)                                             | Ngày đầu tiên của tháng trước một ngày (không tương thích với Excel)                                                                          |
| MONTH.END(date)                                               | Ngày cuối cùng của tháng sau một ngày (không tương thích với Excel)                                                                           |
| QUARTER(date)                                                 | Quý trong năm mà một ngày cụ thể rơi vào (không tương thích với Excel)                                                                        |
| QUARTER.START(date)                                           | Ngày đầu tiên của quý trong năm mà một ngày cụ thể rơi vào (không tương thích với Excel)                                                      |
| QUARTER.END(date)                                             | Ngày cuối cùng của quý trong năm mà một ngày cụ thể rơi vào (không tương thích với Excel)                                                     |
| YEAR.START(date)                                              | Ngày đầu tiên của năm mà một ngày cụ thể rơi vào (không tương thích với Excel)                                                                |
| YEAR.END(date)                                                | Ngày cuối cùng của năm mà một ngày cụ thể rơi vào (không tương thích với Excel)                                                               |

<a id="functions-engineering"></a>

## Kỹ thuật

| Tên và đối số             | Mô tả hoặc liên kết                                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|
| DELTA(number1, [number2]) | [Bài viết về hàm Excel DELTA](https://support.microsoft.com/office/delta-function-2f763672-c959-4e07-ac33-fe03220ba432) |

<a id="functions-filter"></a>

## Bộ lọc

| Tên và đối số                                | Mô tả hoặc liên kết                                                                                                       |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| FILTER(range, condition1, [condition2, ...]) | [Bài viết về hàm Excel FILTER](https://support.microsoft.com/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759) |
| UNIQUE(range, [by_column], [exactly_once])   | [Bài viết về hàm Excel UNIQUE](https://support.microsoft.com/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e) |

<a id="functions-financial"></a>

## Tài chính

| Tên và đối số                                                                                                | Mô tả hoặc liên kết                                                                                                               |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ACCRINTM(issue, maturity, rate, redemption, [day_count_convention])                                          | [Bài viết về hàm Excel ACCRINTM](https://support.microsoft.com/office/accrintm-function-f62f01f9-5754-4cc4-805b-0e70199328a7)     |
| AMORLINC(cost, purchase_date, first_period_end, salvage, period, rate, [day_count_convention])               | [Bài viết về hàm Excel AMORLINC](https://support.microsoft.com/office/amorlinc-function-7d417b45-f7f5-4dba-a0a5-3451a81079a8)     |
| COUPDAYS(settlement, maturity, frequency, [day_count_convention])                                            | [Bài viết về hàm Excel COUPDAYS](https://support.microsoft.com/office/coupdays-function-cc64380b-315b-4e7b-950c-b30b0a76f671)     |
| COUPDAYBS(settlement, maturity, frequency, [day_count_convention])                                           | [Bài viết về hàm Excel COUPDAYBS](https://support.microsoft.com/office/coupdaybs-function-eb9a8dfb-2fb2-4c61-8e5d-690b320cf872)   |
| COUPDAYSNC(settlement, maturity, frequency, [day_count_convention])                                          | [Bài viết về hàm Excel COUPDAYSNC](https://support.microsoft.com/office/coupdaysnc-function-5ab3f0b2-029f-4a8b-bb65-47d525eea547) |
| COUPNCD(settlement, maturity, frequency, [day_count_convention])                                             | [Bài viết về hàm Excel COUPNCD](https://support.microsoft.com/office/coupncd-function-fd962fef-506b-4d9d-8590-16df5393691f)       |
| COUPNUM(settlement, maturity, frequency, [day_count_convention])                                             | [Bài viết về hàm Excel COUPNUM](https://support.microsoft.com/office/coupnum-function-a90af57b-de53-4969-9c99-dd6139db2522)       |
| COUPPCD(settlement, maturity, frequency, [day_count_convention])                                             | [Bài viết về hàm Excel COUPPCD](https://support.microsoft.com/office/couppcd-function-2eb50473-6ee9-4052-a206-77a9a385d5b3)       |
| CUMIPMT(rate, number_of_periods, present_value, first_period, last_period, [end_or_beginning])               | [Bài viết về hàm Excel CUMIPMT](https://support.microsoft.com/office/cumipmt-function-61067bb0-9016-427d-b95b-1a752af0e606)       |
| CUMPRINC(rate, number_of_periods, present_value, first_period, last_period, [end_or_beginning])              | [Bài viết về hàm Excel CUMPRINC](https://support.microsoft.com/office/cumprinc-function-94a4516d-bd65-41a1-bc16-053a6af4c04d)     |
| DB(cost, salvage, life, period, [month])                                                                     | [Bài viết về hàm Excel DB](https://support.microsoft.com/office/db-function-354e7d28-5f93-4ff1-8a52-eb4ee549d9d7)                 |
| DDB(cost, salvage, life, period, [factor])                                                                   | [Bài viết về hàm Excel DDB](https://support.microsoft.com/office/ddb-function-519a7a37-8772-4c96-85c0-ed2c209717a5)               |
| DISC(settlement, maturity, price, redemption, [day_count_convention])                                        | [Bài viết về hàm Excel DISC](https://support.microsoft.com/office/disc-function-71fce9f3-3f05-4acf-a5a3-eac6ef4daa53)             |
| DOLLARDE(fractional_price, unit)                                                                             | [Bài viết về hàm Excel DOLLARDE](https://support.microsoft.com/office/dollarde-function-db85aab0-1677-428a-9dfd-a38476693427)     |
| DOLLARFR(decimal_price, unit)                                                                                | [Bài viết về hàm Excel DOLLARFR](https://support.microsoft.com/office/dollarfr-function-0835d163-3023-4a33-9824-3042c5d4f495)     |
| DURATION(settlement, maturity, rate, yield, frequency, [day_count_convention])                               | [Bài viết về hàm Excel DURATION](https://support.microsoft.com/office/duration-function-b254ea57-eadc-4602-a86a-c8e369334038)     |
| EFFECT(nominal_rate, periods_per_year)                                                                       | [Bài viết về hàm Excel EFFECT](https://support.microsoft.com/office/effect-function-910d4e4c-79e2-4009-95e6-507e04f11bc4)         |
| FV(rate, number_of_periods, payment_amount, [present_value], [end_or_beginning])                             | [Bài viết về hàm Excel FV](https://support.microsoft.com/office/fv-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3)                 |
| FVSCHEDULE(principal, rate_schedule)                                                                         | [Bài viết về hàm Excel FVSCHEDULE](https://support.microsoft.com/office/fvschedule-function-bec29522-bd87-4082-bab9-a241f3fb251d) |
| INTRATE(settlement, maturity, investment, redemption, [day_count_convention])                                | [Bài viết về hàm Excel INTRATE](https://support.microsoft.com/office/intrate-function-5cb34dde-a221-4cb6-b3eb-0b9e55e1316f)       |
| IPMT(rate, period, number_of_periods, present_value, [future_value], [end_or_beginning])                     | [Bài viết về hàm Excel IPMT](https://support.microsoft.com/office/ipmt-function-5cce0ad6-8402-4a41-8d29-61a0b054cb6f)             |
| IRR(cashflow_amounts, [rate_guess])                                                                          | [Bài viết về hàm Excel IRR](https://support.microsoft.com/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc)               |
| ISPMT(rate, period, number_of_periods, present_value)                                                        | [Bài viết về hàm Excel ISPMT](https://support.microsoft.com/office/ispmt-function-fa58adb6-9d39-4ce0-8f43-75399cea56cc)           |
| MDURATION(settlement, maturity, rate, yield, frequency, [day_count_convention])                              | [Bài viết về hàm Excel MDURATION](https://support.microsoft.com/office/mduration-function-b3786a69-4f20-469a-94ad-33e5b90a763c)   |
| MIRR(cashflow_amounts, financing_rate, reinvestment_return_rate)                                             | [Bài viết về hàm Excel MIRR](https://support.microsoft.com/office/mirr-function-b020f038-7492-4fb4-93c1-35c345b53524)             |
| NOMINAL(effective_rate, periods_per_year)                                                                    | [Bài viết về hàm Excel NOMINAL](https://support.microsoft.com/office/nominal-function-7f1ae29b-6b92-435e-b950-ad8b190ddd2b)       |
| NPER(rate, payment_amount, present_value, [future_value], [end_or_beginning])                                | [Bài viết về hàm Excel NPER](https://support.microsoft.com/office/nper-function-240535b5-6653-4d2d-bfcf-b6a38151d815)             |
| NPV(discount, cashflow1, [cashflow2, ...])                                                                   | [Bài viết về hàm Excel NPV](https://support.microsoft.com/office/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568)               |
| PDURATION(rate, present_value, future_value)                                                                 | [Bài viết về hàm Excel PDURATION](https://support.microsoft.com/office/pduration-function-44f33460-5be5-4c90-b857-22308892adaf)   |
| PMT(rate, number_of_periods, present_value, [future_value], [end_or_beginning])                              | [Bài viết về hàm Excel PMT](https://support.microsoft.com/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441)               |
| PPMT(rate, period, number_of_periods, present_value, [future_value], [end_or_beginning])                     | [Bài viết về hàm Excel PPMT](https://support.microsoft.com/office/ppmt-function-c370d9e3-7749-4ca4-beea-b06c6ac95e1b)             |
| PV(rate, number_of_periods, payment_amount, [future_value], [end_or_beginning])                              | [Bài viết về hàm Excel PV](https://support.microsoft.com/office/pv-function-23879d31-0e02-4321-be01-da16e8168cbd)                 |
| PRICE(settlement, maturity, rate, yield, redemption, frequency, [day_count_convention])                      | [Bài viết về hàm Excel PRICE](https://support.microsoft.com/office/price-function-3ea9deac-8dfa-436f-a7c8-17ea02c21b0a)           |
| PRICEDISC(settlement, maturity, discount, redemption, [day_count_convention])                                | [Bài viết về hàm Excel PRICEDISC](https://support.microsoft.com/office/pricedisc-function-d06ad7c1-380e-4be7-9fd9-75e3079acfd3)   |
| PRICEMAT(settlement, maturity, issue, rate, yield, [day_count_convention])                                   | [Bài viết về hàm Excel PRICEMAT](https://support.microsoft.com/office/pricemat-function-52c3b4da-bc7e-476a-989f-a95f675cae77)     |
| RATE(number_of_periods, payment_per_period, present_value, [future_value], [end_or_beginning], [rate_guess]) | [Bài viết về hàm Excel RATE](https://support.microsoft.com/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce)             |
| RECEIVED(settlement, maturity, investment, discount, [day_count_convention])                                 | [Bài viết về hàm Excel RECEIVED](https://support.microsoft.com/office/received-function-7a3f8b93-6611-4f81-8576-828312c9b5e5)     |
| RRI(number_of_periods, present_value, future_value)                                                          | [Bài viết về hàm Excel RRI](https://support.microsoft.com/office/rri-function-6f5822d8-7ef1-4233-944c-79e8172930f4)               |
| SLN(cost, salvage, life)                                                                                     | [Bài viết về hàm Excel SLN](https://support.microsoft.com/office/sln-function-cdb666e5-c1c6-40a7-806a-e695edc2f1c8)               |
| SYD(cost, salvage, life, period)                                                                             | [Bài viết về hàm Excel SYD](https://support.microsoft.com/office/syd-function-069f8106-b60b-4ca2-98e0-2a0f206bdb27)               |
| TBILLPRICE(settlement, maturity, discount)                                                                   | [Bài viết về hàm Excel TBILLPRICE](https://support.microsoft.com/office/tbillprice-function-eacca992-c29d-425a-9eb8-0513fe6035a2) |
| TBILLEQ(settlement, maturity, discount)                                                                      | [Bài viết về hàm Excel TBILLEQ](https://support.microsoft.com/office/tbilleq-function-2ab72d90-9b4d-4efe-9fc2-0f81f2c19c8c)       |
| TBILLYIELD(settlement, maturity, price)                                                                      | [Bài viết về hàm Excel TBILLYIELD](https://support.microsoft.com/office/tbillyield-function-6d381232-f4b0-4cd5-8e97-45b9c03468ba) |
| VDB(cost, salvage, life, start, end, [factor], [no_switch])                                                  | [Bài viết về hàm Excel VDB](https://support.microsoft.com/office/vdb-function-dde4e207-f3fa-488d-91d2-66d55e861d73)               |
| XIRR(cashflow_amounts, cashflow_dates, [rate_guess])                                                         | [Bài viết về hàm Excel XIRR](https://support.microsoft.com/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d)             |
| XNPV(discount, cashflow_amounts, cashflow_dates)                                                             | [Bài viết về hàm Excel XNPV](https://support.microsoft.com/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7)             |
| YIELD(settlement, maturity, rate, price, redemption, frequency, [day_count_convention])                      | [Bài viết về hàm Excel YIELD](https://support.microsoft.com/office/yield-function-f5f5ca43-c4bd-434f-8bd2-ed3c9727a4fe)           |
| YIELDDISC(settlement, maturity, price, redemption, [day_count_convention])                                   | [Bài viết về hàm Excel YIELDDISC](https://support.microsoft.com/office/yielddisc-function-a9dbdbae-7dae-46de-b995-615faffaaed7)   |
| YIELDMAT(settlement, maturity, issue, rate, price, [day_count_convention])                                   | [Bài viết về hàm Excel YIELDMAT](https://support.microsoft.com/office/yieldmat-function-ba7d1809-0d33-4bcb-96c7-6c56ec62ef6f)     |

<a id="functions-info"></a>

## Thông tin

| Tên và đối số    | Mô tả hoặc liên kết                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------|
| ISERR(value)     | [Bài viết về hàm Excel IS](https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665) |
| ISERROR(value)   | [Bài viết về hàm Excel IS](https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665) |
| ISLOGICAL(value) | [Bài viết về hàm Excel IS](https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665) |
| ISNA(value)      | [Bài viết về hàm Excel IS](https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665) |
| ISNONTEXT(value) | [Bài viết về hàm Excel IS](https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665) |
| ISNUMBER(value)  | [Bài viết về hàm Excel IS](https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665) |
| ISTEXT(value)    | [Bài viết về hàm Excel IS](https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665) |
| ISBLANK(value)   | [Bài viết về hàm Excel IS](https://support.microsoft.com/office/is-functions-0f2d7971-6019-40a0-a171-f2d869135665) |
| NA()             | [Bài viết về hàm Excel NA](https://support.microsoft.com/office/na-function-5469c2d1-a90c-4fb5-9bbc-64bd9bb6b47c)  |

<a id="functions-logical"></a>

## Logic

| Tên và đối số                                             | Mô tả hoặc liên kết                                                                                                         |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| AND(logical_expression1, [logical_expression2, ...])      | [Bài viết về hàm Excel AND](https://support.microsoft.com/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9)         |
| FALSE()                                                   | [Bài viết về hàm Excel FALSE](https://support.microsoft.com/office/false-function-2d58dfa5-9c03-4259-bf8f-f0ae14346904)     |
| IF(logical_expression, value_if_true, [value_if_false])   | [Bài viết về hàm Excel IF](https://support.microsoft.com/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)           |
| IFERROR(value, [value_if_error])                          | [Bài viết về hàm Excel IFERROR](https://support.microsoft.com/office/iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611) |
| IFNA(value, [value_if_error])                             | [Bài viết về hàm Excel IFNA](https://support.microsoft.com/office/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461)       |
| IFS(condition1, value1, [condition2, ...], [value2, ...]) | [Bài viết về hàm Excel IFS](https://support.microsoft.com/office/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45)         |
| NOT(logical_expression)                                   | [Bài viết về hàm Excel NOT](https://support.microsoft.com/office/not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77)         |
| OR(logical_expression1, [logical_expression2, ...])       | [Bài viết về hàm Excel OR](https://support.microsoft.com/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0)           |
| TRUE()                                                    | [Bài viết về hàm Excel TRUE](https://support.microsoft.com/office/true-function-7652c6e3-8987-48d0-97cd-ef223246b3fb)       |
| XOR(logical_expression1, [logical_expression2, ...])      | [Bài viết về hàm Excel XOR](https://support.microsoft.com/office/xor-function-1548d4c2-5e47-4f77-9a92-0533bba14f37)         |

<a id="functions-lookup"></a>

## Tìm kiếm

| Tên và đối số                                                                                | Mô tả hoặc liên kết                                                                                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ADDRESS(row, column, [absolute_relative_mode], [use_a1_notation], [sheet])                   | [Bài viết về hàm Excel ADDRESS](https://support.microsoft.com/office/address-function-d0c26c0d-3991-446b-8de4-ab46431d4f89) |
| COLUMN([cell_reference])                                                                     | [Bài viết về hàm Excel COLUMN](https://support.microsoft.com/office/column-function-44e8c754-711c-4df3-9da4-47a55042554b)   |
| COLUMNS(range)                                                                               | [Bài viết về hàm Excel COLUMNS](https://support.microsoft.com/office/columns-function-4e8e7b4e-e603-43e8-b177-956088fa48ca) |
| HLOOKUP(search_key, range, index, [is_sorted])                                               | [Bài viết về hàm Excel HLOOKUP](https://support.microsoft.com/office/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f) |
| INDEX(reference, row, column)                                                                | [Bài viết về hàm Excel INDEX](https://support.microsoft.com/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd)     |
| LOOKUP(search_key, search_array, [result_range])                                             | [Bài viết về hàm Excel LOOKUP](https://support.microsoft.com/office/lookup-function-446d94af-663b-451d-8251-369d5e3864cb)   |
| MATCH(search_key, range, [search_type])                                                      | [Bài viết về hàm Excel MATCH](https://support.microsoft.com/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a)     |
| ROW([cell_reference])                                                                        | [Bài viết về hàm Excel ROW](https://support.microsoft.com/office/row-function-3a63b74a-c4d0-4093-b49a-e76eb49a6d8d)         |
| ROWS(range)                                                                                  | [Bài viết về hàm Excel ROWS](https://support.microsoft.com/office/rows-function-b592593e-3fc2-47f2-bec1-bda493811597)       |
| VLOOKUP(search_key, range, index, [is_sorted])                                               | [Bài viết về hàm Excel VLOOKUP](https://support.microsoft.com/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1) |
| XLOOKUP(search_key, lookup_range, return_range, [if_not_found], [match_mode], [search_mode]) | [Bài viết về hàm Excel XLOOKUP](https://support.microsoft.com/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929) |

<a id="functions-math"></a>

## Toán

| Tên và đối số                                                                                 | Mô tả hoặc liên kết                                                                                                                         |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ABS(value)                                                                                    | [Bài viết về hàm Excel ABS](https://support.microsoft.com/office/abs-function-3420200f-5628-4e8c-99da-c99d7c87713c)                         |
| ACOS(value)                                                                                   | [Bài viết về hàm Excel ACOS](https://support.microsoft.com/office/acos-function-cb73173f-d089-4582-afa1-76e5524b5d5b)                       |
| ACOSH(value)                                                                                  | [Bài viết về hàm Excel ACOSH](https://support.microsoft.com/office/acosh-function-e3992cc1-103f-4e72-9f04-624b9ef5ebfe)                     |
| ACOT(value)                                                                                   | [Bài viết về hàm Excel ACOT](https://support.microsoft.com/office/acot-function-dc7e5008-fe6b-402e-bdd6-2eea8383d905)                       |
| ACOTH(value)                                                                                  | [Bài viết về hàm Excel ACOTH](https://support.microsoft.com/office/acoth-function-cc49480f-f684-4171-9fc5-73e4e852300f)                     |
| ASIN(value)                                                                                   | [Bài viết về hàm Excel ASIN](https://support.microsoft.com/office/asin-function-81fb95e5-6d6f-48c4-bc45-58f955c6d347)                       |
| ASINH(value)                                                                                  | [Bài viết về hàm Excel ASINH](https://support.microsoft.com/office/asinh-function-4e00475a-067a-43cf-926a-765b0249717c)                     |
| ATAN(value)                                                                                   | [Bài viết về hàm Excel ATAN](https://support.microsoft.com/office/atan-function-50746fa8-630a-406b-81d0-4a2aed395543)                       |
| ATAN2(x, y)                                                                                   | [Bài viết về hàm Excel ATAN2](https://support.microsoft.com/office/atan2-function-c04592ab-b9e3-4908-b428-c96b3a565033)                     |
| ATANH(value)                                                                                  | [Bài viết về hàm Excel ATANH](https://support.microsoft.com/office/atanh-function-3cd65768-0de7-4f1d-b312-d01c8c930d90)                     |
| CEILING(value, [factor])                                                                      | [Bài viết về hàm Excel CEILING](https://support.microsoft.com/office/ceiling-function-0a5cd7c8-0720-4f0a-bd2c-c943e510899f)                 |
| CEILING.MATH(number, [significance], [mode])                                                  | [Bài viết về hàm Excel CEILING.MATH](https://support.microsoft.com/office/ceiling-math-function-80f95d2f-b499-4eee-9f16-f795a8e306c8)       |
| CEILING.PRECISE(number, [significance])                                                       | [Bài viết về hàm Excel CEILING.PRECISE](https://support.microsoft.com/office/ceiling-precise-function-f366a774-527a-4c92-ba49-af0a196e66cb) |
| COS(angle)                                                                                    | [Bài viết về hàm Excel COS](https://support.microsoft.com/office/cos-function-0fb808a5-95d6-4553-8148-22aebdce5f05)                         |
| COSH(value)                                                                                   | [Bài viết về hàm Excel COSH](https://support.microsoft.com/office/cosh-function-e460d426-c471-43e8-9540-a57ff3b70555)                       |
| COT(angle)                                                                                    | [Bài viết về hàm Excel COT](https://support.microsoft.com/office/cot-function-c446f34d-6fe4-40dc-84f8-cf59e5f5e31a)                         |
| COTH(value)                                                                                   | [Bài viết về hàm Excel COTH](https://support.microsoft.com/office/coth-function-2e0b4cb6-0ba0-403e-aed4-deaa71b49df5)                       |
| COUNTBLANK(value1, [value2, ...])                                                             | [Bài viết về hàm Excel COUNTBLANK](https://support.microsoft.com/office/countblank-function-6a92d772-675c-4bee-b346-24af6bd3ac22)           |
| COUNTIF(range, criterion)                                                                     | [Bài viết về hàm Excel COUNTIF](https://support.microsoft.com/office/countif-function-e0de10c6-f885-4e71-abb4-1f464816df34)                 |
| COUNTIFS(criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])              | [Bài viết về hàm Excel COUNTIFS](https://support.microsoft.com/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842)               |
| COUNTUNIQUE(value1, [value2, ...])                                                            | Đếm số lượng giá trị duy nhất trong một dải ô (không tương thích với Excel)                                                                 |
| COUNTUNIQUEIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...]) | Đếm số giá trị duy nhất trong một dải ô, được lọc theo một bộ tiêu chí (không tương thích với Excel)                                        |
| CSC(angle)                                                                                    | [Bài viết về hàm Excel CSC](https://support.microsoft.com/office/csc-function-07379361-219a-4398-8675-07ddc4f135c1)                         |
| CSCH(value)                                                                                   | [Bài viết về hàm Excel CSCH](https://support.microsoft.com/office/csch-function-f58f2c22-eb75-4dd6-84f4-a503527f8eeb)                       |
| DECIMAL(value, base)                                                                          | [Bài viết về hàm Excel DECIMAL](https://support.microsoft.com/office/decimal-function-ee554665-6176-46ef-82de-0a283658da2e)                 |
| DEGREES(angle)                                                                                | [Bài viết về hàm Excel DEGREES](https://support.microsoft.com/office/degrees-function-4d6ec4db-e694-4b94-ace0-1cc3f61f9ba1)                 |
| EXP(value)                                                                                    | [Bài viết về hàm Excel EXP](https://support.microsoft.com/office/exp-function-c578f034-2c45-4c37-bc8c-329660a63abe)                         |
| FLOOR(value, [factor])                                                                        | [Bài viết về hàm Excel FLOOR](https://support.microsoft.com/office/floor-function-14bb497c-24f2-4e04-b327-b0b4de5a8886)                     |
| FLOOR.MATH(number, [significance], [mode])                                                    | [Bài viết về hàm Excel FLOOR.MATH](https://support.microsoft.com/office/floor-math-function-c302b599-fbdb-4177-ba19-2c2b1249a2f5)           |
| FLOOR.PRECISE(number, [significance])                                                         | [Bài viết về hàm Excel FLOOR.PRECISE](https://support.microsoft.com/office/floor-precise-function-f769b468-1452-4617-8dc3-02f842a0702e)     |
| INT(value)                                                                                    | [Bài viết về hàm Excel INT](https://support.microsoft.com/office/int-function-a6c4af9e-356d-4369-ab6a-cb1fd9d343ef)                         |
| ISEVEN(value)                                                                                 | [Bài viết về hàm Excel ISEVEN](https://support.microsoft.com/office/iseven-function-aa15929a-d77b-4fbb-92f4-2f479af55356)                   |
| ISO.CEILING(number, [significance])                                                           | [Bài viết về hàm Excel ISO.CEILING](https://support.microsoft.com/office/iso-ceiling-function-e587bb73-6cc2-4113-b664-ff5b09859a83)         |
| ISODD(value)                                                                                  | [Bài viết về hàm Excel ISODD](https://support.microsoft.com/office/isodd-function-1208a56d-4f10-4f44-a5fc-648cafd6c07a)                     |
| LN(value)                                                                                     | [Bài viết về hàm Excel LN](https://support.microsoft.com/office/ln-function-81fe1ed7-dac9-4acd-ba1d-07a142c6118f)                           |
| MOD(dividend, divisor)                                                                        | [Bài viết về hàm Excel MOD](https://support.microsoft.com/office/mod-function-9b6cd169-b6ee-406a-a97b-edf2a9dc24f3)                         |
| MUNIT(dimension)                                                                              | [Bài viết về hàm Excel MUNIT](https://support.microsoft.com/office/munit-function-c9fe916a-dc26-4105-997d-ba22799853a3)                     |
| ODD(value)                                                                                    | [Bài viết về hàm Excel ODD](https://support.microsoft.com/office/odd-function-deae64eb-e08a-4c88-8b40-6d0b42575c98)                         |
| PI()                                                                                          | [Bài viết về hàm Excel PI](https://support.microsoft.com/office/pi-function-264199d0-a3ba-46b8-975a-c4a04608989b)                           |
| POWER(base, exponent)                                                                         | [Bài viết về hàm Excel POWER](https://support.microsoft.com/office/power-function-d3f2908b-56f4-4c3f-895a-07fb519c362a)                     |
| PRODUCT(factor1, [factor2, ...])                                                              | [Bài viết về hàm Excel PRODUCT](https://support.microsoft.com/office/product-function-8e6b5b24-90ee-4650-aeec-80982a0512ce)                 |
| RAND()                                                                                        | [Bài viết về hàm Excel RAND](https://support.microsoft.com/office/rand-function-4cbfa695-8869-4788-8d90-021ea9f5be73)                       |
| RANDARRAY([rows], [columns], [min], [max], [whole_number])                                    | [Bài viết về hàm Excel RANDARRAY](https://support.microsoft.com/office/randarray-function-21261e55-3bec-4885-86a6-8b0a47fd4d33)             |
| RANDBETWEEN(low, high)                                                                        | [Bài viết về hàm Excel RANDBETWEEN](https://support.microsoft.com/office/randbetween-function-4cc7f0d1-87dc-4eb7-987f-a469ab381685)         |
| ROUND(value, [places])                                                                        | [Bài viết về hàm Excel ROUND](https://support.microsoft.com/office/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c)                     |
| ROUNDDOWN(value, [places])                                                                    | [Bài viết về hàm Excel ROUNDDOWN](https://support.microsoft.com/office/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53)             |
| ROUNDUP(value, [places])                                                                      | [Bài viết về hàm Excel ROUNDUP](https://support.microsoft.com/office/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7)                 |
| SEC(angle)                                                                                    | [Bài viết về hàm Excel SEC](https://support.microsoft.com/office/sec-function-ff224717-9c87-4170-9b58-d069ced6d5f7)                         |
| SECH(value)                                                                                   | [Bài viết về hàm Excel SECH](https://support.microsoft.com/office/sech-function-e05a789f-5ff7-4d7f-984a-5edb9b09556f)                       |
| SIN(angle)                                                                                    | [Bài viết về hàm Excel SIN](https://support.microsoft.com/office/sin-function-cf0e3432-8b9e-483c-bc55-a76651c95602)                         |
| SINH(value)                                                                                   | [Bài viết về hàm Excel SINH](https://support.microsoft.com/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7)                       |
| SQRT(value)                                                                                   | [Bài viết về hàm Excel SQRT](https://support.microsoft.com/office/sqrt-function-654975c2-05c4-4831-9a24-2c65e4040fdf)                       |
| SUM(value1, [value2, ...])                                                                    | [Bài viết về hàm Excel SUM](https://support.microsoft.com/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)                         |
| SUMIF(criteria_range, criterion, [sum_range])                                                 | [Bài viết về hàm Excel SUMIF](https://support.microsoft.com/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b)                     |
| SUMIFS(sum_range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])     | [Bài viết về hàm Excel SUMIFS](https://support.microsoft.com/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b)                   |
| TAN(angle)                                                                                    | [Bài viết về hàm Excel TAN](https://support.microsoft.com/office/tan-function-08851a40-179f-4052-b789-d7f699447401)                         |
| TANH(value)                                                                                   | [Bài viết về hàm Excel TANH](https://support.microsoft.com/office/tanh-function-017222f0-a0c3-4f69-9787-b3202295dc6c)                       |
| TRUNC(value, [places])                                                                        | [Bài viết về hàm Excel TRUNC](https://support.microsoft.com/office/trunc-function-8b86a64c-3127-43db-ba14-aa5ceb292721)                     |

<a id="functions-misc"></a>

## Thông tin khác

| Tên và đối số                      | Mô tả hoặc liên kết                                    |
|------------------------------------|--------------------------------------------------------|
| FORMAT.LARGE.NUMBER(value, [unit]) | Áp dụng định dạng số lớn (không tương thích với Excel) |

<a id="functions-odoo"></a>

## Odoo

| Tên và đối số                                                                       | Mô tả hoặc liên kết                                                                                                                                                     |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ODOO.CREDIT(account_codes, date_range, [offset], [company_id], [include_unposted])  | Lấy tổng có cho (các) tài khoản và kỳ xác định (không tương thích với Excel)                                                                                            |
| ODOO.DEBIT(account_codes, date_range, [offset], [company_id], [include_unposted])   | Lấy tổng nợ cho (các) tài khoản và kỳ xác định (không tương thích với Excel)                                                                                            |
| ODOO.BALANCE(account_codes, date_range, [offset], [company_id], [include_unposted]) | Lấy tổng số dư cho (các) tài khoản và kỳ xác định (không tương thích với Excel)                                                                                         |
| ODOO.FISCALYEAR.START(day, [company_id])                                            | Trả về ngày bắt đầu năm tài chính bao gồm ngày đã cho (không tương thích với Excel)                                                                                     |
| ODOO.FISCALYEAR.END(day, [company_id])                                              | Trả về ngày kết thúc năm tài chính bao gồm ngày đã cho (không tương thích với Excel)                                                                                    |
| ODOO.ACCOUNT.GROUP(type)                                                            | Trả về ID tài khoản của một nhóm nhất định (không tương thích với Excel)                                                                                                |
| ODOO.CURRENCY.RATE(currency_from, currency_to, [date])                              | Hàm này lấy hai mã tiền tệ làm đối số và trả về tỷ giá hối đoái chuyển đổi từ loại tiền đầu tiên sang loại tiền thứ hai dưới dạng thả nổi (không tương thích với Excel) |
| ODOO.LIST(list_id, index, field_name)                                               | Lấy giá trị từ một danh sách (không tương thích với Excel)                                                                                                              |
| ODOO.LIST.HEADER(list_id, field_name)                                               | Lấy header của một danh sách (không tương thích với Excel)                                                                                                              |
| ODOO.FILTER.VALUE(filter_name)                                                      | Trả về giá trị hiện tại của bộ lọc bảng tính (không tương thích với Excel)                                                                                              |
| ODOO.PIVOT(pivot_id, measure_name, [domain_field_name, ...], [domain_value, ...])   | Lấy giá trị từ một pivot (không tương thích với Excel)                                                                                                                  |
| ODOO.PIVOT.HEADER(pivot_id, [domain_field_name, ...], [domain_value, ...])          | Lấy header của một pivot (không tương thích với Excel)                                                                                                                  |
| ODOO.PIVOT.TABLE(pivot_id, [row_count], [include_total], [include_column_titles])   | Lấy bảng pivot (không tương thích với Excel)                                                                                                                            |

<a id="functions-operators"></a>

## Người đại diện

| Tên và đối số              | Mô tả hoặc liên kết                                                                                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ADD(value1, value2)        | Tổng của hai số (không tương thích với Excel)                                                                             |
| CONCAT(value1, value2)     | [Bài viết về hàm Excel CONCAT](https://support.microsoft.com/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2) |
| DIVIDE(dividend, divisor)  | Một số bị chia cho một số khác (không tương thích với Excel)                                                              |
| EQ(value1, value2)         | Bằng (không tương thích với Excel)                                                                                        |
| GT(value1, value2)         | Tuyệt đối lớn hơn (không tương thích với Excel)                                                                           |
| GTE(value1, value2)        | Lớn hơn hoặc bằng (không tương thích với Excel)                                                                           |
| LT(value1, value2)         | Nhỏ hơn (không tương thích với Excel)                                                                                     |
| LTE(value1, value2)        | Nhỏ hơn hoặc bằng (không tương thích với Excel)                                                                           |
| MINUS(value1, value2)      | Hiệu của hai số (không tương thích với Excel)                                                                             |
| MULTIPLY(factor1, factor2) | Tích của hai số (không tương thích với Excel)                                                                             |
| NE(value1, value2)         | Không bằng (không tương thích với Excel)                                                                                  |
| POW(base, exponent)        | Một số được nâng lên lũy thừa (không tương thích với Excel)                                                               |
| UMINUS(value)              | Một số có dấu bị đảo ngược (không tương thích với Excel)                                                                  |
| UNARY.PERCENT(percentage)  | Giá trị được diễn giải theo phần trăm (không tương thích với Excel)                                                       |
| UPLUS(value)               | Một số cụ thể, không thay đổi (không tương thích với Excel)                                                               |

<a id="functions-statistical"></a>

## Thống kê

| Tên và đối số                                                                                     | Mô tả hoặc liên kết                                                                                                                                |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| AVEDEV(value1, [value2, ...])                                                                     | [Bài viết về hàm Excel AVEDEV](https://support.microsoft.com/office/avedev-function-58fe8d65-2a84-4dc7-8052-f3f87b5c6639)                          |
| AVERAGE(value1, [value2, ...])                                                                    | [Bài viết về hàm Excel AVERAGE](https://support.microsoft.com/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6)                        |
| AVERAGE.WEIGHTED(values, weights, [additional_values, ...], [additional_weights, ...])            | Bình quân gia quyền (không tương thích với Excel)                                                                                                  |
| AVERAGEA(value1, [value2, ...])                                                                   | [Bài viết về hàm Excel AVERAGEA](https://support.microsoft.com/office/averagea-function-f5f84098-d453-4f4c-bbba-3d2c66356091)                      |
| AVERAGEIF(criteria_range, criterion, [average_range])                                             | [Bài viết về hàm Excel AVERAGEIF](https://support.microsoft.com/office/averageif-function-faec8e2e-0dec-4308-af69-f5576d8ac642)                    |
| AVERAGEIFS(average_range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...]) | [Bài viết về hàm Excel AVERAGEIFS](https://support.microsoft.com/office/averageifs-function-48910c45-1fc0-4389-a028-f7c5c3001690)                  |
| CORREL(data_y, data_x)                                                                            | [Bài viết về hàm Excel CORREL](https://support.microsoft.com/office/correl-function-995dcef7-0c0a-4bed-a3fb-239d7b68ca92)                          |
| COUNT(value1, [value2, ...])                                                                      | [Bài viết về hàm Excel COUNT](https://support.microsoft.com/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c)                            |
| COUNTA(value1, [value2, ...])                                                                     | [Bài viết về hàm Excel COUNTA](https://support.microsoft.com/office/counta-function-7dc98875-d5c1-46f1-9a82-53f3219e2509)                          |
| COVAR(data_y, data_x)                                                                             | [Bài viết về hàm Excel COVAR](https://support.microsoft.com/office/covar-function-50479552-2c03-4daf-bd71-a5ab88b2db03)                            |
| COVARIANCE.P(data_y, data_x)                                                                      | [Bài viết về hàm Excel COVARIANCE.P](https://support.microsoft.com/office/covariance-p-function-6f0e1e6d-956d-4e4b-9943-cfef0bf9edfc)              |
| COVARIANCE.S(data_y, data_x)                                                                      | [Bài viết về hàm Excel COVARIANCE.S](https://support.microsoft.com/office/covariance-s-function-0a539b74-7371-42aa-a18f-1f5320314977)              |
| FORECAST(x, data_y, data_x)                                                                       | [Bài viết về hàm Excel FORECAST](https://support.microsoft.com/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99) |
| GROWTH(known_data_y, [known_data_x], [new_data_x], [b])                                           | Khớp dữ liệu với một xu hướng tăng trưởng lũy thừa lý tưởng (không tương thích với Excel)                                                          |
| INTERCEPT(data_y, data_x)                                                                         | [Bài viết về hàm Excel INTERCEPT](https://support.microsoft.com/office/intercept-function-2a9b74e2-9d47-4772-b663-3bca70bf63ef)                    |
| LARGE(data, n)                                                                                    | [Bài viết về hàm Excel LARGE](https://support.microsoft.com/office/large-function-3af0af19-1190-42bb-bb8b-01672ec00a64)                            |
| LINEST(data_y, [data_x], [calculate_b], [verbose])                                                | [Bài viết về hàm Excel LINEST](https://support.microsoft.com/office/linest-function-84d7d0d9-6e50-4101-977a-fa7abf772b6d)                          |
| LOGEST(data_y, [data_x], [calculate_b], [verbose])                                                | [Bài viết về hàm Excel LOGEST](https://support.microsoft.com/office/logest-function-f27462d8-3657-4030-866b-a272c1d18b4b)                          |
| MATTHEWS(data_x, data_y)                                                                          | Tính hệ số tương quan Matthews của tập dữ liệu (không tương thích với Excel)                                                                       |
| MAX(value1, [value2, ...])                                                                        | [Bài viết về hàm Excel MAX](https://support.microsoft.com/office/max-function-e0012414-9ac8-4b34-9a47-73e662c08098)                                |
| MAXA(value1, [value2, ...])                                                                       | [Bài viết về hàm Excel MAXA](https://support.microsoft.com/office/maxa-function-814bda1e-3840-4bff-9365-2f59ac2ee62d)                              |
| MAXIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])             | [Bài viết về hàm Excel MAXIFS](https://support.microsoft.com/office/maxifs-function-dfd611e6-da2c-488a-919b-9b6376b28883)                          |
| MEDIAN(value1, [value2, ...])                                                                     | [Bài viết về hàm Excel MEDIAN](https://support.microsoft.com/office/median-function-d0916313-4753-414c-8537-ce85bdd967d2)                          |
| MIN(value1, [value2, ...])                                                                        | [Bài viết về hàm Excel MIN](https://support.microsoft.com/office/min-function-61635d12-920f-4ce2-a70f-96f202dcc152)                                |
| MINA(value1, [value2, ...])                                                                       | [Bài viết về hàm Excel MINA](https://support.microsoft.com/office/mina-function-245a6f46-7ca5-4dc7-ab49-805341bc31d3)                              |
| MINIFS(range, criteria_range1, criterion1, [criteria_range2, ...], [criterion2, ...])             | [Bài viết về hàm Excel MINIFS](https://support.microsoft.com/office/minifs-function-6ca1ddaa-079b-4e74-80cc-72eef32e6599)                          |
| PEARSON(data_y, data_x)                                                                           | [Bài viết về hàm Excel PEARSON](https://support.microsoft.com/office/pearson-function-0c3e30fc-e5af-49c4-808a-3ef66e034c18)                        |
| PERCENTILE(data, percentile)                                                                      | [Bài viết về hàm Excel PERCENTILE](https://support.microsoft.com/office/percentile-exc-function-bbaa7204-e9e1-4010-85bf-c31dc5dce4ba)              |
| PERCENTILE.EXC(data, percentile)                                                                  | [Bài viết về hàm Excel PERCENTILE.EXC](https://support.microsoft.com/office/percentrank-exc-function-d8afee96-b7e2-4a2f-8c01-8fcdedaa6314)         |
| PERCENTILE.INC(data, percentile)                                                                  | [Bài viết về hàm Excel PERCENTILE.INC](https://support.microsoft.com/office/percentile-inc-function-680f9539-45eb-410b-9a5e-c1355e5fe2ed)          |
| POLYFIT.COEFFS(data_y, data_x, order, [intercept])                                                | Tính hệ số hồi quy đa thức của tập dữ liệu (không tương thích với Excel)                                                                           |
| POLYFIT.FORECAST(x, data_y, data_x, order, [intercept])                                           | Dự đoán giá trị bằng cách tính toán hồi quy đa thức của tập dữ liệu (không tương thích với Excel)                                                  |
| QUARTILE(data, quartile_number)                                                                   | [Bài viết về hàm Excel QUARTILE](https://support.microsoft.com/office/quartile-function-93cf8f62-60cd-4fdb-8a92-8451041e1a2a)                      |
| QUARTILE.EXC(data, quartile_number)                                                               | [Bài viết về hàm Excel QUARTILE.EXC](https://support.microsoft.com/office/quartile-exc-function-5a355b7a-840b-4a01-b0f1-f538c2864cad)              |
| QUARTILE.INC(data, quartile_number)                                                               | [Bài viết về hàm Excel QUARTILE.INC](https://support.microsoft.com/office/quartile-inc-function-1bbacc80-5075-42f1-aed6-47d735c4819d)              |
| RANK(value, data, [is_ascending])                                                                 | [Bài viết về hàm Excel RANK](https://support.microsoft.com/office/rank-function-6a2fc49d-1831-4a03-9d8c-c279cf99f723)                              |
| RSQ(data_y, data_x)                                                                               | [Bài viết về hàm Excel RSQ](https://support.microsoft.com/office/rsq-function-d7161715-250d-4a01-b80d-a8364f2be08f)                                |
| SMALL(data, n)                                                                                    | [Bài viết về hàm Excel SMALL](https://support.microsoft.com/office/small-function-17da8222-7c82-42b2-961b-14c45384df07)                            |
| SLOPE(data_y, data_x)                                                                             | [Bài viết về hàm Excel SLOPE](https://support.microsoft.com/office/slope-function-11fb8f97-3117-4813-98aa-61d7e01276b9)                            |
| SPEARMAN(data_y, data_x)                                                                          | Tính hệ số tương quan xếp hạng Spearman của tập dữ liệu (không tương thích với Excel)                                                              |
| STDEV(value1, [value2, ...])                                                                      | [Bài viết về hàm Excel STDEV](https://support.microsoft.com/office/stdev-function-51fecaaa-231e-4bbb-9230-33650a72c9b0)                            |
| STDEV.P(value1, [value2, ...])                                                                    | [Bài viết về hàm Excel STDEV.P](https://support.microsoft.com/office/stdev-p-function-6e917c05-31a0-496f-ade7-4f4e7462f285)                        |
| STDEV.S(value1, [value2, ...])                                                                    | [Bài viết về hàm Excel STDEV.S](https://support.microsoft.com/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23)                        |
| STDEVA(value1, [value2, ...])                                                                     | [Bài viết về hàm Excel STDEVA](https://support.microsoft.com/office/stdeva-function-5ff38888-7ea5-48de-9a6d-11ed73b29e9d)                          |
| STDEVP(value1, [value2, ...])                                                                     | [Bài viết về hàm Excel STDEVP](https://support.microsoft.com/office/stdevp-function-1f7c1c88-1bec-4422-8242-e9f7dc8bb195)                          |
| STDEVPA(value1, [value2, ...])                                                                    | [Bài viết về hàm Excel STDEVPA](https://support.microsoft.com/office/stdevpa-function-5578d4d6-455a-4308-9991-d405afe2c28c)                        |
| STEYX(data_y, data_x)                                                                             | [Bài viết về hàm Excel STEYX](https://support.microsoft.com/office/steyx-function-6ce74b2c-449d-4a6e-b9ac-f9cef5ba48ab)                            |
| TREND(known_data_y, [known_data_x], [new_data_x], [b])                                            | Điểm khớp với xu hướng tuyến tính xuất phát từ bình phương nhỏ nhất (không tương thích với Excel)                                                  |
| VAR(value1, [value2, ...])                                                                        | [Bài viết về hàm Excel VAR](https://support.microsoft.com/office/var-function-1f2b7ab2-954d-4e17-ba2c-9e58b15a7da2)                                |
| VAR.P(value1, [value2, ...])                                                                      | [Bài viết về hàm Excel VAR.P](https://support.microsoft.com/office/var-p-function-73d1285c-108c-4843-ba5d-a51f90656f3a)                            |
| VAR.S(value1, [value2, ...])                                                                      | [Bài viết về hàm Excel VAR.S](https://support.microsoft.com/office/var-s-function-913633de-136b-449d-813e-65a00b2b990b)                            |
| VARA(value1, [value2, ...])                                                                       | [Bài viết về hàm Excel VARA](https://support.microsoft.com/office/vara-function-3de77469-fa3a-47b4-85fd-81758a1e1d07)                              |
| VARP(value1, [value2, ...])                                                                       | [Bài viết về hàm Excel VARP](https://support.microsoft.com/office/varp-function-26a541c4-ecee-464d-a731-bd4c575b1a6b)                              |
| VARPA(value1, [value2, ...])                                                                      | [Bài viết về hàm Excel VARPA](https://support.microsoft.com/office/varpa-function-59a62635-4e89-4fad-88ac-ce4dc0513b96)                            |

<a id="functions-text"></a>

## Văn bản

| Tên và đối số                                                             | Mô tả hoặc liên kết                                                                                                                   |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| CHAR(table_number)                                                        | [Bài viết về hàm Excel CHAR](https://support.microsoft.com/office/char-function-bbd249c8-b36e-4a91-8017-1c133f9b837a)                 |
| CLEAN(text)                                                               | [Bài viết về hàm Excel CLEAN](https://support.microsoft.com/office/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba41)               |
| CONCATENATE(string1, [string2, ...])                                      | [Bài viết về hàm Excel CONCATENATE](https://support.microsoft.com/office/concatenate-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d)   |
| EXACT(string1, string2)                                                   | [Bài viết về hàm Excel EXACT](https://support.microsoft.com/office/exact-function-d3087698-fc15-4a15-9631-12575cf29926)               |
| FIND(search_for, text_to_search, [starting_at])                           | [Bài viết về hàm Excel FIND](https://support.microsoft.com/office/find-findb-functions-c7912941-af2a-4bdf-a553-d0d89b0a0628)          |
| JOIN(delimiter, value_or_array1, [value_or_array2, ...])                  | Nối các phần tử của mảng bằng dấu phân cách (không tương thích với Excel)                                                             |
| LEFT(text, [number_of_characters])                                        | [Bài viết về hàm Excel LEFT](https://support.microsoft.com/office/left-leftb-functions-9203d2d2-7960-479b-84c6-1ea52b99640c)          |
| LEN(text)                                                                 | [Bài viết về hàm Excel LEN](https://support.microsoft.com/office/len-lenb-functions-29236f94-cedc-429d-affd-b5e33d2c67cb)             |
| LOWER(text)                                                               | [Bài viết về hàm Excel LOWER](https://support.microsoft.com/office/lower-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4)               |
| MID(text, starting_at, extract_length)                                    | [Bài viết về hàm Excel MID](https://support.microsoft.com/office/mid-midb-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028)             |
| PROPER(text_to_capitalize)                                                | [Bài viết về hàm Excel PROPER](https://support.microsoft.com/office/proper-function-52a5a283-e8b2-49be-8506-b2887b889f94)             |
| REPLACE(text, position, length, new_text)                                 | [Bài viết về hàm Excel REPLACE](https://support.microsoft.com/office/replace-replaceb-functions-8d799074-2425-4a8a-84bc-82472868878a) |
| RIGHT(text, [number_of_characters])                                       | [Bài viết về hàm Excel RIGHT](https://support.microsoft.com/office/right-rightb-functions-240267ee-9afa-4639-a02b-f19e1786cf2f)       |
| SEARCH(search_for, text_to_search, [starting_at])                         | [Bài viết về hàm Excel SEARCH](https://support.microsoft.com/office/search-searchb-functions-9ab04538-0e55-4719-a72e-b6f54513b495)    |
| SPLIT(text, delimiter, [split_by_each], [remove_empty_text])              | [Bài viết về hàm Excel TEXTSPLIT](https://support.microsoft.com/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7)       |
| SUBSTITUTE(text_to_search, search_for, replace_with, [occurrence_number]) | [Bài viết về hàm Excel SUBSTITUTE](https://support.microsoft.com/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332)     |
| TEXT(number, format)                                                      | [Bài viết về hàm Excel TEXT](https://support.microsoft.com/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c)                 |
| TEXTJOIN(delimiter, ignore_empty, text1, [text2, ...])                    | [Bài viết về hàm Excel TEXTJOIN](https://support.microsoft.com/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c)         |
| TRIM(text)                                                                | [Bài viết về hàm Excel TRIM](https://support.microsoft.com/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9)                 |
| UPPER(text)                                                               | [Bài viết về hàm Excel UPPER](https://support.microsoft.com/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6)               |

<a id="functions-web"></a>

## Web

| Tên và đối số                | Mô tả hoặc liên kết                                                                                                             |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| HYPERLINK(url, [link_label]) | [Bài viết về hàm Excel HYPERLINK](https://support.microsoft.com/office/hyperlink-function-333c7ce6-c5ae-4164-9c47-7de9b76f577f) |
