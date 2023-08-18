# homelab
IaC repository for managing my home kubespray cluster

# pre-reqs

1. `ansible-playbook`
2. `kubespray`

# build/update cluster

```
ansible-playbook -i inventory/mycluster/hosts.yml cluster.yml -b -v \
  --private-key=~/.ssh/private_key
```
