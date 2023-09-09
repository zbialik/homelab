# Updating MySQL manifests

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm template mysql bitnami/mysql -n jhu -f helm/values.yaml > generated.yaml
```
