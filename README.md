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

## Ingres/DNS

### DuckDNS

I DuckDNS as a free service to host my DNS records under the following subdomain: zeb17.duckdns.org

I must update the subdomain IP every 30 days, and can automate that with curl commands.

#### Internal DNS

1. DuckDNS hosts subdomain `zeb17-int.duckdns.org` which targets ingress-controller's internal IP (`192.168.0.181`).

Update record like so:

```
curl -g "https://www.duckdns.org/update/zeb17-int/${DUCKDNS_TOKEN}/192.168.0.181"
```

#### External DNS

I've since disabled external access, but if I were to set this up again, I'd start with something like:

1. DuckDNS hosts subdomain `zeb17-ext.duckdns.org` which targets ingress-controller's internal IP (`192.168.0.181`).
1. Setup Port Forwarding (in NAT forwarding section in my Archer C7 router) to route `443` --> `443` on ingress-controller's internal IP (`192.168.0.181`).

Update record like so:

```
curl -g "https://www.duckdns.org/update/zeb17-ext/${DUCKDNS_TOKEN}/"
```

NOTE: I would want to do some network segmentation here ideally. Maybe using a separate set of ingress controllers for the externally reachable records and hosting these on isolated hosts.
