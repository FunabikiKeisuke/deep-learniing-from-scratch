#!/bin/bash

TAG='deep-learning-from-scratch:1.0.0'
docker run -it --rm \
  -v $(pwd):/workspace \
  -w /workspace \
  "${TAG}"