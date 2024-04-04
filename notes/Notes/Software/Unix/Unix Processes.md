A process is a program in execution.  The process that controls the screen is called the foreground process.  It can take input from the keyboard and write it to the window.

- programs are compiled into objects (binaries/executables)
- programs in execution are processes
- process images are the memory a process occupies
- 3 kinds of processes 
  - user
  - system
  - kernel

## Background Processes

More than one process can run in a window by making other processes background processes.  This can be done by appending `&` to a command.

- background processes can't handle i/o
- this can be achieved by writing to a file

`ps` lists currently running processes.

- `-l` gives lots of information information
- `-f` provides command args

`top` list the processes using the most CPU resources at a given time

`kill <options> <PIDs>` sends a kill signal to the listed process, with options allowing more forceful process killing. (up to `kill -9`)