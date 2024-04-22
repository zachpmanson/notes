> Docker is kinda like [[Git]]. A really solid core concept with just enough surface inconsistencies to be annoying but not enough for a better solution to take the crown.

-- [David Ellis](https://techhub.social/@ISV_Damocles/111868958232964170)

Docker is a system for running virtual machines called containers.

## Advantages of Docker

- provides consistent, contained environment on your local machine
- containers are lightweight, portable, and boot fast
- useful for hardware agnostic software [[Development]]
- can be used for non-interactive application execution

## Comparison to Traditional VMs

- docker containers are stateless, container storage is erased when the container stops (mapping drives can resolve this)
- uses OS-level virtualisation, so containers share the host OS without needing a Hypervisor
  - smaller and faster than VM
- docker platform can run many containers simultaneously and they can communicate with each other
- docker registries allows straightforward deployment of docker images

## Architecture

- Client - CLI interface
- Daemon - background service that listend for API requests and manages docker objects
- Docker desktop - manager for other components
- Docker registry - a package repo, docker hub is the default
- Docker objects
  - image is a read only template for container
  - container is a runnable instance of an image

![[docker-architecture.png]]

![[docker-vs-vm.png]]

## Running

```bash
docker run \
--mount type=bind,source=HOST_PATH,target=CONTAINER_PATH \
-it IMAGE:TAG
```

- `mount` sets an folder on host to folder in container
  - use absolute folders
- `it` allows interaction
- `TAG` is the version of the image
