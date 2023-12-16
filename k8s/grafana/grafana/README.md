# Updating manifests

```
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm template grafana -f helm/values.yaml grafana/grafana --version 7.0.17 > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

```bash
# get curr commit sha of helm/default.yaml
CURR_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# update helm/default.yaml with changes from next chart version and commit
helm show values grafana/grafana --version 7.0.17 > helm/default.yaml
git add .
git commit -m "updating longhorn helm/default.yaml"

# get new commit sha of helm/default.yaml
NEW_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# get diff between helm/default.yaml versions + patch helm/values.yaml
git diff --relative $CURR_SHA $NEW_SHA helm/default.yaml > /tmp/values.diff
patch helm/values.yaml /tmp/values.diff 
rm -rf helm/values.yaml.*

# solve all the conflicts
```


## Update admin credentials sealed secret

```
kubectl create secret generic grafana-admin -n grafana \
    --from-literal=username=${ADMIN_USER} \
    --from-literal=password=${ADMIN_PASSWORD} \
    --dry-run -o yaml > /tmp/secret.yaml
kubeseal -f /tmp/secret.yaml -w sealed-secret.yaml
```
