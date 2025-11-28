import json
from pprint import pprint
import tatsu


# ----------------- helpers -----------------
def _load_grammar():
    with open('minioberon.ebnf', encoding='utf-8') as f:
        return f.read()

def _print_result(title, ast):
    print(f'# {title}')
    pprint(ast, width=120)
    print(f'\n# {title} JSON')
    print(json.dumps(ast, indent=2))
    print('-' * 80)


# ----------------- your originals -----------------
def parse_if_statement():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)  # default start
    src = 'IF x < 0 THEN x := 0 ELSE x := x - 1 END'
    ast = parser.parse(src, rule_name='statement')
    _print_result('IF STATEMENT AST', ast)

def parse_full_module():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)  # было: tatsu.compile(grammar, start='program')
    module_src = '''
    MODULE Demo;
      VAR x: INTEGER;
    BEGIN
      IF x < 0 THEN
        x := 0
      ELSIF x = 0 THEN
        x := 1
      ELSE
        x := x - 1
      END
    END Demo.
    '''
    ast = parser.parse(module_src, rule_name='program')  # добавили rule_name
    _print_result('MODULE AST', ast)


# ----------------- more handy parsers -----------------

def parse_assignment():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'x := 1 + 2 * 3'
    ast = parser.parse(src, rule_name='statement')
    _print_result('ASSIGNMENT', ast)

def parse_while():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'WHILE i < 10 DO i := i + 1 END'
    ast = parser.parse(src, rule_name='statement')
    _print_result('WHILE', ast)

def parse_for():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'FOR i := 0 TO 10 BY 2 DO x := x + i END'
    ast = parser.parse(src, rule_name='statement')
    _print_result('FOR', ast)

def parse_call_with_args():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'Foo(1, x, 3)'
    ast = parser.parse(src, rule_name='statement')
    _print_result('CALL WITH ARGS', ast)

def parse_call_no_args():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'Bar()'
    ast = parser.parse(src, rule_name='statement')
    _print_result('CALL NO ARGS', ast)

def parse_designator():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    # приклад з полями та індексацією
    src = 'a.b[1, 2].c'
    ast = parser.parse(src, rule_name='designator')
    _print_result('DESIGNATOR', ast)

def parse_expression():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = '(1 + 2) * 3 < 10'
    ast = parser.parse(src, rule_name='expr')
    _print_result('EXPRESSION', ast)

def parse_var_decls_module():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)  # без start=
    module_src = '''
    MODULE Vars;
      VAR
        a: INTEGER;
        b: REAL;
        s: STRING;
        m: ARRAY[3,4] OF INTEGER;
        t: ARRAY[2,2,2] OF REAL;
    END Vars.
    '''
    ast = parser.parse(module_src, rule_name='program')
    _print_result('MODULE VAR DECLS', ast)



def parse_proc_module():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)  # было: tatsu.compile(grammar, start='program')
    module_src = '''
    MODULE P;
      VAR g: INTEGER;

      PROCEDURE Inc(VAR x: INTEGER; y: INTEGER);
        VAR z: INTEGER;
      BEGIN
        x := x + y
      END Inc;

      FUNCTION Add(a: INTEGER; b: INTEGER): INTEGER;
      BEGIN
        RETURN a + b
      END Add;

    BEGIN
      g := 0;
      Inc(g, 5);
      g := Add(g, 1)
    END P.
    '''
    ast = parser.parse(module_src, rule_name='program')  # добавили rule_name
    _print_result('MODULE WITH PROC/FUNC', ast)

def parse_if_elsif_only():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'IF a = 0 THEN x := 1 ELSIF a = 1 THEN x := 2 END'
    ast = parser.parse(src, rule_name='statement')
    _print_result('IF + ELSIF (NO ELSE)', ast)

def parse_if_only_then():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'IF a > 0 THEN x := a END'
    ast = parser.parse(src, rule_name='statement')
    _print_result('IF THEN ONLY', ast)

def parse_return_with_expr():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'RETURN 1 + 2 * 3'
    ast = parser.parse(src, rule_name='statement')
    _print_result('RETURN WITH EXPR', ast)

def parse_return_plain():
    grammar = _load_grammar()
    parser = tatsu.compile(grammar)
    src = 'RETURN'
    ast = parser.parse(src, rule_name='statement')
    _print_result('RETURN PLAIN', ast)





# ----------------- driver -----------------

def simple_parse():

     parse_if_statement()
     parse_full_module()


     parse_assignment()
     parse_while()
     parse_for()
     parse_call_with_args()
     parse_call_no_args()
     parse_designator()
     parse_expression()
     parse_var_decls_module()
     parse_proc_module()
     parse_if_elsif_only()
     parse_if_only_then()
     parse_return_with_expr()
     parse_return_plain()


if __name__ == '__main__':
    simple_parse()
