Mistakes in computing that were only realised after the point of no return.

## Referer HTTP Field
"Referer" is a field in the HTTP request headers that contains the previous page that linked to the requested page. This misspelling of the word "referrer" was present in the original proposal for the field in the HTTP specification, made by Phillip Hallam-Baker. This spelling was then widely implemented by the software of the time, and solidified by RFC 1945 which documented the HTTP/1.0 protocol as it was being comtemporarily used.

More details on this can be found on this field and its etymology on its [Wikipedia entry](https://en.wikipedia.org/wiki/HTTP_referer).

## Dotfiles Being Hidden
On Unix systems a file can be hidden from `ls` and other applications by prefixing the filename with a period.  This was introduced in Unix Version 2 as a side-effect of adding  files `.` and `..` to support the new hierarchical filesystem.  To avoid these navigation files appearing in every directory when `ls` was executed, filenames with the first character `'.'` were filtered out.  This unintentionally hid other files with this prefix. Once this precedent was set, other programs implemented the same behaviour, which continues to this day.

More details on this can be read [here](https://web.archive.org/web/20180827160401/https://plus.google.com/+RobPikeTheHuman/posts/R58WgWwN9jp).
