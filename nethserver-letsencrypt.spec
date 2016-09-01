Summary: nethserver letsencrypt integration
Name: nethserver-letsencrypt
Version: 1.1.2
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name} 

BuildRequires: nethserver-devtools >= 1.1.0-5

AutoReq: no
Requires: nethserver-base, nethserver-httpd
Requires: certbot


%description
NethServer Let's Encrypt integration

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
mkdir -p %{buildroot}/var/www/html/.well-known/acme-challenge/ 
echo "%doc COPYING" >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir /var/www/html/.well-known/acme-challenge/
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Sep 01 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- Let's Encrypt: generated certificate is invalid - Bug NethServer/dev#5092
- Apache vhost-default template expansion - NethServer/dev#5088

* Thu Aug 25 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- nethserver-letsencrypt: apache acl for 2.4 - Bug NethServer/dev#5082

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

* Fri May 20 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Let's Encrypt: apache template not expanded - Bug #3386 [NethServer]

* Tue Mar 15 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Let's Encrypt: missing update event - Bug #3365 [NethServer]

* Fri Feb 26 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Let's Encrypt (partial) support  - Feature #3355 [NethServer]

