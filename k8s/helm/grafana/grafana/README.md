# Updating manifests

## Update admin credentials sealed secret

```
kubectl create secret generic grafana-admin -n grafana \
    --from-literal=username=${ADMIN_USER} \
    --from-literal=password=${ADMIN_PASSWORD} \
    --dry-run -o yaml > /tmp/secret.yaml
kubeseal -f /tmp/secret.yaml -w sealed-secret.yaml
```

