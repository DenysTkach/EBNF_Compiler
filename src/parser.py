from pathlib import Path
from pprint import pprint
import tatsu

def load_grammar_text() -> str:
    # .../project/src/parser.py -> подняться на уровень вверх и в папку grammar
    grammar_path = Path(__file__).parent.parent / 'grammar' / 'minioberon.ebnf'
    return grammar_path.read_text(encoding='utf-8')

def parse_source(src: str):
    grammar = load_grammar_text()
    parser = tatsu.compile(grammar)  # старт можно не указывать, если используем rule_name
    return parser.parse(src, rule_name='program')  # явный старт

if __name__ == '__main__':
    code = '''
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
    ast = parse_source(code)
    pprint(ast, width=120)
