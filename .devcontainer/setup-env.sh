#!/usr/bin/env bash
# Creates backend/.env on first container creation.
# If ARCGIS_API_KEY is already present as a Codespaces/Dev Container secret
# (environment variable), it is written straight into .env so the developer
# never has to hand-edit a file to get started.
set -euo pipefail

ENV_FILE="backend/.env"
EXAMPLE_FILE="backend/.env.example"

if [ ! -f "$ENV_FILE" ]; then
  cp "$EXAMPLE_FILE" "$ENV_FILE"
  echo "Created $ENV_FILE from $EXAMPLE_FILE"
fi

if [ -n "${ARCGIS_API_KEY:-}" ]; then
  if grep -q '^ARCGIS_API_KEY=' "$ENV_FILE"; then
    sed -i "s|^ARCGIS_API_KEY=.*|ARCGIS_API_KEY=${ARCGIS_API_KEY}|" "$ENV_FILE"
  else
    echo "ARCGIS_API_KEY=${ARCGIS_API_KEY}" >> "$ENV_FILE"
  fi
  echo "Injected ARCGIS_API_KEY from environment/Codespaces secret into $ENV_FILE"
else
  echo "No ARCGIS_API_KEY secret found yet. Set it as a Codespaces secret"
  echo "(Settings > Codespaces > Secrets) named ARCGIS_API_KEY, or edit $ENV_FILE manually."
fi
