%define fname PropList
%define major 0
%define libname %mklibname %fname %major
%define develname %mklibname %fname -d

Summary:	Library for configuration or preference files compatible GNUstep/OPENSTEP
Name:		libPropList
Version:	0.10.1
Release:	%mkrel 18
License:	GPL/LGPL
Group:		System/Libraries

Source:		ftp://ftp.windowmaker.org/libs/libPropList-%{version}.tar.bz2
Patch0:		libPropList-0.10.1-fix-str-fmt.patch

BuildRequires:	flex
Buildroot:	%{_tmppath}/libPropList-root
Obsoletes:	wmakerconf <= 2.5-1mdk

%description
The purpose of PL is to closely mimic the behavior of the property
lists used in the GNUstep/OPENSTEP (they're formed with the NSString,
NSData, NSArray and NSDictionary classes) and to be duly compatible.

PL enables programs that use configuration or preference3 files to
make these compatible with GNUstep/OPENSTEP's user defaults
handling mechanism, without needing to use Objective-C or GNUstep/
OPENSTEP themselves.

%package -n %libname
Group:      System/Libraries
Summary:	Library for configuration or preference files compatible GNUstep/OPENSTEP
Provides: %name = %version-%release
Obsoletes: %name

%description -n %libname
The purpose of PropList is to closely mimic the behavior of the property
lists used in the GNUstep/OPENSTEP (they're formed with the NSString,
NSData, NSArray and NSDictionary classes) and to be duly compatible.

PropList enables programs that use configuration or preference3 files to
make these compatible with GNUstep/OPENSTEP's user defaults
handling mechanism, without needing to use Objective-C or GNUstep/
OPENSTEP themselves.

%package -n %develname
Summary:	Library for configuration or preference files compatible GNUstep/OPENSTEP
Group:		Development/C
Requires:	%libname = %version-%release
Provides:   %name-devel = %version-%release
Provides:   %fname-devel = %version-%release
Provides:   %{libname}-devel = %version-%release
Obsoletes:  %name-devel
Obsoletes:  %mklibname %fname 0 -d

%description -n %develname
This package contains libraries and header files needs for development.

%prep 
%setup -q
%patch0 -p0

%build
%configure2_5x \
	--disable-static \
	--host=%{_host} \
	--target=%{_target_platform}
make

%install
rm -fr %buildroot
%makeinstall_std

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README TODO
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*.h



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-18mdv2011.0
+ Revision: 662344
- mass rebuild

* Mon Feb 14 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.10.1-17
+ Revision: 637748
- Rebuild since "-devel" packages seem to have disappeared

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-16mdv2011.0
+ Revision: 602516
- rebuild

  + Matthew Dawkins <mattydaw@mandriva.org>
    - dropped major from devel pkg name
    - disabled static build
    - cleanups on summary and descriptions

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-14mdv2010.1
+ Revision: 520746
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.10.1-13mdv2010.0
+ Revision: 425511
- rebuild

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 0.10.1-12mdv2009.1
+ Revision: 365692
- set target
- fix str fmt

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.10.1-12mdv2009.0
+ Revision: 222970
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.10.1-11mdv2008.1
+ Revision: 150790
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Oct 20 2005 Olivier Thauvin <nanardon@mandriva.org> 0.10.1-10mdk
- rebuild

* Tue Jul 08 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.10.1-9mdk
- reupload, again
- rebuild for requires/provides

* Wed May 28 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.10.1-8mdk 
- fix version
- reupload

* Sun May 04 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.10.1-7mdk
- rebuild for rpm 4.2
- use %%mklibname

* Thu Sep 06 2001 Stefan van der Eijk <stefan@eijk.nu> 0.10.1-6mdk
- BuildRequires:	flex
- Copyright --> License

* Fri Nov 10 2000 David BAUDENS <baudens@mandrakesoft.com> 0.10.1-5mdk
- Rebuild with glibc-2.2 & gcc-2.96

* Mon Sep 25 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 0.10.1-4mdk
- changed path in Copyright header to /usr/share/doc

* Fri Aug 04 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.10.1-3mdk
- rebuild with macros
- move *.so to devel

* Fri Apr 14 2000 David BAUDENS <baudens@mandrakesoft.com> 0.10.1-2mdk
- Make rpmlint happy

* Mon Apr 03 2000 David BAUDENS <baudens@mandrakesoft.com> 0.10.1-1mdk
- 0.10.1

* Thu Mar 30 2000 David BAUDENS <baudens@mandrakesoft.com> 0.10.0-2mdk
- Split in two packages (normal and devel)

* Thu Mar 30 2000 David BAUDENS <baudens@mandrakesoft.com> 0.10.0-1mdk
- 0.10.0
- Use new Groups
- Use %%{_tmppath} for BuildRoot
- Clean spec

* Mon Nov 29 1999 - David BAUDENS <baudens@mandrakesoft.com>
- Back to 0.9.1 (WindowMaker seems unstable with 0.9.2)
- Add a defattr

* Fri Oct 01 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- 0.9.2

* Thu Aug 05 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- changed Summary, it was too large

* Mon Jun 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Last CVS version from Mon Jun 28 1999.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Feb 02 1999 Cristian Gafton <gafton@redhat.com>
- packaged independently

