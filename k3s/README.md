# k3s

Build cluster by:

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
