#!/usr/bin/env bash
# Single start command for the Developer Sandbox.
# Launches the FastAPI backend (port 8000) and the static frontend (port 8080).
set -euo pipefail

cd "$(dirname "$0")"

echo "Starting backend (FastAPI) on :8000 ..."
(cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload) &
BACKEND_PID=$!

echo "Starting frontend (static server) on :8080 ..."
(cd frontend && python3 -m http.server 8080) &
FRONTEND_PID=$!

echo ""
echo "Backend:  http://localhost:8000/health"
echo "Frontend: http://localhost:8080"
echo ""
echo "Press Ctrl+C to stop both servers."

trap 'kill $BACKEND_PID $FRONTEND_PID 2>/dev/null' EXIT
wait
