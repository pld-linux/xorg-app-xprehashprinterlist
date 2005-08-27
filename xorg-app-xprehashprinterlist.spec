# $Rev: 3413 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xprehashprinterlist application
Summary(pl):	Aplikacja xprehashprinterlist
Name:		xorg-app-xprehashprinterlist
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xprehashprinterlist-%{version}.tar.bz2
# Source0-md5:	492ce2b8283780c3a86b7e0376fdd02d
Patch0:		xprehashprinterlist-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/xprehashprinterlist-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xprehashprinterlist application.

%description -l pl
Aplikacja xprehashprinterlist.


%prep
%setup -q -n xprehashprinterlist-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
