%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	FastTemplate
Summary:	CGI-FastTemplate perl module
Summary(pl):	Modu³ perla CGI-FastTemplate
Name:		perl-CGI-FastTemplate
Version:	1.09
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-FastTemplate manages templates and parses templates replacing
variable names with values.

%description -l pl
Modu³ perla CGI-FastTemplate.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz templates
%{perl_sitelib}/CGI/FastTemplate.pm
%{_mandir}/man3/*
