%include	/usr/lib/rpm/macros.perl
Summary:	CGI-FastTemplate perl module
Summary(pl):	Modu³ perla CGI-FastTemplate
Name:		perl-CGI-FastTemplate
Version:	1.09
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-FastTemplate-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-FastTemplate manages templates and parses templates replacing
variable names with values.

%description -l pl
Modu³ perla CGI-FastTemplate.

%prep
%setup -q -n CGI-FastTemplate-%{version}

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
