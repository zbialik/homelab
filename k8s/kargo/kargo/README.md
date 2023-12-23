# Kargo

## Generate manifests

```
helm template kargo \
  oci://ghcr.io/akuity/kargo-charts/kargo \
  --namespace kargo \
  --create-namespace \
  --set api.adminAccount.password=admin \
  --set api.adminAccount.tokenSigningKey=iwishtowashmyirishwristwatch \
  -f helm/values.yaml --version $(cat helm/CHART_VERSION) > generated.yaml
```
