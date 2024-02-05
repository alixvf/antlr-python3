from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from gen.TACLexer import TACLexer
from gen.TACParser import TACParser
from CustomListener import *

input_string = 'y=3*4+5*6*(7*3+3*6*(2+9))'

#input_string = 'y=3/2'

stream = InputStream(input_string)
lexer = TACLexer(stream)
token_stream = CommonTokenStream(lexer)
parser = TACParser(token_stream)

parse_tree = parser.start()

walker = ParseTreeWalker()
walker.walk(listener=MyCustomListener(), t=parse_tree)
