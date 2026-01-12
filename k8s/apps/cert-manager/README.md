# Cert-Manager

Add helm repo
```
helm repo add jetstack https://charts.jetstack.io
helm repo update
```

## Generate manifests

```
VERSION=v1.13.3
helm template \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --set installCRDs=true \
  -f helm/values.yaml --version $VERSION > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

Get latest chart version like so:
```bash
helm repo update
helm search repo jetstack/cert-manager # redefine VERSION
helm show values --version $VERSION jetstack/cert-manager > helm/default.yaml

# update helm/values.yaml appropriately + regenerate manifests
```
