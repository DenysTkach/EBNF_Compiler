# src/frontend.py
from antlr4 import *
import sys
from pprint import pprint

from generated.MiniOberonLexer import MiniOberonLexer
from generated.MiniOberonParser import MiniOberonParser
from src.ast_builder import AstBuilderVisitor
from src.sema import SemanticAnalyzer, SemanticError


def load_source(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        return f.read()


def parse_source(code: str):
    input_stream = InputStream(code)
    lexer = MiniOberonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniOberonParser(token_stream)

    tree = parser.program()
    ast = AstBuilderVisitor().visit(tree)
    return ast


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.frontend <file.mod>")
        return

    filename = sys.argv[1]
    print(f"Parsing file: {filename}")
    code = load_source(filename)

    ast = parse_source(code)

    print("\n=== AST ===")
    pprint(ast, width=100, sort_dicts=False)

    print("\n=== Semantic analysis ===")
    analyzer = SemanticAnalyzer()
    try:
        analyzer.analyze(ast)
        print("OK: semantic analysis completed without errors.")
    except SemanticError as e:
        print("SEMANTIC ERROR:", e)


if __name__ == "__main__":
    main()
