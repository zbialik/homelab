# Pre-req before cluster init + gitops

By using Ubuntu on these Raspberry Pi's, only the `wlan0` gets setup automatically. We need to manually update the network setup so that the pi's setup `eth0` properly (and get the IP from DHCP).

To do this, create a tmp.ini with the IP assigned to the Pi via Wi-Fi and then run the `setup-pi.yml` ansible playbook like so:

```
ansible-playbook -i /tmp/homelab.ini --become --become-user=root playbooks/network.yml
ansible-playbook -i /tmp/homelab.ini --become --become-user=root playbooks/common.yml
```
