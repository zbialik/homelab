```
helm repo add gitlab https://charts.gitlab.io
helm repo update gitlab
```

```
helm template --namespace jhu gitlab-runner -f helm/values.yaml gitlab/gitlab-runner > generated.yaml
```



### runner secret

```
# generate plaintext secret
kubectl create secret generic gitlab-runner-secret -n jhu \
    --from-literal=runner-registration-token="" \
    --from-literal=runner-token="REDACTED" \
    --dry-run -o yaml > /tmp/secret.yaml

# seal the secret
kubeseal -f /tmp/secret.yaml -w sealed-token.yaml
```
