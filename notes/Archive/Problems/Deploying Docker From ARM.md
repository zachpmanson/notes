
Azure container instances are not built to serve docker builds created on ARM machines, like Macbooks with M-series chips.  If you attempt to run these they will immediately crash and be restarted.

```
docker build -t your-image-tag --platform linux/amd64 .
```

Thank god for [this StackOverflow post](https://stackoverflow.com/a/77182483), I only found after hours of failure.  [dunnkers](https://stackoverflow.com/users/3047500/dunnkers) is a hero.  The person who commented this is now my enemy for life:

> FYI the OP solved this on their own, 3 years ago. The question should be closed at this point. Also, fyi - this really isn't on-topic here, as it's not a programming question.

-- [David Makogon](https://stackoverflow.com/users/272109/david-makogon "69,925 reputation")