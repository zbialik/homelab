# traefik

## install

```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update
```

## upgrades

```bash
# identify chart version
helm search repo traefik/traefik -l

# update version
VERSION=38.0.2
helm show values traefik/traefik --version $VERSION > helm/default.yaml
helm template traefik traefik/traefik --version $VERSION \
    -n traefik \
    -f helm/values.yaml > generated.yaml
```
