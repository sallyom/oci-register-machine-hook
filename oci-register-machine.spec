%global hooksdir "/usr/lib/docker/hooks.d"

Name:		oci-register-machine
Version:	0.1.0	
Release:	1%{?dist}
Summary:	This is the golang binary RPM spec for using systemd-machined service methods RegisterMachine and TerminateMachine.
License:	GPLv2.1+	
URL:		https://github.com/projectatomic/oci-register-machine
Source0:	https://github.com/projectatomic/oci-register-machine/archive/v%{version}.tar.gz
    
BuildRequires:  gcc
BuildRequires:	golang >= 1.2-7
BuildRequires:  golang-github-godbus-dbus-devel
BuildRequires:  golang-github-cpuguy83-go-md2man

%description
oci-register-machine implements a container manager that makes use of systemd-machined.
RegisterMachine and TerminateMachine are called using prestart and poststop hooks.

%prep
%setup -q -n Register-%{version}

%build
mkdir -p ./_build/src/github.com/oci
ln -s $(pwd) ./_build/src/github.com/oci/register-machine
make 

%install
make DESTDIR="%{buildroot}" install

%files
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/docker/hooks.d/oci-register-machine
%{_mandir}/man1/oci-register-machine.1.gz

%changelog
* Tue Nov 03 2015 Sally O'Malley <somalley@redhat.com> - 1.0.0-1
- package oci-register-machine
