# TODO:
# - maybe better descriptions
#
# NOTE:
# - patching the desktop file make no sense for a moment,
#   due to lack of pl translations (Summary fields are created
#   automagically)
#
%define cvs 20031106
#
Summary:	Very easy to use GNOME Jabber client
Summary(pl):	Bardzo prosty w u�yciu klient Jabbera dla GNOME
Name:		gossip
Version:	0.6
Release:	0.%{cvs}.1
License:	GPL
Group:		Applications/Communications
# releases: http://ftp.gnome.org/pub/gnome/sources/gossip/
Source0:	gossip-cvs-%{cvs}.tar.gz
# Source0-md5:	f4d4ad880564c9231475cfc5f1996267
URL:		http://www.imendio.com/projects/gossip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	gnutls-devel >= 0.9.95
BuildRequires:	gtk+2-devel >= 2.0.4
BuildRequires:	intltool >= 0.23
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	loudmouth-devel >= 0.12
Requires(post):	GConf2 >= 2.3.0
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gossip aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl
Celem Gossipa jest komunikowanie si� przy pomocy Jabbera najpro�ciej
jak to tylko mo�liwe.

%prep
%setup -q -n gossip

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
%config %{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
