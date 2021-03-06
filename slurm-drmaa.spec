Name:		slurm-drmaa
Version:	dev
Release:	1%{?dist}

Summary:	PSNC DRMAA for SLURM
Group:		Development/Libraries
License:	GPLv3+
URL:		https://github.com/natefoo/slurm-drmaa
Requires:	slurm

BuildRequires:	slurm-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

Source:		%{name}-%{version}.tar.gz

%description
PSNC DRMAA for Simple Linux Utility for Resource Management (SLURM) is an
implementation of Open Grid Forum DRMAA 1.0 (Distributed Resource Management
Application API)  specification for submission and control of jobs to SLURM.
Using DRMAA, grid applications builders, portal developers and ISVs can use the
same high-level API to link their software with different cluster/resource
management systems.

%prep
%setup

%build
# -O2 causes sporadic uninterruptible hangs during job submission, decrease
# optimization to -O1 until this is fixed
RPM_OPT_FLAGS=`echo "$RPM_OPT_FLAGS" | sed -e 's/-O2 /-O0 /'`
CFLAGS="$RPM_OPT_FLAGS"
export CFLAGS
%configure

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"
DESTDIR="$RPM_BUILD_ROOT" make install
rm -rf "$RPM_BUILD_ROOT/etc"

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%doc COPYING
%doc NEWS
%doc README.md
%doc slurm_drmaa/slurm_drmaa.conf.example
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
