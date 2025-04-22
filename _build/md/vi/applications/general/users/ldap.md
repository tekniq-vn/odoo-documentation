# LDAP authentication

To configure  authentication in Odoo:

1. Open the Settings app, scroll down to the Integrations section, and enable
   LDAP Authentication.
2. Click Save, then go back to the Integrations section and click
   LDAP Server.
3. In the Set up your LDAP Server list, click New, then select the required
   company in the dropdown list.
4. In the Server information section, enter the server's IP address and port in the
   LDAP server address and LDAP Server port fields, respectively.
5. Enable Use TLS to request secure TLS/SSL encryption when connecting to the LDAP
   server, providing the server has StartTLS enabled.
6. In the Login information section, enter the ID and password of the account used to
   query the server in the LDAP binddn and LDAP password fields,
   respectively. If the fields are left empty, the server will perform the query anonymously.
7. In the Process parameter section, enter:
   - the LDAP server's name in the LDAP base field using LDAP format
     (e.g., `dc=example,dc=com`);
   - `uid=%s` in the LDAP filter field.
8. In the User information section:
   - Enable Create user to create a user profile in Odoo the first time someone logs in
     using LDAP;
   - Select the User template to be used to create the new user profiles. If no template
     is selected, the administrator's profile is used.

#### NOTE
When using Microsoft Active Directory (AD) for LDAP authentication, if users experience login
issues despite using valid credentials, create a new system parameter to disable referral chasing
in the LDAP client:

> 1. [Activate the developer mode.](applications/general/developer_mode.md#developer-mode)
> 2. Go to Settings ‣ Technical ‣ System Parameters and click
>    New.
> 3. Fill in the fields:
>    - Khoá: `auth_ldap.disable_chase_ref`
>    - Giá trị: `True`
