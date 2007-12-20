%define module	DBIx-ContextualFetch
%define name	perl-%{module}
%define version 1.03
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
summary:	Add contextual fetches to DBI
license:	Artistic
group:		Development/Perl
url:		http://search.cpan.org/dist/%{module}
source:		http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{module}-%{version}.tar.bz2
buildroot:	%{_tmppath}/%{name}-%{version}
buildarch:	noarch

%description
It always struck me odd that DBI didn't take much advantage of Perl's
context sensitivity. DBIx::ContextualFetch redefines some of the various
fetch methods to fix this oversight. It also adds a few new methods for
convenience (though not necessarily efficiency).

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/DBIx
%{_mandir}/*/*


