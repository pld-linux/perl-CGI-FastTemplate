%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	FastTemplate
Summary:	CGI::FastTemplate - Perl extension for managing templates, and performing variable interpolation
Summary(pl):	CGI::FastTemplate - rozszerzenie Perla do zarządzania wzorcami i zastępowania zmiennych
Name:		perl-CGI-FastTemplate
Version:	1.09
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c5fe8ead04c525c8d5633c9453af802f
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::FastTemplate Perl module manages templates and parses templates
replacing variable names with values.

%description -l pl
Moduł Perla CGI::FastTemplate zarządza wzorcami i analizuje je,
zastępując przy tym nazwy zmiennych wartościami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README templates
%{perl_vendorlib}/CGI/FastTemplate.pm
%{_mandir}/man3/*
