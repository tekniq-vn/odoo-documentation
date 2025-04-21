# Đa công ty

In Odoo, multiple companies can exist within a single database. This allows for some data to be
shared among companies, while still maintaining some level of separation between entities.

Before deciding to use the multi-company feature, there are several factors to consider.

#### IMPORTANT
Multi-company is **only** available in *One App Free* databases, or with [Custom](https://www.odoo.com/pricing-plan) plans.

## Accessing multiple companies

Danh sách [các công ty mà nhân viên có quyền truy cập](companies.md#general-employee-access) trong multi-company database có thể được tìm thấy ở góc trên bên phải của thanh menu chính của Odoo, nơi liệt kê những công ty đang hoạt động. Nhấp vào tên công ty để hiển thị danh sách tất cả công ty được phép. Để chuyển sang một công ty khác, hãy nhấp vào tên công ty trong menu thả xuống. Để bật nhiều công ty cùng một lúc, hãy đánh dấu vào hộp kiểm bên cạnh mỗi tên công ty mong muốn.

![An example of the list of companies a user has access to when logged into a database.](applications/general/multi_company/company-access.png)

#### NOTE
The database may refresh after each checkbox is ticked.

<a id="general-active-companies"></a>

### Multiple active companies

If more than one company is active at a time, one company is highlighted in purple, and is listed on
the menu bar. This is the considered the *current* company.

When creating a new record, the current company is added to the record in the *Company* field,
except under the following circumstances:

- The *Company* field for a new product, or a new contact, is left blank.
- If there is a related document already in the system, the *Company* field on the new record
  defaults to the same company.

<a id="general-sharing-data"></a>

## Chia sẻ dữ liệu

In a multi-company database, certain records are able to be utilized by all of the companies (or several, based on
permissions).

### Sản phẩm

In an multi-company database, new products are created with the [Company field](#general-active-companies)
blank, by default. If the *Company* field remains blank, the product is shared across all companies.

### Liên hệ

Similar to products, contact records are shared across companies, by default. To limit access to a
single company, click the [Company field](#general-active-companies) on a contact form, and
select a company to assign the contact to.

## Giao dịch liên công ty

The [Inter-Company Transactions](companies.md#general-inter-company) feature allows for one company in the
database to sell or purchase goods and services from another company within the same database.
Counterpart documents for orders and invoices can be automatically generated and synchronized,
depending on the configuration settings.

#### WARNING
To ensure inter-company transactions are handled appropriately, certain configurations, such as
fiscal positions and localizations, need to be accurately assigned. See [Inter-Company
Transactions](companies.md#general-inter-company) for additional information.

## Trường hợp vận dụng

### Công ty đa quốc gia

A multinational retail chain, which operates in the United States and Canada, needs to manage
transactions in both USD and CAD currencies.

Additionally, because both countries have different tax laws and regulations, it is in the best
interest of the customer to utilize the multi-company feature.

This allows for inter-company transactions they need to manage inventory moves across international
borders, while making it simple to sell to customers in both countries in their own currency.

### Separate processes

A small furniture company is developing a new line of products that require a separate procurement,
inventory, and manufacturing process. The new products are drastically different from the existing
catalog. The company is considering utilizing the multi-company feature to treat this new line as a
different entity.

To keep their database from becoming overly complex, the furniture company does not need to add an
entirely new company. Instead, they can take advantage of existing features, such as [analytic
accounting](../finance/accounting/reporting/analytic_accounting.md), and multiple warehouses, to
manage the new product line, without having to overly complicate transactions.

## Limitations

In some instances, a multi-company database may *not* be the best option, due to potential limitations.

### Quyền truy cập

A user's access rights are configured on a database level. If a user has access to more than one
company in a multi-company database, their access rights are the same across every company.

### Shared records

Individual records are either [shared](#general-sharing-data) between all companies, or belong
to a single company.

### Báo cáo PDF

Some customizations, specifically for PDF reports, apply to all companies. It is not always possible
to separate reports for individual companies.
