# argocd

## Updating admin password

```
# install argocd CLI
brew install argocd

# generate and copy bcrypt hash of desired password to clipboard
BCRYPT_PW=`argocd account bcrypt --password <YOUR-PASSWORD-HERE>`

# generate plaintext secret
kubectl create secret generic argocd-secret -n argocd \
    --from-literal=admin.password=${BCRYPT_PW} \
    --from-literal=admin.passwordMtime="$(date +%FT%T%Z)" \
    --from-literal=tls.crt="" \
    --from-literal=tls.key="" \
    --dry-run -o yaml > /tmp/secret.yaml

# seal the secret
kubeseal -f /tmp/secret.yaml -w sealed-secret.yaml

# upon commit/update you need to bounce argocd
kubectl -n argocd rollout restart sts,deploy -l app=argocd
```
