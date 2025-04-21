# Salary attachment report

*Salary attachments* in Odoo refer to a portion of an employee's earnings that are designated for
a specific purpose, both voluntary and involuntary. These can include contributions to a retirement
plan, repayment of a loan, wage garnishments, or child support.

Các khoản khấu trừ lương tự nguyện, chẳng hạn như trả nợ vay hoặc đóng góp từ thiện hàng tháng, được xem là *Chuyển nhượng lương* trong Odoo. Các khoản khấu trừ lương bắt buộc, như thanh toán theo phán quyết của tòa án hoặc trả nợ thuế, được xem là *Khấu trừ lương* trong Odoo. Các khoản thanh toán trợ cấp nuôi con có một danh mục riêng và được gọi đơn giản là *Trợ cấp nuôi con* trong Odoo.

Để xem báo cáo này, đi đến Ứng dụng Bảng lương ‣ Báo cáo ‣ Báo cáo Khấu trừ lương. Báo cáo khấu trừ lương hiển thị tất cả các khoản khấu trừ hoặc phân bổ theo từng nhân viên, được sắp xếp theo phiếu lương trong một bảng pivot mặc định. Bộ lọc mặc định là cuối năm hiện tại (Ngày kết thúc phiếu lương: (năm)). Các nhân viên được hiển thị theo hàng, trong khi các khoản khấu trừ khác nhau được hiển thị theo cột, sắp xếp theo loại khấu trừ và được nhóm thêm theo từng phiếu lương riêng lẻ.

The default report contains **all** payslips for the current year, so the report typically contains
a large number of columns. This could make it difficult to view all the data at once, as the report
may be very wide and require scrolling to view all the data.

To view a condensed version of salary attachments, and have all the salary attachment columns
visible on one page, click the <i class="fa fa-minus-square-o"></i> Total icon at the top of the
report, above the various payslips.

This presents the salary attachments for the current year, and only displays three columns,
Attachment of Salary, Assignment of Salary, and Child Support.

Each entry displays the total amount paid for each specific type of salary attachment, for each
employee.

![The Attachment of Salary report that shows all salary garnishments in a condensed view.](applications/hr/payroll/salary_attachment/salary-attachment.png)

The report can be downloaded as an XLSX file, or [inserted into a spreadsheet](../../productivity/spreadsheet/insert.md) using the corresponding buttons at the top.

Click the Measures button to reveal the options of what data is displayed.
Assignment of salary, Attachment of salary, and Child support
are all selected and visible, by default, while the Count option is not.

Click an option to either show or hide that particular metric. A <i class="fa fa-check"></i>
(checkmark) icon indicates the data is visible.

## Compare to previous year

The Salary Attachment Report can be compared to the report for the previous time period
or the previous year.

To view these comparisons, click the <i class="fa fa-caret-down"></i> (down arrow) icon in the
search bar, then click either Payslip End Date: Previous Period or Payslip
End Date: Previous Year, beneath the <i class="fa fa-adjust"></i> Comparison column.

The report updates and displays the current time period values, and the previous time period values,
as well as the Variation between the two, in a percentage.

![The salary attachment report modified to compare to the previous year.](applications/hr/payroll/salary_attachment/comparison-attachment.png)
