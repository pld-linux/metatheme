Summary:	The GNOME Metatheme component
Summary(pl):	Komponent GNOME Metatheme
Name:		metatheme
Version:	0.9.6
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	GConf2-devel
BuildRequires:	libbonobo-devel
BuildRequires:	libbonoboui-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnome-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	nautilus-devel >= 1.1.13
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
A theme control for GTK+, Sawfish, the Background and XMMS.

%description -l pl
Kontrola motywów dla GTK+, Sawfisha, XMMS oraz t³a.

%package devel
Summary:	Header files for use with the GNOME Metatheme Component
Summary(pl):	Pliki nag³ówkowe do komponentu GNOME Metatheme
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
The headers for creating the GNOME Metatheme Component plugins.

%description devel -l pl
Pliki nag³ówkowe do tworzenia wtyczek dla komponentu GNOME Metatheme.

%package static
Summary:	GNOME Metatheme Component static libraries
Summary(pl):	Statyczne biblioteki komponentu GNOME Metatheme
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries with which to link when building plugins for the
GNOME Metatheme Component.

%description static -l pl
Statyczne biblioteki z którymi mo¿na linkowaæ wtyczki dla komponentu
GNOME Metatheme.

%prep
%setup -q

%build
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/metatheme
%dir %{_libdir}/metatheme/plugins
%dir %{_libdir}/metatheme/plugins/%{version}
%attr(755,root,root) %{_libdir}/metatheme/plugins/%{version}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/metatheme/plugins/%{version}/lib*.??
%{_datadir}/applications/*
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/metatheme-glade
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.??
%{_includedir}/mtm

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/metatheme/plugins/%{version}/*.a
