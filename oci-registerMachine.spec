%global commit  88555c9e80851819c21b649090d5b9afd43649c2

Name:		oci-registerMachine
Version:	1.0.0	
Release:	1%{?dist}
Summary:	This is the golang binary RPM spec for using systemd-machined service methods RegisterMachine and TerminateMachine.
License:	GPLv2.1+	
URL:		https://github.com/sallyom/Register	
Source0:	https://github.com/sallyom/Register/archive/%{commit}.zip
    
BuildRequires:  gcc
BuildRequires:	golang >= 1.2-7
BuildRequires:  dbus

%description
oci-registerMachine implements a container manager that makes use of systemd-machined.
RegisterMachine and TerminateMachine are called using prestart and poststop hooks.

%prep
%setup -q -n Register-%{commit}

rm -rf vendor

%build
mkdir -p ./_build/src/github.com/oci
ln -s $(pwd) ./_build/src/github.com/oci/registerMachine

export GOPATH=$(pwd)/_build:%{gopath}
function gobuild { go build -a -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x "$@"; }
gobuild -o oci-registerMachine .

%install
install -d %{buildroot}%{_libexecdir}/docker/hooks.d
install -p -m 0755 ./oci-registerMachine %{buildroot}%{_libexecdir}/docker/hooks.d

%files
%defattr(-,root,root,-)
%doc README.md
%{_libexecdir}/docker/hooks.d/oci-registerMachine

%changelog
* Tue Nov 03 2015 Sally O'Malley <somalley@redhat.com> - 1.0.0-1
- package oci-registerMachine
