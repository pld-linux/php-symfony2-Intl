%define		pearname	Intl
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Intl Component
Name:		php-symfony2-Intl
Version:	2.4.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	650a7e4b119e035900b66837a796bf29
URL:		http://symfony.com/doc/2.4/components/intl.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.674
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-Icu >= 1.0
Suggests:	php(intl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A PHP replacement layer for the C intl extension that also provides
access to the localization data of the ICU library.

The replacement layer is limited to the locale "en". If you want to
use other locales, you should install the intl extension instead.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# dev tools
mv .%{php_pear_dir}/Symfony/Component/Intl/Resources/bin .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .
mv .%{php_pear_dir}/Symfony/Component/Intl/CONTRIBUTING.md .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md CONTRIBUTING.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/Intl
%{php_pear_dir}/Symfony/Component/Intl/*.php
%{php_pear_dir}/Symfony/Component/Intl/Collator
%{php_pear_dir}/Symfony/Component/Intl/DateFormatter
%{php_pear_dir}/Symfony/Component/Intl/Exception
%{php_pear_dir}/Symfony/Component/Intl/Globals
%{php_pear_dir}/Symfony/Component/Intl/Locale
%{php_pear_dir}/Symfony/Component/Intl/NumberFormatter
%{php_pear_dir}/Symfony/Component/Intl/ResourceBundle
%{php_pear_dir}/Symfony/Component/Intl/Util

%dir %{php_pear_dir}/Symfony/Component/Intl/Resources
%{php_pear_dir}/Symfony/Component/Intl/Resources/stubs
