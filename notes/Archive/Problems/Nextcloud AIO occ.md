---
tags:
  - nextcloud
  - self-hosting
---
To access the `occ` command when running Nextcloud through the [[Notes/Software/Programs/Docker]] AIO.  Tested on Ubuntu 22.04.2.

```bash
sudo docker exec --user www-data -it nextcloud-aio-nextcloud php occ <commands>
```

For example:

```bash
sudo docker exec --user www-data -it nextcloud-aio-nextcloud php occ config:app:set text rich_editing_enabled --value=0
```
