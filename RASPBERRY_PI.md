## Initial Raspberry Pi Setup ( + enabling SSH)

### 1. Flashing SD with Ubuntu

Use Raspberry Pi Imager to install Ubuntu Server on MicroSD with the following configs:

***TBD***

(enabling SSH)

### 2. OS Pre-reqs

Copy over ssh key from personal Macbook to rpi:

```
ssh-copy-id -i ~/.ssh/id_rsa IP_ADDRESS
```

On RaspberryPi, run:

```
sudo su -
apt update
apt install linux-modules-extra-$(uname -r)
apt-get install linux-modules-extra-raspi # https://github.com/kubernetes-sigs/kubespray/issues/9456#issuecomment-1501250889
apt upgrade
reboot
```

## (optional) Adding USB external disk

Verify connected USB storage:
```
lsblk 

NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0         7:0    0  59.2M  1 loop /snap/core20/1977
loop1         7:1    0  59.3M  1 loop /snap/core20/2019
loop2         7:2    0 109.6M  1 loop /snap/lxd/24326
loop3         7:3    0  35.5M  1 loop /snap/snapd/19998
loop4         7:4    0  35.5M  1 loop /snap/snapd/20102
sda           8:0    0 931.5G  0 disk 
mmcblk0     179:0    0 119.1G  0 disk 
├─mmcblk0p1 179:1    0   256M  0 part /boot/firmware
└─mmcblk0p2 179:2    0 118.8G  0 part /mnt/usb1
```

Execute:
```
mkfs.ext4 /dev/sda
```

Verify:
```
lsblk -f
NAME        FSTYPE   FSVER LABEL       UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
loop0       squashfs 4.0                                                          0   100% /snap/core20/1977
loop1       squashfs 4.0                                                          0   100% /snap/core20/2019
loop2       squashfs 4.0                                                          0   100% /snap/lxd/24326
loop3       squashfs 4.0                                                          0   100% /snap/snapd/19998
loop4       squashfs 4.0                                                          0   100% /snap/snapd/20102
sda         ext4     1.0               80a2c16d-b7cb-4d09-88fa-6f54f6580d64                
mmcblk0                                                                                    
├─mmcblk0p1 vfat     FAT32 system-boot F04B-5543                              64.3M    74% /boot/firmware
└─mmcblk0p2 ext4     1.0   writable    877a65cf-888e-47c6-b4e0-ec5c52c54be8  102.6G     8% /mnt/usb1
                                                                                           /
```

Create folder for mounting: 
```
mkdir /mnt/usb01
chown zbialik:zbialik -R /mnt/usb01
```

Execute/add the following line to /etc/fstab to mount storage on reboot:
```
echo "UUID=$(blkid --output value /dev/sda | head -n1) /mnt/usb01 ext4 defaults 0 0" >> /etc/fstab
```

Mount the storage to folder manually without reboot: `mount -o defaults /dev/sda /mnt/usb01`
