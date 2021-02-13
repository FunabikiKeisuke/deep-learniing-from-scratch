#!/bin/bash

TAG='deep-learning-from-scratch:1.0.0'
cd "$(dirname "${0}")/.."  || exit

DOCKER_BUILDKIT=1 docker build --progress=plain -t ${TAG} -f docker/Dockerfile .
