from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser
from MyCustomListener import *

input_string = 'y=3*(2+5+(3*6))*8/2'

stream = InputStream(input_string)
lexer = ExprLexer(stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
parse_tree = parser.start()
my_listener = MyCustomListener()

walker = ParseTreeWalker()
walker.walk(listener=my_listener, t=parse_tree)
print("y =", my_listener.value)
