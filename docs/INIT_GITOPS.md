# Initialize GitOps


1. `cd` to root repository directory
1. deploy namespaces + sealed secrets
    ```
    kubectl apply -R -f k8s/apps/namespaces
    kubectl apply -k k8s/apps/sealed-secrets
    ```
1. seal all needed secrets
    ```
    # seal cert-manager-webhook-duckdns secret
    kubectl create secret generic duckdns-token -n cert-manager \
        --from-literal=token=${DUCKDNS_TOKEN} \
        --dry-run=client -o yaml > /tmp/secret.yaml
    kubeseal -f /tmp/secret.yaml -w k8s/apps/cert-manager-webhook-duckdns/sealed-secret.yaml

    # seal argocd secret
    brew install argocd # to generate bcrypt has of desired password
    BCRYPT_PW=`argocd account bcrypt --password ${ARGOCD_ADMIN_PASSWORD}` 

    kubectl create secret generic argocd-secret -n argocd \
        --from-literal=admin.password=${BCRYPT_PW} \
        --from-literal=admin.passwordMtime="$(date +%FT%T%Z)" \
        --dry-run=client -o yaml > /tmp/secret.yaml
    kubeseal -f /tmp/secret.yaml -w k8s/apps/argocd/sealed-secret.yaml
    ```
1. deploy argocd
    ```
    kubectl apply -k k8s/apps/argocd
    ```
1. initialize gitops!
    ```
    git add . 
    git commit -m "initializing gitops w/sealed secrets"
    git push
    kubectl apply -f k8s/root.yaml
    ```
