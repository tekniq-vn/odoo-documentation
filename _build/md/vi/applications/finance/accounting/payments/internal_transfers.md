# Internal transfers

Internal money transfers can be handled in Odoo. At least two bank accounts are needed to make
internal transfers.

#### SEE ALSO
[How to add an additional bank account](applications/finance/accounting/bank.md)

## Cấu hình

An internal transfer account is automatically created on your database based on your company's
localization and depending on your country’s legislation. To modify the default Internal
transfer account, go to Accounting ‣ Configuration ‣ Settings and scroll down
to the Default Accounts section.

## Register an internal transfer from one bank to another

If you want to transfer money from one bank to another, access the Accounting Dashboard, click the
drop-down selection button (⋮) on the bank from which you want to make the transfer,
then click Payments. Select or create a payment, tick the Internal Transfer
checkbox, and select a Destination Journal before you Confirm the internal
transfer.

The money is now booked in the transfer account and another payment is automatically created in the
destination journal.

Once this is done, you can book and reconcile your bank statement lines as usual.

#### SEE ALSO
[Đối chiếu ngân hàng](applications/finance/accounting/bank/reconciliation.md)
