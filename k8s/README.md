# Initialize GitOps


1. `cd` to root repository directory
1. deploy initial k8s infra
    ```
    kubectl apply -k k8s/kube-system/sealed-secrets
    kubectl apply -k k8s/metallb-system/metallb # may need to execute twice for CRD
    kubectl apply -k k8s/cert-manager/cert-manager

    # will need to create sealed secret first
    kubectl apply -k k8s/cert-manager/cert-manager-webhook-duckdns

    # will need to wait for cert-manager-webhook-duckdns
    kubectl apply -k k8s/ingress-nginx/ingress-nginx
    ```
1. install argocd cli: 
    ```
    brew install argocd
    ```
1. generate bcrypt has of desired password: 
    ```
    BCRYPT_PW=`argocd account bcrypt --password <YOUR-PASSWORD-HERE>`
    ```
1. create secret ArgoCD `Secret` from bcrypted password
    ```
    kubectl create ns argocd
    kubectl create secret generic argocd-secret -n argocd \
        --from-literal=admin.password=${BCRYPT_PW} \
        --from-literal=admin.passwordMtime="$(date +%FT%T%Z)"
    ```
1. deploy ArgoCD
    ```
    kubectl apply -k k8s/argocd/argocd

    # NOTE: ignore the error about SealedSecret CRD not existing yet
    ```
1. initialize Gitops
    ```
    kubectl apply -f root.yaml
    ```
