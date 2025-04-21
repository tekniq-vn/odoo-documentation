# Ponto

**Ponto** is a service that allows companies and professionals to aggregate their accounts in one
place and directly see all their transactions within one app. It is a third-party solution that is
continuously expanding the number of bank institutions that can be synchronized with Odoo.

**Odoo** can synchronize directly with your bank to get all bank statements imported automatically
into your database.

Ponto is a paid third-party provider that can handle the synchronization between your bank accounts
and Odoo.

#### SEE ALSO
- [Đồng bộ hoá ngân hàng](../bank_synchronization.md)
- [Giao dịch](../transactions.md)

## Cấu hình

### Link your bank accounts with Ponto

1. Go to [Ponto's website (https://myponto.com)](https://myponto.com).
2. Create an account if you don't have one yet.
3. Once you are logged in, create an *organization*.
   ![Fill out the form to add an organization in Ponto.](ponto/ponto-organization.png)
4. Go to Accounts ‣ Live, and click Add account. You might have to
   add your **Billing Information** first.
5. Select your country, your bank institutions, give your consent to Ponto, and follow the steps
   on-screen to link your bank account with your Ponto account.
   ![Add bank accounts to your Ponto account.](ponto/ponto-add-account.png)
6. Add all bank accounts you want to synchronize with your Odoo database and move to the next steps.

### Link your Ponto account with your Odoo database

1. Go to Accounting ‣ Configuration ‣ Add a Bank Account.
2. Search for your institution and select it so you can verify that the third party provider is
   Ponto.
3. Click Connect and follow the steps.
4. Select **all accounts** you want to access and synchronize in Odoo, even the ones coming from
   other banking institutions.
   ![Selection of the accounts you wish to synchronize with Odoo.](ponto/ponto-select-accounts.png)
5. Finish the flow.

#### NOTE
You have to authorize all the accounts you want to access in Odoo, but Odoo will filter the
accounts based on the institution you selected in the second step.

### Update your synchronization credentials

To update your Ponto credentials or modify the synchronization settings, activate the
[developer mode](../../../../general/developer_mode.md#developer-mode), go to Accounting ‣ Configuration ‣
Online Synchronization, and select the institution from which you want to fetch the other
accounts. Click Fetch Accounts to start the flow.

#### NOTE
During the update, select **all accounts** you want to synchronize, even the ones coming from
other banking institutions.

### Fetch new accounts

To add new online accounts to your connection, activate the [developer mode](../../../../general/developer_mode.md#developer-mode),
go to Accounting ‣ Configuration ‣ Online Synchronization, and select the
institution from which you want to fetch the other accounts. Click Fetch Accounts to
start the flow.

#### NOTE
Don't forget to keep authorization for existing accounts (for all institutions that you have
synchronized with Ponto).

## Câu hỏi thường gặp

### After my synchronization, no account appears

You selected an institution from the list and did not authorize any accounts from this institution.

### I have an error about that my authorization has expired

Every **6 months** (180 days) you must re-authorize the connection between your bank account
and Ponto. This must be done from the [Ponto website](https://myponto.com). If you do not
do this, the synchronization will stop for these accounts.

### I have some errors with my beta institution

Ponto provides institutions in *beta*, these institutions are not directly supported by Odoo
and we advise you to contact Ponto directly.

#### IMPORTANT
Using an institution in beta is beneficial for Ponto, it allows them to have real
feedback on the connection with the institution.
