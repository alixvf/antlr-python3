from antlr4 import CommonTokenStream, InputStream

from EvalVisitor import EvalVisitor
from gen.BasicExprLexer import BasicExprLexer
from gen.BasicExprParser import BasicExprParser

while True:
    lexer = BasicExprLexer(InputStream(input('Enter expression: ')))
    tokens = CommonTokenStream(lexer)
    parser = BasicExprParser(tokens)
    tree = parser.start()
    visitor = EvalVisitor()
    visitor.visit(tree)