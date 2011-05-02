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
%{_libdir}/lib*.la
%{_includedir}/*.h

