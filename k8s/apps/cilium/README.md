# cilium

## install

```bash
helm repo add cilium https://helm.cilium.io/
helm repo update
```

## upgrades

```bash
# identify chart version
helm search repo cilium/cilium -l

# update version
CILIUM_VERSION=1.18.5
helm show values cilium/cilium --version $CILIUM_VERSION > helm/default.yaml
helm template cilium cilium/cilium --version $CILIUM_VERSION \
    -n kube-system \
    -f helm/values.yaml > generated.yaml
```