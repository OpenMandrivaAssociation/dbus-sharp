%define name dbus-sharp
%define version 0.7.0
%define release %mkrel 1
%define pkgname %name-1.0

Summary: Managed D-Bus implementation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://github.com/downloads/mono/%name/%{name}-%{version}.tar.gz
License: MIT
Group: System/Libraries
Url: http://mono.github.com/dbus-sharp/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildArch: noarch

%description
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus).

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus).

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%prep
%setup -q -n %name-%version

%build
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING
%_prefix/lib/mono/%pkgname
%_prefix/lib/mono/gac/%name

%files devel
%defattr(-,root,root)
%doc examples
%_datadir/pkgconfig/%pkgname.pc


%changelog
* Wed Sep 15 2010 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 578512
- new version of renamed ndesk-dbus

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.6.1a-6mdv2011.0
+ Revision: 567916
- split out devel package

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.1a-5mdv2010.1
+ Revision: 523409
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6.1a-4mdv2010.0
+ Revision: 426247
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.6.1a-3mdv2009.1
+ Revision: 351629
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.6.1a-2mdv2009.0
+ Revision: 265197
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 0.6.1a-1mdv2009.0
+ Revision: 192442
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 101052
- new version
- fix build

* Mon Aug 06 2007 Götz Waschk <waschk@mandriva.org> 0.5.2-2mdv2008.0
+ Revision: 59367
- remove file conflicting with native dbus

* Mon Aug 06 2007 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 59362
- Import ndesk-dbus


* Wed Dec 13 2006 Götz Waschk <waschk@mandriva.org> 0.70-5mdv2007.0
+ Revision: 96161
- make it a noarch package

* Sat Oct 14 2006 Götz Waschk <waschk@mandriva.org> 0.70-4mdv2006.0
+ Revision: 64570
- Import dbus-sharp

* Sat Oct 14 2006 Götz Waschk <waschk@mandriva.org> 0.70-4mdv2007.1
- build examples with gtk-sharp2

* Fri Sep 22 2006 Götz Waschk <waschk@mandriva.org> 0.70-3mdv2007.0
- split monodoc API documentation to the doc package

* Wed Aug 02 2006 Götz Waschk <waschk@mandriva.org> 0.70-2mdv2007.0
- fix dll map

* Tue Aug 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.70-1mdv2007.0
- Initial package (based on dbus 0.62)

