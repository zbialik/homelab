## Initial Raspberry Pi Setup (after flashing SD with Ubuntu + enabling SSH)

First, copy over ssh key from personal Macbook to rpi:

```
ssh-copy-id -i ~/.ssh/id_rsa IP_ADDRESS
```

Next, ensure eth0 is properly setup. SSH to rpi and do the following:

```
# check for wired connection to internet
ifconfig
```

If you don't see eth0 show up (with appropriate IP address), then write the following to /etc/systemd/network/eth0.network and reboot

```
[Match]
Name=eth0

[Network]
DHCP=yes
```

Finally, install apt depdendencies on the rpi:

```
# see this comment: https://github.com/kubernetes-sigs/kubespray/issues/9456#issuecomment-1501250889
apt-get install linux-modules-extra-raspi 
```

