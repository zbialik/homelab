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
ansible-playbook -i ../inventory/homelab/hosts.yaml  --become --become-user=root cluster.yml
```


## Adding Nodes

First, copy over ssh key to raspberry pi

```
ssh-copy-id -i ~/.ssh/id_rsa IP_ADDRESS
```

Then, update the inventory for the new node.

Finally, execute:

```
cd ansible/kubespray
ansible-playbook -i ../inventory/homelab/hosts.yaml  --become --become-user=root cluster.yml
```

## Access Kubernetes Cluster

For now, I just log into the control-plane node and snag the `/etc/kubernetes/admin.conf` file 

# Disaster Recovery

## Reset Kubernetes Cluster

Only perform the following when you want to completely rebuild the kubernetes cluster.

```
git submodule update
cd ansible/kubespray
ansible-playbook -i ../inventory/homelab/hosts.yaml  --become --become-user=root reset.yml
```
