# Ứng dụng và phân hệ

You can [install](apps_modules.md#general-install), [upgrade](apps_modules.md#general-upgrade) and [uninstall](apps_modules.md#general-uninstall) all apps and modules from the Apps dashboard.

By default, an _Apps_ filter is applied. If you want to search for modules, click o&#x6E;_&#x46;ilters_ and select _Extra_.

![Add "Extra" filter in Odoo Apps](../../.gitbook/assets/apps-search-filter.png)

#### WARNING

Odoo is _not a smartphone_, and its apps shouldn't be installed or uninstalled carelessly. Apply\
caution when adding or removing apps and modules on your database since this may impact your\
subscription costs.

* **Installing or uninstalling apps and managing users is up to you.**\
  As the administrator of your database, you are responsible for its usage, as you know best\
  how your organization works.\

* **Odoo apps have dependencies.**\
  Installing some apps and features with dependencies may also install additional apps and\
  modules that are technically required, even if you won't actively use them.\

* **Test app installation/removal on a duplicate of your database.**\
  This way, you can know what app dependencies may be required or what data may be erased.\


## Install apps and modules

Go to Apps, and click on the _Install_ button of the app you want to install.

#### NOTE

If the module you are looking for is not listed, you can **update the app list**.

To do so, activate the [developer mode](applications/general/developer_mode.md#developer-mode), then go to Apps\
‣ Update Apps List and click on _Update_.

## Upgrade apps and modules

On some occasions, new improvements or app features are added to [supported versions of Odoo](administration/supported_versions.md). To be able to use them, you must **upgrade** your app.

Go to Apps, click on the _dropdown menu_ of the app you want to upgrade, then o&#x6E;_&#x55;pgrade_.

## Uninstall apps and modules

Go to Apps, click on the _dropdown menu_ of the app you want to uninstall, then o&#x6E;_&#x55;ninstall_.

![image](../../.gitbook/assets/uninstall.png)

Some apps have dependencies, meaning that one app requires another. Therefore, uninstalling one app\
may uninstall multiple apps and modules. Odoo warns you which dependent apps and modules are\
affected by it.

![image](../../.gitbook/assets/uninstall_deps.png)

To complete the uninstallation, click on _Confirm_.
