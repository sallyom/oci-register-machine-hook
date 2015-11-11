# This is the Makefile for oci-registerMachine
# Author: Sally O'Malley <somalley@redhat.com>
#
# Targets (see each target for more information):
# 	build: Build code
# 	install: Install binary to specified location
# 	clean: Clean up.

.PHONY:  all build install clean

PREFIX ?= $(DESTDIR)/usr
HOOKSDIR=$(PREFIX)/libexec/docker/hooks.d
CUR_DIR=$(PWD)

# Build code
#
# Example:
# 	make build
oci-registerMachine: registerMachine.go
	go build -v -o oci-registerMachine

build: oci-registerMachine

# Install code (change here to place anywhere you want)
#
# Example:
#	sudo make install
install: oci-registerMachine
	install -d -m 0755 $(HOOKSDIR)
	install -m 755 oci-registerMachine $(HOOKSDIR)

# Clean up
#
# Example:
# 	make clean
clean:
	rm $(CUR_DIR)/oci-registerMachine
