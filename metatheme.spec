Summary:	The GNOME Metatheme component
Summary(pl.UTF-8):	Komponent GNOME Metatheme
Name:		metatheme
Version:	0.9.7
Release:	0.2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/metatheme/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	bba39ec97ddd48f1e1b1f558bfabd6ae
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libbonoboui-devel >= 2.3.3-2
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	nautilus-devel >= 2.3.7-3
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A theme control for GTK+, Sawfish, the Background and XMMS.

%description -l pl.UTF-8
Kontrola motywów dla GTK+, Sawfisha, XMMS oraz tła.

%package devel
Summary:	Header files for use with the GNOME Metatheme Component
Summary(pl.UTF-8):	Pliki nagłówkowe do komponentu GNOME Metatheme
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The headers for creating the GNOME Metatheme Component plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek dla komponentu GNOME Metatheme.

%package static
Summary:	GNOME Metatheme Component static libraries
Summary(pl.UTF-8):	Statyczne biblioteki komponentu GNOME Metatheme
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries with which to link when building plugins for the
GNOME Metatheme Component.

%description static -l pl.UTF-8
Biblioteki statyczne, z którymi można konsolidować wtyczki dla
komponentu GNOME Metatheme.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/metatheme
%dir %{_libdir}/metatheme/plugins
%dir %{_libdir}/metatheme/plugins/%{version}
%attr(755,root,root) %{_libdir}/metatheme/plugins/%{version}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/metatheme/plugins/%{version}/lib*.??
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/metatheme-glade
%{_datadir}/mime-info/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/mtm

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/metatheme/plugins/%{version}/*.a
