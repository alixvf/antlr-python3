from antlr4 import *

from CustomListener import CustomTypeCheckerListener
from gen.TypeCheckerLexer import TypeCheckerLexer
from gen.TypeCheckerParser import TypeCheckerParser

# Step 0: Give an input
input_string = '2+3*3.9'

# Step 1: Convert input to a byte stream
stream = InputStream(input_string)
# Step 2: Create lexer
lexer = TypeCheckerLexer(stream)
# Step 3: Create a list of tokens
token_stream = CommonTokenStream(lexer)
# Step 4: Create parser
parser = TypeCheckerParser(token_stream)
# Step 5: Create parse tree
parse_tree = parser.start()

# Step 6: Adding a listener
my_listener = CustomTypeCheckerListener()


walker = ParseTreeWalker()
try:
    walker.walk(listener=my_listener, t=parse_tree)
except Exception as e:
    print(e)
