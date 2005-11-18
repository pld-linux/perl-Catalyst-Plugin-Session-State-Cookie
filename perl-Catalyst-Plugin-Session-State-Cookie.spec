#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Session-State-Cookie
Summary:	Catalyst::Plugin::Session::State::Cookie - A session ID
#Summary(pl):	
Name:		perl-Catalyst-Plugin-Session-State-Cookie
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc64032b8fadf009fc5ecf86b0dfe50b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst-Plugin-Session >= 0.01
BuildRequires:	perl-Test-MockObject >= 1.01
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In order for Catalyst::Plugin::Session to work the session ID needs to be
stored on the client, and the session data needs to be stored on the server.

This plugin stores the session ID on the client using the cookie mechanism.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Catalyst/Plugin/Session/State/*.pm
%{_mandir}/man3/*