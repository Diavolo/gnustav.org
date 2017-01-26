Title: Crear sitios web estáticos con Python (Pelican + Isso)
Date: 2014-10-19 22:34
Modified: 2016-12-08 10:30
Category: tools
Tags: pelican, Python
Slug: crear-sitios-web-estaticos-con-python-pelican-isso
Authors: Diavolo
Summary: Goodbye Wordpress, Hello Pelican

Cuando empecé en el mundo blogueril, no tenía ni idea sobre que era un CMS, sólo quería escribir o hacer C&P, pues poco me importaba, en aquellos tiempos, desde donde publicar. Desde aquel entonces he probado uno que otro software para crear y mantener un blog: [LifeType][1], Blogger, Wordpress, MovableType, Drupal y Ghost. 

De todos estos CMS, LyfeType y Wordpress fueron con los que use por más tiempo.

Inicialmente, cuando aún no tenía un dominio propio, use el servicio para blogs que ofrecían CJB.NET, luego LifeType en los servidores de PeruBlog.NET y posteriormente me aventuré a usar Wordpress, primero usando uno de los tantos subdominios y hosting gratis que existían por aquellos tiempos y luego sobre un servidor compartido y dominio propio.

En mi temporada con LifeType (PeruBlog.NET) sólo me encargaba de hacer C&P a todo lo que veía en la blogósfera y con algo de suerte lograba adaptar alguna plantilla de Wordpress al formato de LifeType.

Luego, como todo niño que crece, tuve que dejar el hogar para recorrer nuevos senderos, fue así como me hice con un servidor compartido y levanté un Wordpress; tampoco es que sea la gran cosa, pero... en fin. Tenía un Wordpress autohospedado por el cual gastaba algo de pasta cada cierto tiempo. Hasta aquí todo bien con Wordpress, el tema era con el servidor compartido que tenía, en el último año (2013) tenía pensado hacerme con un VPS por lo que renovar el servidor donde tenía el blog con Wordpress no tenía sentido alguno. Llegó el mes de renovar (febrero 2014) y solo hice un backup de los posts que tenia allí, para marzo ya no tenía blog y tampoco tenía el VPS que había planeado tener para esa fecha, entre el nuevo trabajo y mi mudanza a Lima no tuve el tiempo ni el dinero para el VPS y tampoco el ánimo suficiente para renovar el servidor compartido, así que el blog entro en modo offline.

Según lo planeado tendría que dejar Wordpress por un generador de blog estático o construir un blog desde cero, cualquiera de ellos iría sobre el VPS que planeaba tener, pero no fue así hasta que en agosto (2014) y en vista que el VPS aún no llegaría, decidí probar un generador de blog estático. De la lista de software que encontré en [StaticGen][2], para hacer esta tarea, tenía lo siguientre:

- Jekyll (Ruby)
- Pelican (Python)
- Hakyll (Haskell)

De estas tres opciones, Jekyll era del que había escuchado más pero como amo Python elegí Pelican para mi blog, aunque tengo planeado usar Hakyll para mi pagina personal y Jekyll para subir los archivos que tengo de la época de PeruBlog.NET y WordPress.

Bien, como ya tenía a Pelican para el blog era hora de levantar anclas e izar las velas. Aquí la receta:

## Pelican + GitHub Pages + Isso
Esto es una pseudo-mini-guía de como tener un blog con Pelican alojarlo en GitHub Pages y gestionar los comentarios con [Isso][3].

### ¿Qué es Pelican?

> Pelican es un generador de sitios estáticos, escrito en Python, que no requiere una base de datos[...]

Pues eso, no es un CMS como Wordpress sino un *parser* que convierte un fichero correctamente escrito (en uno de los formatos admitidos p.e [Markdown][4]) a un archivo HTML.

Alguna de las características que incluye:

- Escribir contenido en los formatos reStructuredText, Markdown o AsciiDoc
- Archivos estáticos y fáciles de almacenar en cualquier lugar (p.e GitHub Pages)
- Personalizar la plantilla usando el formato [Jinja][5]
- Publicar contenido en múltiples lenguajes
- Feeds Atom/RSS
- Resaltado de código
- Importar desde WordPress, Dotclear, RSS y otros servicios a Pelican
- Un sistema modular de plugins y su correspondiente repositorio.

### ¿Cómo funciona?
Pelican funciona así: lo instalas en tu ordenador, generas una estructura de directorios y ficheros mediante el comando respectivo, guardas tus ficheros *Markdown* dentro del directorio de contenidos y ejecutas Pelican para que convierta los ficheros *Markdown* a archivos HTML

### Ingredientes
Inicialmente estuve probando Pelican con Python 2 pero he actualizado para usarlo con Python 3, aquí los ingredientes para generar y mantener un blog estático con Pelican y alojarlo en GitHub Pages:

- ArchLinux, Slackware, FreeBSD (o el OS de tu preferencia)
- Emacs (si prefieres un editor gráfico con previsualización de markdown, puedes usar [CuteMarkEd][6])
- Python 3.5.*
- Pelican 3.6.3
- [python-virtualenv][7]
- git
- [ghp-import][8]
- Markdown

Antes de empezar con la instalación de Pelican se deberá de instalar el paquete `python-virtualenv` para poder crear nuestro entorno virtual y `python-pip` para instalar Pelican:

Para distribuciones basadas en Arch Linux ya no es necesario instalar Python 3.*, esta ya viene instalada por default, para instalar virtualenv utilizaremos `pacman`

    :::bash
    # pacman -S python-virtualenv

En Slackware si tenemos que instalar Python 3 y virtualenv vía SlackBuilds

    :::bash
    $ cd ~/Slackware
    $ wget https://slackbuilds.org/slackbuilds/14.2/python/python3.tar.gz
    $ tar -xvzf python3.tar.gz
    $ cd python3
    $ wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz
    # ./python3.SlackBuild
    ...
    # installpkg /tmp/python3-3.5.2-i486-1_SBo.tgz
    $ cd ~/Slackware
    $ wget https://slackbuilds.org/slackbuilds/14.2/python/virtualenv.tar.gz
    $ tar -xvzf virtualenv.tar.gz
    $ cd virtualenv
    $ wget https://pypi.python.org/packages/8b/2c/c0d3e47709d0458816167002e1aa3d64d03bdeb2a9d57c5bd18448fd24cd/virtualenv-15.0.3.tar.gz
    # ./virtualenv.SlackBuild
    ...
    # installpkg /tmp/virtualenv-13.1.2-i486-1_SBo.tgz

Asi mismo en FreeBSD instalamos Python 3 y virtualenv via `pkg`

    :::csh
    # pkg install python35
    # pkg install python27-virtualenv

Crear un repositorio en GitHub y clonar dentro del directorio `~/Projects`

    :::bash
    $ mkdir ~/Projects && cd ~/Projects
    $ git clone git@github.com:Diavolo/gnustav.org.git
    $ cd ~/Projects/gnustav.org

Con esto tendremos y estaremos dentro del directorio `~/Projects/gnustav.org` en donde estará el blog.

Al crear el entorno virtual se debe de tener en cuenta que la ruta donde se encuentra instalado Python 3 en FreeBSD no es la misma que en las distribuciones GNU/Linux.

    :::bash
    $ virtualenv -p /usr/bin/python3
    Using base prefix '/usr'
    New python executable in env/bin/python3
    Also creating executable in env/bin/python
    Installing setuptools, pip, wheel...done.


Y activar el entorno virtual

    :::bash
    $ source env/bin/activate


### Instalación de Pelican
Luego de crear y activar el entorno virtual se procederá a instalar, usando `pip`, Pelican, Markdown, typogrify y ghp-import:

    :::bash
    (env)$ pip install pelican
    (env)$ pip install markdown
    (env)$ pip install typogrify
    (env)$ pip install ghp-import

Al momento de instalar Pelican se instalaran automáticamente una serie de dependencias que no viene al caso mencionarlas aquí.

### Generación de la Estructura de nuestro sitio web con `pelican-quickstart`

Una vez que Pelican se encuentre instalado, ejecutamos el comando `pelican-quickstart` y al momento que solicite la ruta donde generar el árbol de directorios ingresaremos un punto (`.`) para que se genere dentro del directorio donde nos encontramos (`~/Projects/gnustav.org`), para el resto de opciones podemos seleccionar un valor específico o presionar enter si queremos mantener los parametros por defecto

    :::bash
    (env)$ pelican-quickstart 
    Welcome to pelican-quickstart v3.6.3.
    
    This script will help you create a new Pelican-based website.
    
    Please answer the following questions so this script can generate the files needed by Pelican.
    
    
    > Where do you want to create your new web site? [.] 
    > What will be the title of this web site? Diavolo
    > Who will be the author of this web site? Diavolo
    > What will be the default language of this web site? [en] es
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) 
    > What is your URL prefix? (see above example; no trailing slash) http://diavolo.me
    > Do you want to enable article pagination? (Y/n) 
    > How many articles per page do you want? [10] 
    > What is your time zone? [Europe/Paris] America/Lima
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) 
    > Do you want to upload your website using FTP? (y/N) 
    > Do you want to upload your website using SSH? (y/N) 
    > Do you want to upload your website using Dropbox? (y/N) 
    > Do you want to upload your website using S3? (y/N) 
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) 
    > Do you want to upload your website using GitHub Pages? (y/N) 
    Done. Your new project is available at /home/diavolo/Projects/diavolo.me



Terminado la configuración tendremos un árbol con el siguiente aspecto:

    :::bash
    gnustav.org
    ├── content/
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── output/
    ├── pelicanconf.py
    └── publishconf.py

En el directorio `content/` estarán los ficheros *Markdown* y en el directorio `output` estarán todos los archvos HTML que generá Pelican y el cual subiremos a GitHub Pages. Los ficheros *.py y *.sh contienen información de la configuración que se hizo a Pelican al momento de crear la estructura de directorios. Si adicionalmente se desea tocar algo a la configuración como cambiar la forma de los enlaces permanentes de las entradas, enlaces para los feeds, cambiar la plantilla, etc se tendrá que editar los ficheros `pelicanconf.py`y/o `publishconf.py`.

### `pelicanconf.py` y `publishconf.py`
Generalmente la mayoría que configuración se hallará en `pelicanconf.py` y que podrá ser visualizado cuando se ejecute pelican en modo local. La configuración de `publishconf.py` (tal como la ruta del feed entre otros) será aplicada cuando queramos generar código HTML para subir al servidor.

El codigo HTML generado con la configuración del fichero `pelicanconf.py` puede ser subido a producción y el sitio funcionará sin problema, el detalle es que los URL son enlaces relativos mientras que el código generado con la configuración del fichero `publishconf.py` generará enlaces absolutos motivo por el cual se recomienda subir este último a producción.

### Escribiendo Contenido

Como comenté al inicio, Pelican acepta diferentes formatos para las entradas, en mi caso uso *Markdown*. Cada fichero *Markdown* es una entrada y tiene el siguiente formato:

    :::markdown
    Title: I'm back... again!
    Date: 2014-08-28 00:53
    Category: me
    Tags: pelican, python
    Slug: i-am-back
    Authors: Diavolo
    Summary: I'm back... again!
    
    I'm back... again!

Lo guardas dentro del directorio `content/` y ¡ya está! ahora solo queda ejecutar Pelican para que genere los archivos HTML

### Generación de tu sitio web con Pelican
La manera por default para generar HTML es usando el comando `pelican`:

    pelican /path/to/your/content/ [-s path/to/your/settings.py]

y luego ver el codigo HTML levantando un simple servidor web en Python

    (env)$ cd output
    (env)$ python -m http.server

**Nota:** En Python 2 utilizar `SimpleHTTPServer` en lugar de `http.server`.

### Generación de tu sitio web con Pelican de manera automatizada
Sin embargo, la generación de codigo HTML con el comando `pelican`, descrito lineas arriba, puede ser mejorado y automatizado siempre y cuando se haya seleccionado que sí se desea generar ficheros para la automatización de generación y publicación en pelican al momento de generar la estructurta de nuestro sitio con `pelican-quickstart`

    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 

En este caso utilizaremos `make`:

    (env)$ make clean
    (env)$ make html
    (env)$ make serve

`make clean` limpia el directorio `outpout`.

`make html` genera el HTML aplicando la configuración del fichero `pelicanconf.py` (si se desea generar código HTML para producción usando configuración del fichero `publishconf.py` usar `make publish`).

`make serve` levanta un servidor en modo local para poder previsualizar el sitio generado en nuestro ordenador.

Si se desea que Pelican automáticamente regenere el sitio (aplicando configuración del fichero `pelicanconf.py`) cada vez que detecte cambios se puede usar `make regenerate`.

`make devserver` permite en un solo comando regenerar el sitio (`make regenerate`) y levantar un servidor local (`make serve`).

Si todo ha estado bien instalado, se observará que Pelican genera el sitio y nos dará una URL donde se podrá ver el sitio generado  http://localhost:8000 y eso es todo, cada vez que se escriba un post generas el HTML y levantas el servidor.


### Subir el blog generado por Pelican a GitHub Pages
Para subir unicamente los archivos HTML que generó Pelican en el directorio `output` dentro del branch `gh-pages` de GitHub se usará `ghp-import`.

    :::bash
    (env)$ make clean
    (env)$ pelican content -s publishconf.py
    (env)$ ghp-import output
    (env)$ git push origin gh-pages

¡Y walá! el blog generado con Pelican ya se encuentra publicado en GitHub Pages.

Luego de esto, se sube los archivos fuente al branch principal, `master`:

    ::::bash
    (env)$ git add .
    (env)$ git commit -m "I'm back... again!"
    (env)$ git push origin master

### Comentarios con Isso
[Isso][3] es un sistema para gestionar comentarios similar a Disqus pero Software Libre escrito en Python y que usa SQLite como base de datos. Tiene la opción de importar comentarios de WordPress y Disqus.

Desafortunadamente, <del>al no tener un servidor donde instalar Isso</del> esta parte quedará pendiente. <del>Mientras tanto (y aunque ya nadie comente en estos tiempos) se usará Disqus (aunque no tengamos el control total) con la esperanza de importar los comentarios de los 3 gatos a Isso en un futuro cercano.</del>

[1]: http://lifetype.net "LifeType"
[2]: http://staticgen.com "StaticGen"
[3]: http://posativ.org/isso "a commenting server similar to Disqus"
[4]: http://daringfireball.net/projects/markdown "Daring Fireball: Markdown"
[5]: http://jinja.pocoo.org "Jinja2 (The Python Template Engine)"
[6]: https://github.com/cloose/CuteMarkEd "Qt Markdown Editor with live HTML preview"
[7]: https://www.archlinux.org/packages/extra/any/python-virtualenv/ "virtualenv"
[8]: https://github.com/davisp/ghp-import "ghp-import"
