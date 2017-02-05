Title: Instalación y configuración de Node.js en Slackware Linux
Date: 2017-02-04 13:13
Category: tools
Tags: Slackware, Node.js
Slug: instalacion-y-configuracion-de-nodejs-en-slackware-linux
Authors: Diavolo
Summary: Ahora que estoy jugando con algunas cosas de JavaScript en el trabajo, quise probar algo de aquello en casa, para eso, primero tenía que instalar nodejs en blackwidow. Este post describe el proceso de instalación y configuración de Node.js en Slackware Linux.


Ahora que estoy jugando con algunas cosas de JavaScript en el trabajo, quise probar algo de aquello en casa, para eso, primero tenía que instalar nodejs en blackwidow. Este post describe el proceso de instalación y configuración de Node.js en Slackware Linux.

## Instalación de NodeJS en Slackware Linux
A la fecha de escribir este post, las versiones disponibles para descarga en la web de [Node.js][1] son las versiones 6.9.5 LTS y 7.5.0 Currrent. A diferencia de esto, la versión que está disponible en la web de [SlackBuilds][2] es una versión desfasada (6.9.4).

<figure><img src="/media/2017/02/nodejs-lts-schedule.png" alt="Node.js LTS schedule" />
<figcaption>Figura 1: Node.js Long Term Support Release Schedule.</figcaption></figure>

Por motivos de soporte y actualizaciones de seguridad, se escogerá la versión LTS. Se procederá a descargar el SlackBuild y adaptar para usarla con la actual versión LTS de Node.js.

    [diavolo@blackwidow:SBo]$ wget https://slackbuilds.org/slackbuilds/14.2/development/nodejs.tar.gz
    [diavolo@blackwidow:gnustav.org]$ tar -xvzf nodejs.tar.gz
    [diavolo@blackwidow:gnustav.org]$ cd nodejs

Luego de descargar, descomprimir e ingresar en el directorio del SlackBuild editar los ficheros `nodejs.info` y `nodejs.SlackBuild` y reemplazar las versiones, url de descarga y 
el código de verificación `MD5SUM` por los datos de la versión LTS actual.

Después de que se haya adaptado el SlackBuild, ejecutar el fichero `nodejs.SlackBuild` para que se genere el paquete de instalación.

    [root@blackwidow:nodejs]# ./nodejs.SlackBuild

E instalar el paquete generado.

    [root@blackwidow:nodejs]# installpkg /tmp/nodejs-6.9.5-i586-1_SBo.tgz
    [diavolo@blackwidow:~]$ node --version
    v6.9.5
    [diavolo@blackwidow:~]$ npm --version
    3.10.10

Hasta este punto, ya se tiene Node.js y npm instalado en Slackware Linux.

## Configuración de Node.js en Slackware Linux
El detalle es que sin ninguna configuración adicional los módulos que se deseen instalar de manera global serán instalados en el directorio por *default* de `npm`: `/usr/local/lib/node_modules`.

Esto significa que cada vez que se desee instalar un módulo de forma global, utilizando `npm`, en Slackware Linux, se requerirá permisos de administrador.

Para "[corregir][3]" esto, se puede realizar de dos diferentes maneras:

1. Cambiar los permisos del directorio por *default* de `npm`.
2. Cambiar el directorio por *default* de `npm` a otro directorio.

### Cambiar permisos del directorio por *default*
Ubicar el directorio por *default* de `npm` mediante el comando `npm config get prefix`.

    [diavolo@blackwidow:~]$ npm config get prefix
    /usr/local/lib/node_modules

Y cambiar el propietario de los directorios al usuario actual.

    [root@blackwidow:~]#  sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}

Esto cambia el permisos de los subdirectorios usados por `npm` y otras herramientas (`lib/node_modules`, `bin`, y `share`).

### Cambiar el directorio por *default* de `npm` a otro directorio

Para configurar y cambiar la ruta del directorio donde se instalan los módulos globales, vía npm, existen 3 maneras de realizarlo:

1. Manualmente, utilizando la opción `--prefix` seguido de la ruta donde se desea instalar (p.e. `npm install -g nombrePaquete --prefix ~/.node_modules`).
2. Usando el entorno de variable `npm_config_prefix`.
3. Usando el fichero de configuración de usuario `~/.npmrc`.

El primer método no es recomendado debido a que se deberá de recordar el directorio de ubicación cada vez que se desee instalar un nuevo módulo global.

Para el segundo método, simplemente se deberá de añadir las siguientes líneas en el fichero de configuración de la shell que se esté utilizando (p.e `~/.bash_profile` para bash).

    PATH="$HOME/.node_modules/bin:$PATH"
    export npm_config_prefix=~/.node_modules

Para el tercer método, utilizar el comando `npm config edit`.

    [diavolo@blackwidow:gnustav]$ npm config edit

Ubicar la opción `prefix`, descomentar y asignar la ruta que se desee utiliar para la instalación de paquetes globales. Adicionalmente se usará un directorio personalizado para almacenar la caché de npm utilizando la opción `cache`.

    ;;;;
    ; npm userconfig file
    ; this is a simple ini-formatted file
    ; lines that start with semi-colons are comments.
    ; read `npm help config` for help on the various options
    ;;;;
    
    ...
        
    ;;;;
    ; all options with default values
    ;;;;
    
    ....
    
    ; cafile=undefined
    cache=/opt/.npm
    ; cache-lock-stale=60000
    
    ....
    
    ; parseable=false
    prefix=/opt/node_modules
    ; production=false
    
    ...

Y añadir al *path* la ubicación de los ejecutables de los paquetes globales (p.e `~/.bash_profile` para bash).

    export PATH="/opt/node_modules/bin:$PATH"

Por último, para actualizar las variables de entorno, ejecutar `source` seguido del fichero de configuración de usuario de la shell que se esté utilizando.

    [diavolo@blackwidow:~]$ source .bashrc

Con esto la instalación de paquetes globales se realizará en un directorio diferente al que viene por defecto.

## Conclusión
Por defecto, el comando `npm` para la instalación de paquetes globales en GNU/Linux los instala en el directorio `/usr/lib/node_modules` lo que requiere permisos de administrador.

Para evitar el tener que usar `su` o `sudo`, cada vez que se requiera instalar un paquete global, se puede utilizar el fichero de configuración de usuario `~/.npmrc` (o alguno de los otro métodos descritos); utilizar `npm config edit` y descomentar la línea donde se encuentre la opción `prefix` asignando la ruta donde almacenar los paquetes globales; añadir al *path* la nueva ruta de ejecutables que se asigno a `prefix`; y actualizar las variables de sistema utilizando `source` seguido del fichero de configuración de usuario de la shell que se encuentre utilizando.

## Fuentes
- [Node.js][1]
- [SlackBuilds.org - Node.js][2]
- [npm Documentation: Fixing npm permissions][3]
- [ArchWiki: Node.js][4]

[1]: https://nodejs.org/ "Node.js"
[2]: https://slackbuilds.org/repository/14.2/development/nodejs/ "SlackBuilds.org - nodejs"
[3]: https://docs.npmjs.com/getting-started/fixing-npm-permissions "Fixing npm permissions"
[4]: https://wiki.archlinux.org/index.php/Node.js "Node.js - ArchWiki"

