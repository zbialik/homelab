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


## Initial Raspberry Pi Setup (after flashing SD with Ubuntu + enabling SSH)

First, copy over ssh key from personal Macbook to rpi:

```
ssh-copy-id -i ~/.ssh/id_rsa IP_ADDRESS
```

Next, ensure eth0 is properly setup. SSH to rpi and do the following:

```
# check for wired connection to internet
ifconfig

# if you don't see eth0 show up (with appropriate IP address), then do the following
sudo dhclient -v 

# check that this fixed things
ifconfig

# update crontab to always perform this eth0 attachment on boot
sudo crontab -e

# and on a new line, at the end, add the following line: 
@reboot dhclient -v
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
