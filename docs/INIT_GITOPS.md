# Initialize GitOps


1. `cd` to root repository directory
1. deploy initial k8s infra
    ```
    kubectl apply -R -f k8s/namespaces/namespaces
    kubectl apply -k k8s/kube-system/sealed-secrets
    kubectl apply -k k8s/metallb-system/metallb # may need to execute twice for CRD
    kubectl apply -k k8s/cert-manager/cert-manager
    ```
1. seal cert-manager-webhook-duckdns secret + deploy
    ```
    # seal the secret
    kubectl create secret generic duckdns-token -n cert-manager \
        --from-literal=token=${DUCKDNS_TOKEN} \
        --dry-run=client -o yaml > /tmp/secret.yaml
    kubeseal -f /tmp/secret.yaml -w k8s/cert-manager/cert-manager-webhook-duckdns/sealed-secret.yaml

    # deploy cert-manager-webhook-duckdns
    kubectl apply -k k8s/cert-manager/cert-manager-webhook-duckdns
    ```
1. deploy ingress-nginx (LoadBalancer wildcard cert will take a bit to sync via webhook duckdns)
    ```
    # will need to wait for cert-manager-webhook-duckdns
    kubectl apply -k k8s/ingress-nginx/ingress-nginx
    ```
1. seal argocd admin secret + deploy
    ```
    # install argocd cli
    brew install argocd
    
    # generate bcrypt has of desired password
    BCRYPT_PW=`argocd account bcrypt --password ${ARGOCD_ADMIN_PASSWORD}`
    
    # seal the secret
    kubectl create secret generic argocd-secret -n argocd \
        --from-literal=admin.password=${BCRYPT_PW} \
        --from-literal=admin.passwordMtime="$(date +%FT%T%Z)" \
        --dry-run=client -o yaml > /tmp/secret.yaml
    kubeseal -f /tmp/secret.yaml -w k8s/argocd/argocd/sealed-secret.yaml

    # deploy argocd
    kubectl apply -k k8s/argocd/argocd
    ```
1. initialize gitops!
    ```
    kubectl apply -f k8s/root.yaml
    ```
