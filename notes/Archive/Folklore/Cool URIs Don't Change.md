
Tim Berners-Lee's essay on URIs, [from 1998](https://www.w3.org/Provider/Style/URI).

---


> What makes a cool URI?  
> A cool URI is one which does not change.  
> What sorts of URI change?  
> _URIs don't change: people change them._

There are no reasons at all in theory for people to change URIs (or stop maintaining documents), but millions of reasons in practice.

In theory, the domain name space owner owns the domain name space and therefore all URIs in it. Except insolvency, nothing prevents the domain name owner from keeping the name. And in theory the URI space under your domain name is totally under your control, so you can make it as stable as you like. Pretty much the only good reason for a document to disappear from the Web is that the company which owned the domain name went out of business or can no longer afford to keep the server running. Then why are there so many dangling links in the world? Part of it is just lack of forethought. Here are some reasons you hear out there:

#### We just reorganized our website to make it better.

Do you really feel that the old URIs cannot be kept running? If so, you chose them very badly. Think of your new ones so that you will be able to keep then running after the next redesign.

#### We have so much material that we can't keep track of what is out of date and what is confidential and what is valid and so we thought we'd better just turn the whole lot off.

That I can sympathize with - the W3C went through a period like that, when we had to carefully sift archival material for confidentiality before making the archives public. The solution is forethought - make sure you capture with every document its acceptable distribution, its creation date and ideally its expiry date. Keep this metadata.

#### Well, we found we had to move the files...

This is one of the lamest excuses. A lot of people don't know that servers such as Apache give you a lot of control over a flexible relationship between the URI of an object and where a file which represents it actually is in a file system. Think of the URI space as an abstract space, perfectly organized. Then, make a mapping onto whatever reality you actually use to implement it. Then, tell your server. You can even write bits of your server to make it just right.

John doesn't maintain that file any more, Jane does.

Whatever was that URI doing with John's name in it? It was in his directory? I see.

#### We used to use a cgi script for this and now we use a binary program.

There is a crazy notion that pages produced by scripts have to be located in a "cgibin" or "cgi" area. This is exposing the mechanism of how you run your server. You change the mechanism (even keeping the content the same ) and whoops - all your URIs change.

For example, take the National Science Foundation:

_NSF Online Documents_  
http://www.nsf.gov/cgi-bin/pubsys/browser/odbrowse.pl

the main page for starting to look for documents, is clearly not going to be something to trust to being there in a few years. "cgi-bin" and "oldbrowse" and ".pl" all point to bits of how-we-do-it-now. By contrast, if you use the page to find a document, you get first an equally bad

_Report of Working Group on Cryptology and Coding Theory_  
http://www.nsf.gov/cgi-bin/getpub?nsf9814

for the document's index page, but the html document itself by contrast is very much better:

http://www.nsf.gov/pubs/1998/nsf9814/nsf9814.htm

Looking at this one, the "pubs/1998" header is going to give any future archive service a good clue that the old 1998 document classification scheme is in progress. Though in 2098 the document numbers might look different, I can imagine this URI still being valid, and the NSF or whatever carries on the archive not being at all embarrassed about it.

#### I didn't think URLs have to be persistent - that was URNs.

This is the probably one of the worst side-effects of the URN discussions. Some seem to think that because there is research about namespaces which will be more persistent, that they can be as lax about dangling links as they like as "URNs will fix all that". If you are one of these folks, then allow me to disillusion you.

Most URN schemes I have seen look something like an authority ID followed by either a date and a string you choose, or just a string you choose. This looks very like an HTTP URI. In other words, if you think your organization will be capable of creating URNs which will last, then prove it by doing it now and using them for your HTTP URIs. There is nothing about HTTP which makes your URIs unstable. It is your organization. Make a database which maps document URN to current filename, and let the web server use that to actually retrieve files.

If you have gotten to this point, then unless you have the time and money and contacts to get some software design done, then you might claim the next excuse:

#### We would like to, but we just don't have the right tools.

Now here is one I can sympathize with. I agree entirely. What you need to do is to have the web server look up a persistent URI in an instant and return the file, wherever your current crazy file system has it stored away at the moment. You would like to be able to store the URI in the file as a check, and constantly keep the database in tune with actuality. You'd like to store the relationships between different versions and translations of the same document, and you'd like to keep an independent record of the checksum to provide a guard against file corruption by accidental error. And web servers just don't come out of the box with these features. When you want to create a new document, your editor asks you for a URI instead of telling you.

You need to be able to change things like ownership, access, archive level security level, and so on, of a document in the URI space without changing the URI.

Too bad. But we'll get there. At W3C we use _Jigedit_ functionality (_Jigsaw_ server used for editing) which does track versions, and we are experimenting with document creation scripts. If you make tools, servers and clients, take note!

This is an outstanding reason, which applies for example to many W3C pages including this one: so do what I say, not what I do.

## Why should I care?

When you change a URI on your server, you can never completely tell who will have links to the old URI. They might have made links from regular web pages. They might have bookmarked your page. They might have scrawled the URI in the margin of a letter to a friend.

When someone follows a link and it breaks, they generally lose confidence in the owner of the server. They also are frustrated - emotionally and practically from accomplishing their goal.

Enough people complain all the time about dangling links that I hope the damage is obvious. I hope it also obvious that the reputation damage is to the maintainer of the server whose document vanished.

## So what should I do? Designing URIs

It is the the duty of a Webmaster to allocate URIs which you will be able to stand by in 2 years, in 20 years, in 200 years. This needs thought, and organization, and commitment.

URIs change when there is some information in them which changes. It is critical how you design them. (What, design a URI? I have to design URIs? Yes, you have to think about it.). Designing mostly means leaving information out.

The creation date of the document - the date the URI is issued - is one thing which will not change. It is very useful for separating requests which use a new system from those which use an old system. That is one thing with which it is good to start a URI. If a document is in any way dated, even though it will be of interest for generations, then the date is a good starter.

The only exception is a page which is deliberately a "latest" page for, for example, the whole organization or a large part of it.

http://www.pathfinder.com/money/moneydaily/latest/

is the latest "Money daily" column in "Money" magazine. The main reason for not needing the date in this URI is that there is no reason for the persistence of the URI to outlast the magazine. The concept of "today's _Money_" vanishes if _Money_ goes out of production. If you want to link to the content, you would link to it where it appears separately in the archives as

http://www.pathfinder.com/money/moneydaily/1998/981212.moneyonline.html

(Looks good. Assumes that "money" will mean the same thing throughout the life of pathfinder.com. There is a duplication of "98" and an ".html" you don't need but otherwise this looks like a strong URI).

### What to leave out

Everything! After the creation date, putting any information in the name is asking for trouble one way or another.

- **Authors name**- authorship can change with new versions. People quit organizations and hand things on.
- **Subject**. This is tricky. It always looks good at the time but changes surprisingly fast. I discuss this more below.
- **Status**- directories like "old" and "draft" and so on, not to mention "latest" and "cool" appear all over file systems. Documents change status - or there would be no point in producing drafts. The latest version of a document needs a persistent identifier whatever its status is. Keep the status out of the name.
- **Access**. At W3C we divide the site into "Team access", "Member access" and "Public access". It sounds good, but of course documents start off as team ideas, are discussed with members, and then go public. A shame indeed if every time some document is opened to wider discussion all the old links to it fail! We are switching to a simple date code now.
- **File name extension**. This is a very common one. "cgi", even ".html" is something which will change. You may not be using HTML for that page in 20 years time, but you might want today's links to it to still be valid. The canonical way of making links to the W3C site doesn't use the extension.([how?](https://www.w3.org/Provider/Style/URI#remove))
- **Software mechanisms**. Look for "cgi", "exec" and other give-away "look what software we are using" bits in URIs. Anyone want to commit to using perl cgi scripts all their lives? Nope? Cut out the .pl. Read the server manual on how to do it.
- Disk name - gimme a break! But I've seen it.

So a better example from our site is simply

http://www.w3.org/1998/12/01/chairs

a report of the minutes of a meeting of W3C chair people.

#### Topics and Classification by subject

I'll go into this danger in more detail as it is one of the more difficult things to avoid. Typically, topics end up in URIs when you classify your documents according to a breakdown of the work you are doing. That breakdown will change. Names for areas will change. At W3C we wanted to change "MarkUp" to "Markup" and then to "HTML" to reflect the actual content of the section. Also, beware that this is often a flat name space. In 100 years are you sure you won't want to reuse anything? We wanted to reuse "History" and "Stylesheets" for example in our short life.

This is a tempting way of organizing a web site - and indeed a tempting way of organizing anything, including the whole web. It is a great medium term solution but has serious drawbacks in the long term

Part of the reasons for this lie in the philosophy of meaning. every term in the language it a potential clustering subject, and each person can have a different idea of what it means. Because the relationships between subjects are web-like rather than tree-like, even for people who agree on a web may pick a different tree representation. These are my (oft repeated) general comments on the dangers of hierarchical classification as a general solution.

Effectively, when you use a topic name in a URI you are binding yourself to some classification. You may in the future prefer a different one. Then, the URI will be liable to break.

A reason for using a topic area as part of the URI is that responsibility for sub-parts of a URI space is typically delegated, and then you need a name for the organizational body - the subdivision or group or whatever - which has responsibility for that sub-space. This is binding your URIs to the organizational structure. It is typically safe only when protected by a date further up the URI (to the left of it): 1998/pics can be taken to mean for your server "what we meant in 1998 by _pics_", rather than "what in 1998 we did with what we now refer to as _pics_."

### Don't forget the domain name.

Remember that this applies not only to the "path" part of a URI but to the server name. If you have separate servers for some of your stuff, remember that that division will be impossible to change without destroying many many links. Some classic "look what software we are using today" domain names are "cgi.pathfinder.com", "secure", "lists.w3.org". They are made to make administration of the servers easier. Whether it represents divisions in your company, or document status, or access level, or security level, be very, very careful before using more than one domain name for more than one type of document. remember that you can hide many web servers inside one apparent web server using redirection and proxying.

Oh, and do think about your domain name. If your name is not soap, will you want to be referred to as "soap.com" even when you have switched your product line to something else. (With apologies to whoever owns soap.com at the moment).

## Conclusion

Keeping URIs so that they will still be around in 2, 20 or 200 or even 2000 years is clearly not as simple as it sounds. However, all over the Web, webmasters are making decisions which will make it really difficult for themselves in the future. Often, this is because they are using tools whose task is seen as to present the best site in the moment, and no one has evaluated what will happen to the links when things change. The message here is, however, that many, many things can change and your URIs can and should stay the same. They only can if you think about how you design them.

See also:

- [Jacob Nielsen's "Alertbox" rant on the same topic](http://www.useit.com/alertbox/990321.html)

---

### Footnote

### How can I remove the file extensions...

...from my URIs in a practical file-based web server?

If you are using, for example, Apache, you can set it up to do content negotiation. You keep the file extension (such as .png) on the file (e.g. `mydog.png`), but refer to the web resource without it. Apache then checks the directory for all files with that name and any extension, and it can also pick the best one out of a set (e.g. GIF and PNG). (You do _not_ have to put different types of file in different directories, in fact the content negotiation won't work if you do.)

- Set up your server to do content negotiation
- Make references always to the URI without the extension

References which do have the extension on will still work but will not allow your server to select the best of currently available and future formats.

(In fact, `mydog`, `mydog.png` and `mydog.gif` are each valid web resources. `mydog` is content-type-generic. `mydog.png` and `mydog.gif` are content-type-specific.)

Of course, if you are building your own server, then using a database to relate persistent identifiers to their current form is a very clean idea -- though beware the unbounded growth of your database.

### Hall of flame -- story 1: Channel 7

During 1999, `http://www.whdh.com/stormforce/closings.shtml` was a page I found documenting school closings due to snow. An alternative to waiting for them to scroll past the bottom of the TV screen! I put a pointer to it from my home page. Come the first big storm of 2000, and I check the page. It says,

> "Closings as of .  
> There are currently no closings in effect. Please check back when the weather warrants"

Can't be such a big storm. Funny the date is missing. But then if I go to the home page of the site, there is a big button "school closings" which takes me to `http://www.whdh.com/stormforce/` which has a list of many closed schools.

Well, maybe they changed the system which got the closings from the definitive list - but they did not need to change the URI.

### Hall of flame -- story 2: Microsoft Netmeeting

One of the smarts which came with a growing dependency on the web was that applications could have built-in links back to the manufacturer's web site. This has been used and abused to a great extent, but - you do have to keep the URL the same. Just the other day I tried a link from Microsoft's Netmeeting 2/something client under a menu "Help/Microsoft on the Web/Free stuff" and got an Error 404 - not found response from the server. They have probably fixed it by now...

(c)1998 [Tim BL](https://www.w3.org/People/Berners-Lee/)

Historical note: At the end of the 20th century when this was written, "cool" was an epithet of approval particularly among young, indicating trendiness, quality, or appropriateness. In the rush to stake our DNS territory involved the choice of domain name and URI path were sometimes directed more toward apparent "coolness" than toward usefulness or longevity. This note is an attempt to redirect the energy behind the quest for coolness.