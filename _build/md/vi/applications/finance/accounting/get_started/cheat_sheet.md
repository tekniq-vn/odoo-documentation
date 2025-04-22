# Accounting cheat sheet

What is owned (an asset) has been financed through debts to reimburse (liabilities) or equity
(profits, capital).

A difference is made between **assets** and **expenses**:
: - An **asset** is a resource with economic value that an individual, corporation, or country owns
    or controls with the expectation that it will provide a future benefit. Assets are reported on
    a company's balance sheet. They are bought or created to increase a firm's value or benefit its
    operations.
  - An **expense** is the costs of operations a company bears to generate revenues.

> Assets = Liabilities + Equity

## Hệ thống tài khoản

The **chart of accounts** lists all the company's accounts: both Balance sheet accounts and P&L
accounts. Every transaction is recorded by debiting and crediting multiple accounts in a journal
entry. In a way, a chart of accounts is like a company's DNA!

Every account listed in the chart of accounts belongs to a specific category. In Odoo, each account
has a unique code and belongs to one of these categories:

- **Equity and subordinated debts**
  : - **Equity** is the amount of money invested by a company's shareholders to finance the
      company's activities.
    - **Subordinated debts** are the amount of money lent by a third party to a company to finance
      its activities. In the event of the dissolution of a company, these third parties are
      reimbursed before the shareholders.
- **Tài sản cố định** là những tài sản hữu hình (tức là tài sản có thể nhìn thấy và chạm được) mà một công ty mua để phục vụ cho việc sản xuất hàng hóa và cung cấp dịch vụ. Đây là các tài sản dài hạn, có nghĩa là chúng có thời gian sử dụng hữu ích kéo dài hơn một năm. Tài sản cố định còn bao gồm bất độn sản, nhà máy, và thiết bị (thường được gọi là “PP&E”) và được ghi nhận trên bảng cân đối kế toán dưới phân loại này.
- **Current assets and liabilities**
  : - The **current assets** account is a balance sheet line item listed under the Assets section,
      which accounts for all company-owned assets that can be converted to cash within one year.
      Current assets include cash, cash equivalents, accounts receivable, stock inventory,
      marketable securities, prepaid liabilities, and other liquid assets.
    - **Current liabilities** are a company's short-term financial obligations due within one year.
      An example of a current liability is money owed to suppliers in the form of accounts payable.
- **Bank and cash accounts**
  : - A **bank account** is a financial account maintained by a bank or other financial institution
      in which the financial transactions between the bank and a customer are recorded.
    - A **cash account**, or cash book, may refer to a ledger in which all cash transactions are
      recorded. The cash account includes both the cash receipts and the cash payment journals.
- **Expenses and income**
  : - An **expense** is the costs of operations a company bears to generate revenues. It is simply
      defined as the cost one is required to spend on obtaining something. Common expenses include
      supplier payments, employee wages, factory leases, and equipment depreciation.
    - The term "**income**" generally refers to the amount of money, property, and other transfers
      of value received over a set period of time in exchange for services or products.

### Ví dụ

<a id="cheat-sheet-journals"></a>

## Bút toán

Every financial document of the company (e.g., an invoice, a bank statement, a pay slip, a capital
increase contract) is recorded as a journal entry, impacting several accounts.

For a journal entry to be balanced, the sum of all its debits must be equal to the sum of all its
credits.

<a id="accounting-reconciliation"></a>

## Đối soát

[Reconciliation](applications/finance/accounting/bank/reconciliation.md) is the process of linking
journal items of a specific account and matching credits and debits.

Its primary purpose is to link payments to their related invoices to mark them as paid. This is done
by doing a reconciliation on the accounts receivable account and/or the accounts payable account.

Reconciliation is performed automatically by the system when:

- the payment is registered directly on the invoice
- the links between the payments and the invoices are detected at the bank matching process

## Đối chiếu thanh toán

Bank reconciliation is the matching of bank statement lines (provided by your bank) with
transactions recorded internally (payments to suppliers or from customers). For each line in a bank
statement, it can be:

- **matched with a previously recorded payment**: a payment is registered when a check is received
  from a customer, then matched when checking the bank statement.
- **recorded as a new payment**: the payment's journal entry is created and reconciled with the
  related invoice when processing the bank statement.
- **recorded as another transaction**: bank transfer, direct charge, etc.

Odoo should automatically reconcile most transactions; only a few should need manual review. When
the bank reconciliation process is finished, the balance on the bank account in Odoo should match
the bank statement's balance.

## Xử lý séc

There are two approaches to managing checks and internal wire transfers:

- Two journal entries and a reconciliation
- One journal entry and a bank reconciliation
