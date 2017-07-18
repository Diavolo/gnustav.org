Title: ReText en Slackware Linux
Date: 2017-07-17 21:30
Category: tools
Tags: Slackware, Markdown, editor
Slug: retext-editor-slackware-linux
Authors: Diavolo
Summary: Instalación de ReText editor en Slackware Linux

Conozco pocos, y usado menos, editores para Markdown...

Desde hace algunos días, estuve en la búsqueda de editores Markdown para poder usarlos en mi Slackware, haciendo una búsqueda rápida en los [Slackbuilds][1] solo encontré [uno][2] que no terminó de gustarme, ante tal situación no quedó otra que preparar unos scripts para instalar un editor decente para Markdown, ReText.

## ReText
ReText es un editor simple pero potente para los lenguajes de Markdown y reStructuredText, está escrito en Python y funciona en GNU/Linux y otras plataformas compatibles con POSIX.

El siguiente artículo describe los pasos para instalar el editor ReText en Slackware Linux.

### Dependencias
Para instalar [ReText][3] se requiere los siguientes paquetes:

- Python -- 3.2 o superior
- PyQt5
- Python Markups -- 2.0 o superior
- Python Markdown

De estos, solo [Python 3][4] y [PyQt5][5] están disponibles en Slackbuilds.org, existe un script para Markdown pero se tuvo que [adaptar el script existente][6] para que pueda soportar Python3; para el paquete de [Python Markups][7] se tuvo que crear un nuevo script. Y también un nuevo script para el propio [ReText][3].

### Instalación de Python 3 en Slackware Linux

    [diavolo@mikasa:SBo]$ wget https://slackbuilds.org/slackbuilds/14.2/python/python3.tar.gz
    [diavolo@mikasa:SBo]$ tar -xvf python3.tar.gz
    [diavolo@mikasa:SBo]$ cd python3
    [diavolo@mikasa:python3]$ source python3.info
    [diavolo@mikasa:python3]$ wget $DOWNLOAD
    [root@mikasa:python3]$ ./python3.SlackBuild
    [root@mikasa:python3]$ installpkg /tmp/python3-3.6.1-x86_64-1_SBo.tgz

### Instalación de PyQt5 con soporte para Python3

    [diavolo@mikasa:SBo]$ wget https://slackbuilds.org/slackbuilds/14.2/libraries/python3-PyQt5.tar.gz
    [diavolo@mikasa:SBo]$ tar -xvf python3-PyQt5.tar.gz
    [diavolo@mikasa:SBo]$ cd python3-PyQt5
    [diavolo@mikasa:python3-PyQt5]$ source python3-PyQt5.info
    [diavolo@mikasa:python3-PyQt5]$ wget $DOWNLOAD
    [root@mikasa:python3-PyQt5]$ ./python3-PyQt5.SlackBuild
    [root@mikasa:python3-PyQt5]$ installpkg /tmp/python3-PyQt5-5.6-x86_64-1_SBo.tgz

Nota: Realizar las mismas acciones para las dependencias del paquete.

### Instalación de Python Markdown con soporte para Python3
Descargar todos los ficheros de `https://gitlab.com/Diavolo/slackbuilds/tree/master/Markdown` y continuar con la ejecución del script.

    [diavolo@mikasa:Markdown]$ source Markdown.info
    [diavolo@mikasa:Markdown]$ wget $DOWNLOAD
    [root@mikasa:Markdown]$ ./Markdown.SlackBuild
    [root@mikasa:Markdown]$ installpkg /tmp/Markdown-2.6.8-x86_64-1_gahd.tgz

### Instalación de Python Markups
Descargar todos los ficheros de `https://gitlab.com/Diavolo/slackbuilds/tree/master/Markups` y continuar con la ejecución del script.

    [diavolo@mikasa:Markups]$ source Markups.info
    [diavolo@mikasa:Markups]$ wget $DOWNLOAD
    [root@mikasa:Markups]$ ./Markups.SlackBuild
    [root@mikasa:Markups]$ installpkg /tmp/Markups-2.0.1-x86_64-1_gahd.tgz

### Instalación de ReText en Slackware Linux
Finalmente cuando ya se tenga todas las dependencias instaladas, se procede a la instalación de ReText en Slackware Linux.

Descargar todos los ficheros de `https://gitlab.com/Diavolo/slackbuilds/tree/master/ReText` y continuar con la ejecución del script.

    [diavolo@mikasa:ReText]$ source ReText.info
    [diavolo@mikasa:ReText]$ wget $DOWNLOAD
    [root@mikasa:ReText]$ ./ReText.SlackBuild
    [root@mikasa:ReText]$ installpkg /tmp/ReText-7.0.1-x86_64-1_gahd.tgz

<figure><img src="/media/2017/07/retext.png" alt="Retext en Slackware Linux" />
<figcaption>Figura 1: ReText en Slackware Linux.</figcaption></figure>

[1]: https://slackbuilds.org/result/?search=markdown&sv=14.2 "Search Results for "markdown""
[2]: http://www.inkcode.net/qute "Qute is a text editor with Markdown and TeX support"
[3]: https://gitlab.com/Diavolo/slackbuilds/tree/master/ReText "Slackbuild para ReText"
[4]: https://slackbuilds.org/repository/14.2/python/python3/ "Python3 en SBo"
[5]: https://slackbuilds.org/repository/14.2/libraries/python3-PyQt5/ "PyQt5 en SBo"
[6]: https://gitlab.com/Diavolo/slackbuilds/tree/master/Markdown "Slackbuild para Markdown con soporte para Python3"
[7]: https://gitlab.com/Diavolo/slackbuilds/tree/master/Markups "Slackbuild para Markups"