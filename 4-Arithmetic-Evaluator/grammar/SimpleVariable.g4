grammar SimpleVariable;

start: stmt+ EOF;
stmt:
    ('int'|'float') IDENTIFIER '=' NUMBER ';' #varDecl
    | 'print' '(' arithmeticExpr ')' ';'      #printStmt
    ;

arithmeticExpr: arithmeticTerm (('+' | '-') arithmeticTerm)* #arithmeticExpr_
    ;

arithmeticTerm: arithmeticFactor (('*' | '/') arithmeticFactor)* #arithmeticTerm_
    ;

arithmeticFactor:
    | '(' arithmeticExpr ')'
    | NUMBER
    | IDENTIFIER
    ;

IDENTIFIER: IdentifierNondigit (IdentifierNondigit | NUMBER)*;
IdentifierNondigit: [a-zA-Z_]+;

NUMBER: [0-9]*'.'[0-9]+ | [0-9]+;
WS: [ \t\r\n]+ -> skip;

COMMENT
    : '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;
