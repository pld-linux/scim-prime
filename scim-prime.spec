Summary:	SCIM IMEngine module using PRIME for Japanese input
Summary(pl.UTF-8):	Silnik IM SCIM dla metody wprowadzania znaków japońskich PRIME
Name:		scim-prime
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://osdn.jp/projects/scim-imengine/releases/p3523
Source0:	http://dl.osdn.jp/scim-imengine/29156/%{name}-%{version}.tar.gz
# Source0-md5:	12eae8334f73c70408b2f60c0ea0c82c
Patch0:		%{name}-no-rpath.patch
Patch1:		%{name}-gtk3.patch
Patch2:		%{name}-nobr.patch
URL:		https://osdn.jp/projects/scim-imengine/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.0
Requires:	prime >= 1.0.0
Requires:	scim >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scim-prime is a SCIM IMEngine module using PRIME.

PRIME is a predictive Japanese conversion engine written in Ruby.

%description -l pl.UTF-8
scim-prime to moduł silnika IM SCIM wykorzystujący metodę PRIME.

PRIME to silnik przewidującej konwersji dla języka japońskiego
napisany w języku Ruby.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/prime.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/prime-imengine-setup.so
%{_datadir}/scim/icons/scim-prime.png
