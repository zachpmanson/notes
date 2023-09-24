---
tags:
  - linux
---
For when Ubuntu server only takes up 98GiB for some reason, despite the HDD being much larger.

```bash
> df -h

Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              784M  1.4M  783M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   98G  7.3G   86G   8% /
tmpfs                              3.9G     0  3.9G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          2.0G  127M  1.7G   7% /boot
tmpfs                              784M  4.0K  784M   1% /run/user/1000
```

To fix (will need root access):

```bash
> vgdisplay
> lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
> resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```

Results afterwards.

```bash
> df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              784M  1.4M  783M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv  456G  7.3G  430G   2% /
tmpfs                              3.9G     0  3.9G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          2.0G  127M  1.7G   7% /boot
tmpfs                              784M  4.0K  784M   1% /run/user/1000
```

## Links

 - [Source](https://askubuntu.com/a/1330709)
