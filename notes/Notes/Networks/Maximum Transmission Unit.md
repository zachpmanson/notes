---
tags:
  - relics
---

A maximum transmission unit is the max size a given protocol can transmit in a single transaction in a network.

To this day, the Ethernet MTU is 1500 bytes.  This is a relic of the Xerox Alto computer.

> if you add the Ethernet header – 36 bytes – then an MTU of 1500 plus that header is 1536 bytes, which is 12288 bits, which takes 2^12 microseconds to transmit at 3Mb/second, and because the [Xerox Alto](https://en.wikipedia.org/wiki/Xerox_Alto) computer for which Ethernet was invented had an internal data path that ran at 3Mhz, then you could _just_ write the bits into the Alto’s memory at the precise speed at which they arrived, saving the very-expensive-then cost of extra silicon for an interface or any buffering hardware.

-- [Mike Hoye](https://exple.tive.org/blarg/2024/04/24/magic-numbers/)
