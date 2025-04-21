# Devices and integrations

 can be used on many different devices, such as a
computer, tablet, mobile phone, and many more. This is helpful in that it reduces costs, and
employees can work from anywhere in the world, so long as they have a broadband internet connection.

Odoo *VoIP* is SIP (Session Initiation Protocol) compatible, which means it can be used with *any*
 compatible application.

This document covers the process of setting up Odoo *VoIP* across different devices and
integrations.

Odoo is fully-integrated with all Odoo apps, allowing users to click into any app, and schedule a
call as an activity in the chatter.

## Odoo VoIP (laptop/desktop computer)

The Odoo *VoIP* (Voice over Internet Protocol) module and widget can be used from any browser on a
laptop or desktop device. Simply click on the ☎️ (phone) icon in the upper-right corner,
while in the Odoo database, and the widget appears.

#### SEE ALSO
To see how to use the  widget on a desktop/laptop
computer, check out this documentation: [VoIP widget](voip_widget.md).

## Odoo VoIP (tablet/mobile device)

The Odoo *VoIP* app can be used on tablets and mobile phones, through the Odoo Android or Apple IOS
applications. Additionally, a mobile web browser can be used to access the database.

#### WARNING
Odoo Android and Apple IOS applications are no longer being maintained by Odoo on the Android and
Apple portals. This means Odoo support only handles limited scopes of Odoo Android or Apple IOS
support tickets.

#### IMPORTANT
Mặc dù các cuộc gọi đi có thể được thực hiện bằng Odoo trên thiết bị di động, nhưng cần lưu ý rằng Odoo **không** hoàn toàn là một ứng dụng  và **không** đổ chuông khi có cuộc gọi đến. Nếu người dùng cần nhận cuộc gọi trên thiết bị di động mọi lúc, thì nên sử dụng một ứng dụng như Zoiper. Các ứng dụng đó sẽ luôn duy trì kết nối trong nền.

For more information, see this documentation: [Zoiper Lite](#voip-zoiper).

While in the mobile application on a mobile device/tablet, access the Odoo *VoIP* widget, by tapping
on the ☎️ (phone) icon in the upper-right corner. The widget appears in the lower-left
corner.

When first making a call from the tablet using the mobile application, the user is prompted to
Allow the database to use the microphone. Click Allow when prompted to
continue with the call using the microphone.

This step is **necessary**, whether using the mobile Odoo application or web browser.

![Allow the database to access the microphone.](applications/productivity/voip/devices_integrations/allow-mic.png)

Odoo then asks how to make the call. The two options are : VOIP or Phone
(should the tablet be enabled for calling). Click the box next to Remember ? should this
decision be the default moving forward.

![Window prompt to choose whether to use VOIP or the devices phone to make the call.](applications/productivity/voip/devices_integrations/voip-phone.png)

Here is the layout of what the Odoo *VoIP* app looks like on a mobile device:

![Layout of what the VoIP app looks like on the a mobile device.](applications/productivity/voip/devices_integrations/voip-odoo-dashboard.png)

<a id="voip-zoiper"></a>

## Zoiper Lite

*Zoiper Lite* is a free   dialer with voice and video.

To start using the *Zoiper* app, download it to the device, via the [Zoiper download page](https://www.zoiper.com/en/voip-softphone/download/current).

A mobile device is the most common installation, and this document covers how to set up on the
*Zoiper* IOS application. Screenshots and steps may differ depending on the set up conditions.

After installing the *Zoiper* application on the mobile phone, open the application, and tap on
Settings. Navigate to Accounts, and tap on the + (plus)
icon to add an account.

If the  account is already set up, then click
Yes. This means an account username and password has already been produced.

![Zoiper account setup, shown in the view from a mobile device.](applications/productivity/voip/devices_integrations/account-settings-zoiper-group.png)

Next, tap on Select a provider. On the screen that populates, tap Country,
in the upper-right corner, to narrow the providers down to a specific country. Choose the country
for the provider that is being configured, then find the Provider, and select it.

![Zoiper account setup, choosing the provider.](applications/productivity/voip/devices_integrations/provider-zoiper-odoo.png)

Under  options, enter the Account name,
Domain, Username, and Password. All this information varies,
based on the account.

| Trường Zoiper   | Trường Axivox      |
|-----------------|--------------------|
| Account name    | *Can be anything*  |
| Miền            | Miền               |
| Tên đăng nhập   | Tên người dùng SIP |
| Mật khẩu        | Mật khẩu SIP       |

Once this account information is entered, click the green Register button at the top of
the screen. Once the registration information is checked, *Zoiper* populates a message, stating
Registration Status: OK.

At this point, *Zoiper* is now set up to make phone calls using the  service.

![Zoiper account setup, registration successful.](applications/productivity/voip/devices_integrations/sip-options-zoiper.png)

## Linphone

*Linphone* is an open-source   softphone, used for voice, video, messaging (group and individual), as well as
conference calls.

To start using the *Linphone* app, download it to the device, via the [Linphone download page](https://new.linphone.org/technical-corner/linphone?qt-technical_corner=2#qt-technical_corner).

A mobile device is the most common installation, and this document covers how to set up the
*Linphone* IOS application. Screenshots and steps may differ depending on the circumstances.

To begin configuring *Linphone* for use with a  provider,
first open *Linphone*, and an assistant screen appears.

From this screen, select Use SIP Account. Then, on the following screen, enter the
Username, Password, Domain, and Display Name. Once
complete, press Login.

At this point, *Linphone* is ready to start making calls, once there is a green button at the top of
the application screen that reads, Connected.

![Linphone account setup, registration successful.](applications/productivity/voip/devices_integrations/linphone-odoo-setup.png)
