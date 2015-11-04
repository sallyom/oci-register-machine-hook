## Systemd RegisterMachine

`Systemd-machined` is a virtual machine and container registration manager.  It is a tiny daemon that
tracks locally running virtual machines and containers and the processes belonging to them.


If you install this program, a binary will be placed in `/usr/libexec/docker/hooks.d` named `oci-registerMachine`.
With minor changes to Docker code, this binary will be executed when starting and stopping Docker containers via
prestart and poststop hooks.  `RegisterMachine()` and `TerminateMachine()` are systemd-machined.service methods.  These
and other methods are described here: [systemd-machined freedesktop.org](http://www.freedesktop.org/wiki/Software/systemd/machined/)


Running Docker containers with this executable, just before a container is started and after it is provisioned, RegisterMachine() is called.
All running containers' IDs will be listed when you run the command `machinectl` or `machinectl list`.  When containers are
stopped/exited, TerminateMachine() is called, all container processes are terminated and container ID is no longer listed in `machinectl` output.


This doc assumes you are running at least docker version 1.9 with the dockerhooks patch. 


To install these systemd-machined methods that work with Docker's prestart and poststop hooks (with yet-to-merge upstream
changes):

`sudo dnf install oci-registerMachine`
