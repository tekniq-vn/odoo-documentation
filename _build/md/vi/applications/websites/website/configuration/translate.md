# Dịch thuật

Your website is displayed in the language that matches your visitor’s browser. If the browser’s
language has not been installed and added to your website, the content is shown in the
[default language](#translate-default-language). When additional languages are installed, users
can choose their preferred language using the [language selector](#translate-language-selector).

The [Translate](#translate-translate) feature on your website allows automatic translation of
standard terms and provides a tool for manual content translation.

## Cài đặt ngôn ngữ

Để cho phép dịch trang web của bạn, trước tiên bạn phải [cài đặt](../../../general/users/language.md) các ngôn ngữ cần thiết và thêm chúng vào trang web. Để thực hiện, hãy truy cập Trang web ‣ Cấu hình ‣ Cài đặt và nhấp <i class="fa fa-arrow-right"></i> Cài đặt ngôn ngữ trong phần Thông tin trang web. Trong hộp thoại mở ra, chọn Ngôn ngữ bạn muốn từ menu thả xuống, tích vào Trang web cần dịch và nhấp Thêm.

To edit your website's languages, go to Website -–> Configuration -–> Settings and
add/remove the required languages in/from the Languages field in the
Website info section.

<a id="translate-default-language"></a>

### Ngôn ngữ mặc định

When multiple languages are available on your website, you can set a default language to be used if
the visitor’s browser language is not available. To do so, go to Website –->
Configuration -–> Settings, and select a language in the Default field.

#### NOTE
This field is only visible if multiple languages have been installed and added to your website.

<a id="translate-language-selector"></a>

## Bộ chọn ngôn ngữ

Your website’s visitors can switch languages using the language selector, available by default in
the Copyright section at the bottom of the page. To edit the language selector menu:

1. Go to your website and click Edit;
2. Click the language selector available in the Copyright block and go to the
   Copyright section of the website builder;
3. Set the Language Selector field to either Dropdown or Inline.
   Click None if you do not want to display the  Language selector;
   > ![Add a language selector menu.](applications/websites/website/configuration/translate/language-selector.png)
4. Nhấp Lưu.

<a id="translate-translate"></a>

## Translate your website

Select your desired language from the language selector to see your content in another language.
Then, click the Translate button in the top-right corner to manually activate the
translation mode so that you can translate what has not been translated automatically by Odoo.

Translated text strings are highlighted in green; text strings that were not translated
automatically are highlighted in yellow.

![Entering the translation mode](applications/websites/website/configuration/translate/translated-text.png)

In this mode, you can only translate text. To change the page's structure, you must edit the master
page, i.e., the page in the original language of the database. Any changes made to the master page
are automatically applied to all translated versions.

To replace the original text with the translation, click the block, edit its contents, and
Save.

#### NOTE
Khi một trang web hỗ trợ nhiều ngôn ngữ, cấu trúc URL cốt lõi vẫn giữ nguyên khi chuyển đổi giữa các ngôn ngữ, trong khi các yếu tố cụ thể như tên sản phẩm hoặc danh mục sẽ được dịch. Ví dụ: `https://www.mywebsite.com/shop/product/my-product-1` là phiên bản tiếng Anh của một trang sản phẩm, còn `https://www.mywebsite.com/fr/shop/product/mon-produit-1` là phiên bản tiếng Pháp của cùng trang đó. Cấu trúc (/shop/product/) không thay đổi, nhưng các thành phần được dịch (VD: tên sản phẩm) sẽ được điều chỉnh theo ngôn ngữ đã chọn.

### Content visibility by language

You can hide content (such as images or videos, for example) depending on the language. To do so:

1. Click Edit and select an element of your website;
2. Go to the Text - Image section and Visibility;
3. Click No condition and select Conditionally instead;
4. Go to Languages to configure the condition(s) to apply by selecting
   Visible for or Hidden for, and click Choose a record to
   decide which languages are impacted.
