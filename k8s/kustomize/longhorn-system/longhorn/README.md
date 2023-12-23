# Updating manifests

```
helm repo add longhorn https://charts.longhorn.io
helm repo update
```

## Generate manifests

```
helm template longhorn/longhorn \
    --namespace longhorn-system \
    -f helm/values.yaml \
    --version $(cat helm/CHART_VERSION) > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

Get latest chart version like so:
```bash
helm repo update
helm search repo longhorn/longhorn
```

```bash
../../update_helm_values.sh longhorn/longhorn TARGET_CHART_VERSION
```
