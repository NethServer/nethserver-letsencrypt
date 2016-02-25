Summary: nethserver letsencrypt integration
Name: nethserver-letsencrypt
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name} 

BuildRequires: nethserver-devtools >= 1.1.0-5

AutoReq: no
Requires: nethserver-base, nethserver-httpd
Requires: letsencrypt.sh


%description
NethServer Let's Encrypt integration

%prep
%setup

%build
%{makedocs}

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

%changelog
