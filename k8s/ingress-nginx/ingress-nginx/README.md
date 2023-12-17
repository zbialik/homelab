# Updating Ingress Nginx manifests

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm template ingress-nginx ingress-nginx/ingress-nginx -n ingress-nginx -f helm/values.yaml --version 4.8.4 > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

```bash
# get curr commit sha of helm/default.yaml
CURR_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# update helm/default.yaml with changes from next chart version and commit
helm show values ingress-nginx/ingress-nginx > helm/default.yaml
git add .
git commit -m "updating ingress-nginx helm/default.yaml"

# get new commit sha of helm/default.yaml
NEW_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# get diff between helm/default.yaml versions + patch helm/values.yaml
git diff --relative $CURR_SHA $NEW_SHA helm/default.yaml > /tmp/values.diff
patch helm/values.yaml /tmp/values.diff

# solve all the conflicts
```
