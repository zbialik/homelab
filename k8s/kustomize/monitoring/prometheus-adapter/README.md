# Prometheus Adapter

Primarily deployed as a vanilla metrics-server given my cluster can't auto-scale.

Add helm repo:
```
helm repo add jetstack https://charts.jetstack.io
helm repo update
```

## Generate manifests

```
helm template \
    prometheus-adapter prometheus-community/prometheus-adapter \
    --api-versions apiregistration.k8s.io/v1 \
    -f helm/values.yaml --version $(cat helm/CHART_VERSION) > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

Get latest chart version like so:
```bash
helm repo update
helm search repo prometheus-community/prometheus-adapter
```

```bash
../../update_helm_values.sh prometheus-community/prometheus-adapter TARGET_CHART_VERSION
```
