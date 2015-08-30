Summary:	A tool to copy files into or out of a cpio or tar archive
Name:		cpio
Version:	2.11
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/cpio
Group:		BLFS/SystemUtilities
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	 http://ftp.gnu.org/pub/gnu/cpio/%{name}-%{version}.tar.bz2
%description
The cpio package contains tools for archiving.
%prep
%setup -q
sed -i -e '/gets is a/d' gnu/stdio.in.h
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--libexecdir=/tmp \
	--mandir=%{_mandir} \
	--enable-mt \
	--with-rmt=%{_sbindir}/rmt \
	 --disable-silent-rules
make %{?_smp_mflags}
makeinfo --html			-o doc/html		doc/cpio.texi
makeinfo --html --no-split	-o doc/cpio.html	doc/cpio.texi
makeinfo --plaintext		-o doc/cpio.txt		doc/cpio.texi
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -m755 -d %{buildroot}%{_datadir}/doc/%{name}-%{version}/html 
install -v -m644    doc/html/*		%{buildroot}%{_datadir}/doc/%{name}-%{version}/html
install -v -m644    doc/cpio.{html,txt}	%{buildroot}%{_datadir}/doc/%{name}-%{version}
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%{_fixperms} %{buildroot}/*
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}/*
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/doc/%{name}-%{version}/*
%{_mandir}/man1/*
%changelog
*	Thu May 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.11-1
-	Initial build.	First version