Title: Renovación Automática de Certificados SSL/TLS en FreeBSD y NGINX con Let's Encrypt y Certbot
Date: 2016-12-15 22:21
Category: security
Tags: FreeBSD, NGINX, SSL, TLS
Slug: renovacion-de-certificado-ssl-tls-en-freebsd-y-nginx-con-lets-encrypt
Authors: Diavolo
Summary: Una vez que se obtiene un certificado SSL/TLS de Let’s Encrypt, tocará renovarlo cada 90 días. En este artículo se detallará como relizar dicha renovación.

Una vez que se obtiene un [certificado SSL/TLS de Let's Encrypt](https://gnustav.org/security/certificado-ssl-tls-en-freebsd-y-nginx-con-lets-encrypt.html "Certificado SSL/TLS en FreeBSD y NGINX con Let’s Encrypt"), tocará renovarlo cada [90 días][1], entre las muchas opciones que existen para realizar esta renovación usaremos la renovación de certificados mediante Certbot.

## Renovar certificado Let's Encrypt en FreeBSD y NGINX via Certbot
[La renovación de un certificado Let's Encrypt con Certbot][2] es mucho mas sencilla que el proceso de generación. Solo bastará con ejecutar el comando de actualización `certbot renew` (opcional y previamente se puede ejecutar el comando de simulación `certbot renew --dry-run` para ver, en el caso de tener varios sitios, que certificados serán renovados).

    [root@freebsd:~]# certbot renew
    
    -------------------------------------------------------------------------------
    Processing /usr/local/etc/letsencrypt/renewal/gnustav.org.conf
    -------------------------------------------------------------------------------
    
    -------------------------------------------------------------------------------
    new certificate deployed without reload, fullchain is
    /usr/local/etc/letsencrypt/live/gnustav.org/fullchain.pem
    -------------------------------------------------------------------------------
    
    -------------------------------------------------------------------------------
    Processing /usr/local/etc/letsencrypt/renewal/gahd.net.conf
    -------------------------------------------------------------------------------
    
    -------------------------------------------------------------------------------
    new certificate deployed without reload, fullchain is
    /usr/local/etc/letsencrypt/live/gahd.net/fullchain.pem
    -------------------------------------------------------------------------------
    
    -------------------------------------------------------------------------------
    Processing /usr/local/etc/letsencrypt/renewal/wiki.gahd.net.conf
    -------------------------------------------------------------------------------
    
    The following certs are not due for renewal yet:
      /usr/local/etc/letsencrypt/live/wiki.gahd.net/fullchain.pem (skipped)
    Congratulations, all renewals succeeded. The following certs have been renewed:
      /usr/local/etc/letsencrypt/live/gnustav.org/fullchain.pem (success)
      /usr/local/etc/letsencrypt/live/gahd.net/fullchain.pem (success)
    
Y reiniciar nuestro servidor NGINX

    [root@freebsd:~]# service nginx restart

<figure><img src="/media/2016/12/certificate-viewer.png" alt="certificate-viewer" />
<figcaption>Figura 1: Vista del certificado (vía Mozilla Firefox) antes de la renovación</figcaption></figure>


<figure><img src="/media/2016/12/certificate-viewer-renewed.png" alt="certificate-viewer-renewed" />
<figcaption>Figura 2: Vista del certificado (vía Mozilla Firefox) después de la renovación</figcaption></figure>

## Renovación automática de certificados Let's Encrypt en FreeBSD y NGINX via Certbot y crontab
Renovar un certificado Let's Encrypt cada 90 días es una tarea manual que puede ser automatizada creando un crontab.

Para esto crearemos un shell script (renew-letsencrypt.sh) que contenga el comando de renovación que será ejecutado cada cierto tiempo por el daemon cron.

    #!/bin/sh
    certbot renew --pre-hook "service nginx stop" --post-hook "service nginx start"

Este script detendrá NGINX, renovará los certificados y reiniciará NGINX solo si existen certificados por renovar.

Y creamos su respectivo crontab para, [según las recomendaciones][3], ejecutarlo 2 veces al día


    # .---------------- minute (0 - 59) 
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ... 
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)  OR sun,mon,tue,wed,thu,fri,sat 
    # |  |  |  |  |
    # *  *  *  *  *  command to be executed
    30  11  *  *  *  /home/diavolo/renew-letsencrypt.sh
    30  23  *  *  *  /home/diavolo/renew-letsencrypt.sh

## Conclusiones
La renovación de certificados Let's Encrypt en un servidor FreeBSD y NGINX mediante Certbot resulta ser un proceso relativamente sencillo, solo basta ejecutar el respectivo comando de renovación `certbot renew` y reiniciar NGINX 
`service nginx restart`.

En el caso de realizar las renovaciones de certificados de manera automática con un cron, tocará crear un shell script y generar su respectivo crontab para que se ejecute periódicamente.

**Fuentes:**

1. [Let's Encrypt: Why ninety-day lifetimes for certificates?][1]
2. [Certbot: Renewing certificates][2]
3. [Certbot: NGINX on FreeBSD][1]
4. [FreeBSD Man Pages: crontab(5)][4]

[1]: https://letsencrypt.org/2015/11/09/why-90-days.html
[2]: https://certbot.eff.org/docs/using.html#renewal
[3]: https://certbot.eff.org/#freebsd-nginx
[4]: https://www.freebsd.org/cgi/man.cgi?query=crontab&sektion=5&apropos=0&manpath=FreeBSD+10.3-RELEASE+and+Ports