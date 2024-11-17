# Updating manifests

```
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

## Generate manifests

```
VERSION=7.0.17
helm template grafana grafana/grafana \
    -f helm/values.yaml \
    --version $VERSION > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

Get latest chart version like so:
```bash
helm repo update
helm search repo grafana/grafana # update VERSION
helm show values grafana/grafana --version $VERSION > helm/default.yaml

# update helm/values.yaml appropriately + regenerate manifests
```

```bash
../../update_helm_values.sh grafana/grafana TARGET_CHART_VERSION
```

## Update admin credentials sealed secret

```
kubectl create secret generic grafana-admin -n grafana \
    --from-literal=username=${ADMIN_USER} \
    --from-literal=password=${ADMIN_PASSWORD} \
    --dry-run -o yaml > /tmp/secret.yaml
kubeseal -f /tmp/secret.yaml -w sealed-secret.yaml
```
