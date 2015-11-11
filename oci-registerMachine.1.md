% OCI-REGISTERMACHINE(1) oci-registerMachine
% November 2015
## NAME
oci-registerMachine - Register Docker containers with systemd-machined

## SYNOPSIS

**oci-registerMachine**

## DESCRIPTION

It is not expected that `oci-registerMachine` be executed manually.  Instead, it should be placed in $HOOKSDIR, where docker prestart and poststop hooks will find it and it will run automatically.
`oci-registerMachine` will be executed when starting and stopping Docker containers
via prestart and poststop hooks.  After starting a Docker container, the container 
will be listed with the `machinectl`.  The machine name will be the container ID.
When container exits, the associated machine will be terminated and will no longer be listed.


## EXAMPLES

	$ docker run --it busybox /bin/sh

	(In new terminal):
	
	$ machinectl


```
#
MACHINE                          CLASS     SERVICE
5556287c7fa1c2312243f5ca2d75c90b container docker 

1 machines listed.

``` 

## SEE ALSO

docker-run(1), systemd-machined(8)

## HISTORY
November 2015, updated by Sally OMalley <somalley@redhat.com>
