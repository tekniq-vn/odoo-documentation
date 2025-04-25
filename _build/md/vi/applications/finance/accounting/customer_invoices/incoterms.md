# Incoterm

 là những điều khoản thương mại chuẩn được sử dụng trong các giao dịch quốc tế để xác định quyền và trách nhiệm của người mua và người bán. Chúng thiết lập các nghĩa vụ liên quan đến việc giao hàng, chuyển giao rủi ro và phân phối chi phí giữa các bên liên quan. Incoterm chỉ rõ những chi tiết quan trọng, chẳng hạn như thời điểm rủi ro và chi phí chuyển từ người bán sang người mua, trách nhiệm vận chuyển, bảo hiểm, thủ tục hải quan và các khía cạnh liên quan khác của giao dịch.

#### NOTE
By default, all 11 Incoterms are available in Odoo:

- **EXW**: Giao hàng tại xưởng
- **FCA**: Giao cho người chuyển chở
- **FAS**: Free alongside ship
- **FOB**: Free on board
- **CFR**: Cost and freight
- **CIF**: Cost, insurance and freight
- **CPT**: Carriage paid to
- **CIP**: Carriage and insurance paid to
- **DPU**: Delivered at place unloaded
- **DAP**: Delivered at place
- **DDP**: Delivered duty paid

#### SEE ALSO
- [Intrastat](../reporting/intrastat.md)
- [Hóa đơn bán hàng](./)
- [Vendor bills](../vendor_bills/)

<a id="incoterms-invoices"></a>

## Chỉ định Incoterm

To define an Incoterm manually, create an invoice or bill, click the Other Info tab, and
select the Incoterm.

### địa điểm Incoterm

A location relevant to the chosen Incoterm can be added to the invoice or bill under
Other Info in the Incoterm Location field.

<a id="incoterms-default"></a>

## Cấu hình Incoterm mặc định

You can set a default Incoterm rule to **automatically** populate the Incoterm field on all newly
created invoices and bills. Under Accounting/Invoicing ‣ Configuration ‣
Settings, scroll down to the Customer Invoices section, and select an Incoterm in the
Default Incoterm field.
