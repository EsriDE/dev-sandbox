# Developer Sandbox

Developer Sandbox showing best practices using ArcGIS Location Platform.

Goal:

Run a complete ArcGIS web application with Python backend in less than five minutes.

No local setup required.

Supported environments:

- GitHub Codespaces
- Docker Desktop
- Dev Containers
- Azure Container Apps

---

## Features

- ArcGIS Maps SDK for JavaScript
- FastAPI Backend
- ArcGIS Location Platform
- Geocoding
- Routing
- Places
- Ready-to-use Samples

---

## Open in GitHub Codespaces

You do **not** need to own or fork this repo. Codespaces secrets can be set on
your own GitHub account and scoped to any repository you can access:

1. Go to [github.com/settings/codespaces](https://github.com/settings/codespaces).
2. Under **Codespaces secrets**, click **New secret**.
3. Name: `ARCGIS_API_KEY`, Value: your ArcGIS Location Platform API key.
4. Under **Repository access**, select this repository (`EsriDE/dev-sandbox`),
   or search for it if you're working from your own fork.
5. Go back to this repo -> Code -> Codespaces -> Create Codespace.
6. That's it. The container automatically:
   - installs backend dependencies,
   - writes `backend/.env` with your secret,
   - starts both the backend and frontend servers.

No manual commands required. The frontend port opens a preview automatically.

If you didn't set the secret beforehand, run manually after adding it:

```bash
./start.sh
```

---

## Environment Variables

If you prefer local setup (Docker Desktop / Dev Containers) instead of a
Codespaces secret, copy the example file and fill in your key:

```bash
cp backend/.env.example backend/.env
```

```env
ARCGIS_API_KEY=YOUR_API_KEY
```

---

## Backend Endpoint

Test:

```bash
curl http://localhost:8000/geocode?q=Berlin
```

Health check (confirms the API key was picked up):

```bash
curl http://localhost:8000/health
```

---

## Sample Applications

### Geocoding

Convert addresses into coordinates.

### Routing

Calculate routes.

### Places

Search nearby locations.

### Static Maps

Generate map images.

---

## Deployment

### Azure Container Apps

```bash
az containerapp up
```

### Docker

```bash
docker compose up
```

---

## Developer Experience Goals

- Clone to running app < 5 minutes
- No Node.js required
- No ArcGIS Enterprise required
- Browser-based development