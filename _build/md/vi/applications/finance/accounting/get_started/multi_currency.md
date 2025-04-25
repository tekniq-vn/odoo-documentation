# Hệ thống đa tiền tệ

Odoo allows you to issue invoices, receive bills, and record transactions in currencies other than
the main currency configured for your company. You can also set up bank accounts in other currencies
and run reports on your foreign currency activities.

#### SEE ALSO
- [Manage a bank account in a foreign currency](../bank/foreign_currency.md)

<a id="multi-currency-config"></a>

## Cấu hình

<a id="multi-currency-config-main-currency"></a>

### Tiền tệ chính

The **main currency** is defined by default according to the company's country. You can change it by
going to Accounting ‣ Configuration ‣ Settings ‣ Currencies and changing the
currency in the Main Currency setting.

<a id="multi-currency-config-enable"></a>

### Enable foreign currencies

Go to Accounting ‣ Configuration ‣ Currencies, and enable the currencies you
wish to use by toggling the Active button.

![Enable the currencies you wish to use.](../../../../.gitbook/assets/enable-foreign-currencies.png)

<a id="multi-currency-config-rates"></a>

### Tỷ giá

#### Cập nhật thủ công

To manually create and set a currency rate, go to Accounting ‣ Configuration ‣
Currencies, click on the currency you wish to change the rate of, and under the Rates
tab, click Add a line to create a new rate.

![Create or modify the currency rate.](../../../../.gitbook/assets/manual-rate-update.png)

#### Cập nhật tự động

When you activate a second currency for the first time, Automatic Currency Rates appears
under Accounting Dashboard ‣ Configuration ‣ Settings ‣ Currencies. By
default, you have to click on the **Update now** button (🗘) to update the rates.

Odoo can update the rates at regular intervals. To do so, change the Interval from
Manually to Daily, Weekly, or Monthly. You can also
select the web service from which you want to retrieve the latest currency rates by clicking on the
Service field.

<a id="multi-currency-config-exch-diff"></a>

### Exchange difference entries

Odoo automatically records exchange differences entries on dedicated accounts, in a dedicated
journal.

You can define which journal and accounts to use to **post exchange difference entries** by
going to Accounting ‣ Configuration ‣ Settings ‣ Default Accounts and editing
the Journal, Gain Account, and Loss Account.

<a id="multi-currency-config-coa"></a>

### Hệ thống tài khoản

Each account can have a set currency. By doing so, all moves relevant to the account are forced to
have that account's currency.

To do so, go to Accounting ‣ Configuration ‣ Charts of Accounts and select a
currency in the field Account Currency. If left empty, all active currencies are handled
instead of just one.

<a id="multi-currency-config-journals"></a>

### Sổ nhật ký

If a currency is set on a **journal**, that journal only handles transactions in that currency.

To do so, go to Accounting ‣ Configuration ‣ Journals, open the journal you
want to edit, and select a currency in the field Currency.

![Select the currency for the journal to handle.](../../../../.gitbook/assets/journal-currency.png)

<a id="multi-currency-mca"></a>

## Kế toán đa tiền tệ

<a id="multi-currency-mca-documents"></a>

### Invoices, bills, and other documents

For all documents, you can select the currency and journal to use for the transaction on the
document itself.

![Select the currency and journal to use.](../../../../.gitbook/assets/currency-field.png)

<a id="multi-currency-mca-payment"></a>

### Payment registration

To register a payment in a currency other than your company's main currency, click on the
Register Payment payment button of your document and, in the pop-up window, select a
**currency** in the Amount field.

![Select the currency and journal to use before registering the payment.](../../../../.gitbook/assets/register-payment.png)

<a id="multi-currency-mca-statements"></a>

### Giao dịch ngân hàng

When creating or importing bank transactions, the amount is in the company's main currency. To input
a **foreign currency**, select a currency in the Foreign Currency. Once selected, enter
the Amount in your main currency for it to automatically get converted in the foreign
currency in the Amount in Currency field.

![The extra fields related to foreign currencies.](../../../../.gitbook/assets/foreign-fields.png)

When reconciling, Odoo displays both the foreign currency amount and the equivalent amount in your
company's main currency.

<a id="multi-currency-mca-exch-entries"></a>

### Exchange rate journal entries

To see **exchange difference journal entries**, go to Accounting Dashboard ‣
Accounting ‣ Journals: Miscellaneous.

![Exchange rate journal entry.](../../../../.gitbook/assets/exchange-journal-currency.png)
