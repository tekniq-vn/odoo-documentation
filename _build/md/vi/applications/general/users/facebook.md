# Facebook sign-in authentication

The *Facebook* OAuth sign-in function allows Odoo users to sign in to their database with their
Facebook account.

## Meta for Developers setup

Go to [Meta for Developers](https://developers.facebook.com/) and log in. Click My
Apps. On the Apps page, click Create App.

On the Use cases page, select Authenticate and request data from users with
Facebook Login, then click Next.

In the Add an app name field, enter `Odoo Login OAuth`, or a similar title.

#### NOTE
The App contact email automatically defaults to the email address associated with the
Meta account. If this email address is not regularly monitored, it may be wise to use another
email address.

Click Next. Review the Publishing requirements, the Meta
Platform Terms, and Developer Policies. Then, click Create app.

#### IMPORTANT
Clicking Create app may require password re-entry.

### Customize app

After the new app is created, the Dashboard page appears, with a list of steps to be
completed before the app can be published. From here, click Customize adding a Facebook
Login button.

![The App Dashboard in the Meta for developers platform.](applications/general/users/facebook/app-requirements.png)

On the Customize page, click Settings.

In the Valid OAuth Redirect URIs field, enter `https://<odoo base
url>/auth_oauth/signin`, replacing `<odoo base url>` with the URL of the applicable database.

Click Save changes when finished.

### Configure settings

At the far left of the page, click App settings ‣ Basic. This page contains
additional settings that are required before the app can be submitted for approval.

In the Privacy Policy URL field, enter `https://www.odoo.com/privacy`.

#### NOTE
[https://www.odoo.com/privacy](https://www.odoo.com/privacy) is the default privacy policy for databases hosted on Odoo.com.

Click the App Icon field to open a file upload window. From here, select and upload an
app icon.

In the User data deletion field, enter
`https://www.odoo.com/documentation/17.0/administration/odoo_accounts.html`.

#### NOTE
This document provides instructions on how a user can delete their Odoo account.

Lastly, click the Category field, and select Business and pages from the
drop-down menu.

Nhấp Lưu thay đổi.

![An exampled of the Basic Settings page in the Meta for developers platform.](applications/general/users/facebook/app-id.png)

<a id="users-app-id"></a>

### Capture app ID

After the app is created, and approved, select and copy the App ID. Paste this
information on a clipboard or notepad file, as it is needed in a later step to complete the setup.

### Công khai

On the left side of the page, click Publish. Depending on the status of the connected
Facebook account, additional verification and testing steps may be required, and are listed on this
page.

After reviewing the information, click Publish.

#### SEE ALSO
Additional information regarding Meta App Development, including further details on building,
testing, and use cases, can be found in the [Meta for developers documentation](https://developers.facebook.com/docs/development).

## Thiết lập Odoo

First, activate [Developer mode](../developer_mode.md#developer-mode-activation).

Navigate to the Settings app, and scroll down to the Integrations
section. There, tick the checkbox labeled, OAuth Authentication. Click Save.

![The enable OAuth setting in the Settings app.](applications/general/users/facebook/enable-oauth.png)

Then, sign in to the database once the login screen loads.

After successfully logging in, navigate to Settings app ‣ Users & Companies ‣
OAuth Providers. Click Facebook Graph.

In the Client ID field, enter the [App ID](#users-app-id) from the previous
section, then tick the Allowed checkbox.

![The Facebook Graph record in Odoo.](applications/general/users/facebook/facebook-graph.png)
