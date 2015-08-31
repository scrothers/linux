Summary:        Kernel
Name:           linux
Version:        3.13.3
Release:        2
License:        GPLv2
URL:            http://www.kernel.org/
Group:          System Environment/Kernel
Vendor:         Layerworx
Distribution:	  Layerworx/Linux
Source0:        http://www.kernel.org/pub/linux/kernel/v3.x/%{name}-%{version}.tar.xz
Source1:        linux-config-%{version}
BuildRequires:  kmod, patch, bash, sh-utils, tar bzip2, xz, findutils, gzip, m4 gawk
BuildRequires:  diffutils, gcc, binutils, bc
Provides:       %{name} = %{version}
Obsoletes:      %{name}

%package headers
Summary:        Header files for the Linux kernel for use by glibc
Group:          Development/System
Requires:       %{name} = %{version}
Obsoletes:      kernel-headers
Provides:       kernel-headers = %{version}

%package devel
Summary:        Development package for building kernel modules to match the %{version} kernel
Group:          System Environment/Kernel
Requires:       %{name} = %{version}
Obsoletes:      kernel-devel
Provides:       kernel-devel = %{version}

%package gpu
Summary:        Kernel GPU Drivers
Group:          System Environment/Kernel
Requires:       %{name} = %{version}
Obsoletes:      kernel-gpu
Provides:       kernel-gpu = %{version}

%package sound
Summary:        Kernel Sound modules
Group:          System Environment/Kernel
Requires:       %{name} = %{version}
Obsoletes:      kernel-sound
Provides:       kernel-sound = %{version}

%package docs
Summary:        Kernel Documentation
Group:          System Environment/Kernel
Requires:       %{name} = %{version}
Obsoletes:      kernel-docs
Provides:       kernel-docs = %{version}

%description
The kernel package contains the Linux kernel (vmlinuz), the core of any
Linux operating system.  The kernel handles the basic functions
of the operating system: memory allocation, process allocation, device
input and output, etc.

%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%description devel
This package provides headers and makefiles in order to build additional modules.

%description gpu
The Linux package contains the Linux kernel drivers for GPU

%description sound
The Linux package contains the Linux kernel sound support

%description docs
The Linux package which includes all of the Kernel documentation

%prep
%setup -q

%build
cp %{SOURCE1} .config
make mrproper
make LC=ALL= oldconfig
make VERBOSE=1 %{?_smp_mflags}

%install
# Create directories in the BUILDROOT
install -vdm 755 %{buildroot}/etc
install -vdm 755 %{buildroot}/boot
install -vdm 755 %{buildroot}%{_defaultdocdir}/%{name}-%{version}
install -vdm 755 %{buildroot}/etc/modprobe.d

# Install the firmware, modules and headers
make INSTALL_MOD_PATH=%{buildroot} modules_install
make INSTALL_HDR_PATH=%{buildroot} headers_install
make INSTALL_FW_PATH=%{buildroot} firmware_install

# Copy files to their correct locations
cp -v arch/x86/boot/bzImage	%{buildroot}/boot/vmlinuz-%{version}
cp -v System.map		%{buildroot}/boot/system.map-%{version}
cp -v .config			%{buildroot}/boot/config-%{version}
cp -r Documentation/*		%{buildroot}%{_defaultdocdir}/%{name}-%{version}

# Setup USB module probing on demand
cat > %{buildroot}/etc/modprobe.d/usb.conf << "EOF"
install ohci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i ohci_hcd ; true
install uhci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i uhci_hcd ; true
EOF

#	Cleanup dangling symlinks
rm -rf %{buildroot}/lib/modules/%{version}/source
rm -rf %{buildroot}/lib/modules/%{version}/build

%files
%defattr(-,root,root)
/boot/*
/lib/modules/%{version}/*
%exclude /lib/firmware/*
%exclude /lib/modules/%{version}/build
%exclude /lib/modules/%{version}/source
%exclude /lib/modules/%{version}/kernel/drivers/gpu
%exclude /lib/modules/%{version}/kernel/sound
%exclude /usr/share/*
%exclude /usr/include/*
%config(noreplace)/etc/modprobe.d/usb.conf
%{_defaultdocdir}/%{name}-%{version}/*

%files headers
%defattr (-, root, root)
/usr/include/*

%files devel
%defattr (-, root, root)
/usr/src/kernels/%{version}
/lib/modules/%{version}/build
/lib/modules/%{version}/source

%files sound
%defattr(-,root,root)
/lib/modules/%{version}/kernel/sound

%files gpu
%defattr(-,root,root)
%exclude /lib/modules/%{version}/kernel/drivers/gpu/drm/cirrus/
/lib/modules/%{version}/kernel/drivers/gpu

%files docs
%defattr(-,root,root)
/usr/share/doc/linux-%{version}/*

%changelog
* Mon Aug 31 2015 Steven Crothers <steven@layerworx.com> 3.13.3-2
- Setup additional packages for headers, devel, sound, gpu and docs.
- Reduce the size of the linux package to be installed
- Setup BuildRequires in the RPM spec to ensure a proper build is completed
- Setup Provides in the RPM spec to provide that data to RPM
- General clean up of the RPM spec file
* Sun Aug 30 2015 Steven Crothers <steven@layerworx.com> 3.13.3.-1
- Initial import from LFS Kernel build 3.13.3 (LFS 7.5)
