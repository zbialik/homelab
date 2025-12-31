# ArgoCD

# Updating manifests

Add helm repo:
```
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
```

## Chart upgrades

1. Get latest chart version like so:
    ```bash
    helm repo update
    helm search repo argo/argo-cd # redefine VERSION
    helm show values argo/argo-cd --version $VERSION > helm/default.yaml
    ```

## Generate manifests

```bash
VERSION=9.2.3
helm template \
    argocd argo/argo-cd \
    -n argocd \
    -f helm/values.yaml --version $VERSION --include-crds > generated.yaml
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
