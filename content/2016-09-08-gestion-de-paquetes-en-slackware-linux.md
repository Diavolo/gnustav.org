Title: Gestión de Paquetes en Slackware Linux
Date: 2016-09-08 22:34
Category: operating system
Tags: Slackware, GNU/Linux
Slug: gestion-de-paquetes-en-slackware-linux
Authors: Diavolo
Summary: Gestión de paquetes en Slackware Linux

La gestión de paquetes es una parte esencial de toda distribución GNU/Linux. A diferencia de algunas distribuciones populares que manejan sus propias extensiones para distribuir sus paquetes, como los .deb o .rpm, Slackware utiliza el viejo y conocido tarball [.tgz y .txz][1] como formato estándar para sus paquetes.

Estos tarballs son archivos tar.gz/tar.xz que contienen binarios construidos para Slackware, archivos de ayuda, un archivo de descripción y scripts de instalación. A pesar de que se pueden descomprimir y desempaquetar como un archivo normal, son (en general) sólo paquetes binarios destinados a ser instalados a través de las herramientas de gestión de paquetes de Slackware.

La información sobre un paquete se almacena en dos maneras, en el nombre de archivo del paquete y un archivo de descripción dentro de ese paquete.

A continuación vamos a ver algunas herramientas utilizadas para la manipulación y [gestión de paquetes en Slackware][2].

## pkgtool
La forma más sencilla de realizar tareas de mantenimiento de paquetes en Slackware es invocar a la herramienta *pkgtool*.

*pkgtool* es una herramienta para el mantenimiento de paquetes en Slackware que permite instalar o eliminar paquetes, así como ver el contenido de los paquetes y la lista de paquetes instalados actualmente en una interfaz basado en ncurses que es fácil de usar.

    [root@blackwidow ~]# pkgtool

<figure><img src="/media/2016/09/slackware-pkgtool.png "Slackware pkgtool" alt="pkgtool" />
<figcaption>Figura 1: pkgtool y su interfaz basada en ncurses.</figcaption></figure>

*pkgtool* es una vía fácil y conveniente para realizar tareas básicas, pero para tareas más avanzadas es necesario otras herramientas más versátiles.

## Instalar, Remover y Actualizar paquetes en Slackware
### installpkg

    [root@blackwidow ~]# installpkg /tmp/optipng-0.7.6-i486-1_SBo.tgz
    [root@blackwidow ~]# installpkg /mnt/cdrom/slackware/n/*.txz

Permite instalar rápidamente un solo paquete o todo un conjunto de lista de paquetes, *installpkg* toma una lista de los paquetes a instalar, y simplemente lo instala sin mostrar algún mensaje de confirmación. De manera más simple, *installpkg* simplemente toma una lista de los paquetes a instalar, y hace exactamente lo que cabría esperar.

    [root@blackwidow ~]# installpkg /tmp/optipng-0.7.6-i486-1_SBo.tgz 
    Verifying package optipng-0.7.6-i486-1_SBo.tgz.
    Installing package optipng-0.7.6-i486-1_SBo.tgz:
    PACKAGE DESCRIPTION:
    # OptiPNG (Advanced PNG Optimizer)
    #
    # OptiPNG is a PNG optimizer that recompresses image files to a
    # smaller size, without losing any information. This program also
    # converts external formats (BMP, GIF, PNM and TIFF) to optimized
    # PNG, and performs PNG integrity checks and corrections.
    #
    # Homepage: http://optipng.sourceforge.net/
    #
    Package optipng-0.7.6-i486-1_SBo.tgz installed.

### removepkg

    [root@blackwidow ~]# removepkg /tmp/optipng-0.7.6-i486-1_SBo.tgz

De igual manera, la eliminación de un paquete es tan fácil como instalar uno. El comando para realizar esto es removepkg. A diferencia del comando para instalar paquetes *installpkg*, en donde se tiene que indicar la ruta donde se ubica el paquete, para remover paquetes con *removepkg* solo es necesario indicar el nombre del paquete. Por ejemplo, para remover el paquete *optipng-0.7.6-i486-1_SBo.tgz* se puede realizar de cualquiera de las siguientes maneras:

    [root@blackwidow ~]# removepkg optipng-0.7.6-i486-1_SBo.tgz 
    [root@blackwidow ~]# removepkg optipng-0.7.6-i486-1_SBo
    [root@blackwidow ~]# removepkg optipng.tgz 
    [root@blackwidow ~]# removepkg optipng

Y también indicando la ubicación del paquete generado

    [root@blackwidow ~]# removepkg /tmp/optipng-0.7.6-i486-1_SBo.tgz
    
    Removing package /var/log/packages/optipng-0.7.6-i486-1_SBo...
    Removing files:
      --> Deleting /usr/bin/optipng
      --> Deleting /usr/doc/optipng-0.7.6/AUTHORS.txt
      --> Deleting /usr/doc/optipng-0.7.6/LICENSE.txt
      --> Deleting /usr/doc/optipng-0.7.6/README.txt
      --> Deleting /usr/doc/optipng-0.7.6/history.txt
      --> Deleting /usr/doc/optipng-0.7.6/optipng.SlackBuild
      --> Deleting /usr/doc/optipng-0.7.6/optipng.man.html
      --> Deleting /usr/doc/optipng-0.7.6/optipng.man.pdf
      --> Deleting /usr/doc/optipng-0.7.6/optipng.man.txt
      --> Deleting /usr/doc/optipng-0.7.6/png_optimization.html
      --> Deleting /usr/doc/optipng-0.7.6/todo.txt
      --> Deleting /usr/man/man1/optipng.1.gz
      --> Deleting empty directory /usr/doc/optipng-0.7.6/

### upgradepkg

    [root@blackwidow ~]# upgradepkg /tmp/optipng-0.7.6-i486-1_SBo.tgz

Por último, la actualización de un paquete en Slackware se realiza con el comando *upgradepkg*. Una cosa importante a recordar es que *upgradepkg* no comprueba si el paquete previamente instalado tiene un número de versión más alto que el paquete “nuevo”, por lo que también se puede utilizar para cambiar a versiones anteriores.

## Actualizar a una nueva versión de Slackware
### slackpkg
Una vía común y sencilla para mantener al día nuestro Slackware, ya sea realizando actualizaciones de seguridad o actualizando a una nueva versión, es mediante el uso de la herramienta *slackpkg*.

*slackpkg* es una herramienta para la gestión automatizada de paquetes en Slackware. [Originalmente apareció en el directorio /extra de la versión Slackware 12.1][3], y posteriormente fue incluido como parte de la serie ap/ en la version Slackware 12.2.

Así como se usa *installpkg* para instalar paquetes del directorio `/extra` que se incluye en el medio de instalación o para aquellos que fueron previamente descargados a nuestro ordenador, podemos usar *slackpkg* para instalar paquetes, del servidor slackware.com o algun otro mirror, directamente desde internet.

#### Configuración de *slackpkg*
Para poder utilizar *slackpkg*, primeramente, debemos de escoger uno y solo un mirror de los que se encuentran disponibles en el fichero `/etc/slackpkg/mirrors`. Esto se realiza descomentando uno de los enlaces correspondientes al mirror que se desee utilizar.

    [root@blackwidow ~]# emacs -nw /etc/slackpkg/mirrors

Luego de haber escogido un mirror, el siguiente paso es actualizar las llaves GPG.

    [root@blackwidow ~]# slackpkg update gpg

#### Blacklisting (Lista Negra)
*slackpkg* tomará en consideración cualquier patrón de la lista negra `/etc/slackpkg/blacklist`. Por ejemplo los siguientes patrones harán que *slackpkg* haga caso omiso de cualquier paquete que se instaló desde SBo y desde el repositorio de alienBob:

    [0-9]+_SBo
    [0-9]+alien

#### Actualización completa de Slackware con *slackpkg*
Para poder actualizar completamente nuestro Slackware, ejecutamos los siguientes comandos:

    [root@blackwidow ~]# slackpkg update
    [root@blackwidow ~]# slackpkg install-new
    [root@blackwidow ~]# slackpkg upgrade-all
    [root@blackwidow ~]# slackpkg clean-system

Al ejecutar estos comandos, lo que *slackpkg* realizó fue: actualizar la lista de paquetes disponibles (*update*), instalar los nuevos paquetes encontrados (*install-new*), actualizar todos los paquetes instalados a una nueva versión (*upgrade-all*) y finalmente limpiar aquellos paquetes que se encuentren obsoletos (*clean-system*).

<figure><img src="/media/2016/09/slackpkg-upgrade-all.jpg" alt="slackpkg upgrade-all" />
<figcaption>Figura 2: Captura de pantalla luego de ejecutar <a href="https://identi.ca/diavolo/image/36N1s4pZSN-0E8i7oZ3bxQ">slackpkg upgrade-all</a>.</figcaption></figure>

**Nota:** Debido a que Slackware no ofrece una gran lista de paquetes, como lo hace el resto de distribuciones conocidas, de manera oficial, mucho de los paquetes instalados desde repositorios de usuarios, considerados como no-oficiales, pueden ser listados para su eliminación al ejecutar *clean-system* a menos que se indiquen en la lista negra para que *slackpkg* los ignore.

## Conclusión
Slackware no posee una cantidad enorme de paquetes en sus repositorios oficiales como los que ofrecen otras distribuciones (Debian, Arch Linux, etc), sin embargo existen repositorios no-oficiales ofrecidos por usuarios que contienen paquetes y scripts para la construcción de paquetes (conocidos como SlackBuilds) que pueden ser descargados, instalados y gestionados mediante las herramientas *installpkg*, *removepkg* y *upgradepkg*.

Para la gestión de paquetes del repositorio oficial y actualización del sistema se usa la herramienta *slackpkg*.

**Fuentes:**  
1. [SlackWiki: Packages][1]  
2. [SlackDocs: Package management][2]  
3. [SlackBook: Chapter 18 Slackware Package Management][3]  
4. man pages: installpkg(8), removepkg(8) y upgradepkg(8)

[1]: http://slackwiki.com/Packages "SlackWiki: Packages"
[2]: http://docs.slackware.com/slackbook:package_management ""
[3]: http://docs.slackware.com/slackbook:package_management#slackpkg "SlackBook: Chapter 18 Slackware Package Management"
[4]: https://identi.ca/diavolo/image/36N1s4pZSN-0E8i7oZ3bxQ ""