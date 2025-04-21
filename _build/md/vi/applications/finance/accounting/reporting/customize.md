# Custom reports

Odoo comes with a powerful and easy-to-use reporting framework. The engine allows you to create new
reports, such as **tax reports**, or **balance sheets** and **income statements** with **specific
groupings** and **layouts**.

#### IMPORTANT
Activate the [developer mode](../../../general/developer_mode.md#developer-mode) to access the accounting report creation
interface.

To create a new report, go to Accounting ‣ Configuration ‣ Management:
Accounting Reports. From here, you can either create a [root report](#customize-reports-root)
or a [variant](#customize-reports-variants).

![Accounting reports engine.](applications/finance/accounting/reporting/customize/engine-accounting-reports.png)

<a id="customize-reports-root"></a>

## Root reports

Root reports can be regarded as generic, neutral accounting reports. They serve as models on which
local accounting versions are built. If a report has no root report, it is considered to be a root
report itself.

When creating a new root report, you need to create a **menu item** for it. To do so, open the
report and then, on that same report, click on Action ‣ Create Menu Item. Refresh
the page; the report is now available under Accounting ‣ Reporting.

#### NOTE
Cases that require creating a new root report are rare, such as when a country's tax authorities
require a new and specific type of report.

![Create Menu Item button.](applications/finance/accounting/reporting/customize/engine-create-menu-item.png)

<a id="customize-reports-variants"></a>

## Biến thể

Variants are country-specific versions of root reports and, therefore, always refer to a root
report. To create a variant, select a generic (root) report in the Root Report field
when creating a new report.

When a root report is opened from one of the accounting app's main menus, all its variants are
displayed in the variant selector in the top right corner of the view.

## Chi tiết

Sau khi tạo báo cáo (dạng gốc hoặc biến thể), bạn cần thêm các dòng vào báo cáo. Bạn có thể tạo dòng mới bằng cách nhấp Thêm dòng, hoặc chỉnh sửa dòng hiện có bằng cách nhấp vào nó. Tất cả dòng *bắt buộc* phải có Tên, và có thể thêm Mã tùy chọn (tự chọn) nếu muốn sử dụng giá trị của chúng trong công thức.

![Engine lines options.](applications/finance/accounting/reporting/customize/engine-lines-options.png)

## Biểu thức

Each line can contain one or multiple **expressions**. Expressions can be seen as **sub-variables**
needed by a report line. To create an expression, click on Add a line *within* a line
report.

Khi tạo biểu thức, bạn phải gán một nhãn dùng để tham chiếu đến biểu thức đó. Do đó, nhãn này phải là **duy nhất** trong số các biểu thức của mỗi dòng. Bạn cũng cần chỉ định cả Công cụ tính toán và Công thức. **Công cụ** xác định cách **(các) công thức** và **(các) công thức phụ** được diễn giải. Bạn có thể kết hợp các biểu thức sử dụng công cụ tính toán khác nhau trong cùng một dòng nếu cần.

#### NOTE
Depending on the engine, subformulas may also be required.

### 'Odoo Domain' engine

With this engine, a formula is interpreted as an [Odoo domain](../../../../developer/reference/backend/orm.md#reference-orm-domains)
targeting `account.move.line` objects.

The subformula allows you to define how the move lines matching the domain are used to compute the
value of the expression:

`sum`
: The result is the sum of all the balances of the matched move lines.

`sum_if_pos`
: The result is the sum of all the balances of the matched move lines if this amount is positive.
  Otherwise, it is `0`.

`sum_if_neg`
: The result is the sum of all the balances of the matched move lines if this amount is negative.
  Otherwise, it is `0`.

`count_rows`
: The result is the number of sub-lines of this expression. If the parent line has a group-by
  value, this will correspond to the number of distinct grouping keys in the matched move lines.
  Otherwise, it will be the number of matched move lines.

You can also put a `-` sign at the beginning of the subformula to **reverse** the sign of the
result.

![Expression line within a line report](applications/finance/accounting/reporting/customize/engine-expressions.png)

### 'Tax Tags' engine

A formula made for this engine consists of a name used to match tax tags. If such tags do not exist
when creating the expression, they will be created.

When evaluating the expression, the expression computation can roughly be expressed as: **(amount of
the move lines with** `+` **tag)** `-` **(amount of the move lines with** `-` **tag)**.

### 'Aggregate Other Formulas' engine

Sử dụng công cụ này khi cần thực hiện các phép toán số học trên những giá trị thu được từ các biểu thức khác. Công thức ở đây bao gồm các tham chiếu đến biểu thức, được phân tách bởi một trong bốn toán tử số học cơ bản (cộng `+`, trừ `-`, chia `/`, và nhân `*`). Để tham chiếu đến một biểu thức, nhập **mã** của dòng chính, sau đó là dấu chấm `.` và **nhãn** của biểu thức (VD: **code.label**).

**Subformulas** can be one of the following:

`if_above(CUR(amount))`
: The value of the arithmetic expression will be returned only if it is greater than the provided
  bound. Otherwise, the result will be `0`.

`if_below(CUR(amount))`
: The value of the arithmetic expression will be returned only if it is lower than the provided
  bound. Otherwise, the result will be `0`.

`if_between(CUR1(amount1), CUR2(amount2))`
: The value of the arithmetic expression will be returned only if it is strictly between the
  provided bounds. Otherwise, it will be brought back to the closest bound.

`if_other_expr_above(LINE_CODE.EXPRESSION_LABEL, CUR(amount))`
: The value of the arithmetic expression will be returned only if the value of the expression
  denoted by the provided line code and expression label is greater than the provided bound.
  Otherwise, the result will be `0`.

`if_other_expr_below(LINE_CODE.EXPRESSION_LABEL, CUR(amount))`
: The value of the arithmetic expression will be returned only if the value of the expression
  denoted by the provided line code and expression label is lower than the provided bound.
  Otherwise, the result will be `0`.

`CUR` is the currency code in capital letters, and `amount` is the amount of the bound expressed in
that currency.

You can also use the `cross_report` subformula to match an expression found in another report.

### 'Prefix of Account Codes' engine

This engine is used to match amounts made on accounts using the prefixes of these accounts' codes as
variables in an arithmetic expression.

It is also possible to ignore a selection of sub-prefixes.

You can apply 'sub-filtering' on **credits and debits** using the `C` and `D` suffixes. In this
case, an account will only be considered if its prefix matches, *and* if the total balance of the
move lines made on this account is **credit/debit**.

Prefix exclusions can be mixed with the `C` and `D` suffixes.

To match the letter `C` or `D` in a prefix and not use it as a suffix, use an empty exclusion `()`.

In addition to using code prefixes to include accounts, you can also match them with **account
tags**. This is especially useful, for example, if your country lacks a standardized chart of
accounts, where the same prefix might be used for different purposes across companies.

If the tag you reference is defined in a data file, an xmlid can be used instead of the id.

You can also use arithmetic expressions with tags, possibly combining them with prefix selections.

`C` and `D` suffixes can be used in the same way with tags.

Prefix exclusion also works with tags.

### 'External Value' engine

The 'external value' engine is used to refer to **manual** and **carryover values**. Those values
are not stored using `account.move.line`, but with `account.report.external.value`. Each of these
objects directly points to the expression it impacts, so very little needs to be done about their
selection here.

**Formulas** can be one of the following:

`sum`
: If the result must be the sum of all the external values in the period.

`most_recent`
: If the result must be the value of the latest external value in the period.

In addition, **subformulas** can be used in two ways:

`rounding=X`
: Replacing `X` with a number instructs to round the amount to X decimals.

`có thể chỉnh sửa`
: Indicates this expression can be edited manually, triggering the display of an icon in the
  report, allowing the user to perform this action.

#### NOTE
Manual values are created at the `date_to` currently selected in the report.

Both subformulas can be mixed by separating them with a `;`.

### 'Custom Python Function' engine

This engine is a means for developers to introduce custom computation of expressions on a
case-by-case basis. The formula is the name of a **python function** to call, and the subformula is
a **key** to fetch in the **dictionary** returned by this function. Use it only if you are making a
custom module of your own.

## Cột

Báo cáo có thể có **số lượng cột không giới hạn** để hiển thị. Mỗi cột nhận giá trị từ các **biểu thức** được khai báo trên **dòng**. Trường expression_label của cột cung cấp nhãn cho các biểu thức có giá trị được hiển thị. Nếu một dòng không có **biểu thức** trong trường đó, thì không có gì được hiển thị cho nó trong cột này. Nếu cần nhiều cột, bạn phải sử dụng các nhãn **biểu thức** khác nhau.

![Columns of report.](applications/finance/accounting/reporting/customize/engine-columns.png)

When using the **period comparison** feature found under the Options tab of an
accounting report, all columns are repeated in and for each period.
