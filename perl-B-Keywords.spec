#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-Keywords
Version  : 1.18
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Keywords-1.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Keywords-1.18.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libb/libb-keywords-perl/libb-keywords-perl_1.18-1.debian.tar.xz
Summary  : 'Lists of reserved barewords and symbol names'
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-B-Keywords-license
Requires: perl-B-Keywords-man

%description
NAME
B::Keywords - Lists of reserved barewords and symbol names
SYNOPSIS
use B::Keywords;
print join "\n", @B::Keywords::Symbols,
@B::Keywords::Barewords;

%package license
Summary: license components for the perl-B-Keywords package.
Group: Default

%description license
license components for the perl-B-Keywords package.


%package man
Summary: man components for the perl-B-Keywords package.
Group: Default

%description man
man components for the perl-B-Keywords package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n B-Keywords-1.18
mkdir -p %{_topdir}/BUILD/B-Keywords-1.18/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/B-Keywords-1.18/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-B-Keywords
cp LICENSE %{buildroot}/usr/share/doc/perl-B-Keywords/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-B-Keywords/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/B/Keywords.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-B-Keywords/LICENSE
/usr/share/doc/perl-B-Keywords/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/B::Keywords.3
