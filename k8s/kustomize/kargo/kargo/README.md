# Kargo

## Generate manifests

```
helm template kargo \
  oci://ghcr.io/akuity/kargo-charts/kargo \
  --namespace kargo \
  --set api.adminAccount.password=admin \
  --set api.adminAccount.tokenSigningKey=iwishtowashmyirishwristwatch \
  --include-crds \
  -f helm/values.yaml --version $(cat helm/CHART_VERSION) > generated.yaml
```
