from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from MyCustomListener import MyCustomListener
from MyErrorListener import MyErrorListener
from gen.SimpleVariableLexer import SimpleVariableLexer
from gen.SimpleVariableParser import SimpleVariableParser

# reading from input.txt
lexer = SimpleVariableLexer(InputStream(open("input.txt", "r").read()))
lexer.removeErrorListeners()
lexer.addErrorListener(MyErrorListener())
token_stream = CommonTokenStream(lexer)
parser = SimpleVariableParser(token_stream)
try:
    parse_tree = parser.start()
    listener = MyCustomListener()
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)
except Exception as e:
    print(e)