Summary: nethserver letsencrypt integration
Name: nethserver-letsencrypt
Version: 1.0.6
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name} 

BuildRequires: nethserver-devtools >= 1.1.0-5

AutoReq: no
Requires: nethserver-base, nethserver-httpd
Requires: dehydrated
Obsoletes: letsencrypt.sh


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
mkdir -p %{buildroot}/etc/letsencrypt.sh/certs/
echo "%doc COPYING" >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir /var/www/html/.well-known/acme-challenge/
%dir /etc/letsencrypt.sh/
%dir /etc/letsencrypt.sh/certs/

%changelog
* Fri Oct 11 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.6-1
- Let's Encrypt: staging request always fails - Bug #3453 [NethServer 6]

* Fri Nov 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.5-1
- Impossible to obtain Let's encrypt certs on NS6 - Bug NethServer/dev#5389

* Wed Mar 29 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.4-1
- Avoid certificate generation on Let's Encrypt renewal - #3438

* Mon Jun 06 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1
- Let's Encrypt: certificates not renewed - Bug #3399 [NethServer]

* Fri May 20 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Let's Encrypt: apache template not expanded - Bug #3386 [NethServer]

* Tue Mar 15 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Let's Encrypt: missing update event - Bug #3365 [NethServer]

* Fri Feb 26 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Let's Encrypt (partial) support  - Feature #3355 [NethServer]

