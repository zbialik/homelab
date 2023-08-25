# Initialize GitOps

```
# 1. initialize ArgoCD
kubectl apply -k argocd/argocd

# 2. initialize GitOps
kubectl apply -f root.yaml
```

