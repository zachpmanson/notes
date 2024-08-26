The best sorting algorithm, [anonymously invented on 2011-01-20.](https://web.archive.org/web/20151231221001/http://bl0ckeduser.github.io/sleepsort/sleep_sort_trimmed.html).

---

Man, am I a genius. Check out this sorting algorithm I just invented.  

```sh
#!/bin/bash
function f() {
    sleep "$1"
    echo "$1"
}
while [ -n "$1" ]
do
    f "$1" &
    shift
done
wait
```

example usage:  
`./sleepsort.bash 5 3 6 3 6 3 1 4 7`