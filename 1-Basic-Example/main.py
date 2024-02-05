from antlr4 import CommonTokenStream, InputStream
from gen.BasicExprLexer import BasicExprLexer
from gen.BasicExprParser import BasicExprParser

while True:
    lexer = BasicExprLexer(InputStream(input('Enter expression: ')))
    tokens = CommonTokenStream(lexer)
    parser = BasicExprParser(tokens)
    tree = parser.start()
    print(tree.toStringTree(recog=parser))