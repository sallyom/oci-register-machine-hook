%global hooksdir "/usr/libexec/docker/hooks.d"

Name:		oci-registerMachine
Version:	0.1.0	
Release:	1%{?dist}
Summary:	This is the golang binary RPM spec for using systemd-machined service methods RegisterMachine and TerminateMachine.
License:	GPLv2.1+	
URL:		https://github.com/sallyom/Register	
Source0:	https://github.com/sallyom/Register/archive/v%{version}.tar.gz
    
BuildRequires:  gcc
BuildRequires:	golang >= 1.2-7
BuildRequires:  golang-github-godbus-dbus-devel
BuildRequires:  golang-github-cpuguy83-go-md2man

%description
oci-registerMachine implements a container manager that makes use of systemd-machined.
RegisterMachine and TerminateMachine are called using prestart and poststop hooks.

%prep
%setup -q -n Register-%{version}

rm -rf vendor

%build
mkdir -p ./_build/src/github.com/oci
ln -s $(pwd) ./_build/src/github.com/oci/registerMachine

export GOPATH=$(pwd)/_build:%{gopath}
function gobuild { go build -a -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x "$@"; }
gobuild -o oci-registerMachine .
go-md2man -in "oci-registerMachine.1.md" -out "oci-registerMachine.1"
sed -i 's|$HOOKSDIR|%{hooksdir}|' oci-registerMachine.1
gzip -f oci-registerMachine.1

%install
install -d %{buildroot}%{_libexecdir}/docker/hooks.d
install -p -m 0755 ./oci-registerMachine %{buildroot}%{_libexecdir}/docker/hooks.d
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 ./oci-registerMachine.1.gz %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root,-)
%doc README.md
%{_libexecdir}/docker/hooks.d/oci-registerMachine
%{_mandir}/man1/oci-registerMachine.1.gz

%changelog
* Tue Nov 03 2015 Sally O'Malley <somalley@redhat.com> - 1.0.0-1
- package oci-registerMachine
