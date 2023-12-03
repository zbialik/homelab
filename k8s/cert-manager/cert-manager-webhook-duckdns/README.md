# cert-manager custom webhook

https://github.com/ebrianne/cert-manager-webhook-duckdns

```
helm template cert-manager-webhook-duckdns \
    --namespace cert-manager \
    ./chart \
    -f helm/values.yaml > generated.yaml
```