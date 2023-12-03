# Updating Metallb manifests

```
helm repo add metallb https://metallb.github.io/metallb
helm repo update
helm template metallb metallb/metallb -f helm/values.yaml -n metallb-system > generated.yaml
```

You'll also need to grab the CRD's separately, which I got from [here](https://doc.traefik.io/traefik/reference/dynamic-configuration/kubernetes-crd/)

## Update `helm/values.yaml` with changes from chart upgrade

```bash
# get curr commit sha of helm/default.yaml
CURR_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# update helm/default.yaml with changes from next chart version and commit
helm show values metallb/metallb > helm/default.yaml
git add .
git commit -m "updating metallb helm/default.yaml"

# get new commit sha of helm/default.yaml
NEW_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# get diff between helm/default.yaml versions + patch helm/values.yaml
git diff --relative $CURR_SHA $NEW_SHA helm/default.yaml > /tmp/values.diff
patch helm/values.yaml /tmp/values.diff

# solve all the conflicts
```
