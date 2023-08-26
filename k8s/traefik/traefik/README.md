# Updating Traefik manifests

```
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm template traefik traefik/traefik -f helm/values.yaml > generated.yaml
```
