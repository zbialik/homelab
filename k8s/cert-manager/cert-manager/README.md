# Cert-Manager

Add helm repo
```
helm repo add jetstack https://charts.jetstack.io
helm repo update
```

## Generate manifests

```
helm template \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --set installCRDs=true \
  -f helm/values.yaml --version $(cat helm/CHART_VERSION) > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

Get latest chart version like so:
```bash
helm repo update
helm search repo jetstack/cert-manager
```

```bash
../../update_helm_values.sh jetstack/cert-manager TARGET_CHART_VERSION
```
