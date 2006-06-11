Summary:	Very easy to use GNOME Jabber client
Summary(pl):	Bardzo prosty w u¿yciu klient Jabbera dla GNOME
Name:		gossip
Version:	0.11.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gossip/0.11/%{name}-%{version}.tar.bz2
# Source0-md5:	f67bbeac01b48b1f140c93ea64045e65
Patch0:		%{name}-desktop.patch
URL:		http://gossip.imendio.org/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	gtk+2-devel >= 2:2.9.2
BuildRequires:	intltool >= 0.35
BuildRequires:	iso-codes
BuildRequires:	libgalago-devel
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.15.1
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	loudmouth-devel >= 1.0.3
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libXScrnSaver-devel
Requires(post,postun):	gtk+2 >= 2:2.9.2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	hicolor-icon-theme
Requires:	loudmouth >= 1.0.3
Obsoletes:	gnome-jabber
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
	--disable-schemas-install \
	--disable-scrollkeeper \
	--enable-libnotify \
	--enable-dbus \
	--with-galago
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gossip.schemas
%scrollkeeper_update_post
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%preun
%gconf_schema_uninstall gossip.schemas

%postun
%scrollkeeper_update_postun
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/sounds/gossip
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/gossip.schemas
%{_sysconfdir}/sound/events/*
