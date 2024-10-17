%define svn   1102486

Name:          kfacebook
Summary:       Plasma applet aimed to show your facebook friends with their status
Version:       1.0
Release:       %mkrel 0.%svn.1
Url:           https://websvn.kde.org/trunk/playground/pim/kfacebook/
License:       GPLv2+
Group:         Graphical desktop/KDE
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source0:       %{name}-%version.%svn.tar.bz2
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: kdepim4-devel
BuildRequires: boost-devel
%description
Plasma applet aimed to show your facebook friends with their status

#---------------------------------------------

%define kfacebook_major 4
%define libkfacebook %mklibname kfacebook %{kfacebook_major}

%package -n %libkfacebook
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkfacebook
%name library

%files -n %libkfacebook
%defattr(-,root,root)
%_kde_libdir/libkfacebook.so.%{kfacebook_major}*

#-----------------------------------------------------------------------------

%package -n plasma-applet-facebook
Summary:   Plasma applet aimed to show your facebook friends with their status
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet
Requires: plasma-engine-facebook = %version
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-applet-facebook
Plasma applet aimed to show your facebook friends with their status

%files -n plasma-applet-facebook
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_facebook.so
%_kde_datadir/kde4/services/plasma-applet-facebook.desktop

#-----------------------------------------------------------------------------

%package -n plasma-engine-facebook
Summary: Plasma facebook engine
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-engine
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-engine-facebook
Plasma facebook engine.

%files -n plasma-engine-facebook
%defattr(-,root,root)
%_kde_bindir/akonadi_facebook_resource
%_kde_datadir/akonadi/agents/facebookresource.desktop
%_kde_appsdir/desktoptheme/default/widgets/facebookbg.svg
%_kde_libdir/kde4/plasma_engine_facebook.so
%_kde_datadir/kde4/services/plasma-engine-facebook.desktop

#-----------------------------------------------------------------------------


%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: %libkfacebook = %version

%description  devel
Files needed to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_libdir/libkfacebook.so
%_kde_includedir/kfacebook

#---------------------------------------------

%prep
%setup -q  -n %name

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
