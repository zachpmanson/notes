Fixing Keychron function keys on Linux machines.

Tested on Keychron K2v2 on Xubuntu 20.04 and 22.04 on trenzalore.

To enable Function keys on Keychron K2:
+ Set the keyboard to Windows mode
+ Run the following command:

```sh
echo 0 | sudo tee /sys/module/hid_apple/parameters/fnmode
```

To make this change persistent, add a module option for hid_apple:

```sh
echo "options hid_apple fnmode=0" | sudo tee -a /etc/modprobe.d/hid_apple.conf
```

To toggle function mode, hold Fn + X + L for 4 seconds.

If this all fails, set it back to 1:

```sh
echo 1 | sudo tee /sys/module/hid_apple/parameters/fnmode
```

## Links
Original post: https://www.reddit.com/r/MechanicalKeyboards/comments/d5io49/keychron_k2_f_keys_dont_work_w_linux_help/
Adding persistency: https://mikeshade.com/posts/keychron-linux-function-keys/
Archived Adding persistency: https://web.archive.org/web/20220721020355/https://mikeshade.com/posts/keychron-linux-function-keys/
Other Keychron settings: https://github.com/Kurgol/keychron/blob/master/k2.md)
Other Keychron settings fork: https://github.com/pavo-etc/keychron
