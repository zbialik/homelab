# Personal Kubernetes Homelab
IaC repository for managing my home kubespray cluster made up of Raspberry Pi's

If building the cluster as-new, goto [this doc](docs/INIT_CLUSTER.md).

# Cluster Maintenance

## Update Cluster Configs

```
git submodule update
source venv/bin/activate
cd ansible
ansible-playbook -i inventory/homelab/hosts.yaml --become --become-user=root  --user zbialik playbooks/cluster.yml
mv ~/.kube/homelab ~/.kube/homelab.bak && cp -rp inventory/homelab/artifacts/admin.conf ~/.kube/homelab
```

## Kubernetes Version Upgrades

```
git submodule update
source venv/bin/activate
cd ansible/kubespray
git pull
git checkout ${desired_kubespray_release_tag}
pip install requirements.txt
cd ../
ansible-playbook -i inventory/homelab/hosts.yaml --become --become-user=root  --user zbialik playbooks/cluster.yml
```

## Adding Worker Node

1. Configure env
    ```
    git submodule update
    source venv/bin/activate
    cd ansible
    ```
1. Run the `raspberrypi-patch.yml` for the desired host (**WARNING: this will reboot the server**)
    ```
    ansible-playbook -i inventory/homelab/hosts.yaml --become --become-user=root --user zbialik playbooks/raspberrypi-patch.yml --limit=$NODE_NAME
    ```
1. Run the `facts.yml` playbook for all hosts
    ```
    ansible-playbook -i inventory/homelab/hosts.yaml --become --become-user=root --user zbialik kubespray/facts.yml
    ```
1. Run the `scale.yml` playbook for the desired host
    ```
    ansible-playbook -i inventory/homelab/hosts.yaml --become --become-user=root --user zbialik playbooks/scale.yml --limit=$NODE_NAME
    ```

## Updating Worker Node (e.g. apt packages)

1. Prepare the `Node` by draining all workloads
    ```
    kubectl drain $NODE_NAME --ignore-daemonsets --delete-local-data
    ```
1. Configure the ansible env
    ```
    git submodule update
    source venv/bin/activate
    cd ansible
    ```
1. Run the `raspberrypi-patch.yml` for the desired host (**WARNING: this will reboot the server**)
    ```
    ansible-playbook -i inventory/homelab/hosts.yaml --become --become-user=root --user zbialik raspberrypi-patch.yml --limit=$NODE_NAME
    ```
1. Uncordon the `Node`
    ```
    kubectl uncordon $NODE_NAME
    ```

# Disaster Recovery

Only perform the following when you want to completely rebuild the kubernetes cluster.

```
git submodule update
source venv/bin/activate
cd ansible
ansible-playbook -i inventory/homelab/hosts.yaml --become --become-user=root --user zbialik kubespray/reset.yml
```

## Ingress/DNS

### DuckDNS

I DuckDNS as a free service to host my DNS records under the following subdomain: zeb17.duckdns.org

I must update the subdomain IP every 30 days, and can automate that with curl commands.

#### Internal DNS

1. DuckDNS hosts subdomain `zeb17-int.duckdns.org` which targets ingress-controller's internal IP (`192.168.1.100`).

Update record like so:

```
curl -g "https://www.duckdns.org/update/zeb17-int/${DUCKDNS_TOKEN}/192.168.1.100"
```

#### External DNS

I've since disabled external access, but if I were to set this up again, I'd start with something like:

1. DuckDNS hosts subdomain `zeb17-ext.duckdns.org` which targets ingress-controller's internal IP (`192.168.1.200`).
1. Setup Port Forwarding (in NAT forwarding section in my Archer C7 router) to route `443` --> `443` on ingress-controller's internal IP (`192.168.1.200`).

Update record like so:

```
curl -g "https://www.duckdns.org/update/zeb17-ext/${DUCKDNS_TOKEN}/"
```

NOTE: I would want to do some network segmentation here ideally. Maybe using a separate set of ingress controllers for the externally reachable records and hosting these on isolated hosts.
