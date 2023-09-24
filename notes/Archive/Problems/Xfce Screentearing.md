---
tags:
  - linux
---
Tested myself on Xfce 4.12 on Xubuntu 20.04 on trenzalore (Intel HD Graphics 530), allegedly works on Xubuntu 16.04.03.

Create file `/etc/X11/xorg.conf` with the content:
```
		Section "Device"
			Identifier	"Intel Graphics"
			Driver		"intel"
			Option		"AccelMethod"	"sna"
			Option		"TearFree"	"true"
		EndSection
```

## Links

 - [Source](https://forum.xfce.org/viewtopic.php?id=12019)
