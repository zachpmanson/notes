I had a `docker compose build` running on the same host machine that the final deployment would run on, but the host machine was running out of RAM and/or CPU when the build occurred parallel to a running instance. To constrain the resources of the build, I made the build process run inside a [[docker]] container itself using:

```sh
docker buildx create --name constrainedbuilder --driver docker-container --driver-opt cpu-quota=50000 --driver-opt cpu-period=100000 --use
docker buildx inspect constrainedbuilder --bootstrap
```

When I would run a `docker compose build` that used constrainedbuilder, the build would work for the `poetry install` but fail for the `yarn install`, citing:

```
#37 [celery webpack 5/7] RUN yarn install
#37 67.59 info There appears to be trouble with your network connection. Retrying...
```

This was infuriating, I tried removing yarn HTTP and HTTPS proxies, I tried increasing the network timeouts, no avail.

The only thing that worked changing my package registry from registry.yarnpkg.com to registry.npmjs.org.

```dockerfile
# Install dependencies based on the preferred package manager
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./

# Required 
RUN yarn config set registry https://registry.npmjs.org/
RUN --mount=type=cache,target=/usr/local/share/.cache \
  if [ -f yarn.lock ]; then yarn --frozen-lockfile --network-timeout 60000; \
  else echo "Lockfile not found." && exit 1; \
  fi

```

This was very strange as the constrainedbuilder container had internet access, and the normal default builder container could access yarnpkg registry just fine.

Oh well. The magic of [[JavaScript]].