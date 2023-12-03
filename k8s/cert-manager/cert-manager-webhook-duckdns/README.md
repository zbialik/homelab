# cert-manager custom webhook

https://github.com/ebrianne/cert-manager-webhook-duckdns

```
helm template cert-manager-webhook-duckdns \
    --namespace cert-manager \
    ./chart \
    -f helm/values.yaml > generated.yaml
```

## Update secret token

```
# generate plaintext secret
kubectl create secret generic duckdns-token -n cert-manager \
    --from-literal=token=${DUCKDNS_TOKEN} \
    --dry-run -o yaml > /tmp/secret.yaml

# seal the secret
kubeseal -f /tmp/secret.yaml -w sealed-secret.yaml
```
