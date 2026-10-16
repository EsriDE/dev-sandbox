# Offline map lesson — scope and constraints

`lessons/04-offline-maps.html` is a standalone HTML lesson. Register it in `lessons/manifest.js`. Nothing needs changing in `app.js` or the shared sandbox shell.

## What the demo actually does

1. Displays an **online** ArcGIS basemap using declarative Web Components.
2. Switches between ArcGIS topographic, navigation, and imagery basemap styles.
3. Reads the JSON for a **public** ArcGIS Online Web Map item ID using the Portal REST API.
4. Lists basemap/operational layer types and, where accessible, checks `Sync` capability at the FeatureServer service root.
5. Links to the actual portal item and Esri tutorials for enabling offline mode and creating map areas.

## Not implemented and why

- No in-browser offline map download: ArcGIS Maps SDK for JavaScript does not support the ArcGIS Native Apps offline map workflow.
- No portal sign-in or private organization maps: this requires user authentication (OAuth), not just the sandbox's basemap API key.
- No automatic `offlineEnabled` certification: service Sync alone is insufficient; map and basemap packaging capabilities plus portal settings must be reviewed.
- No automatic portal change or package generation: those actions require the signed-in owner/admin's privileges.
- ArcGIS Location Platform support for building offline apps is limited and may require contacting Esri; consult the linked documentation.

## Manual test

1. Run `python3 -m http.server 8080`, open the sandbox, enter an API key with basemap access.
2. Switch basemaps and check that the preview updates.
3. Click *Inspect Web Map* (an Esri SDK documentation example item ID is prefilled; it is not asserted to be offline-enabled).
4. Inspect an accessible public Web Map that you own; compare results to its portal `Settings → Offline` page.
5. Open the code panel, edit an HTML attribute, and run/reset the preview.
6. If you need private items, use the portal in a separate tab. No credentials should be pasted into lesson code.

## Authoritative references

- https://developers.arcgis.com/documentation/offline-mapping-apps/tutorials/tools/create-an-offline-enabled-web-map/
- https://developers.arcgis.com/documentation/offline-mapping-apps/tutorials/tools/create-an-offline-map-area/
- https://developers.arcgis.com/documentation/offline-mapping-apps/partially-offline-apps/offline-maps/
- https://developers.arcgis.com/rest/services-reference/enterprise/sync-enabled-feature-services/
- https://developers.arcgis.com/documentation/offline-mapping-apps/get-started/
