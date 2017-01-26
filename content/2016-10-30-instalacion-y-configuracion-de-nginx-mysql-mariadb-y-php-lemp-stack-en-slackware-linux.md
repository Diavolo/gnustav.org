Title: Instalación y configuración de NGINX, MySQL/MariaDB y PHP (LEMP stack) en Slackware Linux
Date: 2016-10-30 13:40
Category: Operating System
Tags: LEMP, MariaDB, MySQL, NGINX, PHP, Slackware
Slug: instalacion-y-configuracion-de-nginx-mysql-mariadb-y-php-lemp-stack-en-slackware-linux
Authors: Diavolo
Summary: Configuración del Stack LEMP en Slackware Linux.

<figure><img src="/media/2016/10/lemp.png" alt="LEMP" />
<figcaption>Figura 1: LEMP Stack.</figcaption></figure>

Ahora que he vuelto a usar WordPress, me vi en la necesidad de instalar y configurar un stack LEMP para tener un ambiente de desarrollo para ir jugando con algunas cosas de WP y PHP antes de subirlas al servidor.

Una instalación completa de Slackware Linux trae consigo varios paquetes útiles que estan, algunos, listos o casi listos para ser usados. Alguno de los muchos paquetes que incluye Slackware son:

- MariaDB
- PHP

Asi que, para cumplir el propósito de este artículo, solo quedaría instalar:

- NGINX

Si por algún motivo no se tuviera instalado MariaDB y PHP ya sea por no haber realizado una “Instalación Completa (Recomendada)” u otra razón, se procederá a instalar estos paquetes desde el repositorio oficial de Slackware con los siguientes comandos:

    [root@slackware:~]# slackpkg install php
    [root@slackware:~]# slackpkg install mariadb

Si bien es cierto que en una instalación completa de Slackware se tiene por defecto a Apache webserver, si se desea usar otro servidor web como NGINX se tendría que acudir a los slackbuilds o algun otro repositorio de usuarios ya que NGINX no se encuentra en los repositorios oficiales de Slackware.

## Instalar NGINX en Slackware via slackbuild
Al momento de redactar este post, la actual versión de NGINX es la versión nginx-1.10.2, sin embargo el SlackBuild que se encuentra en [slackbuilds.org][1] está preparado para la versión nginx-1.8.0. Hasta aqui se puede tomar dos caminos para tener NGINX en Slackware, instalar la versión que está en el slackbuild o hacer algunas modificaciones a este script para instalar la última versión de NGINX.

Para instalar NGINX con la versión que se encuentra en el slackbuild se deberá de descargar el slackbuild y el código fuente de NGINX.

Descargar el slackbuild

    [diavolo@slackware:~]$ wget https://slackbuilds.org/slackbuilds/14.2/network/nginx.tar.gz

Descomprimir el slackbuild descargado

    [diavolo@slackware:~]$ tar -xvzf nginx.tar.gz

Luego, ingresar al directorio del slackbuild y descargar el código fuente de NGINX

    [diavolo@slackware:~]$ cd nginx
    [diavolo@slackware:nginx]$ wget http://nginx.org/download/nginx-1.8.0.tar.gz

Ejecutar el slackbuild

    [root@slackware:nginx]$ ./nginx.SlackBuild

Una vez que el script haya terminado de ejecutarse, instalar el paquete generado

    [root@slackware:nginx]# installpkg /tmp/nginx-1.8.0-i486-1_SBo.tgz
    Verifying package nginx-1.8.0-i486-1_SBo.tgz.
    Installing package nginx-1.8.0-i486-1_SBo.tgz:
    PACKAGE DESCRIPTION:
    # nginx (http/imap/pop3 proxy)
    #
    # Nginx [engine x] is a high-performance HTTP server and reverse proxy,
    # as well as an IMAP/POP3 proxy server.
    #
    # Nginx was written by Igor Sysoev.
    #
    # Homepage: http://nginx.net/
    #
    Executing install script for nginx-1.8.0-i486-1_SBo.tgz.
    Package nginx-1.8.0-i486-1_SBo.tgz installed.

## Configuración de PHP en Slackware
Para [versiones de PHP inferiores a php-5.3.9][2] editar el fichero /etc/php.ini para que quede de la siguiente manera.

    ...
    cgi.fix_pathinfo=0
    ...

Y reiniciar PHP para coger los cambios.

    [root@slackware:nginx]# /etc/rc.d/rc.php-fpm restart

## Configuración de NGINX en Slackware
[Editar][3] el [fichero][4] `/etc/nginx/nginx.conf`

    ...
            location / {
                root   /var/www/html;
                index  index.php index.html index.htm;
            }
    
    ...
    
            location ~ \.php$ {
            root /var/www/html;
            try_files $uri =404;
            fastcgi_split_path_info ^(.+\.php)(/.+)$;
            fastcgi_pass    127.0.0.1:9000;
            fastcgi_index   index.php;
            #fastcgi_param   SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_param  SCRIPT_FILENAME $request_filename;
            include         fastcgi_params;
            }
    ...

Y reinicar el daemon de NGINX.

    [root@slackware:nginx]# /etc/rc.d/rc.nginx restart

## Configuración de MariaDB en Slackware
Instalar la base de datos del [sistema][5].

    [root@slackware:~]# mysql_install_db

Otorgar los permisos al usuario mysql

    [root@slackware:~]# chown -R mysql.mysql /var/lib/mysql

Asignar una clave al usuario root de MariaDB

    [root@slackware:~]# mysqladmin -u root password 'NUEVO_PASSWORD'

Otorgar permisos para ejecutar el daemon de MariaDB

    [root@slackware:~]# chmod 755 /etc/rc.d/rc.mysqld

Iniciar el daemon de MariaDB

    [root@slackware:~]# /etc/rc.d/rc.mysqld start

**Fuentes:**  
1. [Server Fault: Is the PHP option ‘cgi.fix_pathinfo’ really dangerous with Nginx + PHP-FPM?][2]  
2. [ArchWiki: nginx][3]  
3. [LinuxQuestions][4]  
4. [SlackDocs: Install MariaDB On Slackware][5]


[1]: https://slackbuilds.org/repository/14.2/network/nginx/
[2]: http://serverfault.com/a/701500
[3]: https://wiki.archlinux.org/index.php/Nginx#Error:_.22File_not_found.22_in_browser_or_.22Primary_script_unknown.22_in_log_file
[4]: http://www.linuxquestions.org/questions/slackware-14/slack14-1-nginx-works-but-no-php-4175503648/
[5]: http://docs.slackware.com/howtos:databases:install_mariadb_on_slackware