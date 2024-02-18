# OpenEBS Monitoring

# Updating manifests

Add helm repo:
```
helm repo add openebs-monitoring https://openebs.github.io/monitoring/
helm repo update
```

## Generate manifests

```
helm template \
    openebs openebs-monitoring/openebs-monitoring \
    -n openebs \
    -f helm/values.yaml --version $(cat helm/CHART_VERSION) --include-crds > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

Get latest chart version like so:
```bash
helm repo update
helm search repo openebs-monitoring/openebs-monitoring
```

```bash
../../update_helm_values.sh openebs-monitoring/openebs-monitoring TARGET_CHART_VERSION
```
