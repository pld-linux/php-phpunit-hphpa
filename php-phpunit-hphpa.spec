%define		pearname	hphpa
%include	/usr/lib/rpm/macros.php
Summary:	Convenience wrapper for HipHop's static analyzer
Name:		php-phpunit-hphpa
Version:	1.3.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	9fd2e38cd7d69f8cbd418e2d52d0b5c6
URL:		http://pear.phpunit.de/package/hphpa/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	hiphop-php >= 2.1
Requires:	php-channel(pear.phpunit.de)
Requires:	php-ezc-ConsoleTools >= 1.6
Requires:	php-pear
Requires:	php-phpunit-FinderFacade >= 1.1.0
Requires:	php-phpunit-Version >= 1.0.0
Requires:	php-theseer-fDOMDocument >= 1.2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convenience wrapper for HipHop's static analyzer.

%prep
%pear_package_setup
mv docs/hphpa/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE ChangeLog.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/hphpa
%{php_pear_dir}/SebastianBergmann/HPHPA
%{php_pear_dir}/data/hphpa
