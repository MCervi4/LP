import System.Random
import Data.List

type Tauler = [[Char]]


-- FUNCIONS AUXILIARS 

randInt :: Int -> Int -> IO Int
-- randInt low high is an IO action that returns a
-- pseudo-random integer between low and high (both included).

randInt low high = do
    random <- randomIO :: IO Int
    let result = low + random `mod` (high - low + 1)
    return result

    
--crea el tauler n*m
inicialitza_tauler :: Int -> Int -> Tauler

inicialitza_tauler n m = map (const cols) [1..n]
    where cols = map (const '0') [1..m]
        
        
--li pases una matriu i et retorna la matriu transposada
transposar :: Tauler -> Tauler

transposar ([]:_) = []
transposar t = (map head t) : transposar (map tail t)
     
     
--per mostra el tauler passat per parametre
mostra_tauler :: Tauler -> [Char]

mostra_tauler [x] = show x
mostra_tauler (x:xs) = show x ++"\n"++ mostra_tauler xs


--li passes el numero de columa i et retorna la columna
--se li ha de passar taula per columnes(transp)

--tauler -> numero -> cont -> col
busca_col1 :: Tauler -> Int -> Int -> [Char]

busca_col1 [] _ _ = []
busca_col1 (x:xs) y cont
    | y == cont = x
    | otherwise = busca_col1 xs y (cont+1)
    
busca_col :: Tauler -> Int -> [Char]

{-busca_col tau y 
    | (y>(length $ head tau)) = [('e')]
    | otherwise = tau !! (y-1) 
    -}

busca_col tau y = busca_col1 tau y 1

--et retorna la columna seguent no plena
columna_seguent :: Tauler -> Int -> Int
 
columna_seguent tau x
    | (fila_plena (busca_col (transposar tau) x) ) && (x>(length $ head tau)) = columna_seguent tau 1
    | (fila_plena (busca_col (transposar tau) x) ) =  columna_seguent tau (x+1) 
    | otherwise = x

    
--li passes un tauler i un jugador i et diu el maxim de fitxes del jugador seguides

max_ratlla2 :: [Char] -> Char -> Int -> Int -> Int

max_ratlla2 [] _ _ maxcont = maxcont
max_ratlla2 (x:xs) fitxa cont maxcont
    | x == fitxa = max_ratlla2 xs fitxa (cont+1) (max (cont+1) maxcont)
    | otherwise = max_ratlla2 xs fitxa 0 maxcont
    
    
max_ratlla :: Tauler -> Char -> Int
    
max_ratlla [] _ = 0
max_ratlla (x:xs) fitxa = max ( max_ratlla2 x fitxa 0 0 ) ( max_ratlla xs fitxa )

max_ratlla_tauler :: Tauler -> Char -> Int

max_ratlla_tauler tau fitxa = maximum [ (max_ratlla tau fitxa),
                                            (max_ratlla (transposar tau) fitxa),
                                            (max_ratlla (transpose (convertir_tauler_diagonals tau [] 0)) fitxa),
                                            (max_ratlla (transpose (convertir_tauler_diagonals (reverse tau) [] 0)) fitxa ) ]
                                            
                                            
max_ratlla_tauler2 :: Tauler -> Char -> Int

max_ratlla_tauler2 tau fitxa = (maximum [ (max_ratlla tau fitxa),
                                            (max_ratlla (transposar tau) fitxa),
                                            (max_ratlla (transpose (convertir_tauler_diagonals tau [] 0)) fitxa),
                                            (max_ratlla (transpose (convertir_tauler_diagonals (reverse tau) [] 0)) fitxa ) ] )^2 +
                                                    (max_ratlla tau fitxa) +
                                                    (max_ratlla (transposar tau) fitxa) +
                                                    (max_ratlla (transpose (convertir_tauler_diagonals tau [] 0)) fitxa) +
                                                    (max_ratlla (transpose (convertir_tauler_diagonals (reverse tau) [] 0)) fitxa )


                                            
--li passes una llista i un valor i et retorna les posicions del valor en una llista                                  
llista_max :: [Int] -> Int -> Int -> [Int] -> [Int]

llista_max vec val cont llistaux 
    | cont >= (length vec) = reverse llistaux
    | val == (vec !! cont) = llista_max vec val (cont+1) ((cont+1):llistaux)
    | otherwise = llista_max vec val (cont+1) llistaux









--POSAR FITXES

--insertar fitxa a la columna :: columna -> fitxa -> columna auxiliar -> columna modificada
--afegeix fitxa a la primera casella vuida de la columna començant per abaix
--se li ha de passar el reverse de la columna!
posar_fitxa_col :: [Char] -> Char -> Bool -> [Char] -> [Char]

posar_fitxa_col [] _ _ colaux = colaux
posar_fitxa_col (x:xs) fitxa primer colaux
    | x == '0' && primer = posar_fitxa_col xs fitxa False (fitxa:colaux)
    | otherwise = posar_fitxa_col xs fitxa primer (x:colaux)

    
--intertar fitxa al tauler :: tauler -> posicio -> contador -> fitxa -> tauleraux -> tauler
--posicio entre 1 i m
--es llegeix per columnes! (transposada)
posar_fitxa_tau :: Tauler -> Int -> Int -> Char -> Tauler -> Tauler

posar_fitxa_tau [] _ _ _ tauleraux = reverse tauleraux
posar_fitxa_tau (x:xs) pos cont fitxa tauleraux
     | pos == cont = posar_fitxa_tau xs pos (cont+1) fitxa ((posar_fitxa_col (reverse x) fitxa True []):tauleraux)
     | otherwise = posar_fitxa_tau xs pos (cont+1) fitxa (x:tauleraux)
     
     
     
     
     
--COMPROVAR FINAL PARTIDA

--comprova si la fila o la columna esta plena : fila -> bool
--true si la fila esta plena
fila_plena :: [Char] -> Bool

fila_plena [] = True
fila_plena x = (all (/='0') x)

    
--comprova si el tauler esta ple : tauler -> bool
--true si el tauler esta ple
taula_plena :: Tauler -> Bool

taula_plena [] = True
taula_plena (x:xs) = (fila_plena x) && (taula_plena xs)


--comprova si hi ha 4 en ralla a les files amb un contador
--per comprovar columnes es lo mateix pero amb la matriu transposada
comprovar_files2 :: [Char] -> Char -> Int -> Bool

comprovar_files2 [] _ cont
    | cont == 4 = True
    | otherwise = False
comprovar_files2 (x:xs) fitxa cont
    | cont == 4 = True
    | x == fitxa = comprovar_files2 xs fitxa (cont+1)
    | otherwise = comprovar_files2 xs fitxa 0

comprovar_files :: Tauler -> Char -> Bool

comprovar_files [] _ = False
comprovar_files (x:xs) fitxa = ( comprovar_files2 x fitxa 0 ) || ( comprovar_files xs fitxa )



--comprova si hi ha 4 en ralla a les diagonals
afegir_espais :: [Char] -> Int -> [Char]

--afegeix el caracter '-' tants cops com cont
afegir_espais x cont
    | cont == 0 = x
    | otherwise = afegir_espais ('-':x) ( cont-1 )


convertir_tauler_diagonals :: Tauler -> Tauler -> Int -> Tauler

convertir_tauler_diagonals [] tauaux _ = reverse tauaux
convertir_tauler_diagonals (x:xs) tauaux cont = convertir_tauler_diagonals xs ( (afegir_espais x cont):tauaux ) (cont+1)

comprovar_diagonals :: Tauler -> Char -> Bool

comprovar_diagonals tau fitxa = comprovar_files (transpose (convertir_tauler_diagonals tau [] 0)) fitxa



--comprova si el jugador ha guanyat : tauler -> jugador -> bool
--true si el jugador ha guanyat



guanyador :: Tauler -> Char -> Bool
guanyador tau jug = ( comprovar_files tau jug ) ||  --comproves files
                    ( comprovar_files (transposar tau) jug ) ||    --comproves columnes
                    ( comprovar_diagonals tau jug ) ||  --comproves diagonals /
                    ( comprovar_diagonals (reverse tau) jug ) --comproves diagonals \



                    
                    

--ESTRATEGIES


--aquesta estrategia tria una columna al atzar on tirar
estrategia_random :: Tauler -> IO Int

estrategia_random tau = do
    let m = length $ head tau
    col <- randInt 1 m
    --Hem de comprovar que la columna random elegida no estigui plena, si esta plena elegirem la seguent columna no plena
    if (fila_plena $ busca_col (transposar tau) col ) then do
        let colaux = col+1
        let col = columna_seguent tau colaux
        return col
    else do return col
    


    
--part recursiva de l'estrategia greedy
--retorna el maxim de fitxes seguides de cada columna ficat a llista_col
--tauler -> m -> llista
greedy_rec :: Tauler -> Int -> [Int] -> [Int]

greedy_rec tau cont_col llista_col
    | cont_col < 0 = [-1]
    | cont_col == 0 = llista_col
    | otherwise = greedy_rec tau (cont_col-1) ( max_ratlla_tauler (posar_fitxa_tau (transposar tau) cont_col 1 '2' []) '2': llista_col)


--mira si afegint una fitxa pot guanyar
pot_guanyar :: Tauler -> Int -> Int

pot_guanyar tau cont_col
    | cont_col <= 0 = -1
    | (guanyador tau_virtual '1') = cont_col
    | otherwise = pot_guanyar tau (cont_col-1)
    where tau_virtual = (posar_fitxa_tau (transposar tau) cont_col 1 '1' [])


--aquesta estrategia tria la columna que mes s'acosti a la solucio
estrategia_greedy :: Tauler -> IO Int

estrategia_greedy tau = do
    let col_guanyadora = pot_guanyar tau (length $ head tau)
    if ( col_guanyadora /= (-1) ) then do
        return col_guanyadora
    else do
        let vec_col = greedy_rec tau (length $ head tau) []
        let valmax = maximum vec_col
        let col = head ( llista_max vec_col valmax 0 [] )
        --putStrLn $ show (vec_col)
        --Hem de comprovar que la columna random elegida no estigui plena, si esta plena elegirem la seguent columna no plena
        if (fila_plena $ busca_col (transposar tau) col ) then do
            let colaux = col+1
            let col = columna_seguent tau colaux
            return col
        else do return col

        
        
smart_rec :: Tauler -> Int -> [Int] -> [Int]

smart_rec tau cont_col llista_col
    | cont_col < 0 = [-1]
    | cont_col == 0 = llista_col
    | otherwise = smart_rec tau (cont_col-1) ( max_ratlla_tauler2 (posar_fitxa_tau (transposar tau) cont_col 1 '2' []) '2': llista_col)
    
    

estrategia_smart:: Tauler -> IO Int

estrategia_smart tau = do
    let col_guanyadora = pot_guanyar tau (length $ head tau)
    if ( col_guanyadora /= (-1) ) then do
        return col_guanyadora
    else do
        let vec_col = smart_rec tau (length $ head tau) []
        let valmax = maximum vec_col
        let col = head ( llista_max vec_col valmax 0 [] )
        --Hem de comprovar que la columna random elegida no estigui plena, si esta plena elegirem la seguent columna no plena
        if (fila_plena $ busca_col (transposar tau) col ) then do
            let colaux = col+1
            let col = columna_seguent tau colaux
            return col
        else do return col


--comences a jugar :: tauler -> jugador -> io
jugar :: Tauler -> (Tauler -> IO Int) -> Char -> IO ()

jugar tau estrategia jug = do
    --comprovar si el tauler esta ple
    if (taula_plena tau) then do
        putStrLn "El tauler esta ple\nHA SIGUT EMPAT ----- FI DE PARTIDA!"
        return ()
    else do
            
        --tirada jugador 1
        if (jug == '1') then do
            putStrLn "Ets el jugador 1, a quina columna vols tirar?"
            columna <- getLine
            let col = read columna :: Int
            --comprovar que tires be
            if ( col < 1 || col > (length $ head tau) || (fila_plena $ busca_col (transposar tau) col) ) then do
                putStrLn "ERROR, has tirat malament\n(has d'elegir un nombre entre 1 i el nombre de columnes d'una columna no plena)"
                return ()
            else do
                let tauler = transposar $ posar_fitxa_tau (transposar tau) col 1 '1' []
                putStrLn ""
                putStrLn (mostra_tauler tauler)
                putStrLn ""
                --comprovar guanyador 1
                if (guanyador tauler '1') then do
                        putStrLn "\n EL GUANYADOR ES EL JUGADOR 1!\n"
                        return ()
                else do jugar tauler estrategia '2'
            
        --tirada jugador 2
        else do
             putStrLn "Tira la maquina (jugador 2)"
             col <- estrategia tau
             let tauler = transposar $ posar_fitxa_tau (transposar tau) col 1 '2' []
             putStrLn ""
             putStrLn (mostra_tauler tauler)
             putStrLn ""
             --comprovar guanyador 2
             if (guanyador tauler '2') then do
                 putStrLn "\n EL GUANYADOR ES EL JUGADOR 2!\n"
                 return ()
             else do jugar tauler estrategia '1'
             --prova per si vols jugar com a jugador 2
  {-          putStrLn "Ets el jugador 2, a quina columna vols tirar?"
            columna <- getLine
            let col = read columna :: Int
            let tauler = transposar $ posar_fitxa_tau (transposar tau) col 1 '2' []
            putStrLn ""
            putStrLn (mostra_tauler tauler)
            putStrLn ""
            --comprovar guanyador 2
            if (guanyador tauler '2') then do
                    putStrLn "\n EL GUANYADOR ES EL JUGADOR 2!\n"
                    return ()
                    else do jugar tauler estrategia '1'-}

         
         
main :: IO ()
-- main program

main = do
    --entrada tamany del tauler
    putStrLn "Insereix nombre de files:"
    files <- getLine
    let n = read files :: Int
    putStrLn "Insereix nombre de columnes:"
    columnes <- getLine
    let m = read columnes :: Int
    putStrLn "\nINSTRUCCIONS:\n"
    putStrLn "Els valors que introduiras per jugar han d'estar entre 1 i el nombre de columnes."
    putStrLn "El primer jugador en fer el 4 en ratlla guanya."
    putStrLn "Si el tauler es plena sera un empat.\n"
    
    
    --crear tauler
    let tauler = inicialitza_tauler n m
    print (n, m)
    putStrLn (mostra_tauler tauler)
    putStrLn ""

    
    
    --elegir estrategia
    putStrLn "Insereix la estrategia que vols utilitzar:"
    putStrLn "(1) Random"
    putStrLn "(2) Greedy"
    putStrLn "(3) Smart"
    estrategia <- getLine
    
    --elegir el jugador que comença aleatoriament
    random <- randInt 1 2
    
    --començar a jugar depenent del parametre i passar el jugador que comença
    if (random==1) then
        if (estrategia == "1") then jugar tauler estrategia_random '1'
                            else if (estrategia == "2") then jugar tauler estrategia_greedy '1'
                                                        else jugar tauler estrategia_smart '1'
    
    
    else if (estrategia == "1") then jugar tauler estrategia_random '2'
                           else if (estrategia == "2") then jugar tauler estrategia_greedy '2'
                                                       else jugar tauler estrategia_smart '2'
    
    
    return ()
    
    