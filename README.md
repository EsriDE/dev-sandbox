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

Click:

Code -> Codespaces -> Create Codespace

After startup:

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend

python -m http.server 8080
```

Open:

http://localhost:8080

---

## Environment Variables

Copy:

```bash
cp .env.example .env
```

Configure:

```env
ARCGIS_API_KEY=YOUR_API_KEY
```

---

## Backend Endpoint

Test:

```bash
curl http://localhost:8000/geocode?q=Berlin
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