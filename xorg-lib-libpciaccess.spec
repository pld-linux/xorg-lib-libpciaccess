Summary:	libpciaccess library to access PCI bus and devices
Summary(pl.UTF-8):	Biblioteka libpciaccess do dostępu do szyny i urządzeń PCI
Name:		xorg-lib-libpciaccess
Version:	0.14
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/archive/individual/lib/libpciaccess-%{version}.tar.bz2
# Source0-md5:	8f436e151d5106a9cfaa71857a066d33
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	zlib-devel
# pci.ids
Requires:	hwdata >= 0.243-2
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
This package contains the header files needed to develop programs that
use pciaccess library.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki pciaccess.

%package static
Summary:	Static pciaccess library
Summary(pl.UTF-8):	Biblioteka statyczna pciaccess
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static pciaccess library.

%description static -l pl.UTF-8
Pakiet zawiera statyczną bibliotekę pciaccess.

%prep
%setup -q -n libpciaccess-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pciids-path=/lib/hwdata \
	--with-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpciaccess.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libpciaccess.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpciaccess.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpciaccess.so
%{_pkgconfigdir}/pciaccess.pc
%{_includedir}/pciaccess.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpciaccess.a
