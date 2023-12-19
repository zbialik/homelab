# Updating Cert-Manager manifests

```
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm template \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --set installCRDs=true \
  -f helm/values.yaml > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

```bash
../../update_helm_values.sh jetstack/cert-manager TARGET_CHART_VERSION
```
