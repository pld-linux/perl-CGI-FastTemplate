%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	FastTemplate
Summary:	CGI::FastTemplate perl module
Summary(pl):	Modu³ perla CGI::FastTemplate
Name:		perl-CGI-FastTemplate
Version:	1.09
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::FastTemplate manages templates and parses templates replacing
variable names with values.

%description -l pl
Modu³ perla CGI::FastTemplate - zarz±dza wzorcami i analizuje je,
zastêpuj±c przy tym nazwy zmiennych warto¶ciami.

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
