# Updating manifests

Add helm repo:
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

## Generate manifests

```
helm template \
    node-exporter prometheus-community/prometheus-node-exporter \
    -n monitoring \
    -f helm/values.yaml --version $(cat helm/CHART_VERSION) > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

Get latest chart version like so:
```bash
helm repo update
helm search repo prometheus-community/prometheus-node-exporter
```

```bash
../../update_helm_values.sh prometheus-community/prometheus-node-exporter TARGET_CHART_VERSION
```
