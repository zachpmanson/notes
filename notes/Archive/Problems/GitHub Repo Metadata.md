To get general metadata about a given GitHub repo hit the endpoint:

```
https://api.github.com/repos/:owner/:reponame/branches/master
```

E.g. https://api.github.com/repos/pavo-etc/alculator-data/branches/master

Returns something like:

```json
{
  "name": "master",
  "commit": {
    "sha": "727a3b7c461d3f08129e7bbaa251c3ccce580867",
    "node_id": "C_kwDOJzazG9oAKDcyN2EzYjdjNDYxZDNmMDgxMjllN2JiYWEyNTFjM2NjY2U1ODA4Njc",
    "commit": {
      "author": {
        "name": "pavo-etc",
        "email": "pavo-etc@users.noreply.github.com",
        "date": "2023-06-25T01:09:55Z"
      },
      "committer": {
        "name": "pavo-etc",
        "email": "pavo-etc@users.noreply.github.com",
        "date": "2023-06-25T01:09:55Z"
      },
      "message": "Update data: Sun Jun 25 01:09:55 UTC 2023",
      "tree": {
        "sha": "ab4146a8e95b85892962f8ba0831ed58912db34c",
        "url": "https://api.github.com/repos/pavo-etc/alculator-data/git/trees/ab4146a8e95b85892962f8ba0831ed58912db34c"
      },
      "url": "https://api.github.com/repos/pavo-etc/alculator-data/git/commits/727a3b7c461d3f08129e7bbaa251c3ccce580867",
      "comment_count": 0,
      "verification": {
        "verified": false,
        "reason": "unsigned",
        "signature": null,
        "payload": null
      }
    },
    "url": "https://api.github.com/repos/pavo-etc/alculator-data/commits/727a3b7c461d3f08129e7bbaa251c3ccce580867",
    "html_url": "https://github.com/pavo-etc/alculator-data/commit/727a3b7c461d3f08129e7bbaa251c3ccce580867",
    "comments_url": "https://api.github.com/repos/pavo-etc/alculator-data/commits/727a3b7c461d3f08129e7bbaa251c3ccce580867/comments",
    "author": {
      "login": "pavo-etc",
      "id": 24368336,
      "node_id": "MDQ6VXNlcjI0MzY4MzM2",
      "avatar_url": "https://avatars.githubusercontent.com/u/24368336?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/pavo-etc",
      "html_url": "https://github.com/pavo-etc",
      "followers_url": "https://api.github.com/users/pavo-etc/followers",
      "following_url": "https://api.github.com/users/pavo-etc/following{/other_user}",
      "gists_url": "https://api.github.com/users/pavo-etc/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/pavo-etc/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/pavo-etc/subscriptions",
      "organizations_url": "https://api.github.com/users/pavo-etc/orgs",
      "repos_url": "https://api.github.com/users/pavo-etc/repos",
      "events_url": "https://api.github.com/users/pavo-etc/events{/privacy}",
      "received_events_url": "https://api.github.com/users/pavo-etc/received_events",
      "type": "User",
      "site_admin": false
    },
    "committer": {
      "login": "pavo-etc",
      "id": 24368336,
      "node_id": "MDQ6VXNlcjI0MzY4MzM2",
      "avatar_url": "https://avatars.githubusercontent.com/u/24368336?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/pavo-etc",
      "html_url": "https://github.com/pavo-etc",
      "followers_url": "https://api.github.com/users/pavo-etc/followers",
      "following_url": "https://api.github.com/users/pavo-etc/following{/other_user}",
      "gists_url": "https://api.github.com/users/pavo-etc/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/pavo-etc/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/pavo-etc/subscriptions",
      "organizations_url": "https://api.github.com/users/pavo-etc/orgs",
      "repos_url": "https://api.github.com/users/pavo-etc/repos",
      "events_url": "https://api.github.com/users/pavo-etc/events{/privacy}",
      "received_events_url": "https://api.github.com/users/pavo-etc/received_events",
      "type": "User",
      "site_admin": false
    },
    "parents": [
      {
        "sha": "6a231cca1a6dfecbb2fcef14e5ade0a2b7f6c7b9",
        "url": "https://api.github.com/repos/pavo-etc/alculator-data/commits/6a231cca1a6dfecbb2fcef14e5ade0a2b7f6c7b9",
        "html_url": "https://github.com/pavo-etc/alculator-data/commit/6a231cca1a6dfecbb2fcef14e5ade0a2b7f6c7b9"
      }
    ]
  },
  "_links": {
    "self": "https://api.github.com/repos/pavo-etc/alculator-data/branches/master",
    "html": "https://github.com/pavo-etc/alculator-data/tree/master"
  },
  "protected": false,
  "protection": {
    "enabled": false,
    "required_status_checks": {
      "enforcement_level": "off",
      "contexts": [

      ],
      "checks": [

      ]
    }
  },
  "protection_url": "https://api.github.com/repos/pavo-etc/alculator-data/branches/master/protection"
}
```

Taken from [here](https://stackoverflow.com/questions/29845346/how-to-get-latest-commit-date-github-api).  Learned while adding the "Last updated" indicator on [[Alculator]].