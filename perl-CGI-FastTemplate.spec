%define	pdir	CGI
%define	pnam	FastTemplate
%include	/usr/lib/rpm/macros.perl
Summary:	CGI-FastTemplate perl module
Summary(pl):	Modu� perla CGI-FastTemplate
Name:		perl-CGI-FastTemplate
Version:	1.09
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-FastTemplate manages templates and parses templates replacing
variable names with values.

%description -l pl
Modu� perla CGI-FastTemplate.

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
