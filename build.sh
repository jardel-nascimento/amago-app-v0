#!/usr/bin/env bash

set -e

if ! command -v buildozer >/dev/null 2>&1; then
  echo "buildozer nao encontrado no PATH."
  exit 1
fi

if ! command -v java >/dev/null 2>&1; then
  echo "java nao encontrado no PATH."
  exit 1
fi

mkdir -p logs
buildozer android debug 2>&1 | tee logs/buildozer.log
