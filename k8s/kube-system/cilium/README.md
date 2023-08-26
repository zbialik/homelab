# Updating Cilium manifests

```
helm repo add cilium https://helm.cilium.io/
helm repo update
helm template cilium -n kube-system cilium/cilium -f helm/values.yaml > generated.yaml
```
