Summary:	xprehashprinterlist application
Summary(pl.UTF-8):	Aplikacja xprehashprinterlist
Name:		xorg-app-xprehashprinterlist
Version:	1.0.1
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xprehashprinterlist-%{version}.tar.bz2
# Source0-md5:	99ee20a9af25375895f5d7ebc1004163
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xprehashprinterlist application.

%description -l pl.UTF-8
Aplikacja xprehashprinterlist.

%prep
%setup -q -n xprehashprinterlist-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xprehashprinterlist
%{_mandir}/man1/xprehashprinterlist.1*
