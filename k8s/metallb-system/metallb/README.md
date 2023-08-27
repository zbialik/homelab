# Updating Metallb manifests

```
helm repo add metallb https://metallb.github.io/metallb
helm repo update
helm template metallb metallb/metallb -f helm/values.yaml -n metallb-system > generated.yaml
```

You'll also need to grab the CRD's separately, which I got from [here](https://doc.traefik.io/traefik/reference/dynamic-configuration/kubernetes-crd/)
