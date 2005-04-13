%define		_snap	20050413
Summary:	Very easy to use GNOME Jabber client
Summary(pl):	Bardzo prosty w u¿yciu klient Jabbera dla GNOME
Name:		gossip
Version:	0.8.90
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications/Communications
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	f3e24e18bb83c2f0b3338fc35b50a1f0
#Source0:	http://ftp.gnome.org/pub/GNOME/sources/gossip/0.8/%{name}-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
URL:		http://gossip.imendio.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnutls-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 1:2.6.0
BuildRequires:	intltool >= 0.23
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	loudmouth-devel >= 0.17
BuildRequires:	dbus-glib-devel >= 0.22
BuildRequires:  rpmbuild(macros) >= 1.197
Requires(post,preun):   GConf2
Requires(post,postun):  scrollkeeper
Requires:	dbus >= 0.22-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gossip aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl
Celem Gossipa jest komunikowanie siê przy pomocy Jabbera najpro¶ciej
jak to tylko mo¿liwe.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-dbus

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
	
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no	

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gossip.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall gossip.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/gossip.png
%{_sysconfdir}/gconf/schemas/*
