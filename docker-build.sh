#!/usr/bin/env bash
set -e

mkdir -p .docker-buildozer .docker-buildozer-home
docker compose build
docker compose run --rm buildozer
