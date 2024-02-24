# k3s

## k3s cluster init/maintenance

1. copy configs for each Node to `/etc/rancher/k3s/config.yaml`, respectively
1. on rpi01, execute:
    ```
    curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server" INSTALL_K3S_VERSION=v1.28.6+k3s2 sh -s
    
    cat /var/lib/rancher/k3s/server/node-token # will need this for remaining node bootstrap commands
    ```
1. on rpi02 and rpi03, execute:
    ```
    curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="agent" INSTALL_K3S_VERSION=v1.28.6+k3s2 K3S_URL=https://IP_RPI01:6443 K3S_TOKEN=redacted sh -s 
    ```
1. on local machine execute:
    ```
    scp rpi01:/home/zbialik/.kube/config ~/.kube/homelab && sed -i 's|127.0.0.1|rpi01|g' ~/.kube/homelab
    kubectl label no rpi02 rpi03 node-role.kubernetes.io/worker= # to add worker role label to agents
    ```

## Initialize GitOps

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
