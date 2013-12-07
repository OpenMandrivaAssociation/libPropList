%define fname	PropList
%define major	0
%define libname	%mklibname %{fname} %{major}
%define devname	%mklibname %{fname} -d

Summary:	Library for configuration or preference files compatible GNUstep/OPENSTEP
Name:		libPropList
Version:	0.10.1
Release:	22
License:	LGPLv2
Group:		System/Libraries
Source0:	ftp://ftp.windowmaker.org/libs/%{name}-%{version}.tar.bz2
Patch0:		libPropList-0.10.1-fix-str-fmt.patch
BuildRequires:	flex

%description
The purpose of PL is to closely mimic the behavior of the property
lists used in the GNUstep/OPENSTEP (they're formed with the NSString,
NSData, NSArray and NSDictionary classes) and to be duly compatible.

PL enables programs that use configuration or preference3 files to
make these compatible with GNUstep/OPENSTEP's user defaults
handling mechanism, without needing to use Objective-C or GNUstep/
OPENSTEP themselves.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for configuration or preference files compatible GNUstep/OPENSTEP
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
The purpose of PropList is to closely mimic the behavior of the property
lists used in the GNUstep/OPENSTEP (they're formed with the NSString,
NSData, NSArray and NSDictionary classes) and to be duly compatible.

PropList enables programs that use configuration or preference3 files to
make these compatible with GNUstep/OPENSTEP's user defaults
handling mechanism, without needing to use Objective-C or GNUstep/
OPENSTEP themselves.

%package -n %{devname}
Summary:	Library for configuration or preference files compatible GNUstep/OPENSTEP
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{fname}-devel = %{version}-%{release}

%description -n %{devname}
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
%makeinstall_std

%files -n %{libname}
%{_libdir}/libPropList.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README TODO
%{_libdir}/lib*.so
%{_includedir}/*.h

