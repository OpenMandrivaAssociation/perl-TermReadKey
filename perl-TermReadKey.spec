### EL6 ships with perl-TermReadKey-2.30-10.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name TermReadKey

Summary: Perl module for simple terminal control
Name: perl-TermReadKey
Version: 2.30
Release: %mkrel 1
License: Artistic/GPL
Group: Development/Perl
URL: https://search.cpan.org/dist/TermReadKey/
Source: http://www.cpan.org/modules/by-module/Term/TermReadKey-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl
Obsoletes: perl-Term-ReadKey <= %{version}-%{release}
Provides: perl-Term-ReadKey = %{version}-%{release}

%description
Term::ReadKey is a compiled perl module dedicated to providing simple
control over terminal driver modes (cbreak, raw, cooked, etc.,) support for
non-blocking reads, if the architecture allows, and some generalized handy
functions for working with terminals. One of the main goals is to have the
functions as portable as possible, so you can just plug in "use Term::ReadKey"
on any architecture and have a good likelyhood of it working.

%prep
%setup -q -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorarch}/Term/
%{perl_vendorarch}/Term/ReadKey.pm
%dir %{perl_vendorarch}/auto/Term/
%{perl_vendorarch}/auto/Term/ReadKey/

%changelog
* Wed Aug 22 2007 Dag Wieers <dag@wieers.com> - 2.30-3 - 7981+/dag
- Obsolete package perl-Term-ReadKey.

* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 2.30-1
- Initial package. (using DAR)
