Title: Netbeans JDK is missing
Date: 2014-09-03 22:06
Modified: 2014-11-15 12:31
Category: tools
Tags: Java, JDK, ArchLinux, NetBeans, IDE
Slug: netbeans-jdk-is-missing
Authors: Diavolo
Summary: Netbeans JDK is missing

El error es el siguiente:

> The JDK is missing and is required to run some Netbeans modules
> Please use the --jdkhome command line option to especify a JDK
> instalation or see http://wiki.netbeans.org/FaqRunningOnJre for
> more information.

Lo solucionamos editando el fichero /usr/share/netbeans/etc/netbeans.conf

Descomentamos la linea netbeans_jdkhome y le asignamos el JDK que queramos usar por defecto con el IDE.

    :::bash
    netbeans_jdkhome="/usr/lib/jvm/java-default-runtime"

##Elegir/Ver el entorno Java predeterminado##
Ingresamos el comando `archlinux-java status` para ver cuál es el JDK predeterminado y las demás versiones de JDK que tenemos instalado en nuestro ordenador

    :::bash
    $ archlinux-java status
    Available Java environments:
    
    java-8-jdk
    java-8-openjdk (default)

Si se desea cambiar de JDK prederminado lo hacemos mediante `archlinux-java set`

    :::bash
    # archlinux-java set java-8-jdk

