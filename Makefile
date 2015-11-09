# This is the Makefile for oci-registerMachine
# Author: Sally O'Malley <somalley@redhat.com>
#
# Targets (see each target for more information):
# 	build: Build code
# 	install: Install binary to specified location
# 	clean: Clean up.

.PHONY:  all build install clean

INSTALL_LOCATION="/usr/libexec/docker/hooks.d"
CUR_DIR=$(PWD)

# Build code
#
# Example:
# 	make build
build:
	go build -v -o oci-registerMachine

# Install code (change here to place anywhere you want)
#
# Example:
#	sudo make install
install:
	mkdir -p /usr/libexec/docker/hooks.d
	cp oci-registerMachine $(INSTALL_LOCATION)

# Clean up
#
# Example:
# 	make clean
clean:
	rm $(CUR_DIR)/oci-registerMachine

