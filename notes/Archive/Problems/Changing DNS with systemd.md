On systems using systemd, `/etc/resolve` is managed by systemd. To change DNS server, you need to edit `/etc/systemd/resolved.conf`.


```
[Resolve]
DNS=8.8.8.8
#FallbackDNS=8.8.8.8
#Domains=
#DNSSEC=no
#DNSOverTLS=no
#MulticastDNS=no
#LLMNR=no
#Cache=no-negative
#CacheFromLocalhost=no
DNSStubListener=no
#DNSStubListenerExtra=
#ReadEtcHosts=yes
#ResolveUnicastSingleLabel=no
```

Then restart services:

```sh
sudo systemctl daemon-reload
sudo systemctl restart systemd-networkd
sudo systemctl restart systemd-resolved
```

Tags: #linux