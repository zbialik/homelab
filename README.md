# Personal Kubernetes Homelab
IaC repository for managing my home kubespray cluster made up of Raspberry Pi's

# Pre-reqs
IaC repository for managing my home kubespray cluster

- Ubuntu 22 on Raspberry Pi (Model 4)

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

## install apt depdendencies

```
# see this comment: https://github.com/kubernetes-sigs/kubespray/issues/9456#issuecomment-1501250889
apt-get install linux-modules-extra-raspi 
```

# Deployment Instructions

## source virtual env

```
source venv/bin/activate
```

## init/update k8s cluster and nodes

```
git submodule update
cd ansible/kubespray
ansible-playbook -i ../inventory/homelab/hosts.yaml  --become --become-user=root cluster.yml --user zbialik --ask-pass --ask-become-pass
```


## access k8s cluster

```
TBD
```

# Disaster Recovery

## reset k8s cluster

Only perform the following when you want to completely rebuild the kubernetes cluster.

```
git submodule update
cd ansible/kubespray
ansible-playbook -i ../inventory/homelab/hosts.yaml  --become --become-user=root reset.yml --user zbialik --ask-pass --ask-become-pass
```
