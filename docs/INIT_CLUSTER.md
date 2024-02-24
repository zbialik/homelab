# Initializing New Cluster
This document outlines how you'd initialize a brand new kubespray cluster from scratch using this IaC repository.

# Pre-reqs (only need to do 1 time)

1. init kubespray git submodule
    ```
    git submodule init
    ```
1. setup python virtual env
    ```
    python3 -m venv venv
    ```

# Initialize Kubernetes Cluster and Nodes

1. source python venv
    ```
    source venv/bin/activate
    git submodule update
    cd ansible/kubespray
    git pull
    git checkout v2.23.1 # replace with desired tag/release
    pip install -r requirements.txt
    cd ../
    ```
1. run `cluster.yml` playbook
    ```
    ansible-playbook -i inventory/homelab/homelab.ini --become --become-user=root --user zbialik playbooks/common.yml
    ansible-playbook -i inventory/homelab/homelab.ini --become --become-user=root --user zbialik kubespray/cluster.yml
    ```
1. initialize GitOps pattern by following [this document](./INIT_GITOPS.md)
