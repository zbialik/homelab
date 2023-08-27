# Updating Ingress Nginx manifests

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm template ingress-nginx ingress-nginx/ingress-nginx -n ingress-nginx -f helm/values.yaml > generated.yaml
```
