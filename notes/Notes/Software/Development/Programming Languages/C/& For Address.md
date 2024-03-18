Why were `*` and `&` chosen for pointer operations in C?

Chris Mulligan emailed Ken Thompson to find out.  Chris initially assumed it was because \* looked like a point and & was beside it on the keyboard.

> **From: Ken Thompson < ken@google.com >**
> 
> near on the keyboard: no.  
> c copied from b so & and * are same there.  
> b got * from earlier languages - some assembly,  
> bcpl and i think pl/1.  
> i think that i used & because the name (ampersand)  
> sounds like "address." b was designed to be run with  
> a teletype model 33 teletype. (5 bit baud-o code)  
> so the use of symbols was restricted.