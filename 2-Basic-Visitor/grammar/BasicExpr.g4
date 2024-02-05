grammar BasicExpr;

start: expr EOF;
expr: expr PLUS expr
    | NUM
    ;

NUM: [0-9]+;
PLUS: '+';
WS: [ \t\r\n]+ -> skip;
