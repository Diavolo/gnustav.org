Title: Yaourt curl error: Couldn't connect to server
Date: 2014-09-07 22:44
Modified: 2014-09-10 22:50
Category: operating system
Tags: ArchLinux, Yaourt
Slug: yaourt-curl-error-couldnt-connect-to-server
Authors: Diavolo
Summary: Yaourt curl error: Couldn't connect to server

El error sale luego de querer instalar algun paquete que se encuentre en AUR

    :::bash
    $ yaourt strife
    curl error: Couldn't connect to server

Lo solucionamos haciendo ping a http://aur.archlinux.org 

    :::bash
    $ ping aur.archlinux.org
    PING aur.archlinux.org (5.9.250.164) 56(84) bytes of data.
    64 bytes from aur.archlinux.org (5.9.250.164): icmp_seq=1 ttl=250 time=231 ms
    64 bytes from aur.archlinux.org (5.9.250.164): icmp_seq=2 ttl=250 time=216 ms
    ^C
    --- aur.archlinux.org ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1001ms
    rtt min/avg/max/mdev = 216.805/224.032/231.260/7.242 ms

añadimos la dirección 5.9.250.164 a nuestro fichero /etc/hosts

    :::bash
    $ echo "5.9.250.164     aur.archlinux.org" >> /etc/hosts

Y eso es todo, ya podemos seguir usando AUR :D

Fuente: [Unix & Linux Stack Exchange](http://unix.stackexchange.com/questions/109371/yaourt-curl-error-couldnt-connect-to-server "Unix & Linux Stack Exchange")