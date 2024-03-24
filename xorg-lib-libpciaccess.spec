#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	libpciaccess library to access PCI bus and devices
Summary(pl.UTF-8):	Biblioteka libpciaccess do dostępu do szyny i urządzeń PCI
Name:		xorg-lib-libpciaccess
Version:	0.18.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/archive/individual/lib/libpciaccess-%{version}.tar.xz
# Source0-md5:	57c7efbeceedefde006123a77a7bc825
URL:		https://xorg.freedesktop.org/
BuildRequires:	meson >= 0.48.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Requires:	zlib-devel

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

%if %{with static_libs}
%{__sed} -i -e '/^libpciaccess = / s/shared_library/library/' src/meson.build
%endif

%build
%meson build \
	-Dpci-ids=/lib/hwdata \
	-Dzlib=enabled

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.md
%attr(755,root,root) %{_libdir}/libpciaccess.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpciaccess.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpciaccess.so
%{_pkgconfigdir}/pciaccess.pc
%{_includedir}/pciaccess.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpciaccess.a
%endif
