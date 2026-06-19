Using the [[Nextcloud]] AIO [[Docker]] image on [[Nix]]OS. 

I transferred from a Ubuntu installation of Nextcloud to a new machine on NixOS. The old installation had been doing daily borg backups to an external drive at `/mnt/blackup/nc-backups`.

I set up the new machine, installed the AOI docker image, plugged in the external drive to the new machine. Once that was up and running I was able to restore from the last backup on the drive. This even restored the daily backup cadence.

For some reason, a few days later the daily backup reported this failure:

```
2026-06-19T00:05:25.627864000Z Performing backup...
2026-06-19T00:05:25.628005000Z Did not find borg.config file in the mastercontainer volume.
2026-06-19T00:05:25.628245000Z Cannot create a backup as this is wrong.
```

Luckily [this GitHub thread](https://github.com/nextcloud/all-in-one/discussions/2837#discussioncomment-6275617) reports the same issue.

Solution:

The backup directory contains a borg.config file that needs to be copied into the new Docker image's volume.

```sh
[zach@naboo:~/nixos-config]$ sudo find /mnt/blackup/ -type f -name config
/mnt/blackup/nc-backups/borg/config
[zach@naboo:~/nixos-config]$ sudo cp /mnt/blackup/nc-backups/borg/config /var/lib/docker/volumes/nextcloud_aio_mastercontainer/_data/data/borg.config
```

Then the next backup ran successfully.