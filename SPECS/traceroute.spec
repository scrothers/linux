Summary:	Tracks the route taken by packets over an IP network
Name:		traceroute
Version:	2.0.19
Release:	1
License:	GPLv2
URL:		http://traceroute.sourceforge.net/
Group:		BLFS/NetworkingUtilities
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	 http://downloads.sourceforge.net/traceroute/%{name}-%{version}.tar.gz
%description
The Traceroute package contains a program which is used to display 
the network route that packets take to reach a specified host. This
is a standard network troubleshooting tool. If you find yourself 
unable to connect to another system, traceroute can help pinpoint 
the problem.
%prep
%setup -q
%build
make %{?_smp_mflags} CFLAGS="%{optflags}"
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make prefix=/usr DESTDIR=%{buildroot} install
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man8/*
%changelog
*	Sat Jun 01 2013 baho-utot <baho-utot@columbus.rr.com> 2.0.19-1
-	Initial build.	First version