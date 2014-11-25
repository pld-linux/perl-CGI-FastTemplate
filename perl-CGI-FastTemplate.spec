#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	CGI
%define		pnam	FastTemplate
%include	/usr/lib/rpm/macros.perl
Summary:	CGI::FastTemplate - Perl extension for managing templates, and performing variable interpolation
Summary(pl.UTF-8):	CGI::FastTemplate - rozszerzenie Perla do zarządzania wzorcami i zastępowania zmiennych
Name:		perl-CGI-FastTemplate
Version:	1.09
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c5fe8ead04c525c8d5633c9453af802f
URL:		http://search.cpan.org/dist/CGI-FastTemplate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::FastTemplate Perl module manages templates and parses templates
replacing variable names with values.

%description -l pl.UTF-8
Moduł Perla CGI::FastTemplate zarządza wzorcami i analizuje je,
zastępując przy tym nazwy zmiennych wartościami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README templates
%{perl_vendorlib}/CGI/FastTemplate.pm
%{_mandir}/man3/*
