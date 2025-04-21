# Planning an itinerary

By default, **Odoo Field Service** shows a static map where all task locations for the day are
pinned. To make it more useful for the field service workers, it is possible to display an itinerary
on the map using MapBox. To do so, enable the **Map Routes** feature as follows:

1. Create or sign in to a MapBox account using the following link: [https://www.mapbox.com/](https://www.mapbox.com/).
2. [Create a token](https://docs.mapbox.com/help/getting-started/access-tokens/#adding-url-restrictions-to-access-tokens).
3. Go to the [Access tokens page on Mapbox](https://account.mapbox.com/access-tokens/) and copy
   your token.
4. In Odoo, go to the Settings app and scroll down to the Integrations
   section. Paste your Mapbox access token in the Token field under
   Map Routes, and click Save.

## Displaying your itinerary on a map

#### IMPORTANT
For a field service task to be featured on the map, a **valid address** must be provided for the
customer.

To display your tasks on a map, go to Field Service ‣ My Tasks ‣ Map. To create
your itinerary, Odoo sorts out your field service tasks based on their Planned Date to
show the way from one location to the next.

To open your itinerary on the Google Maps website or app, click View in Google Maps.
Google Maps includes your current location as a starting point for your itinerary.
