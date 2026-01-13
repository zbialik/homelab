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
TRAEFIK_VERSION=38.0.2
helm show values traefik/traefik --version $TRAEFIK_VERSION > helm/default.yaml
helm template traefik traefik/traefik --version $TRAEFIK_VERSION \
    -n traefik \
    -f helm/values.yaml > generated.yaml
```
