# Updating manifests

```
helm repo add longhorn https://charts.longhorn.io
helm repo update
helm template -f helm/values.yaml longhorn/longhorn --namespace longhorn-system --version 1.5.3 > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

```bash
# get curr commit sha of helm/default.yaml
CURR_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# update helm/default.yaml with changes from next chart version and commit
helm show values longhorn/longhorn --version 1.5.3 > helm/default.yaml
git add .
git commit -m "updating longhorn helm/default.yaml"

# get new commit sha of helm/default.yaml
NEW_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# get diff between helm/default.yaml versions + patch helm/values.yaml
git diff --relative $CURR_SHA $NEW_SHA helm/default.yaml > /tmp/values.diff
patch helm/values.yaml /tmp/values.diff && rm -rf helm/values.yaml.*

# solve all the conflicts
```
