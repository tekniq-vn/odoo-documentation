# Product images with Google Images

Having appropriate product images in Odoo is useful for a number of reasons. However, if a lot of
products need images, assigning them can become incredibly time-consuming.

Fortunately, by configuring the *Google Custom Search* API within an Odoo database, finding product
images for products (based on their barcode) is extremely efficient.

<a id="product-images-configuration"></a>

## Cấu hình

In order to utilize *Google Custom Search* within an Odoo database, both the database and the Google
API must be properly configured.

#### NOTE
Free Google accounts allow users to select up to 100 free images per day. If a higher amount is
needed, a billing upgrade is required.

<a id="product-images-google-api-dashboard"></a>

### Google API dashboard

1. Go to the [Google Cloud Platform API & Services](https://console.developers.google.com/) page
   to generate Google Custom Search API credentials. Then, log in with a Google account. Next, agree
   to their Terms of Service by checking the box, and clicking Agree and
   Continue.
2. From here, select (or create) an API project to store the credentials. Start by giving it a
   memorable Project Name, select a Location (if any), then click
   Create.
3. With the Credentials option selected in the left sidebar, click Create
   Credentials, and select API key from the drop-down menu.
   ![API & Services page on Google Cloud Platform.](../../../../../_images/credentials-api-key.png)
4. Doing so reveals an API key created pop-up window, containing a custom API
   key. Copy and save Your API key in the pop-up window -- it will be used later. Once
   the key is copied (and saved for later use), click Close to remove the pop-up window.
   ![The API key created pop-up window that appears.](../../../../../_images/api-key-pop-up.png)
5. On this page, search for `Custom Search API`, and select it.
   ![Search bar containing "Custom Search API" on Google Cloud Platform.](../../../../../_images/custom-search-api-search-bar.png)
6. From the Custom Search API page, enable the API by clicking Enable.
   !["Custom Search API" page with Enable button highlighted on Google Cloud Platform.](../../../../../_images/gcp-custom-search-api-page.png)

<a id="product-images-google-pse-dashboard"></a>

### Google Programmable Search dashboard

1. Next, go to [Google Programmable Search Engine](https://programmablesearchengine.google.com/),
   and click either of the Get started buttons. Log in with a Google account, if not
   already logged in.
   ![Google Programmable Search Engine page with the Get Started buttons.](../../../../../_images/google-pse-get-started.png)
2. On the Create a new search engine form, fill out the name of the search engine, along
   with what the engine should search, and be sure to enable Image Search and
   SafeSearch.
   ![Create new search engine form that appears with search engine configurations.](../../../../../_images/create-new-search.png)
3. Validate the form by clicking Create.
4. Doing so reveals a new page with the heading: Your new search engine has been
   created.
   ![The Your New Search Engine Has Been Created page that appears with copy code.](../../../../../_images/new-search-engine-has-been-created.png)
5. From this page, click Customize to open the Overview ‣ Basic page.
   Then, copy the ID in the Search engine ID field. This ID is needed for the Odoo
   configuration.
   ![Basic overview page with search engine ID field.](../../../../../_images/basic-overview-search-engine-id.png)

<a id="product-images-setup-in-odoo"></a>

### Odoo

1. In the Odoo database, go to the Settings app and scroll to the
   Integrations section. From here, check the box beside Google Images.
   Then, click Save.
   ![The Google Images setting in the Odoo Settings app page.](../../../../../_images/google-images-setting.png)
2. Next, return to the Settings app, and scroll to the Integrations
   section. Then, enter the API Key and Search Engine ID in the fields
   beneath the Google Images feature.
3. Nhấp Lưu.

<a id="product-images-get-product-images"></a>

## Product images in Odoo with Google Custom Search API

Adding images to products in Odoo can be done on any product or product variant. This process can be
completed in any Odoo application that provides access to product pages (e.g. *Sales* app,
*Inventory* app, etc.).

Below is a step-by-step guide detailing how to utilize the *Google Custom Search API* to assign
images to products in Odoo using the Odoo *Sales* application:

1. Navigate to the Products page in the *Sales* app (Sales app ‣
   Products ‣ Products). Or, navigate to the Product Variants page in the *Sales* app
   (Sales app ‣ Products ‣ Product Variants).
2. Select the desired product that needs an image.

   #### NOTE
   Only products (or product variants) that have a barcode, but **not** an image, are processed.

   If a product with one or more variants is selected, each variant that matches the
   aforementioned criteria is processed.
3. Click the Action ⚙️ (gear) icon on the product page, and select Get
   Pictures from Google Images from the menu that pops up.
   ![The Get Pictures from Google Images option from the Action drop-down menu in Odoo.](../../../../../_images/get-pictures-from-google-action.png)
4. On the pop-up window that appears, click Get Pictures.
   ![The pop-up that appears in which the user should click Get Picture in Odoo Sales.](../../../../../_images/click-get-picture-from-pop-up.png)
5. Once clicked, the image(s) will appear incrementally.

   #### NOTE
   Only the first 10 images are fetched immediately. If you selected more than 10, the rest are
   fetched as a background job.

   The background job processes about 100 images in a minute. If the quota authorized by Google
   (either with a free or a paid plan) is reached, the background job puts itself on hold for 24
   hours. Then, it will continue where it stopped the day before.

#### SEE ALSO
[Create, modify, or close your Google Cloud Billing account](https://cloud.google.com/billing/docs/how-to/manage-billing-account)
