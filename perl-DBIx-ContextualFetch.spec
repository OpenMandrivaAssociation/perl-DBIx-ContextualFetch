%define upstream_name	 DBIx-ContextualFetch
%define upstream_version 1.03

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DBI::db\\)|perl\\(DBI::st\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Add contextual fetches to DBI
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
It always struck me odd that DBI didn't take much advantage of Perl's
context sensitivity. DBIx::ContextualFetch redefines some of the various
fetch methods to fix this oversight. It also adds a few new methods for
convenience (though not necessarily efficiency).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/DBIx
%{_mandir}/*/*

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 681359
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 403096
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.03-5mdv2009.0
+ Revision: 256584
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-3mdv2008.1
+ Revision: 133632
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Nov 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-2mdv2007.0
+ Revision: 86970
- rebuild
- Import perl-DBIx-ContextualFetch

* Thu Sep 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdk
- New release 1.03
- spec rewrite

* Thu Mar 17 2005 Bruno Cornec <bcornec@mandrakesoft.org> 1.02-1mdk
- Initial build.

