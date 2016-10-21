%{?scl:%scl_package perl-Time-HiRes}

Name:           %{?scl_prefix}perl-Time-HiRes
Version:        1.9739
Release:        2%{?dist}
Summary:        High resolution alarm, sleep, gettimeofday, interval timers
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Time-HiRes/
Source0:        http://www.cpan.org/authors/id/J/JH/JHI/Time-HiRes-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Constant)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
BuildRequires:  %{?scl_prefix}perl(POSIX)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)

%{?perl_default_filter}

%description
The Time::HiRes module implements a Perl interface to the usleep, nanosleep,
ualarm, gettimeofday, and setitimer/getitimer system calls, in other words,
high resolution time and timers.

%prep
%setup -q -n Time-HiRes-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Time*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1.9739-2
- SCL

* Mon Jul 04 2016 Petr Pisar <ppisar@redhat.com> - 1.9739-1
- 1.9739 bump

* Mon Jun 27 2016 Petr Pisar <ppisar@redhat.com> - 1.9738-1
- 1.9738 bump

* Thu Jun 23 2016 Petr Pisar <ppisar@redhat.com> - 1.9737-1
- 1.9737 bump

* Wed Jun 22 2016 Petr Pisar <ppisar@redhat.com> - 1.9735-1
- 1.9735 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9733-365
- Increase release to favour standalone package

* Mon Apr 25 2016 Petr Pisar <ppisar@redhat.com> - 1.9733-1
- 1.9733 bump

* Mon Mar 14 2016 Petr Pisar <ppisar@redhat.com> - 1.9732-1
- 1.9732 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9728-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Petr Pisar <ppisar@redhat.com> - 1.9728-1
- 1.9728 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9726-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.9726-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.9726-311
- Perl 5.22 rebuild

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.9726-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.9726-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9726-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9726-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Petr Šabata <contyk@redhat.com> - 1.9726-1
- 1.9726 bugfix bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9725-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1.9725-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.9725-273
- Perl 5.18 rebuild

* Mon Apr 29 2013 Petr Pisar <ppisar@redhat.com> - 1.9725-272
- Increase release number to superseed perl.spec's sub-package

* Fri Apr 26 2013 Petr Pisar <ppisar@redhat.com> 1.9725-1
- Specfile autogenerated by cpanspec 1.78.
