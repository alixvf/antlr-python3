grammar Expr;
start:
    Id '=' expr EOF
    ;

expr returns [val=float()]:
    expr '+' term                 #expr1
    | expr '-' term               #expr2
    | term                        #expr3
    ;

term returns [val=float()]:
    term '*' fact                 #term1
    | term '/' fact               #term2
    | fact                        #term3
    ;

fact returns [val=float()]:
    Id                            #fact1
    | Number                      #fact2
    | '('expr')'                  #fact3
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



