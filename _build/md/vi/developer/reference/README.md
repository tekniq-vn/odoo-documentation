# Reference

* [Server framework](backend/)
  * [ORM API](backend/orm/)
    * [Changelog](backend/orm/changelog.md)
    * [Models](backend/orm/#models)
    * [Fields](backend/orm/#fields)
    * [Recordsets](backend/orm/#recordsets)
    * [Method decorators](backend/orm/#method-decorators)
    * [Environment](backend/orm/#environment)
    * [Common ORM methods](backend/orm/#common-orm-methods)
    * [Inheritance and extension](backend/orm/#inheritance-and-extension)
    * [Error management](backend/orm/#error-management)
  * [Data Files](backend/data.md)
    * [Structure](backend/data.md#structure)
    * [Core operations](backend/data.md#core-operations)
    * [Shortcuts](backend/data.md#shortcuts)
    * [CSV data files](backend/data.md#csv-data-files)
  * [Actions](backend/actions.md)
    * [Bindings](backend/actions.md#bindings)
    * [Window Actions (`ir.actions.act_window`)](backend/actions.md#window-actions-ir-actions-act-window)
    * [URL Actions (`ir.actions.act_url`)](backend/actions.md#url-actions-ir-actions-act-url)
    * [Server Actions (`ir.actions.server`)](backend/actions.md#server-actions-ir-actions-server)
    * [Report Actions (`ir.actions.report`)](backend/actions.md#report-actions-ir-actions-report)
    * [Client Actions (`ir.actions.client`)](backend/actions.md#client-actions-ir-actions-client)
    * [Automated Actions (`ir.cron`)](backend/actions.md#automated-actions-ir-cron)
  * [QWeb Reports](backend/reports.md)
    * [Report template](backend/reports.md#report-template)
    * [Paper Format](backend/reports.md#paper-format)
    * [Custom Reports](backend/reports.md#custom-reports)
    * [Custom fonts](backend/reports.md#custom-fonts)
    * [Reports are web pages](backend/reports.md#reports-are-web-pages)
  * [Module Manifests](backend/module.md)
    * [Manifest](backend/module.md#manifest)
  * [Security in Odoo](backend/security.md)
    * [`res.groups`](backend/security.md#res.groups)
    * [Access Rights](backend/security.md#access-rights)
    * [Record Rules](backend/security.md#record-rules)
    * [Field Access](backend/security.md#field-access)
    * [Security Pitfalls](backend/security.md#security-pitfalls)
  * [Performance](backend/performance.md)
    * [Profiling](backend/performance.md#profiling)
    * [Database population](backend/performance.md#database-population)
    * [Good practices](backend/performance.md#good-practices)
  * [Testing Odoo](backend/testing.md)
    * [Testing Python code](backend/testing.md#testing-python-code)
    * [Testing JS code](backend/testing.md#testing-js-code)
    * [Integration Testing](backend/testing.md#integration-testing)
    * [Performance Testing](backend/testing.md#performance-testing)
  * [Web Controllers](backend/http.md)
    * [Controllers](backend/http.md#controllers)
    * [API](backend/http.md#api)
  * [Mixins and Useful Classes](backend/mixins.md)
    * [Messaging features](backend/mixins.md#messaging-features)
    * [Website features](backend/mixins.md#website-features)
    * [Others](backend/mixins.md#others)
* [Web framework](frontend/)
  * [Framework Overview](frontend/framework_overview.md)
    * [Introduction](frontend/framework_overview.md#introduction)
    * [Code structure](frontend/framework_overview.md#code-structure)
    * [WebClient Architecture](frontend/framework_overview.md#webclient-architecture)
    * [Environment](frontend/framework_overview.md#environment)
    * [Building Blocks](frontend/framework_overview.md#building-blocks)
    * [Context](frontend/framework_overview.md#context)
    * [Python Interpreter](frontend/framework_overview.md#python-interpreter)
    * [Domains](frontend/framework_overview.md#domains)
    * [Bus](frontend/framework_overview.md#bus)
    * [Browser Object](frontend/framework_overview.md#browser-object)
    * [Debug mode](frontend/framework_overview.md#debug-mode)
  * [Assets](frontend/assets.md)
    * [Asset types](frontend/assets.md#asset-types)
    * [Bundles](frontend/assets.md#bundles)
    * [Lazy loading](frontend/assets.md#lazy-loading)
    * [The asset model (`ir.asset`)](frontend/assets.md#the-asset-model-ir-asset)
  * [Javascript Modules](frontend/javascript_modules.md)
    * [Plain Javascript files](frontend/javascript_modules.md#plain-javascript-files)
    * [Native Javascript Modules](frontend/javascript_modules.md#native-javascript-modules)
    * [Odoo Module System](frontend/javascript_modules.md#odoo-module-system)
  * [Owl components](frontend/owl_components.md)
    * [Using Owl components](frontend/owl_components.md#using-owl-components)
    * [Best practices](frontend/owl_components.md#best-practices)
    * [Reference List](frontend/owl_components.md#reference-list)
  * [Registries](frontend/registries.md)
    * [Registry API](frontend/registries.md#registry-api)
    * [Reference List](frontend/registries.md#reference-list)
  * [Services](frontend/services.md)
    * [Defining a service](frontend/services.md#defining-a-service)
    * [Using a service](frontend/services.md#using-a-service)
    * [Reference List](frontend/services.md#reference-list)
  * [Hooks](frontend/hooks.md)
    * [useAssets](frontend/hooks.md#useassets)
    * [useAutofocus](frontend/hooks.md#useautofocus)
    * [useBus](frontend/hooks.md#usebus)
    * [usePager](frontend/hooks.md#usepager)
    * [usePosition](frontend/hooks.md#useposition)
    * [useSpellCheck](frontend/hooks.md#usespellcheck)
  * [Patching code](frontend/patching_code.md)
    * [Description](frontend/patching_code.md#description)
    * [Patching a simple object](frontend/patching_code.md#patching-a-simple-object)
    * [Patching a javascript class](frontend/patching_code.md#patching-a-javascript-class)
    * [Patching a component](frontend/patching_code.md#patching-a-component)
    * [Removing a patch](frontend/patching_code.md#removing-a-patch)
    * [Applying the same patch to multiple objects](frontend/patching_code.md#applying-the-same-patch-to-multiple-objects)
  * [Error handling](frontend/error_handling.md)
    * [Errors in JavaScript](frontend/error_handling.md#errors-in-javascript)
    * [Lifecycle of errors within the Odoo JS framework](frontend/error_handling.md#lifecycle-of-errors-within-the-odoo-js-framework)
    * [Avoid throwing errors as much as possible](frontend/error_handling.md#avoid-throwing-errors-as-much-as-possible)
    * [Catching errors](frontend/error_handling.md#catching-errors)
    * [Error free control flow](frontend/error_handling.md#error-free-control-flow)
    * [When to throw errors](frontend/error_handling.md#when-to-throw-errors)
  * [Javascript Reference](frontend/javascript_reference.md)
    * [Overview](frontend/javascript_reference.md#overview)
    * [Web client](frontend/javascript_reference.md#web-client)
    * [Loading Javascript Code](frontend/javascript_reference.md#loading-javascript-code)
    * [Registries](frontend/javascript_reference.md#registries)
    * [Services](frontend/javascript_reference.md#services)
    * [Notifications](frontend/javascript_reference.md#notifications)
    * [Systray](frontend/javascript_reference.md#systray)
    * [Translation management](frontend/javascript_reference.md#translation-management)
    * [Session](frontend/javascript_reference.md#session)
    * [Views](frontend/javascript_reference.md#views)
    * [Fields](frontend/javascript_reference.md#fields)
    * [Client actions](frontend/javascript_reference.md#client-actions)
  * [Mobile JavaScript](frontend/mobile.md)
    * [Introduction](frontend/mobile.md#introduction)
    * [How does it work?](frontend/mobile.md#how-does-it-work)
    * [How to use it?](frontend/mobile.md#how-to-use-it)
  * [QWeb Templates](frontend/qweb.md)
    * [Data output](frontend/qweb.md#data-output)
    * [Conditionals](frontend/qweb.md#conditionals)
    * [Loops](frontend/qweb.md#loops)
    * [attributes](frontend/qweb.md#attributes)
    * [setting variables](frontend/qweb.md#setting-variables)
    * [calling sub-templates](frontend/qweb.md#calling-sub-templates)
    * [Advanced Output](frontend/qweb.md#advanced-output)
    * [Python](frontend/qweb.md#id3)
    * [Javascript](frontend/qweb.md#javascript)
  * [Odoo Editor](frontend/odoo_editor.md)
    * [Powerbox](frontend/odoo_editor.md#powerbox)
* [User interface](user_interface/)
  * [View records](user_interface/view_records.md)
    * [Generic structure](user_interface/view_records.md#generic-structure)
    * [View types](user_interface/view_records.md#view-types)
    * [Fields](user_interface/view_records.md#fields)
    * [Inheritance](user_interface/view_records.md#inheritance)
    * [Model commons](user_interface/view_records.md#model-commons)
  * [View architectures](user_interface/view_architectures.md)
    * [Generic architecture](user_interface/view_architectures.md#generic-architecture)
    * [Python expression](user_interface/view_architectures.md#python-expression)
    * [Form](user_interface/view_architectures.md#form)
    * [Settings](user_interface/view_architectures.md#settings)
    * [List](user_interface/view_architectures.md#list)
    * [Search](user_interface/view_architectures.md#search)
    * [Kanban](user_interface/view_architectures.md#kanban)
    * [QWeb](user_interface/view_architectures.md#qweb)
    * [Graph](user_interface/view_architectures.md#graph)
    * [Pivot](user_interface/view_architectures.md#pivot)
    * [Calendar](user_interface/view_architectures.md#calendar)
    * [Activity](user_interface/view_architectures.md#activity)
    * [Cohort](user_interface/view_architectures.md#cohort)
    * [Grid](user_interface/view_architectures.md#grid)
    * [Gantt](user_interface/view_architectures.md#gantt)
    * [Map](user_interface/view_architectures.md#map)
  * [SCSS inheritance](user_interface/scss_inheritance.md)
    * [Overview](user_interface/scss_inheritance.md#overview)
    * [SCSS's `!default` directive](user_interface/scss_inheritance.md#scss-s-default-directive)
    * [Odoo's SCSS inheritance system](user_interface/scss_inheritance.md#odoo-s-scss-inheritance-system)
  * [UI icons](user_interface/icons.md)
    * [Icons](user_interface/icons.md#icons)
    * [RTL adaptations](user_interface/icons.md#rtl-adaptations)
* [Standard modules](standard_modules/)
  * [Accounting](standard_modules/account/)
    * [Account Tag](standard_modules/account/account_account_tag.md)
    * [Account](standard_modules/account/account_account.md)
    * [Fiscal Position](standard_modules/account/account_fiscal_position.md)
    * [Account Group](standard_modules/account/account_group.md)
    * [Report](standard_modules/account/account_report.md)
    * [Report Line](standard_modules/account/account_report_line.md)
    * [Taxes](standard_modules/account/account_tax.md)
    * [Tax Repartitions](standard_modules/account/account_tax_repartition.md)
  * [Payment](standard_modules/payment/)
    * [Payment Method](standard_modules/payment/payment_method.md)
    * [Payment Provider](standard_modules/payment/payment_provider.md)
    * [Payment Token](standard_modules/payment/payment_token.md)
    * [Payment Transaction](standard_modules/payment/payment_transaction.md)
* [Command-line interface (CLI)](cli.md)
  * [Help & version](cli.md#help-version)
  * [Running the server](cli.md#running-the-server)
  * [Testing Configuration](cli.md#testing-configuration)
    * [Database](cli.md#database)
    * [Emails](cli.md#emails)
    * [Internationalisation](cli.md#internationalisation)
    * [Advanced Options](cli.md#advanced-options)
  * [Configuration file](cli.md#configuration-file)
  * [Shell](cli.md#shell)
  * [Neutralize](cli.md#neutralize)
  * [Scaffolding](cli.md#scaffolding)
  * [Database Population](cli.md#database-population)
  * [Cloc](cli.md#cloc)
    * [Command-line options](cli.md#command-line-options)
    * [Processed files](cli.md#processed-files)
    * [Identifying Extra Modules](cli.md#identifying-extra-modules)
    * [Error Handling](cli.md#error-handling)
  * [TSConfig Generator](cli.md#tsconfig-generator)
* [Upgrades](upgrades/)
  * [Upgrade scripts](upgrades/upgrade_scripts.md)
    * [`migrate()`](upgrades/upgrade_scripts.md#migrate)
    * [Writing upgrade scripts](upgrades/upgrade_scripts.md#writing-upgrade-scripts)
    * [Phases of upgrade scripts](upgrades/upgrade_scripts.md#phases-of-upgrade-scripts)
  * [Upgrade utils](upgrades/upgrade_utils.md)
    * [Installation](upgrades/upgrade_utils.md#installation)
    * [Using upgrade utils](upgrades/upgrade_utils.md#using-upgrade-utils)
    * [Util functions](upgrades/upgrade_utils.md#util-functions)
* [External API](external_api.md)
  * [Connection](external_api.md#connection)
    * [Configuration](external_api.md#configuration)
    * [Logging in](external_api.md#logging-in)
  * [Calling methods](external_api.md#calling-methods)
    * [List records](external_api.md#list-records)
    * [Count records](external_api.md#count-records)
    * [Read records](external_api.md#read-records)
    * [List record fields](external_api.md#list-record-fields)
    * [Search and read](external_api.md#search-and-read)
    * [Create records](external_api.md#create-records)
    * [Update records](external_api.md#update-records)
    * [Delete records](external_api.md#delete-records)
    * [Inspection and introspection](external_api.md#inspection-and-introspection)
* [Extract API](extract_api.md)
  * [Overview](extract_api.md#overview)
    * [Version](extract_api.md#version)
    * [Flow](extract_api.md#flow)
  * [Parse](extract_api.md#parse)
    * [Routes](extract_api.md#routes)
    * [Request](extract_api.md#request)
    * [Response](extract_api.md#response)
  * [Get results](extract_api.md#get-results)
    * [Routes](extract_api.md#extract-api-get-result)
    * [Request](extract_api.md#id2)
    * [Response](extract_api.md#id3)
  * [Integration Testing](extract_api.md#integration-testing)
