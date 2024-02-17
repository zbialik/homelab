# OpenEBS

# Updating manifests

Add helm repo:
```
helm repo add openebs https://openebs.github.io/charts
helm repo update
```

## Generate manifests

```
helm template \
    openebs openebs/openebs \
    -n openebs \
    -f helm/values.yaml --version $(cat helm/CHART_VERSION) --include-crds > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

Get latest chart version like so:
```bash
helm repo update
helm search repo openebs/openebs
```

```bash
../../update_helm_values.sh openebs/openebs TARGET_CHART_VERSION
```
