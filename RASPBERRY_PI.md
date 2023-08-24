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

Then, install apt depdendencies on the rpi:

```
# see this comment: https://github.com/kubernetes-sigs/kubespray/issues/9456#issuecomment-1501250889
apt-get install linux-modules-extra-raspi 
```
