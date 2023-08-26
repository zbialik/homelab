# Updating Traefik manifests

```
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm template traefik traefik/traefik -f helm/values.yaml > generated.yaml
```

You'll also need to grab the CRD's separately, which I got from [here](https://doc.traefik.io/traefik/reference/dynamic-configuration/kubernetes-crd/)
