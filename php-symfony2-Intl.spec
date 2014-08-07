%define		pearname	Intl
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Intl Component
Name:		php-symfony2-Intl
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	cee0e1e9ace6b9651c6d940ab6988a03
URL:		http://symfony.com/doc/2.4/components/intl.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.674
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
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
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests
# dev tools for Intl package maintainer
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Resources/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md CONTRIBUTING.md
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
