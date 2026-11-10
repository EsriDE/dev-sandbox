# Location Platform demo catalogue (without Data Hosting)

Pricing reference: https://location.arcgis.com/pricing/ (reviewed 2026-10-12). **12 usage allowances** are represented below. These are separate billing counters, not necessarily distinct services. Free quotas can change; check before presenting. A suitable API key and permissions are required, and usage above an allowance may be billed.

| Demo | Initial allowance | What is shown |
|---|---|---|
| [Basemap tiles](../lessons/01-map-basics.html) | 2,000,000 tiles | Navigable interactive basemap |
| [Basemap sessions](../lessons/05-basemap-sessions.html) | 1,000 sessions | Explicit session request and expiry |
| [Static maps](../lessons/06-static-maps.html) | 1,000 maps | Rendered PNG response |
| [Nearby Places](../lessons/07-places-nearby.html) | 500 searches | Blue markers at returned place locations |
| [Place attributes](../lessons/08-places-basic.html) | 100 places | Name/category fields |
| [Place address](../lessons/09-places-address.html) | 100 places | Address fields |
| [Place contact details](../lessons/10-places-details.html) | 100 places | Contact information when available |
| [Precise place locations](../lessons/11-places-location.html) | 100 places | Orange marker at returned coordinate |
| [Geocoding](../lessons/02-place-search.html) | 20,000 results | Search field, result pin, map navigation |
| [Routing](../lessons/12-routes.html) | 20,000 routes | Green A/orange B and calculated blue route |
| [Service areas](../lessons/13-service-areas.html) | 5,000 areas | Orange origin and shaded drive-time polygon |
| [Elevation](../lessons/14-elevation.html) | 50,000 points | Click-to-select orange marker and height label |

Additional educational examples: [3D scenes](../lessons/03-scene-basics.html) and [offline map preparation](../lessons/04-offline-maps.html).

## Suggested showcase (5–8 minutes)

1. **Basemap tiles:** pan, zoom, toggle styles.
2. **Geocoding:** search an address; observe its marker.
3. **Nearby Places:** click to select a search center, then find cafés; blue results appear.
4. **Routing:** click two stops and calculate; observe a street-following blue route.
5. **Service area:** choose a location and 5 or 10 minutes; observe the shaded polygon.
6. **Elevation:** select a hill or valley and retrieve its height; a label appears at the selected point.

## Before presenting

- Use a restricted API key with Basemaps, Places, Geocoding, Routing, Service Areas and Elevation privileges as needed.
- Avoid repeatedly clicking billed request buttons; this is a usage-metered service demo.
- Basemap sessions are a *separate billing method*, not a map overlay. The existing basemap map does not use a returned session token.
- Attribute lessons deliberately don't request the Location group unless demonstrating it, to avoid extra metered requests.
- The examples are validated statically and using simulated service responses; test real rendering and privileges with your account.
