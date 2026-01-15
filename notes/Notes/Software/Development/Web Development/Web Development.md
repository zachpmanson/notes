---
tags:
  - posts
date: 2026-01-14
---

> **"Full-stack" now includes a lot more pancakes.** We've added layers and layers of abstractions, tools, and professionalism into every stage of "hosting a site." This is in part due to real factors related to adding hundreds of millions of people to the internet, giving them always-on supercomputers they check at several dozen times a day, common infrastructure and cloud platforms providing solutions for minutiae that used to gate out amateur players, and the explosion of VC/zero-interest capital in the last decade meaning a ton of companies were playing the "eat the world or die" game.

-- [Pablo Meier](https://morepablo.com/2022/11/programming-culture-in-the-late-aughts.html)

Web development is an exercise in distributed execution of program, where some parts of your program execute in a (mostly) trusted environment on the server and some execute on a untrusted environment on the client.  Almost all problems in web development can be derived from this breakdown, and the limitations of each of these environments.

1. How can these two environments communicate efficiently, securely, and effectively
2. Which processing is better handled on the server and which is better handled on the client
3. Half of your program runs in an untrusted environment
4. Half of your program has a limited set of system resources that are shared between all users, performance of the server can impact all users simultaneously

None of this has even gotten to [[JavaScript]] and [[CSS]], each of which are their own rabbit-holes.

Problems that arise from this:

- You have a machine in your house you want to serve [[HTML]] files to people on the internet (Apache, Nginx)
	- They don't look pretty (CSS)
		- Your CSS looks bad on small screens! (responsive design, flexbox)
	- There's no way to make them change without manually changing the HTML (server rendering, initially with Perl, PHP)
		- You want your users to be able to send information to you (HTML Forms and later APIs)
			- You want certain users to see different things ([[Authentication]] and [[Authorization]])
		- You want to store data used to render your site, and store data about your users ([[databases]], MySQL, [[Notes/Software/Programs/Postgres]])
			- You need to ensure that your users can't sneak database queries into their data ([[SQL]] sanitisation)
			- Your programming [[language]] of choice doesn't match the model that [[SQL]] databases use ([[ORMs]])
			- Your database is too slow! Your schema wasn't designed for efficient queries with so many users. You need to redesign the database and migrate the data to the new schema (database schema migrations and revision management)
			- Still too many people are trying to read and write to your database at once (Redis, write-through caching)
			- Your database is getting too slow! You need to start scaling (Vertical scaling, data migration)
			- Even on the biggest server you can afford you database is still too slow! (sharding, horizontal scaling)
	- There's no way to make that page move ([[JavaScript]])
		- The page is programmable but there's no way to make that page request more data (XMLHttpRequest)
			- Sending XML kinda sucks (JSON)
			- Now that you can send between your site and your server using APIs! But you need to ensure that the requests and responses actually contain the data you expect them to (Request and Response validation, JSON de/serialisation)
			- You only want your own website to be able to send your server requests (CORS)
				- You want other websites to send your server requests (CORS)
		- JavaScript is really annoying and varies between browsers (JQuery)
			- some new JavaScript features are really nice but old browsers don't support them (polyfills, Babel, Lebab)
		- Even with JQuery, complex applications become pretty hard to manage (JavaScript libraries for complex web applications, AngularJS, [[React]], many many more)
			- These libraries are so nice we want to use them for everything instead of gross HTML (JS managed routing, React Router, single page applications)
			- Interface design with CSS kinda sucks for especially for complex applications (SASS, Tailwind, prebuilt UI component libraries, Styled Components)
			- Complex applications need complex application state models (Redux, Zustand, NGXS)
			- Complex applications need sane data fetching patterns and caching (React Query, SWR, [[RTK Query vs. Infinite Scrolling|RTK Query]])
				 - It's annoying to have to build bespoke APIs for every different combination of data that your frontend wants, wouldn't it be nice if the frontend could just tell us what it wanted and the backend figured it out (GraphQL)
			- Even with caching and internal state and JS routing, single applications are pretty slow to actually show useful information since they take multiple requests roundtrips to build the UI and then load the data
				- Server rendered frontend frameworks, where the frontend code for a page is run on the server before sending it to the client so that the initial data is already present on first load, then normal SPA behaviour can take over after that (made possible because of Node.js, [[Next.js]], Remix)
					- Your server now needs to run JavaScript, which is probably only possible using Node.js
					- This is great for basic applications but starts to get awkward when you have complex data structures and component structures as you need to know all data requirements at a route level rather than a component level
						- Server components allow server side rendering on a component level, by running some of the rendering code on the backend, populating it with data, and slotting that wholesale into a SPA (React Server Components)
		- This language you've been using JavaScript has constant type errors, if only you could specify types ([[TypeScript]], Flow)
		- Both JavaScript and TypeScript are bad at actually representing HTML (JSX)
	- Your marketing team wants a website they can control without writing code (CMS, Wordpress, many more)
		- They want it on the same domain name (server routing configuration, e.g. Nginx conf)
	- Your backend server machine's operating system needs to be configured for security (Linux system administration)
		- Uh oh! CVE in one of the libraries your server uses! You need a way to update your dependencies (package managers)
		- Your server state is getting a bit complicated, you aren't sure if you could recreate it now if you wanted to. You also have trouble matching it on your development device.  ([[Docker]])
		- Your backend server is being crushed by your immense popularity, (bigger server, vertical scaling)
		- You bought the biggest server you can afford and its still too much traffic! (horizontal scaling)
			- How do you distribute load across your multiple servers (load balancing)
			- Sometimes your load is so high that you need to add more servers to your fleet of servers, but it's annoying to do it manually (Kubernetes)
	- Managing your own servers is getting time consuming, if only there was a way to have code handle the provisioning of servers (Terraform)

## Links

- [JavaScript Gom Jabbar](https://frantic.im/javascript-gom-jabbar/)
- [The Web's Grain](https://frankchimero.com/blog/2015/the-webs-grain/)
- Frontend
	- [The single most impor­tant factor that dif­fer­enti­ates front-end frame­works](https://themer.dev/blog/the-single-most-important-factor-that-differentiates-front-end-frameworks)
- [Everyone Has JavaScript, Right?](https://www.kryogenix.org/code/browser/everyonehasjs.html)
- [My love letter to front-end web development](https://bower.sh/my-love-letter-to-front-end-web-development)
- [Handling Cookies is a Minefield](https://grayduck.mn/2024/11/21/handling-cookies-is-a-minefield/)
- [Creating PWAs](https://blog.heroku.com/how-to-make-progressive-web-app)
- [Why is everything so scalable?](https://www.stavros.io/posts/why-is-everything-so-scalable/)