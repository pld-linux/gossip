Summary:	Very easy to use GNOME Jabber client
Summary(pl):	Bardzo prosty w u�yciu klient Jabbera dla GNOME
Name:		gossip
Version:	0.10
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gossip/0.10/%{name}-%{version}.tar.bz2
# Source0-md5:	57a3a1a84ca4451868df2f151bae50aa
Patch0:		%{name}-desktop.patch
URL:		http://gossip.imendio.org/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	gtk+2-devel >= 1:2.6.0
BuildRequires:	intltool >= 0.23
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	loudmouth-devel >= 1.0
BuildRequires:  rpmbuild(macros) >= 1.197
Requires(post,preun):   GConf2
Requires(post,postun):  scrollkeeper
Requires:	loudmouth >= 1.0
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

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

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
%{_datadir}/sounds/gossip
%{_desktopdir}/*.desktop
%{_pixmapsdir}/gossip.png
%{_sysconfdir}/gconf/schemas/gossip.schemas
%{_sysconfdir}/sound/events/*
