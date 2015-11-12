% OCI-REGISTERMACHINE(1) oci-registerMachine
% November 2015
## NAME
oci-registerMachine - Register OCI containers with systemd-machined

## SYNOPSIS

**oci-registerMachine**

## DESCRIPTION

`oci-registerMachine` is a OCI hook program. If you add it to the runc json data
as a hook, runc will execute the application after the container process is created but before it is executed, with a `prestart` flag.  When the container exits
`oci-registerMachine` will be executed, after the container exits but before it is destroyed, with the `poststop` flag.  Docker will execute `oci-registerMachine` as a container hook when it is installed in the $HOOKSDIR directory.

After starting an OCI container, the container will be listed with the `machinectl`.  The machine name will be the container ID.  Machinectl will then be able
to manage the container. When container exits, the oci-registerMachine will remove the instance from machinectl.


## EXAMPLES

	$ docker run --it busybox /bin/sh

	(In different terminal):
	
	$ machinectl


```
#
MACHINE                          CLASS     SERVICE
5556287c7fa1c2312243f5ca2d75c90b container docker 

1 machines listed.

``` 

## SEE ALSO

docker-run(1), machinectl(1), systemd-machined(8)

## HISTORY
November 2015, updated by Sally OMalley <somalley@redhat.com>
