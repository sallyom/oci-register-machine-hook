# This is the Makefile for oci-registerMachine
# Authors: Sally O'Malley <somalley@redhat.com>
#
# Targets (see each target for more information):
# 	build: Build code
# 	install: Install binary to specified location
# 	clean: Clean up.

.PHONY:  build install clean all docs

all: build docs

PREFIX ?= $(DESTDIR)/usr
HOOKSDIR=$(PREFIX)/libexec/docker/hooks.d

# Build code
#
# Example:
# 	make build
oci-registerMachine: registerMachine.go

	go build -v -o oci-registerMachine

oci-registerMachine.1.gz: oci-registerMachine.1.md

	go get github.com/cpuguy83/go-md2man
	go-md2man -in "oci-registerMachine.1.md" -out "oci-registerMachine.1"
	sed -i 's|$$HOOKSDIR|$(HOOKSDIR)|' oci-registerMachine.1
	gzip -f oci-registerMachine.1

docs: oci-registerMachine.1.gz
build: oci-registerMachine

# Install code (change here to place anywhere you want)
#
# Example:
#	make install
install: oci-registerMachine
	install -d -m 0755 $(HOOKSDIR)
	install -m 755 oci-registerMachine $(HOOKSDIR)
	install oci-registerMachine.1.gz $(PREFIX)/share/man/man1

# Clean up
#
# Example:
# 	make clean
clean:
	rm oci-registerMachine
	rm oci-registerMachine.1.gz
