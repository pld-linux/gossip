# TODO:
# - maybe better descriptions
#
%define		snap 20031128
Summary:	Very easy to use GNOME Jabber client
Summary(pl):	Bardzo prosty w u¿yciu klient Jabbera dla GNOME
Name:		gossip
Version:	0.6
Release:	2.%{snap}.1
License:	GPL
Group:		Applications/Communications
#Source0:	http://ftp.gnome.org/pub/GNOME/sources/gossip/0.6/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.gz
# Source0-md5:	444b88855f8fee73638b64d411ab8740
Source1:	%{name}.png
Patch0:		%{name}-desktop-icon.patch
URL:		http://gossip.imendio.org/
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
BuildRequires:	loudmouth-devel >= 0.14.1
Requires(post):	GConf2 >= 2.3.0
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gossip aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl
Celem Gossipa jest komunikowanie siê przy pomocy Jabbera najpro¶ciej
jak to tylko mo¿liwe.

%prep
%setup -q -n %{name}-%{version}-%{snap}
%patch0 -p1

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
install -d $RPM_BUILD_ROOT/%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
	
install -c %{SOURCE1} $RPM_BUILD_ROOT/%{_pixmapsdir}

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
