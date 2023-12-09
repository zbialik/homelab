# Updating Cilium manifests

```
helm repo add cilium https://helm.cilium.io/
helm repo update
helm template cilium -n kube-system cilium/cilium -f helm/values.yaml --version v1.13.9 > generated.yaml
```

## Update `helm/values.yaml` with changes from chart upgrade

```bash
# get curr commit sha of helm/default.yaml
CURR_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# update helm/default.yaml with changes from next chart version and commit
NEW_CHART_VERSION="v1.14.4" # update me every upgrade
helm show values cilium/cilium --version ${NEW_CHART_VERSION} > helm/default.yaml
git add .
git commit -m "updating cilium helm/default.yaml"

# get new commit sha of helm/default.yaml
NEW_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# get diff between helm/default.yaml versions + patch helm/values.yaml
git diff --relative $CURR_SHA $NEW_SHA helm/default.yaml > /tmp/values.diff
patch helm/values.yaml /tmp/values.diff

# solve all the conflicts
```
