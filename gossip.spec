# TODO:
# - maybe better descriptions
#
# NOTE:
# - patching the desktop file make no sense for a moment,
#   due to lack of pl translations (Summary fields are created
#   automagically)
#
Summary:	Very easy to use GNOME Jabber client
Summary(pl):	Bardzo prosty w u¿yciu klient Jabbera dla GNOME
Name:		gossip
Version:	0.3
Release:	0.2
License:	GPL
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gossip/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	771f1422241dcebccb666811908339b2
URL:		http://www.imendio.com/projects/gossip 
BuildRequires:	gtk+2-devel >= 2.0.4
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel
BuildRequires:	libxml2-devel
BuildRequires:	loudmouth-devel >= 0.10.1
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gossip aims at making Instant Messaging with Jabber as easy as
possible.

%description -l pl
Celem Gossipa jest komunikowanie siê przy pomocy Jabbera najpro¶ciej
jak to tylko mo¿liwe.

%prep
%setup -q

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
