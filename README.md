## Systemd RegisterMachine

`Systemd-machined` is a virtual machine and container registration manager.  It is a tiny daemon that
tracks locally running virtual machines and containers and the processes belonging to them.


If you install this program, a binary will be placed in `/usr/libexec/docker/hooks.d` named `oci-registerMachine`.
With minor changes to Docker code, this binary will be executed when starting and stopping Docker containers via
prestart and poststop hooks.  `RegisterMachine()` and `TerminateMachine()` are systemd-machined.service methods.  These
and other methods are described here: [systemd-machined freedesktop.org](http://www.freedesktop.org/wiki/Software/systemd/machined/)


Running Docker containers with this executable, RegisterMachine() is called
iust before a container is started and after it is provisioned.
All running containers' IDs will be listed when you run the command `machinectl` or `machinectl list`.  When containers are
stopped/exited, TerminateMachine() is called, all container processes are terminated and container ID is no longer listed in `machinectl` output.


This doc assumes you are running at least docker version 1.9 with the dockerhooks patch. 


To install (will update when package is available):

    1. Clone this branch
    2. cp oci-registerMachine.spec  ~/rpmbuild/SPECS
    3. rpmbuild -ba oci-registerMachine.spec
    4. sudo dnf install ~/rpmbuild/RPMS/x86_64/oci-registerMachine-1.0.0-1.fc23.x86_64.rpm
       (or sudo dnf install [path to oci-registerMachine rpm])
