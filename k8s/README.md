# Initialize GitOps


1. install argocd cli: 
    ```
    brew install argocd
    ```
1. generate bcrypt has of desired password: 
    ```
    argocd account bcrypt --password <YOUR-PASSWORD-HERE>
    ```
1. set bcrypt hash in `values.yaml` at `configs.secret.argocdServerAdminPassword`
1. helm generate k8s manifests: 
    ```
    helm repo add argo https://argoproj.github.io/argo-helm
    helm template argocd -n argocd argo/argo-cd -f argocd/argocd/helm/values.yaml > argocd/argocd/generated.yaml
    ```
1. deploy ArgoCD
    ```
    kubectl apply -k argocd/argocd
    ```
1. initialize Gitops
    ```
    kubectl apply -f root.yaml
    ```
