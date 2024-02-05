grammar TAC;

start: Id '=' expr EOF;

expr returns [reg=str()]:
    expr '+' term                      #exprPlus
    | expr '-' term                    #exprMinus
    | term                             #exprT
    ;

term returns [reg=str()]:
    term '*' fact                      #termMul
    | term '/' fact                    #termDiv
    | fact                             #termF
    ;

fact returns [reg=str()]:
    Id                                 #factId
    | Number                           #factNum
    | '('expr')'                       #factE
    ;


/* Lexical rules*/
Plus: '+';
MINUS: '-';
MUL: '*';
DIVIDE: '/';
ASSIGN: '=';

Id: IDENTIFIER;
Number: NUMBER;

fragment IDENTIFIER: [a-zA-Z]+;
fragment NUMBER: [0-9]+;

Whitespace: [ \t]+ -> channel(HIDDEN);
Newline: '\n' -> skip;

