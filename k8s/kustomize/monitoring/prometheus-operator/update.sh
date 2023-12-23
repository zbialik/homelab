#!/usr/bin/env bash

VERSION=$1
curl -o bundle.yaml -L "https://github.com/prometheus-operator/prometheus-operator/releases/download/v${VERSION}/bundle.yaml" 
