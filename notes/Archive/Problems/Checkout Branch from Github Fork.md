```sh
git remote add coworker git://path/to/coworkers/repo.git
git fetch coworker
git checkout --track coworker/foo


# then in future
git checkout foo
git pull
```

From this [answer on StackOverflow](https://stackoverflow.com/a/5884825).