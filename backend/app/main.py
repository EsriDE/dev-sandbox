"""Minimal FastAPI backend that proxies ArcGIS Location Platform REST APIs.

Design goals (see .github/copilot-instructions.md):
- Use ArcGIS REST APIs directly via `requests` (no heavy SDK dependency).
- Keep the API key server-side only; the frontend never sees it.
- Fail fast with a clear message if ARCGIS_API_KEY is missing.
"""
import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

API_KEY = os.getenv("ARCGIS_API_KEY")

GEOCODE_URL = (
    "https://geocode-api.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
)
ROUTE_URL = "https://route-api.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World/solve"
PLACES_URL = "https://places-api.arcgis.com/arcgis/rest/services/places-service/v1/places/near-point"
STATIC_MAP_URL = "https://static-map.arcgis.com/arcgis/rest/services/static-map"

app = FastAPI(title="ArcGIS Developer Sandbox")

# Allow the static frontend (served on a different port) to call the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def require_api_key() -> str:
    if not API_KEY or API_KEY == "YOUR_API_KEY":
        raise HTTPException(
            status_code=500,
            detail=(
                "ARCGIS_API_KEY is not set. Add it as a Codespaces secret or in "
                "backend/.env, then restart the backend."
            ),
        )
    return API_KEY


@app.get("/health")
def health():
    return {"status": "ok", "api_key_configured": bool(API_KEY and API_KEY != "YOUR_API_KEY")}


@app.get("/geocode")
def geocode(q: str):
    key = require_api_key()
    params = {"f": "json", "singleLine": q, "token": key, "outFields": "*"}
    resp = requests.get(GEOCODE_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


@app.get("/route")
def route(stops: str):
    """`stops` is a pipe-separated list of 'lon,lat' points, e.g. '13.4,52.5|13.5,52.4'."""
    key = require_api_key()
    params = {"f": "json", "stops": stops, "token": key}
    resp = requests.get(ROUTE_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


@app.get("/places")
def places(x: float, y: float, radius: int = 1000, category: str | None = None):
    key = require_api_key()
    headers = {"Authorization": f"Bearer {key}"}
    params = {"x": x, "y": y, "radius": radius}
    if category:
        params["categoryIds"] = category
    resp = requests.get(PLACES_URL, params=params, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json()


@app.get("/static-map")
def static_map(x: float, y: float, zoom: int = 12):
    key = require_api_key()
    params = {"token": key, "center": f"{x},{y}", "level": zoom, "size": "600,400"}
    resp = requests.get(STATIC_MAP_URL, params=params, timeout=10)
    resp.raise_for_status()
    return {"url": resp.url}
