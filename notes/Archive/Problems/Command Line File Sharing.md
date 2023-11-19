Written by [dabedee](https://news.ycombinator.com/user?id=dabedee) on HN.

---

This is great and very user-friendly. As a quick & dirty alternative for people using the command line, you can easily send files by using netcat.

To quickly copy file from one machine to another.

```
  # on target machine
  $ nc -l PORT > file

  # on source machine
  $ cat file | nc HOST PORT
```

To quickly copy an entire folder:

```
  # on target machine
  $ nc -l PORT | tar xf -

  # on source machine
  $ tar cf - FOLDER | nc HOST PORT
```

And on top of it you can add pv in pipe for progress bar