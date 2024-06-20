> **"Full-stack" now includes a lot more pancakes.** We've added layers and layers of abstractions, tools, and professionalism into every stage of "hosting a site." This is in part due to real factors related to adding hundreds of millions of people to the internet, giving them always-on supercomputers they check at several dozen times a day, common infrastructure and cloud platforms providing solutions for minutiae that used to gate out amateur players, and the explosion of VC/zero-interest capital in the last decade meaning a ton of companies were playing the "eat the world or die" game.

-- [Pablo Meier](https://morepablo.com/2022/11/programming-culture-in-the-late-aughts.html)

Web development is an exercise in distributed execution of program, where some parts of your program execute in a (mostly) trusted environment on the server and some execute on a untrusted environment on the client.  Almost all problems in web development can be derived from this breakdown, and the limitations of each of these environments.

1. How can these two environments communicate efficiently, securely, and effectively
2. Which processing is better handled on the server and which is better handled on the client
3. Half of your program runs in an untrusted environment
4. Half of your program has a limited set of system resources that are shared between all users, performance of the server can impact all users simultaneously

None of this has even gotten to JavaScript and CSS, each of which are their own rabbit-holes.

## Links

- [JavaScript Gom Jabbar](https://frantic.im/javascript-gom-jabbar/)
- [The Web's Grain](https://frankchimero.com/blog/2015/the-webs-grain/)
- Frontend
	- [The single most impor­tant factor that dif­fer­enti­ates front-end frame­works](https://themer.dev/blog/the-single-most-important-factor-that-differentiates-front-end-frameworks)
- [Everyone Has JavaScript, Right?](https://www.kryogenix.org/code/browser/everyonehasjs.html)
- [Old CSS, new CSS](https://eev.ee/blog/2020/02/01/old-css-new-css/)
- [The Web's Grain](https://frankchimero.com/blog/2015/the-webs-grain/)
