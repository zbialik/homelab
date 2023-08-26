# Updating ArgoCD manifests

```
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm template argocd -n argocd argo/argo-cd -f helm/values.yaml > generated.yaml
```
