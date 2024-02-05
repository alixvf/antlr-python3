from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser

input_string = "y=3*(2*ab+55+3*6)*8/(2*3)"
#input_string = "y=3*(2+3)"

stream = InputStream(input_string)
lexer = ExprLexer(stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
_ = parser.start()

