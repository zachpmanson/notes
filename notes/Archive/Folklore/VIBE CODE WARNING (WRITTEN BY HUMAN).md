[Written by Borislav Nikolov on 2025-11-10.](https://github.com/jackdoe/pico2-swd-riscv#0-vibe-code-warning-written-by-human) 

---

About 80% of the code is vibe coded; The readme is almost completely generated (except the whole vibe-code-warning section). I spent many nights with the oscilloscope and the docs and made a working prototype that was able ti do sba/read/write regs and do abstract commands and progbuf, the rest was done with claude code. The tests are quite [comprehensive test suite](https://github.com/jackdoe/pico2-swd-riscv/blob/master/examples/test_suite) and I use the core of the library in my own projects, but, as they say, "hic sunt dracones". I also read the readme and the code didn't notice anything wrong (and removed the wrong/unclear parts).

This project was my casestudy of vibecoding a more complicated project that I dont understand 100% and there is no obvious existing code that can be "used". It started as ~1000 loc that I have written and knew very well, reading the rp2350, arm swd and riscv debug docs, capturing data with oscilloscope and openocd then decoding it and analyzing the wakeup sequence and then read/write commands. After I got it working I gave it to claude to make it into a library that I can use in other projects, and then I slowly built it up.

After about 3-4k lines of code I completely lost track of what is going on, and I woudn't consider this code that I have written, but adding more and more tests felt "nice", or at least reassuring.

There was a some gaslighting, particularly when it misunderstood dap_read_mem32 thinking it is reading from ram and not MEM-AP TAR/DRW/RDBUFF protocol, which lead to incredible amount of nonsense.

Overall I would say it was a horrible experience, even though it took 10 hours to write close to 10000 lines of code, I don't consider this my project, and I have no sense of acomplishment or growth.

In contrast, using AI to read all the docs (which are thousands of pages) and write helpful scripts to decode the oscilloscope data, create packed C structs from docs and etc, was very nice, and I did feel good after. The moment I read the first register and then when I was able to read memory via SBA I felt amazing.

The main issue is `taste`, when I write code I feel if its good or bad, as I am writing it, I know if its wrong, but using claude code I get desensitized very quickly and I just can't tell, it "reads" OK, but I don't know how it feels. In this case it happened when the code grew about 4x, from 1k to 4k lines. And worse of all, my mental model of the code is completely gone, and with it my ownership.

**The tokens have no reason or purpose**, which makes reading code ridiculously difficult, as and each token can be complete nonsense. When reading human code the symbols have a purpose, someone thought "I will put this in a variable, later I will check its status.", so I pretend I am them, and think `why` would they have written this? Shortly after I understand, as they are human and I am human. But the AI symbols have no reason, and worse of all, they all look deceptively correct, so I have to think 10 times harder if it is wrong. With any human code (including your own) it is quite easy to gauge how much you can trust it, and it is quite consistent, with the AI code, one function can be much better than what you woudld've written, and the code 2 lines below can be cargo culted gunk that looks incredibly good, but is structurally wrong.

In the end I would say I have gained good understanding of the wires, timings, and the lower level ap/dp mechanics, sba and progbuf, but I regret not writing the whole thing myself, even if it would've taken 10x the time.

I fucking hate this.

And I can not help, but feel dusgust and shame. Is this what programming is now? I really hope this is some intermediate stage and it changes for the better, the problem is I dont know what "better" is, it seems for some people is not writing the code, for others is not modeling the problem and for third is not having to think. For me, I am not sure, I do want to make things, and many times I dont want to know something, but I want to use it, e.g. the rp2350 usb host controller the way you have to re-arm interrupts and the way the epx register is shared is super annoying, for good reasons probably, but I just want to use it to make my CBI driver.

I guess the question is what is the thing I want to make, because you can go way up the stack, from the USB chip registers to CBI to UFI to FAT16 to the OS of the old school computer I am making, but why stop? make the schematics, the pcbs, the cad files, maybe automatically send it to the factory? and then just ship it to me? but why stop? make my webshop, start selling, make a community, ads, marketing, generate some unboxing videos, maybe some viral memes? process the orders directly to the factory, on demand, if there is an issue, it is ready with customer support.

What do I do in the meanwhile? Sit on the beach? I hate the beach.

Where does it stop?