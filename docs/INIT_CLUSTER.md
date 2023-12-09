# Initializing New Cluster
This document outlines how you'd initialize a brand new kubespray cluster from scratch using this IaC repository.

# Pre-reqs (only need to do 1 time)

1. make sure all Raspberry Pi's are setup based on the [instructions here](./RASPBERRY_PI.md).
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
    ```
1. update kubespray git submodule
    ```
    git submodule update
    ```
1. cd kubespray folder, checkout desired git tag/release, and install relevant python packages
    ```
    cd ansible/kubespray
    git pull
    git checkout v2.23.1 # replace with desired tag/release
    pip install -r requirements.txt
    ```
1. run `cluster.yml` playbook
    ```
    ansible-playbook -i ../inventory/homelab/hosts.yaml  --become --become-user=root cluster.yml --user zbialik 
    ```
1. initialize GitOps pattern by following [this document](../k8s/README.md)
