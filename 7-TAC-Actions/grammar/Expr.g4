grammar Expr;

@parser::members{
temp_counter = 0

def create_temp(self, temp_counter):
    self.temp_counter += 1
    return 'T' + str(self.temp_counter)

def remove_temp(self):
    self.temp_counter -= 1

def get_temp(self):
    return 'T' + str(self.temp_counter)

}

start: Id '=' expr EOF;

expr returns [code=str()]:
    e2=expr '+' t1=term
            {$code = self.create_temp(self.temp_counter)}
            {print($code, '=', $e2.code, '+', $t1.code)}       #expr_Plus_Term

    | e2=expr '-' t1=term
            {$code = self.create_temp(self.temp_counter)}
            {print($code, '=', $e2.code, '-', $t1.code)}       #expr_Minus_Term

    | t1=term
            {$code = $t1.code}                                 #expr_Term
    ;

term returns [code=str()]:
    t2 = term '*' f1 = factor
            {$code = self.create_temp(self.temp_counter)}
            {print($code, '=', $t2.code, '*', $f1.code)}       #term_Mul_Factor

    | t2 = term '/' f1 = factor
            {$code = self.create_temp(self.temp_counter)}
            {print($code, '=', $t2.code, '/', $f1.code)}       #term_Div_Factor

    | f1=factor
            {$code = $f1.code}                                 #term_Factor
    ;

factor returns [code=str()]:
    Id
            {$code = $Id.text}                                 #factor_Id

    | Number
            {$code = $Number.text}                             #factor_Number

    | '('expr')'
            {$code = $expr.code}                               #factor_Expr
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

