# Infrastructure Maintenace with Ansible/Kubespray

## Initializing/Updating Cluster

This section outlines how you'd initialize a brand new kubespray cluster from scratch using this IaC repository.

### Pre-reqs

Run the below if this is your first time cloning this repo:
```bash
git submodule init # init kubespray submodule locally
python3 -m venv venv # init python venv to use
```

For all follow-on maintenance sections, it's required that the below has also been executed beforehand:
```bash
git submodule update
source venv/bin/activate
cd ansible/kubespray
git pull
git checkout ${KUBESPRAY_GIT_TAG} # replace with desired tag/release
pip install -r requirements.txt
cd ../
```

### Playbook: Cluster Init/Update

To initialize the cluster or update specific cluster settings:
```bash
ansible-playbook -i inventory/homelab/homelab.ini --become --become-user=root --user zbialik kubespray/playbooks/cluster.yml
```

### Playbook: Kubernetes Version Upgrade

To perform a cluster upgrade:
```bash
cd kubespray
git pull
git checkout ${KUBESPRAY_GIT_TAG} # replace with desired tag/release
pip install -r requirements.txt
cd ../
rm -rf inventory/sample
mv kubespray/inventory/sample inventory/sample

# use the git diffs for the ansible vars in the sample inventory to make tweak to inventory as-neeeded

# execute cluster upgrade playbook
ansible-playbook -i inventory/homelab/homelab.ini --become --become-user=root  --user zbialik kubespray/playbooks/cluster.yml -e upgrade_cluster_setup=true
```

### Playbook: Add Kubernetes Worker Node

To add a new worker node to the cluster:
```bash
# OS update playbook (if appropriate)
ansible-playbook -i inventory/homelab/homelab.ini --become --become-user=root --user zbialik playbooks/os-update.yml --limit=$NODE_NAME

# Reboot each host if the above is done

# kubespray playbooks
ansible-playbook -i inventory/homelab/homelab.ini --become --become-user=root --user zbialik kubespray/playbooks/facts.yml
ansible-playbook -i inventory/homelab/homelab.ini --become --become-user=root --user zbialik kubespray/playbooks/scale.yml --limit=$NODE_NAME
```
