from antlr4 import *
from generated.MiniOberonLexer import MiniOberonLexer
from generated.MiniOberonParser import MiniOberonParser
from pprint import pprint

# Импортируем твой класс-построитель AST
from src.ast_builder import AstBuilderVisitor


def main():
    # Тестовый пример Oberon-кода
    code = """
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
    """

    # Создаём лексер и парсер
    input_stream = InputStream(code)
    lexer = MiniOberonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniOberonParser(token_stream)

    # Получаем дерево разбора
    tree = parser.program()

    # Применяем визитор, чтобы построить AST
    ast = AstBuilderVisitor().visit(tree)

    # Выводим результат
    print("=== AST ===")
    print(ast)
    pprint(ast, width=100, sort_dicts=False)

if __name__ == '__main__':
    main()
