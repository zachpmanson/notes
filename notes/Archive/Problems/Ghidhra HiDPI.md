Making Ghidra scale on HiDPI screens.

Tested on Kali Linux 5.18.0-kali5-amd64, Ghidra 10.1.4, Java 11.0.16.

Ghidra doesn't scale to HiDPI screens, but this can be fixed by modifying the `launch.properties` file.  This is located in `<GhidraInstallDir>/support/launch.properties`, which when installed using apt is `/usr/share/ghidra/support/launch.properties`.

Change this setting:
```
VMARGS_LINUX=-Dsun.java2d.uiScale=1
```
to:
```
VMARGS_LINUX=-Dsun.java2d.uiScale=2
```

Source: https://gist.github.com/nstarke/baa031e0cab64a608c9bd77d73c50fc6