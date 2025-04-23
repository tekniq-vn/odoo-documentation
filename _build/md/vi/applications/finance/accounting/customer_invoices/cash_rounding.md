# Làm tròn tiền

**Cash rounding** is required when the lowest physical denomination\
of currency, or the smallest coin, is higher than the minimum unit\
of account.

For example, some countries require their companies to round up or\
down the total amount of an invoice to the nearest five cents, when\
the payment is made in cash.

## Cấu hình

Go to Accounting ‣ Configuration ‣ Settings\
and enable _Cash Rounding_, then click on _Save_.

![image](../../../../.gitbook/assets/cash_rounding01.png)

Go to Accounting ‣ Configuration ‣ Cash Roundings,\
and click on _Create_.

Define here your _Rounding Precision_, _Rounding Strategy_, an&#x64;_&#x52;ounding Method_.

Odoo supports two **rounding strategies**:

1. **Add a rounding line**: a _rounding_ line is added on the invoice.\
   You have to define which account records the cash roundings.
2. **Modify tax amount**: the rounding is applied in the taxes section.

## Áp dụng làm tròn

When editing a draft invoice, open the _Other Info_ tab, go to th&#x65;_&#x41;ccounting Information_ section, and select the appropriate _Cash_\
_Rounding Method_.
