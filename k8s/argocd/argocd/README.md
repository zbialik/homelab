# Updating ArgoCD manifests

## 1. update `helm/values.yaml` with changes from chart upgrade

```bash
# get curr commit sha of helm/default.yaml
CURR_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# update helm/default.yaml with changes from next chart version and commit
helm show values argo/argo-cd > helm/default.yaml
git add .
git commit -m "updating argo-cd helm/default.yaml"

# get new commit sha of helm/default.yaml
NEW_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# get diff between helm/default.yaml versions + patch helm/values.yaml
git diff --relative $CURR_SHA $NEW_SHA helm/default.yaml > /tmp/values.diff
patch helm/values.yaml /tmp/values.diff && rm -rf helm/values.yaml.orig

# solve all the conflicts
```

## 2. update `generated.yaml`

```
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm template argocd -n argocd argo/argo-cd -f helm/values.yaml > generated.yaml
```



## Update admin password

```
# install argocd CLI
brew install argocd

# generate and copy bcrypt hash of desired password to clipboard
BCRYPT_PW=`argocd account bcrypt --password <YOUR-PASSWORD-HERE>`

# generate plaintext secret
kubectl create secret generic argocd-secret -n argocd \
    --from-literal=admin.password=${BCRYPT_PW} \
    --from-literal=admin.passwordMtime="$(date +%FT%T%Z)" \
    --dry-run -o yaml > /tmp/secret.yaml

# seal the secret
kubeseal -f /tmp/secret.yaml -w sealed-secret.yaml

# upon commit/update you need to bounce argocd
kubectl -n argocd rollout restart sts,deploy -l app=argocd
```
