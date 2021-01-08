Summary: nethserver letsencrypt integration
Name: nethserver-letsencrypt
Version: 1.2.0
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
* Fri Jan 08 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- Let's Encrypt: support DNS challange - NethServer/dev#6383

* Tue Apr 17 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.6-1
- Let's Encrypt: registration mail address not fully validated - Bug NethServer/dev#5455

* Fri Apr 06 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.5-1
- Certs from Letsencrypt renewal not propagated to https and Admin servers - Bug NethServer/dev#5441

* Tue Apr 04 2017 Davide Principi <davide.principi@nethesis.it> - 1.1.4-1
- httpd does not start after restore if ssl certificate is from LetsEncrypt -- NethServer/dev#5241

* Thu Dec 15 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- Invoke certificate-update event when a valid certificate is renewed - NethServer/dev#5174

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

