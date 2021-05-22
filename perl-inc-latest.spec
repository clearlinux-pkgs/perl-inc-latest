#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-inc-latest
Version  : 0.500
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/inc-latest-0.500.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/inc-latest-0.500.tar.gz
Summary  : 'use modules bundled in inc/ if they are newer than installed ones'
Group    : Development/Tools
License  : Apache-2.0
Requires: perl-inc-latest-license = %{version}-%{release}
Requires: perl-inc-latest-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
inc::latest - use modules bundled in inc/ if they are newer than
installed ones

%package dev
Summary: dev components for the perl-inc-latest package.
Group: Development
Provides: perl-inc-latest-devel = %{version}-%{release}
Requires: perl-inc-latest = %{version}-%{release}

%description dev
dev components for the perl-inc-latest package.


%package license
Summary: license components for the perl-inc-latest package.
Group: Default

%description license
license components for the perl-inc-latest package.


%package perl
Summary: perl components for the perl-inc-latest package.
Group: Default
Requires: perl-inc-latest = %{version}-%{release}

%description perl
perl components for the perl-inc-latest package.


%prep
%setup -q -n inc-latest-0.500
cd %{_builddir}/inc-latest-0.500

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-inc-latest
cp %{_builddir}/inc-latest-0.500/LICENSE %{buildroot}/usr/share/package-licenses/perl-inc-latest/8af75ac213e6a4987d20ae377e4de5e791949f19
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/inc::latest.3
/usr/share/man/man3/inc::latest::private.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-inc-latest/8af75ac213e6a4987d20ae377e4de5e791949f19

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/inc/latest.pm
/usr/lib/perl5/vendor_perl/5.34.0/inc/latest/private.pm
