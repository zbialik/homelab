# Personal Kubernetes Homelab
IaC repository for managing my home kubespray cluster made up of Raspberry Pi's

# Pre-reqs
IaC repository for managing my home kubespray cluster

## init/update kubespray git submodule

```
git submodule init
git submodule update
```

## setup python virtual env

```
python3 -m venv venv
source venv/bin/activate
```

## install python depdendencies

```
pip install -r ansible/kubespray/requirements.txt
```

# Deployment Instructions

## Init/Update Kubernetes Cluster and Nodes

```
git submodule update
cd ansible/kubespray
ansible-playbook -i ../inventory/homelab/hosts.yaml  --become --become-user=root cluster.yml --user zbialik --ask-pass --ask-become-pass
```

## Access Kubernetes Cluster

For now, I just log into the control-plane node and snag the `/etc/kubernetes/admin.conf` file 

# Disaster Recovery

## Reset Kubernetes Cluster

Only perform the following when you want to completely rebuild the kubernetes cluster.

```
git submodule update
cd ansible/kubespray
ansible-playbook -i ../inventory/homelab/hosts.yaml  --become --become-user=root reset.yml --user zbialik --ask-pass --ask-become-pass
```

## Network/DNS Architecture

1. DuckDNS hosts subdomain `zeb17.duckdns.org` which targets my home router's publicly IP assigned by my ISP.
1. Setup port forwarding in my home router to send HTTPS traffic to my ingress controller IP(s)

## DuckDNS

I DuckDNS as a free service to host my DNS records under the following subdomain: zeb17.duckdns.org

I must update the subdomain IP every 30 days, and can automate that with the following command ran inside my local network:

```
curl -g https://www.duckdns.org/update?domains=zeb17&token=${DUCKDNS_TOKEN}[&verbose=true][&clear=true]
```

Where I store DUCKDNS_TOKEN in a secret vault.
