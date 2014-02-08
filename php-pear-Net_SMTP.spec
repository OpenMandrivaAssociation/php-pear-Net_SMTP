%define		_class		Net
%define		_subclass	SMTP
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.6.1
Release:	6
Summary:	An implementation of the SMTP protocol
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket class.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.0-1mdv2011.0
+ Revision: 685575
- update to new version 1.6.0

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.4-2
+ Revision: 667632
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.4-1mdv2011.0
+ Revision: 587645
- update to new version 1.4.4

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.2-1mdv2010.1
+ Revision: 531326
- update to new version 1.4.2

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.1-1mdv2010.1
+ Revision: 495841
- update to new version 1.4.1

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.4-1mdv2010.1
+ Revision: 489154
- update to new version 1.3.4

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-4mdv2010.1
+ Revision: 468721
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Nov 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-3mdv2010.1
+ Revision: 463809
- use rpm filetriggers to register starting from mandriva 2010.1

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-2mdv2010.0
+ Revision: 450225
- use pear installer
- use fedora %%post/%%postun

* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-1mdv2010.0
+ Revision: 400322
- update to new version 1.3.3

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-1mdv2009.1
+ Revision: 357911
- update to new version 1.3.2

  + Jérôme Soyer <saispo@mandriva.org>
    - update to new version 1.3.2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-2mdv2009.1
+ Revision: 322499
- rebuild

* Wed Aug 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.3.1-1mdv2009.0
+ Revision: 276681
- new release 1.3.1

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-2mdv2009.0
+ Revision: 236994
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2.10-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Adam Williamson <awilliamson@mandriva.org> 1.2.10-1mdv2008.0
+ Revision: 55646
- Import php-pear-Net_SMTP

