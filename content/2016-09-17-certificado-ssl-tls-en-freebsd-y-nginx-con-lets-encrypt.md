Title: Certificado SSL/TLS en FreeBSD y NGINX con Let’s Encrypt
Date: 2016-09-17 17:29
Category: security
Tags: FreeBSD, NGINX, SSL, TLS
Slug: certificado-ssl-tls-en-freebsd-y-nginx-con-lets-encrypt
Authors: Diavolo
Summary: HTTPS (Hypertext Transfer Protocol Secure) es un protocolo para la comunicación segura a través de la transferencia de hipertexto (HTTP) dentro de una conexión cifrada por Transfer Layer Security (TLS) o su predecesor, Secure Sockets Layer (SSL).


[HTTPS][1] (Hypertext Transfer Protocol Secure) es un protocolo para la comunicación segura a través de la transferencia de hipertexto (HTTP) dentro de una conexión cifrada por Transfer Layer Security (TLS) o su predecesor, Secure Sockets Layer (SSL).

Es utilizado por entidades financieras, tiendas online y cualquier aplicación web que requiera el envío de información sensible y evitar que ésta pueda ser interceptada y usada por algún atacante mediante técnicas como MiM u otros.

Existen entidades que emiten estos certificados digitales por un determinado precio, pero también hay proyectos como Let’s Encrypt que otorgan certificados gratuitos.

En éste artículo se intentará detallar los pasos a seguir para configurar los certificados de Let’s Encrypt en un servidor FreeBSD con NGINX. El porqué decidir uno u otro certificador no está dentro del alcance de este artículo.

## Let’s Encrypt
[Let’s Encrypt][2] es una autoridad de certificación (CA) gratuita, automatizada y abierta que ofrece certificaciones digitales HTTPS(SSL/TLS) para beneficio público con la finalidad de hacer de nuestras webs más seguras y respetuosas con la privacidad. Es un servicio proporcionado por el [Internet Security Research Group (ISRG)][3].

<figure><img src="/media/2016/09/letsencrypt-logo.png" alt="letsencrypt-logo" />
<figcaption>Figura 1: Logo Let’s Encrypt.</figcaption></figure>

La configuración de certificados SSL en FreeBSD + NGINX con [Let’s Encrypt][5] en muy sencillo, solo hay que seguir las [indicaciones][4] de la web de Let’s Encrypt y luego realizar [algunas configuraciones][6] en nuestro fichero de NGINX para que todo quede listo.

## Instalar un cliente de Let’s Encrypt en FreeBSD
Para obtener un certificado digital emitido por Let’s Encrypt en un sistema operativo FreeBSD debemos de instalar, en caso de no tenerlo, el paquete o port de *Certboot*.

Mediante Port:

    [root@freebsd:~]# cd /usr/ports/security/py-certbot && make install clean

Mediante Paquete:

    [root@freebsd:~]# pkg install py27-certbot

## Obtener un certificado digital de Let’s Encrypt en FreeBSD
Luego de instalar *py27-certbot* en FreeBSD, procedemos a ejecutar el comando `certbot certonly`.

    [root@freebsd:~]# certbot certonly

Luego de ejecutar `certbot certonly`, los pasos a seguir para conseguir un certificado de Let’s Encrypt en FreeBSD es muy intuitivo, solo basta seguir y rellenar/seleccionar los campos que van saliendo en los menus.

Seleccionamos el enlace para la autenticación en Let’s Encrypt.

<figure><img src="/media/2016/09/letsencrypt-auth.png" alt="letsencrypt-auth" />
<figcaption>Figura 2: Let’s Encrypt – How would you link to authenticate with the ACME CA?</figcaption></figure>

Ingresamos los nombres de dominios seguidos por espacios o comas.

<figure><img src="/media/2016/09/letsencrypt-enter-domain.png" alt="letsencrypt-enter-domain" />
<figcaption>Figura 3: Let’s Encrypt – Enter your domain name(s).</figcaption></figure>

Seleccionamos el webroot para nuestro dominio.

<figure><img src="/media/2016/09/letsencrypt-webroot-for-domain.png" alt="letsencrypt-webroot-for-domain" />
<figcaption>Figura 4: Let’s Encrypt – Select the webroot for domain.</figcaption></figure>

Ingresamos la ruta donde se ubican los ficheros que son servidos por NGINX para nuestro dominio.

<figure><img src="/media/2016/09/letsencrypt-webroot-for-domain2.png" alt="letsencrypt-webroot-for-domain2" />
<figcaption>Figura 5: Let’s Encrypt – Input the webroot for domain.</figcaption></figure>

Luego de confirmar la información ingresada obtendremos un mensaje donde se nos indicará que nuestro certificado digital ha sido generado asi como la ruta donde se encuentra.

<figure><img src="/media/2016/09/letsencrypt-successful.png" alt="letsencrypt-successful" />
<figcaption>Figura 6: Let’s Encrypt – Mensaje confirmando la generación de nuestro certificado digital.</figcaption></figure>

    IMPORTANT NOTES:
     - Congratulations! Your certificate and chain have been saved at
       /usr/local/etc/letsencrypt/live/gnustav.org/fullchain.pem. Your
       cert will expire on 2016-12-16. To obtain a new or tweaked version
       of this certificate in the future, simply run certbot again. To
       non-interactively renew *all* of your certificates, run "certbot
       renew"
     - If you like Certbot, please consider supporting our work by:
    
       Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
       Donating to EFF:                    https://eff.org/donate-le

## Configurar SSL/TLS en nuestro servidor web NGINX
Editamos el fichero de configuración de NGINX `/usr/local/etc/nginx/nginx.conf`

        server {
            server_name  gnustav.org;
            ...
    
            listen 443 ssl;
    
            ssl_certificate /usr/local/etc/letsencrypt/live/gnustav.org/fullchain.pem;
            ssl_certificate_key /usr/local/etc/letsencrypt/live/gnustav.org/privkey.pem;
    
            ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
            ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA";
            ssl_prefer_server_ciphers on;
            ssl_ecdh_curve secp384r1;
    
            ssl_session_cache shared:SSL:10m;
            ssl_session_timeout 10m;
            ssl_session_tickets off;
    
            add_header Strict-Transport-Security "max-age=31536000";
            add_header X-Frame-Options SAMEORIGIN;
            add_header X-Content-Type-Options nosniff;
    
            ...

Y por último reiniciamos nuestro servidor web NGINX en FreeBSD, para que coja los cambios realizados en el fichero `nginx.conf`, con el siguiente comando:

    [root@freebsd:~]# service nginx restart

Finalmente, abrimos nuestro browser y cargamos nuestra web para ver que ahora ya tenemos HTTPS habilitado.

<figure><img src="/media/2016/09/gnustav.org-https.png" alt="gnustav.org-https" />
<figcaption>Figura 7: gnustav.org con HTTPS activado.</figcaption></figure>

## Conclusión
Como se ha visto en este artículo, la generación de un certificado digital SSL/TLS con Let’s Encrypt y posterior configuración en FreeBSD con NGINX es sencillo, solo es cuestión de seguir 3 pasos principales:

1. Instalar un cliente Let’s Encrypt
2. Generar el certificado digital con Let’s Encrypt
3. Editar nuestro fichero `nginx.conf` y reiniciar nuestro servidor web NGINX para que lean los cambios y de esta manera pueda servir páginas con HTTPS activado

**Fuentes**  
1. [Wikipedia : HTTPS][1]  
2. [Let’s Encrypt: Getting Started][5]  
3. [Certbot: Nginx on FreeBSD][4]  
4. [Nicolas Vion: Installation of LetsEncrypt with Nginx on FreeBSD][6]

[1]: https://en.wikipedia.org/wiki/HTTPS "HTTPS"
[2]: https://letsencrypt.org/ "Let’s Encrypt"
[3]: https://letsencrypt.org/isrg/ "ISRG"
[4]: https://certbot.eff.org/#freebsd-nginx
[5]: https://letsencrypt.org/getting-started/
[6]: https://nicolas.vion.science/systems-unix-freebsd-letsencrypt-ssl-ca-nginx/installation-of-letsencrypt-with-nginx-on-freebsd.html