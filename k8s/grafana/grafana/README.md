# Updating manifests

```
# create plain text secret
kubectl create secret generic -n grafana grafana-admin \
    --from-literal=admin=admin \
    --from-literal=password="$(GRAFANA_ADMIN_PASSWORD)" \
    --dry-run -o yaml > /tmp/secret.yaml

# seal the secret
kubeseal -f /tmp/secret.yaml -w sealed-secret.yaml
```