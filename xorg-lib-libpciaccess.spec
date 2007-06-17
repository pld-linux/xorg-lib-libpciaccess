%define	snap	20070612
Summary:	libpciaccess library to access PCI bus and devices
Summary(pl.UTF-8):	Biblioteka libpciaccess do dostępu do szyny i urządzeń PCI
Name:		xorg-lib-libpciaccess
Version:	0.8.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	libpciaccess-%{snap}.tar.gz
# Source0-md5:	144304074a1d00842aaedf26600e5e70
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
# /etc/pci.ids
Requires:	pciutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpciaccess library provides generic access to the PCI bus and
devices.

%description -l pl.UTF-8
Biblioteka pciaccess daje ogólny dostep do szyny i urządzeń PCI.

%package devel
Summary:	Header files for pciaccess library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki pciaccess
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
pciaccess library.

This package contains the header files needed to develop programs that
use pciaccess.

%description devel -l pl.UTF-8
Biblioteka pciaccess.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki pciaccess.

%package static
Summary:	Static pciaccess library
Summary(pl.UTF-8):	Biblioteka statyczna pciaccess
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
pciaccess library.

This package contains the static pciaccess library.

%description static -l pl.UTF-8
Biblioteka pciaccess.

Pakiet zawiera statyczną bibliotekę pciaccess.

%prep
%setup -q -n libpciaccess

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pciids-path=/etc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libpciaccess.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpciaccess.so
%{_libdir}/libpciaccess.la
%{_pkgconfigdir}/pciaccess.pc
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpciaccess.a
