Name: NVDARemoteServer
Version: 1.4.1
Release: 1.el6
Summary: NVDARemote server rpm
Source0: server.tar.gz
License: GPLv2
URL: https://github.com/jmdaweb/NVDARemoteServer
Requires: python
Group: System Environment/Daemons
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
%description
This remote server allows NVDARemote users to redirect their traffic.
%prep
%setup -q
%build
%install
chmod -x LICENSE
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/NVDARemoteServer
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/man/man1
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0755 -d $RPM_BUILD_ROOT/etc/init.d
install -m 0644 server.py $RPM_BUILD_ROOT/usr/share/NVDARemoteServer/server.py
install -m 0644 server.pem $RPM_BUILD_ROOT/usr/share/NVDARemoteServer/server.pem
install -m 0644 daemon.py $RPM_BUILD_ROOT/usr/share/NVDARemoteServer/daemon.py
install -m 0755 NVDARemoteServer $RPM_BUILD_ROOT/usr/bin/NVDARemoteServer
install -m 0755 NVDARemoteCertificate $RPM_BUILD_ROOT/usr/bin/NVDARemoteCertificate
install -m 0755 NVDARemoteServerd $RPM_BUILD_ROOT/etc/init.d/nvdaremoteserver
gzip -9 NVDARemoteServer.1
install -m 0644 NVDARemoteServer.1.gz $RPM_BUILD_ROOT/usr/share/man/man1/NVDARemoteServer.1.gz
gzip -9 NVDARemoteCertificate.1
install -m 0644 NVDARemoteCertificate.1.gz $RPM_BUILD_ROOT/usr/share/man/man1/NVDARemoteCertificate.1.gz
%clean
rm -rf $RPM_BUILD_ROOT
%post
chkconfig --add nvdaremoteserver
NVDARemoteServer start
%preun
NVDARemoteServer stop
chkconfig --del nvdaremoteserver
%files
/etc/init.d/nvdaremoteserver
/usr/bin/NVDARemoteServer
/usr/bin/NVDARemoteCertificate
%dir /usr/share/NVDARemoteServer
/usr/share/NVDARemoteServer/server.py
/usr/share/NVDARemoteServer/server.pyc
/usr/share/NVDARemoteServer/server.pyo
/usr/share/NVDARemoteServer/server.pem
/usr/share/NVDARemoteServer/daemon.py
/usr/share/NVDARemoteServer/daemon.pyc
/usr/share/NVDARemoteServer/daemon.pyo
/usr/share/man/man1/NVDARemoteServer.1.gz
/usr/share/man/man1/NVDARemoteCertificate.1.gz
%doc LICENSE
%changelog
* Wed Mar 01 2017 Jose Manuel Delicado <jmdaweb@hotmail.com> - 1.4.1-1
- Fixed massive memory allocation problem.
* Sat Jan 14 2017 Jose Manuel Delicado <jmdaweb@hotmail.com> - 1.4-1
- The server is now threaded. Support for more platforms and protocol v2.
* Mon Apr 4 2016 Technow <info@technow.es> - 1.3-1
- Bugs fixed. New utility to generate server certificates.
* Mon Mar 21 2016 Technow <info@technow.es> - 1.2-1
- Security and stability improvements
* Thu Feb 25 2016 Technow <info@technow.es> - 1.1-1
- Fixed lots of bugs
* Tue Jul 21 2015 Technow <info@technow.es> - 1.0-1
 - First release
