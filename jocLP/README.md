# 4 EN RATLLA

_En aquest projecte desarrollarem un programa en llenguatge de programació Haskell basat en el popular joc 4 en ratlla._

## Introducció 🚀

Bàsicament, l'objectiu del programa és molt bàsic, guanyar a la màquina jugant al 4 en ratlla. Per tant, el nostre objectiu és l'objectiu del joc, aconseguir 4 fitxes consecutives.
Hi haura diferents tipus de màquina, ja que aquesta tindrà diferents estrategies per "lluitar" contra tu, aquestes les veurem més endevant.


### Pre-requisits 📋

Per a poder executar el programa, primer fa falta instalar el següent: (cas linux)

-Llibreria random
```
> sudo apt install cabal-install
> cabal update
> cabal install random
```

-Compilador ghc
```
> sudo apt install ghc
```

Una llibreria que ve per defecte i he utilitzat és la llibreria Data.List.
Tota funció i codi està implementada per mi, però hi ha un cas en el programa que la funció _transposar_ no funciona, en concret quan la matriu té un tamany de fila diferent per cada fila.
Per tant, únicament en aquest cas, he utilitzat la funció transpose de la llibreria.


### Compilació i execució 🔧

Per compilar i executar el programa simplement hem de fer el que feiem servir a laboratori utilitzant el compilador de ghc:

```
> ghc joc.hs
```

_A continuació:_

```
> ./joc
```

### Funcionament del codi ⌨️

_A continuació entrare en detall de com es desenvolupa el codi i les funcions que aquest utilitza._

Abans de que el programa comenci, he creat un tipus anomenat Tauler que utilitzaré molt i serà sinònim a una llista de chars [[Char]]

El programa comença en el main.

main :: IO ()

D'ara en endevant, totes les funcions que retornin un valor en una monada IO utilitzaré la nomenclatura do i return, ja que em permet empaquetar, desempaquetar i utilitzar funcions d'entrada sortida de manera sencilla.

En primer lloc, ens demanara que inserim el nombre de files n i columnes m. També ens mostrará per pantalla unes petites instruccions a tenir en compte per jugar.
A continuació, inicialitzarem el tauler de tamany n*m i el mostrarem per pantalla.

Un cop creat el tauler, ens pregunta quina estrategia volem utilitzar per a la màquina.
Aquestes estrategies són unes funcions que més tard utilitzarem com a funcions d'ordre superior i tenim les següents:

_Els hi passem un tauler com a paràmetre i ens retorna un IO Int de la columna on vol tirar_

-Estrategia random:
    Es basa en elegir una columna random entre 1 i el nombre de columnes. Si la columna escollida a l'atzar està plena, elegirem la següent columna fins a trobar una on poguem tirar. (Si arriva al final de la taula torna a començar per la 1a)

-Estrategia greedy:
    Es basa en, primer de tot, mirar si l'oponent pot acabar, si es així, retorna la columna en la que l'oponent pot acabar per intentar no deixarlo acabar, sinò, evalua tots els taulers virtuals de cada tirada a una columna diferent,  d'aquests taulers virtuals mira a quin d'ells tindrà el major numero de fitxes consecutives i retorna la primera columna que crea un d'aquells taulers amb el màxim de fitxes consecutives.
    Més detalladament, creo un vector on cada posició i representa una tirada a la columna i, en aquella posició es troba el nombre màxim de fitxes consecutives que hi haurà si es tira en aquella columna. D'aquests valors elegim els màxims i tirem a la primera posició on hi hagi un màxim. Com feiem anteriorment, mirem que la columna no estigui plena.
    
-Estrategia smart:
    Aquesta última fa el mateix que l'estrategia greedy, però amb una millora.
    L'estrategia greedy crea el vector amb el màxim nombre de fitxes consecutives que hi haurà si tirem a una posició. En canvi aquest és algo més intel·ligent i, en comptes d'agafar només el nombre de fitxes consecutives que hi haura, fa una ponderació d'un valor que actua com una puntuació. Aquesta puntuació es basa en el màxim nombre de fitxes consecutives al cuadrat i també li sumem les màximes fitxes consecutives de cada possible linea (files, columnes i diagonals) per aixi augmentar la probabilitat de fer 4 en ratlla per diferents mètodes.



El següent pas és començar a jugar en aquell tauler amb aquella estrategia.
Tenim una funció anomenada jugar que s'encarrega del següent:
Si la taula està plena, declara l'empat i finalitza la partida.
Si no, va alternant entre jugador 1 i jugador 2(la màquina) i executant les tirades adients. Per a cada tirada mostra el tauler i avisa de qui és el que ha de tirar. Si en aquella tirada s'aconsegueix un 4 en ratlla es proclama el guanyador.

###### Funcions

_A continuació mostro les funcions que he utilitzat no mencionades anteriorment i algun petit aclariment si fa falta._

_Només agafo les funcions principals!! Hi ha funcions que s'utilitzen en una funció per a fer el problema més petit, aquestes tenen el mateix nom de la funció i algo afegit, però només explicaré les principals._

_funcions auxiliars:_

randInt :: Int -> Int -> IO Int
    Li passes 2 valors (low, high) i et retorna un nombre aleatori entre ells.

inicialitza_tauler :: Int -> Int -> Tauler
    Li passes el tamany del tauler que vols crear n i m i et retorna el tauler n*m inicialitzat amb tot '0'.

transposar :: Tauler -> Tauler
    Li passes una matriu(tauler) i et retorna la matriu transposada, és a dir, canvia les files per les columnes.

mostra_tauler :: Tauler -> [Char]
    Li passes el tauler que vols mostrar i et retorna el string per poder-lo mostrar.
Per mostrar-lo ho faig de la següent manera: putStrLn (mostra_tauler tauler)

busca_col :: Tauler -> Int -> [Char]
    Li passes el tauler i el numero de la columna que vols i et retorna aquella columna.

_IMPORTANT: aquest tipus de funcions es poden utilitzar tant per files com per columnes depenent si li passes la transposada o la normal._

columna_seguent :: Tauler -> Int -> Int
    Li passes un tauler i el numero d'una columna i et retorna la següent columna que no estigui plena.
Si arriva al final del tauler, torna a mirar desde l'inici.

max_ratlla_tauler :: Tauler -> Char -> Int
    Li passes un tauler i el caracter que defineix el jugador i et retorna el màxim nombre de fitxes consecutives d'aquell jugador en el tauler, tant per files, columnes o diagonals. Aquesta funció utilitza 2 subfuncions per a convertir el problema en subproblemes més petits. Utilitzada per a l'estrategia greedy.

max_ratlla_tauler2 :: Tauler -> Char -> Int
    Mateixa explicació que l'anterior funció. Utilitzada per a l'estrategia smart.

llista_max :: [Int] -> Int -> Int -> [Int] -> [Int]
    Li passes una llista i un valor i et retorna les posicions d'aquell valor en la llista. També li has de passar un contador i una llista auxiliar que normalment seran 0 i [], respectivament.


_funcio per posar fitxa:_

posar_fitxa_tau :: Tauler -> Int -> Int -> Char -> Tauler -> Tauler
    Li passes un tauler, una posicio a la que vols tirar, un contador, la fitxa que vols tirar, un tauler auxiliar i et retornara el tauler amb la fitxa tirada. Per tal de fer-ho per columnes (cas del 4enratlla) se li ha de passar la transposada del tauler.

_funcions per compovar final de la partida_

taula_plena :: Tauler -> Bool
    Li passes un tauler i et retorna True si esta ple i False si no.

comprovar_files :: Tauler -> Char -> Bool
    Li passes un tauler i un caràcter que representa al jugador i et retorna si aquell jugador té 4 fitxes consecutives en les files del tauler.

comprovar_diagonals :: Tauler -> Char -> Bool
    Li passes un tauler i un caràcter que representa un jugador i et retorna si aquell jugador té 4 fitxes consecutives en les diagonals del tauler. Per tal de fer això, utilitzo 2 subfuncions: una que em converteix el tauler en unes diagonals i una que m'afegeix espais amb un guio(-) (afegeix més espais com més valor té el número de fila) per tal d'aconseguir una matriu on les files representen les diagonals.

guanyador :: Tauler -> Char -> Bool
    Li passes un tauler i un caràcter que represent un jugador i et retorna, a partir de les funcions anteriors, si el jugador ha guanyat fent 4enratlla.


### Autors 📄


**Marc Cervilla Rovira**




