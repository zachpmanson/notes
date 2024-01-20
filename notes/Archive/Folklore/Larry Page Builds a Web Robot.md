Lawrence Page asks about how to set the User-Agent field in the Java HTTP library.  He is building a little web robot.  Nothing to see here.  Posted to Usenet on [1996-07-01](https://groups.google.com/g/comp.lang.java/c/aSPAJO05LIU/m/ushhUIQQ-ogJ?pli=1).

---

Lawrence Page, Jan 7, 1996, 7:00:00 PM

```
I have a web robot which is a Java app. I need to be able to set the  
User-Agent field in the HTTP header in order to be a good net citizen (so  
people know who is accessing their server). Anyone have any ideas?

Right now, Java sends a request that includes something like:

User-Agent: Java/1.0beta2

I'd rather not rewrite all the HTTP stuff myself. I tried just searching  
in the JDK for the Java/1.0beta2 figuring I could just change the string,  
but I couldn't find it. Perhaps it is stored as a unicode string?

An easy method of setting the User-Agent field should probably be added to  
Java, so people can properly identify their programs.

Thanks, Larry Page
```

---

Joseph Millar, Jan 9, 1996, 7:00:00 PM

```
Larry,

The User-Agent field is built in:

.\javasrc\src\share\sun\sun\net\www\http\HttpClient.java

It looks to be a concatentation of three items:  
1) the system property "http.agent"  
2) the word "Java"  
3) the system property "java.version"

Since the agent string that gets built has only items 2 and  
3, perhaps that means "http.agent" is blank (i.e. settable)?  
If you could set "http.agent" prior to establishing the URL  
connection, you may be able to get the desired effect.

Just a shot in the dark...

  
Joe Millar
```