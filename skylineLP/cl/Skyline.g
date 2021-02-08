grammar Skyline;

root : ( expr | asig ) EOF ;

asig : VAR ASIG expr ;

expr : '(' expr ')'
    | MENYS expr
    | expr PER expr
    | expr PER NUM
    | expr MES expr
    | expr MES NUM
    | expr MENYS NUM
    | creacio
    | VAR
    ;
    
creacio_simple: '(' NUM ',' NUM ',' NUM ')'
    ;

creacio : creacio_simple
    | '[' creacio_simple (',' creacio_simple)+ ']'
    | '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}'
    ;

NUM : [0-9]+ ;
MES : '+' ;
MENYS: '-' ;
PER: '*' ;
ASIG: ':=' ;
VAR: [a-zA-Z] [a-zA-Z0-9]*;

WS : [ \n]+ -> skip ;