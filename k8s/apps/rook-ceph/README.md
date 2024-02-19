# Rook Ceph

# Updating manifests

Add helm repo:
```
helm repo add rook-release https://charts.rook.io/release
helm repo update
```

## Chart upgrades

1. Get latest chart version like so:
    ```bash
    helm repo update
    helm search repo rook-release/rook-ceph
    ```
1. Update `helm/CHART_VERSION` with new chart version
1. Update `helm/default.yaml` 
    ```bash
    helm show values rook-release/rook-ceph --version $(cat helm/CHART_VERSION) > helm/default.yaml
    ```

## Generate manifests

```bash
helm template rook-ceph rook-release/rook-ceph \
    --namespace rook-ceph \
    -f helm/values.yaml \
    --version $(cat helm/CHART_VERSION) \
    --include-crds > generated.yaml
```
