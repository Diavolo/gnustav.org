Title: Redirección HTTP a HTTPS en NGINX
Date: 2016-09-28 19:23
Category: Security
Tags: FreeBSD, NGINX, TLS, SSL
Slug: redireccion-http-a-https-en-nginx
Authors: Diavolo
Summary: Luego de habilitar HTTPS en FreeBSD con NGINX, es momento de realizar la redirección permanente (301) para que aquellos que ingresen a nuestro sitio web via HTTP sean redirigidos a nuestra nueva dirección con HTTPS.

Luego de habilitar [HTTPS en FreeBSD con NGINX][1], es momento de realizar la redirección permanente (301) para que aquellos que ingresen a nuestro sitio web via HTTP sean redirigidos a nuestra nueva dirección con HTTPS.

En FreeBSD, editamos el fichero `/usr/local/etc/nginx/nginx.conf`.

        server {
            listen 80;
            server_name gahd.net;
            return 301 https://$server_name$request_uri;
            ...
        }
        server {
            listen 443 ssl;
            server_name gahd.net;
    
            ...
        }

Y luego reiniciamos nuestro servidor NGINX:

    [root@freebsd:~]# service nginx restart

**Fuentes:**  
1. [Server Fault](http://serverfault.com/a/337893)

[1]: https://gnustav.org/security/certificado-ssl-tls-en-freebsd-y-nginx-con-lets-encrypt.html