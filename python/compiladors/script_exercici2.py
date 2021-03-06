import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.InputStream import InputStream
from ExprVisitorTree import ExprVisitorTree
from ExprVisitorEval import ExprVisitorEval

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))

lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()

visitorTree = ExprVisitorTree()
visitorTree.visit(tree)

visitorEval = ExprVisitorEval()
visitorEval.visit(tree)
