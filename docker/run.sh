#!/bin/bash

TAG='deep-learning-from-scratch:1.0.0'
PROJECT_DIR="$(cd "$(dirname "${0}")/.." || exit; pwd)"

docker run -it --rm \
  -v "${PROJECT_DIR}:/workspace" \
  -w "/workspace" \
  "${TAG}"