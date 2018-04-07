import nltk
from nltk import CFG, parse

grammar = CFG.fromstring("""
S -> VARIABLE
S -> METHOD
S -> SET
S -> PRINT
S -> COMMENT
VARIABLE -> DECLARE NAMING ASSIGN
VARIABLE -> DECLARE NAMING
VARIABLE -> DECLARE ASSIGN
DECLARE -> DVERB DET VAR PREPOSITION DECTYPE
DECLARE -> DVERB DET NEW VAR PREPOSITION DECTYPE
DECLARE -> DVERB DET NEW DECTYPE VAR
DECLARE -> DVERB DET DECTYPE VAR
DECLARE -> DVERB DECTYPE
NAMING -> NAMEVERB SETVARNAME
NAMING -> SETVARNAME
ASSIGN -> ASSIGNMENT VALVAL
ASSIGN -> ASSIGNMENT VALVAR
ASSIGN -> ASSIGNMENT VALEXPR
DECTYPE -> "a boolean" | "an integer" | "a float" | "a double" | "a long"
SET -> SETVERB SETVARNAME ASSIGNMENT VALVAL
SET -> SETVERB SETVARNAME ASSIGNMENT VALVAR
SET -> SETVERB SETVARNAME ASSIGNMENT VALEXPR
SETVERB -> "set" | "make" | "assign" 
OPERATOR -> "plus" | "minus" | "divided by" | "multiplied by" | "modulus"
VALEXPR -> VARVAL OPERATOR VARVAL
VALEXPR -> VARVAR OPERATOR VARVAR
VALEXPR -> VARVAL OPERATOR VARVAR
VALEXPR -> SETVARNAME OPERATOR SETVARNAME
ASSIGNMENT -> "equaling" | "equal to" | "equal" | "to"
METHOD -> CREATEVERB DET MTHD NAMING
METHOD -> CREATEVERB DET MTHD NAMING
METHOD -> CREATEVERB MTHD NAMING RETURN
MTHD -> "method"
MOD -> "public" | "private" | "protected" | "static"
RETURN -> "with return type int"
RETURN -> "with return type double"
RETURN -> "with return type boolean"
RETURN -> "with return type float"
RETURN -> "with return type long"
VAR -> "variable"
DET -> "an" | "a" | "the" | "this" | "that" | "these" | "those"
AND -> "and"
NEW -> "new"
CREATEVERB -> "declare" | "create" | "make" | "initialize" | "instantiate"
NAMEVERB -> "called" | "named"
PREPOSITION -> "as" | "to"
VALVAR -> "number1" | "number2"
SETVARNAME -> "variable1" | "variable2"
PRNT -> "print"
PRNTVAL -> "printStatement"
PRINT -> PRNT PRNTVAL
CMT -> "comment"
COMMENT -> CMT CMTVAL
CMTVAL -> "commentStatement"
  """)

sentence = "create a variable named variable1".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
#It says that the rd_parser doesn't have an nbest_parse
#but all reference on the internet says that this should work
tree = rd_parser.nbest_parse(sentence)
