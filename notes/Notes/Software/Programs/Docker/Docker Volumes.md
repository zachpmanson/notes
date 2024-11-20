Docker volumes are directories that belong to to the host machine that are "mounted" to docker containers, allowing them to have persistent storage. By default, they persist when you down or stop a container.

When using Docker Compose, to remove the volumes as well:

```sh
docker compose down postgres -v
```