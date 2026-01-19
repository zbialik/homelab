# Rook Ceph

## Install

Add helm repo:

```
helm repo add rook-release https://charts.rook.io/release
```

## Upgrades

```bash
helm repo update
helm search repo rook-release/rook-ceph -l # redefine ROOK_CHART_VERSION

ROOK_CHART_VERSION=v1.18.9
helm show values rook-release/rook-ceph --version $ROOK_CHART_VERSION > helm/default.yaml
helm template rook-ceph rook-release/rook-ceph \
    --namespace rook-ceph \
    -f helm/values.yaml \
    --version $ROOK_CHART_VERSION \
    --include-crds > generated.yaml
```
