# Vận chuyển

Odoo eCommerce allows you to configure various shipping methods, enabling customers to choose
their preferred option at checkout. These methods include [external providers](#ecommerce-shipping-external-provider), [custom options](#ecommerce-shipping-custom-method)
such as flat-rate or free shipping, local carriers via
[Sendcloud](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping.md)
or [Based on Rules](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/#inventory-shipping-rules), and [in-store pickup](#ecommerce-shipping-instore-pickup).

<a id="ecommerce-shipping-external-provider"></a>

## External provider integration

To handle product delivery, you can connect your database to [third-party shipping carriers](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.md)
like [FedEx](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/fedex.md),
[UPS](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/ups_credentials.md),
or [DHL](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/dhl_credentials.md).
A shipping connector links to these providers, automating [tracking labels](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/labels.md) and shipping
processes.

To enable a third-party shipping provider, go to Website ‣ Configuration ‣
Settings, scroll to the Shipping section, select the desired shipping provider(s),
and Save.

Go to Website ‣ Configuration ‣ Shipping Methods and select the shipping method
in the list to [configure it](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.md#inventory-shipping-receiving-configure-delivery-method).

#### SEE ALSO
[Third-party shipping carriers](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.md)

#### IMPORTANT
The field used to define additional fees **must** be filled **in your third-party shipping
provider account**, even if you do not plan to charge customers any additional fee. If you do not
want to apply a fee, enter `0`. If the field is left empty, the delivery price cannot be
calculated, and an error message prompts the customer to select an alternative shipping method.

### Margin on delivery rate

To add an additional fee to the base shipping rate (e.g., to cover extra costs), log into your
carrier account and set the desired fee in the related field. The shipping connector retrieves this
fee and includes it in the final price at checkout. Contact your carrier for further assistance
with this configuration.

Alternatively, enter `0` in your third-party shipping provider account, then set the fee in Odoo.
To do so, access the desired [shipping method's form](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.md#inventory-shipping-receiving-configure-delivery-method) and enter the fee in the Margin
on Rate field to add a percentage to the shipping costs and/or the Additional margin
field to add a fixed amount.

#### IMPORTANT
The field used to define additional fees cannot be left empty in your third-party shipping
provider account.

<a id="ecommerce-shipping-custom-method"></a>

## Custom shipping method

Custom shipping methods must be created, for example:

- to integrate shipping carriers through [Sendcloud](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/sendcloud_shipping.md);
- to configure specific rules (e.g., to offer free shipping for orders above a specific amount) for
  a specific provider;
- to configure [Fixed Price](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/#inventory-shipping-fixed) shipping or shipping
  [Based on Rules](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/#inventory-shipping-rules).

To create a custom shipping method, go to Website ‣ Configuration ‣
Shipping Methods, click New and fill in the [fields](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.md#inventory-shipping-receiving-shipping-methods-details).

In the Provider field, select [Based on Rules](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/#inventory-shipping-rules),
[Fixed Price](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/#inventory-shipping-fixed), or [Pickup in store](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/#inventory-shipping-pickup)
if the shiping method does not involve any specific provider.

<a id="ecommerce-shipping-instore-pickup"></a>

## In-store pickup

To allow customers to reserve products online and pay for/collect them in person at the store, go to
Website ‣ Configuration ‣ Settings, scroll to the Shipping section,
enable On Site Payments & Picking, and Save.

Then, click Customize Pickup Sites, select the shipping method or click New
to create a new one and [configure](../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.md#inventory-shipping-receiving-configure-delivery-method)
the fields. Make sure the Provider field is set to Pickup in store.
