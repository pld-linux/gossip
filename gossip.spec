# TODO:
# - maybe better descriptions
#
Summary:	Very easy to use GNOME Jabber client
Summary(pl):	Bardzo prosty w u�yciu klient Jabbera dla GNOME
Name:		gossip
Version:	0.7.6
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gossip/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	76f21e584fe8996ebd44cef2c6bf31c2
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale_names.patch
Patch2:		%{name}-dbus.patch
URL:		http://gossip.imendio.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	gnutls-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2.0.4
BuildRequires:	intltool >= 0.23
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	loudmouth-devel >= 0.15.1
BuildRequires:	dbus-glib-devel >= 0.22
Requires(post):	GConf2 >= 2.3.0
Requires(post):	scrollkeeper
Requires:	dbus >= 0.22-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gossip aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl
Celem Gossipa jest komunikowanie si� przy pomocy Jabbera najpro�ciej
jak to tylko mo�liwe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

mv -f po/{no,nb}.po

%build
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
	
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install
/usr/bin/scrollkeeper-update

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/gossip.png
