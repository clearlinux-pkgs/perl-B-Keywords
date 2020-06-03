#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-Keywords
Version  : 1.21
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Keywords-1.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Keywords-1.21.tar.gz
Summary  : 'Lists of reserved barewords and symbol names'
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-B-Keywords-license = %{version}-%{release}
Requires: perl-B-Keywords-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
B::Keywords - Lists of reserved barewords and symbol names
SYNOPSIS
use B::Keywords qw( @Symbols @Barewords );
print join "\n", @Symbols,
@Barewords;

%package dev
Summary: dev components for the perl-B-Keywords package.
Group: Development
Provides: perl-B-Keywords-devel = %{version}-%{release}
Requires: perl-B-Keywords = %{version}-%{release}

%description dev
dev components for the perl-B-Keywords package.


%package license
Summary: license components for the perl-B-Keywords package.
Group: Default

%description license
license components for the perl-B-Keywords package.


%package perl
Summary: perl components for the perl-B-Keywords package.
Group: Default
Requires: perl-B-Keywords = %{version}-%{release}

%description perl
perl components for the perl-B-Keywords package.


%prep
%setup -q -n B-Keywords-1.21
cd %{_builddir}/B-Keywords-1.21

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-B-Keywords
cp %{_builddir}/B-Keywords-1.21/LICENSE %{buildroot}/usr/share/package-licenses/perl-B-Keywords/0e987cce2b4e94a4d6920e7353f8674a4462528a
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
/usr/share/man/man3/B::Keywords.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-B-Keywords/0e987cce2b4e94a4d6920e7353f8674a4462528a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/B/Keywords.pm
