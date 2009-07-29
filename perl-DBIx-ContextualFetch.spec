%define upstream_name	 DBIx-ContextualFetch
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

summary:	Add contextual fetches to DBI
license:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
It always struck me odd that DBI didn't take much advantage of Perl's
context sensitivity. DBIx::ContextualFetch redefines some of the various
fetch methods to fix this oversight. It also adds a few new methods for
convenience (though not necessarily efficiency).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
