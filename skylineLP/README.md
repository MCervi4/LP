# SKYLINE BOT

_En aquest projecte desarrollarem un chatbot de Telegram per a manimular Skylines._

## Introducció 🚀

Volem crear un chatbot de Telegram en el qual poguem crear Skylines i modificar-los com volguem.
El llenguatge que utilitzarem sera Python i també utilitzarem una gràmatica per a ANTLR4 per a tractar els compiladors.


### Pre-requisits 📋

Per a poder executar el bot, primer fa falta instalar el següent: (cas linux)

-ANTLR4+python3-pip
```
> sudo apt install antlr4
> pip3 install antlr4-python3-runtime
> sudo apt install python3-pip
```

-Llibreria matplotlib
```
> sudo apt-get install python3-matplotlib
```

-Llibreria pickle
```
> sudo apt-get install python3-pickle
```

-Llibreria python-telegram-bot
```
> pip3 install python-telegram-bot
```

### Compilació i execució 🔧

Per compilar i executar el bot utilitzem

```
> python3 bot.py
```

_A continuació obrim el bot a telegram a traves del link: http://t.me/Skyline4_bot i ja podrem parlar amb ell_

### Funcionament del codi ⌨️

_A continuació explicare com es desenvolupa el codi._

Nosaltres comencem executant el programa bot.py, aquest importa la API de Telegram i es comunica a temps real amb l'aplicació.
Quan l'usuari escriu un missatge o una comanda el bot reaccionarà, concretament ens portarà a la funció que hem disenyat i volem executar.
Segons la comanda que s'utilitzi utilitzarem diferents funcions i si l'usuari hi entra text l'avaluarem amb el nostre intèrpret.

Tenim les seguents comandes:
    /start 
    /help 
    /author
    /lst
    /clean
    /save id
    /load id
Per tal de saber que fa cada una tenim la comanda /help, que ens les mostrarà totes i ens donara una breu explicació.

El que escrigui l'usuari cridarà a tota la part de compilació:
En primer lloc, utilitzarem la funcio comprova_mis, aquesta comprovara el que ha escrit el missatge utilitzant tota la compilació, més concretament,
analitzarem l'arbre a traves del visitor. A partir de tota la gramàtica disenyada a Skyline.g i tots els fitxers creats utilitzant la comanda d'antlr4
cridarem a les funcions que ens fagin falta de la classe Skyline, implementada en skyline.py. Aquesta classe serà la que portara el skyline a través
de diferents funcions implementades.


###### skyline.py

Un objecte d'aquesta classe representara un skyline. Els atributs de la classe serán la alçada i area del skyline i, per últim,
una llista de tuples on cada element de la llista (una tupla) representarà un edifici amb caracteristiques (xmin, alçada, xmax)
Aquesta classe tindrà les següents funcions:

_geters i seters:_
-getArea()
-getAlcada()
-getEdificis()
-setArea(area)
-setAlcada(alcada)
-setEdificis(edificis)

_creadors:_
//crea un edifici simple
-crear_simple(xmin, alcada, xmax)

//crea edificis compostos
-crear_compost(ll_edificis)

//crea n edificis aleatoris
-crear_aleatori(n, h, w, xmin, xmax)
-crear_1_aleatori(h, w, xmin, xmax)

//controla que xmax>xmin i que alcada>=0
-control(alcada, xmin, xmax)

_calculadors_
//calcula i actualitza la area de tot el skyline.
-calcula_area()

//calcula i actualitza la alcada total del skyline
-calcula_alcada()

_construccio plot_
//dibuix d'un edifici
-plot_edifici(xmin, alcada, xmax)

//dibuix de tot el skyline
-plot_general()

_operacions_
//desplacament a la dreta del skyline desp posicions
-desplacament_dreta(desp)

//desplacament a la esquerra del skyline desp posicions
-desplacament_esquerra(desp)

//skyline reflectit
-reflexio()

//replicacio mult vegades del skyline
-replicacio(mult)

_funcions auxiliars_
//calcula la x mes petita del skyline
-x_minima()

//calcula la x mes gran del skyline
-x_maxima()

###### SkylineVisitor.py

En aquest fitxer recorrem l'arbre que explora els nodes de la gramàtica. En aquesta classe, li arriba el missatge que ha escrit l'usuari,
depenent del que hagi escrit (pot ser una expressió, una assignació o creacions) passarem per uns nodes o per uns altres.
El que fa es mirar quants paràmetres ha escrit l'usuari, és a dir, mira quants nodes fills té el missatge i recorre l'arbre per tal d'arribar a la funció
que executi el que volia l'usuari.

###### test.py

Aquest fitxer conecta el bot amb el visitor. Agafa el missatge enviat per l'usuari i l'interpreta creant un visitor.

###### bot.py

Aquest el programa que s'executa i té tota la informació a través de Telegram.
Té definides unes funcions que es cridaran quan l'usuari escrigui un missatge o una comanda específica.

###### Skyline.g

En aquest document hem dissenyat la gramàtica que utilitzarem en els missatges que envia l'usuari.
Utilitzarem assignacions, expressions, les quals poden tenir altres expressions i creadors.

### Autors 📄


**Marc Cervilla Rovira**




