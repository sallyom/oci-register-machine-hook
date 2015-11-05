%global commit  6769278cbb35a79fcf13ed4b5a4f61821b7685d9

Name:   	      oci-registerMachine
Version:        1.0.0	
Release:	      1%{?dist}
Summary:	      This is the golang binary RPM spec for using systemd-machined service method RegisterMachine and TerminateMachine.
License:        GPLv2.1+	
URL:	          https://github.com/sallyom/Register	
Source0:	      https://github.com/sallyom/Register/archive/%{commit}.zip
    
BuildRequires:  gcc
BuildRequires:	golang >= 1.2-7
BuildRequires:  dbus

%description
RegisterMachine implements a container manager that makes use of systemd-machined. RegisterMachine and TerminateMachine are called using prestart and poststop hooks.

%prep
%setup -q -n Register-%{commit}

rm -rf vendor

%build
mkdir -p ./_build/src/github.com/oci
ln -s $(pwd) ./_build/src/github.com/oci/registerMachine

export GOPATH=$(pwd)/_build:%{gopath}
go build -o oci-registerMachine .

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./oci-registerMachine %{buildroot}%{_bindir}/oci-registerMachine

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/oci-registerMachine

%changelog
* Tue Nov 03 2015 Sally O'Malley <somalley@redhat.com> - 1.0.0-1
- package oci-registerMachine
