grammar MiniOberon;

// -------------------- Parser rules --------------------

program
  : module EOF
  ;

module
  : MODULE IDENT ';' block IDENT '.'
  ;

block
  : declarations (BEGIN statseq)? END
  ;

declarations
  : (constsec | typesec | varsec | procdecl)*
  ;

/* ----- CONST / TYPE / VAR ----- */

constsec
  : CONST constdecl (';' constdecl)* ';'
  ;

constdecl
  : IDENT '=' expr
  ;

typesec
  : TYPE typedecl (';' typedecl)* ';'
  ;

typedecl
  : IDENT '=' type_
  ;

varsec
  : VAR vardecl (';' vardecl)* ';'
  ;

vardecl
  : identlist ':' type_
  ;

/* ----- Types ----- */

type_
  : basetype
  | arraytype
  | recordtype
  | IDENT
  ;

basetype
  : INTEGER
  | REAL
  | STRING
  | BOOLEAN
  ;

arraytype
  : ARRAY '[' dimlist ']' OF elemtype
  ;

dimlist
  : dimitem (',' dimitem)*
  ;

dimitem
  : IDENT
  | INTLIT
  ;

elemtype
  : basetype
  | arraytype
  | IDENT
  ;

recordtype
  : RECORD (identlist ':' type_ ';')* END
  ;

/* ----- Procedures / Functions ----- */

procdecl
  : PROCEDURE IDENT '(' paramlist? ')' ';' block IDENT ';'
  | FUNCTION  IDENT '(' paramlist? ')' ':' type_ ';' block IDENT ';'
  ;

paramlist
  : param (';' param)*
  ;

param
  : VAR? identlist ':' type_
  ;

identlist
  : IDENT (',' IDENT)*
  ;

/* ----- Statements ----- */

statseq
  : statement (';' statement)* ';'?
  ;

statement
  : assign
  | call
  | ifstmt
  | whilestmt
  | forstmt
  | returnstmt
  ;

assign
  : designator ':=' expr
  ;

call
  : IDENT '(' arglist ')'
  | IDENT '(' ')'
  ;

arglist
  : expr (',' expr)*
  ;

ifstmt
  : IF expr THEN statseq
    (ELSIF expr THEN statseq)*
    (ELSE statseq)?
    END
  ;

whilestmt
  : WHILE expr DO statseq END
  ;

forstmt
  : FOR IDENT ':=' expr TO expr (BY expr)? DO statseq END
  ;

returnstmt
  : RETURN expr
  | RETURN
  ;

/* ----- Designators & Expressions ----- */

designator
  : IDENT selectors?
  ;

selectors
  : selector+
  ;

selector
  : '[' exprlist ']'
  | '.' IDENT
  ;

exprlist
  : expr (',' expr)*
  ;

expr
  : simpleexpr (relop simpleexpr)?
  ;

relop
  : '=' | '#' | '<' | '<=' | '>' | '>='
  ;

simpleexpr
  : sign? term (addop term)*
  ;

sign
  : '+' | '-'
  ;

addop
  : '+' | '-'
  ;

term
  : factor (mulop factor)*
  ;

mulop
  : '*' | '/'
  ;

factor
  : number
  | STRINGLIT
  | boollit
  | call
  | designator
  | '(' expr ')'
  ;

boollit
  : TRUE
  | FALSE
  ;

number
  : REALLIT
  | INTLIT
  ;

// -------------------- Lexer rules --------------------
// Keywords (должны идти ПЕРЕД IDENT, чтобы не распознавались как идентификаторы)

MODULE   : 'MODULE' ;
CONST    : 'CONST' ;
TYPE     : 'TYPE' ;
VAR      : 'VAR' ;
BEGIN    : 'BEGIN' ;
END      : 'END' ;
PROCEDURE: 'PROCEDURE' ;
FUNCTION : 'FUNCTION' ;
OF       : 'OF' ;
ARRAY    : 'ARRAY' ;
RECORD   : 'RECORD' ;
INTEGER  : 'INTEGER' ;
REAL     : 'REAL' ;
STRING   : 'STRING' ;
BOOLEAN  : 'BOOLEAN' ;
TRUE     : 'TRUE' ;
FALSE    : 'FALSE' ;
IF       : 'IF' ;
THEN     : 'THEN' ;
ELSIF    : 'ELSIF' ;
ELSE     : 'ELSE' ;
WHILE    : 'WHILE' ;
DO       : 'DO' ;
FOR      : 'FOR' ;
TO       : 'TO' ;
BY       : 'BY' ;
RETURN   : 'RETURN' ;

// Identifiers & literals

IDENT
  : [A-Za-z] [A-Za-z0-9_]*
  ;

INTLIT
  : [0-9]+
  ;

REALLIT
  : [0-9]+ '.' [0-9]+ ([eE] [+\-]? [0-9]+)?
  ;

STRINGLIT
  : '"' ( ~["\\\r\n] | '\\' . )* '"'
  ;

// Operators & punctuation (можно оставить как лексемы по умолчанию)
WS
  : [ \t\r\n]+ -> skip
  ;

LINE_COMMENT
  : '//' ~[\r\n]* -> skip
  ;

BLOCK_COMMENT
  : '/*' .*? '*/' -> skip
  ;

OBERON_COMMENT
  : '(*' .*? '*)' -> skip
  ;

// Single-character tokens are taken as literals in parser rules:
// ';' ',' '.' ':' '(' ')' '[' ']' '+' '-' '*' '/' '=' '#' '<' '>' '<=' '>=' ':='
// Многосимвольные операторы обеспечим через lexer modes ниже:

LE  : '<=' ;
GE  : '>=' ;
ASSIGN : ':=' ;

// Чтобы не конфликтовать с одиночными символами:
LT  : '<' ;
GT  : '>' ;
