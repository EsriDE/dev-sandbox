# Developer Sandbox

Developer Sandbox shwoing best practices using ArcGIS Location Platform.

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

1. Add your key as a Codespaces secret **before** creating the codespace:
   `GitHub repo -> Settings -> Secrets and variables -> Codespaces -> New secret`
   Name: `ARCGIS_API_KEY`, Value: your ArcGIS Location Platform API key.
2. Click: Code -> Codespaces -> Create Codespace.
3. That's it. The container automatically:
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