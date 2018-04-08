import nltk
import re

grammar = nltk.CFG.fromstring("""
S -> VARIABLE | SET | METHOD | PRINT | COMMENT
VARIABLE -> DECLARE NAMING ASSIGN
VARIABLE -> DECLARE NAMING
VARIABLE -> DECLARE ASSIGN
VARIABLE -> DECLARE
DECLARE -> DVERB DET VAR PREPOSITION DECTYPE
DECLARE -> DVERB DET NEW VAR PREPOSITION DECTYPE
DECLARE -> DVERB DET NEW DECTYPE VAR
DECLARE -> DVERB DET DECTYPE VAR
DECLARE -> DVERB DET DECTYPE
DECLARE -> DVERB DET VAR
NAMING -> NAMEVERB SETVARNAME
NAMING -> SETVARNAME
ASSIGN -> ASSIGNMENT VARVAL
ASSIGN -> ASSIGNMENT SETVARNAME
ASSIGN -> ASSIGNMENT VALEXPR
VALEXPR -> VARVAL OPERATOR VARVAL
VALEXPR -> VARVAL OPERATOR SETVARNAME
VALEXPR -> SETVARNAME OPERATOR VARVAL
VALEXPR -> SETVARNAME OPERATOR SETVARNAME
ASSIGNMENT -> ASSIGNMENT TO | 'equaling' | 'equal' | 'equal' | 'to'
SET -> SETVERB SETVARNAME ASSIGNMENT VARVAL
SET -> SETVERB SETVARNAME ASSIGNMENT SETVARNAME
SET -> SETVERB SETVARNAME ASSIGNMENT VALEXPR
SET -> SETVERB SETVARNAME VALEXPR
SET -> SETVERB VALEXPR TO SETVARNAME
SET -> SETVERB VARVAL TO SETVARNAME
SET -> SETVERB SETVARNAME TO SETVARNAME
METHOD -> DVERB MTHD
METHOD -> DVERB DET MTHD
METHOD -> DVERB DET MOD MTHD
METHOD -> DVERB DET MTHD NAMING
METHOD -> DVERB DET MOD MTHD NAMING
PRINT -> PRNT SETVARNAME
PRINT -> PRNT VARVAL
PRINT -> PRNT VALEXPR
COMMENT -> CMT SETVARNAME
CMT -> 'comment'
PRNT -> 'print'
MTHD -> 'method'
MOD -> 'public' | 'private' | 'protected' | 'static'
SETVERB -> 'set' | 'make' | 'assign' 
NAMEVERB -> 'called' | 'named'
DVERB -> 'create' | 'make'
DET -> 'an' | 'a'
DECTYPE -> 'boolean' | 'integer' | 'float' | 'double' | 'long'
VAR -> 'variable'
SETVARNAME -> 'variable1' | 'variable2' | 'variable3'
VARVAL -> 'number1' | 'number2'
OPERATOR -> OPERATOR BY | 'plus' | 'minus' | 'divided' | 'multiplied' | 'modulus'
BY -> 'by'
TO -> 'to'
NEW -> 'new'
""")
parser = nltk.ChartParser(grammar)


print ("-------------------------------------------------------------------")
print ("\n\tWelcome to the Natural Language Program." + "\n")
print ("-------------------------------------------------------------------")
print ("\n")

cont = 'y'
explaination = True

while cont == 'y':
    userInput = input("Input a string to test: ")
    newInput = userInput.rstrip('.')
    names = re.findall(r'"[^"]*"', newInput)
    numbers =  re.findall(r"[-+]?\d*\.\d+|\d+", newInput)

    varIndex = 1
    for name in names:
        variableName = "variable" + str(varIndex)
        newInput = newInput.replace(name, variableName)
        varIndex = varIndex + 1

    numIndex = 1
    for number in numbers:
        numberName = "number" + str(numIndex)
        newInput = newInput.replace(number, numberName)
        numIndex = numIndex + 1

    if explaination == True:
        if len(names) > 0:
            print ("\nNames found: " + (', '.join(str(e) for e in names)).replace('"',""))
        else:
            print ("\nNo names found.")
        if len(numbers) > 0:
            print ("Numbers found: " + ', '.join(str(e) for e in numbers))
        else:
            print ("No numbers found.")

    newInput = newInput.lower()

    if explaination == True:
        print ("\nSentence put into parser: " + newInput)
    sent = newInput.split()

    successful = True
    try:
        results = list(parser.parse(sent))
        results = ''.join(str(e) for e in results)
        if explaination == True:
            print ("\nParse Of the Entered String\n")
            print (results)
        else:
            print ("Parsing successful.")
    except:
        print ("Invalid sentence. Please try again.")
        successful = False

    if successful:
        if "(VARIABLE" in results:
            print("\nYou are trying to make a variable.")
        elif "(METHOD " in results:
            print ("\nYou are trying to make a method.")
        elif "(SET " in results:
            print ("\nYou are trying to set a variable's value.")
        elif "(PRINT " in results:
            print ("\nYou are trying to print to the screen.\n")
            if len(names) == 1 and len(numbers) == 0:
                print ("System.out.println(" + ''.join(str(e) for e in names) + ");")
                print ("System.out.print(" + ''.join(str(e) for e in names) + ");")
            else:
                print ("System.out.println(" + '\" + \"'.join(str(e) for e in numbers) + ");")
                print ("System.out.print(" + ''.join(str(e) for e in numbers) + ");")
        else:
            print ("\nYou are trying to create a comment.")
            print ("There are three types of comments in Java\n")
            print ("In line:")
            print ("// " + (''.join(str(e) for e in names)).replace('"','') + "\n")
            print ("One line:")
            print ("/*\t" + (''.join(str(e) for e in names)).replace('"','') + "\t*/\n")
            print ("Multi line:")
            print ("/**\n" + "*\t" + (''.join(str(e) for e in names)).replace('"','') + "\n*/")
        
    cont = input("\nEnter y to continue: ")

print ("\n-------------------------------------------------------------------")
print("\n\tThank you for using the natural language program.")
print ("\n-------------------------------------------------------------------")
