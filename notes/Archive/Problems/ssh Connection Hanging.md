I ran into a problem on Ubuntu 22.04 where any ssh connection would hang inexplicably.  It only happened on my home wifi network, not at work.

Resolved with [this thread](https://serverfault.com/questions/210408/cannot-ssh-debug1-expecting-ssh2-msg-kex-dh-gex-reply/670081#670081).


> Change the network interface MTU to solve it. This is a bug for ubuntu 14.04. This worked for me:
> 
> ```
> sudo ip li set mtu 1200 dev wlan0
> ```
> 
> OR
> 
> ```
> sudo ifconfig wlan0 mtu 1200
> ```
> 
> ssh fails to connect to VPN host - hangs at 'expecting SSH2_MSG_KEX_ECDH_REPLY'
