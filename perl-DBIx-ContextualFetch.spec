%define upstream_name	 DBIx-ContextualFetch
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DBI::db\\)|perl\\(DBI::st\\)'
%endif

Name:		perl-%{upstream_name}
Version:	1.03
Release:	9

Summary:	Add contextual fetches to DBI
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/DBIx-ContextualFetch
Source0:	https://cpan.metacpan.org/authors/id/T/TM/TMTM/DBIx-ContextualFetch-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
It always struck me odd that DBI didn't take much advantage of Perl's
context sensitivity. DBIx::ContextualFetch redefines some of the various
fetch methods to fix this oversight. It also adds a few new methods for
convenience (though not necessarily efficiency).

%prep
%setup -q -n %{upstream_name}-%{version}

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
- rebuild using %1.03 Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.03-5mdv2009.0
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

