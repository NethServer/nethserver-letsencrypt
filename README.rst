======================
nethserver-letsencrypt
======================

This package requests and automatically renews Let's Encrypt (LE) certificates.
It adds httpd ACME-related configuration for all defined virtual hosts.

The main helper ``/usr/libexec/nethserver/letsencrypt-certs`` can be executed also from command line.

For more info, see: ::

  /usr/libexec/nethserver/letsencrypt-certs -h 


Database properties under ``pki`` key inside ``configuration`` database:

- ``LetsEncryptRenewDays``: days to the expiration, the certificate will be renewd when the condition is met
- ``LetsEncryptMail``: (optional) registration mail for LE notifications
- ``LetsEncryptDomains``: comma-separated list of domains added to certificate SAN field

DNS challenge
=============

To use the DNS challenge, follow these steps:

- install the required certbot plugin plugin using yum; to see the list of available package use ``yum search certbot-dns``
- configure all required properties accordingly to plugin documentation
- execute ``/usr/libexec/nethserver/letsencrypt-certs`` using the ``-c`` flag to specify the plugin

See the list of available plugin here: https://certbot.eff.org/docs/using.html?highlight=dns#dns-plugins

When using the dns challenge, make sure to set extra properties accordingly to certbot configuration.
All properties for the dns challenge should be in the form ``LetsEncrypt_<certbot_option>``, where
``<certbot_option>``` is the option specific to certbot DNS plugin.

Digitial Ocean example
----------------------

1. Install the plugin: ``yum install python2-certbot-dns-digitalocean``
2. Configure requires props accordingly to https://certbot-dns-digitalocean.readthedocs.io/en/stable/: ::

   config setprop pki LetsEncrypt_dns_digitalocean_token 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
3. Request the certificate for domain ``myserver.nethserver.org``: ::
 
   /usr/libexec/nethserver/letsencrypt-certs -v -c dns-digitalocean -d myserver.nethserver.org