%define	_class	Net
%define	_subclass	SMTP
%define	modname	%{_class}_%{_subclass}

Summary:	An implementation of the SMTP protocol
Name:		php-pear-%{modname}
Version:	1.7.3
Release:	2
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/%{modname}
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket class.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/*
%doc %{modname}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml
%{_datadir}/pear/doc/Net_SMTP
%{_datadir}/pear/test/Net_SMTP
