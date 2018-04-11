'''
Artificial Intelligence Project

This program takes simple english sentences and translates them into
the java programming language as commands.
'''

import nltk     #Holds the CFG and parser
import re       #Used for regular expressions

def commentIntent(names):
    print ("\nThere are three types of comments in Java\n")
    print ("In line:")
    print ("// " + (names[0]).replace('"',"") + "\n")
    print ("One line:")
    print ("/*\t" + (names[0]).replace('"',"") + "\t*/\n")
    print ("Multi line:")
    print ("/**\n" + "*\t" + (names[0]).replace('"',"") + "\n*/")

def printIntent(result, names, numbers):
    if "(VALEXPR" in result:
        print ("\nSystem.out.println(" + (expression(result, names, numbers)).replace('"',"") + ");")
        print ("System.out.print(" + (expression(result, names, numbers)).replace('"',"") + ");")
    elif len(names) == 1 and len(numbers) == 0:   #Printing single string or variable
        print ("\nSystem.out.println(" + names[0] + ");")
        print ("System.out.print(" + names[0] + ");")
    elif len(numbers) == 1 and len(names) == 0: #Printing a single number
        print ("\nSystem.out.println(" + numbers[0] + ");")
        print ("System.out.print(" + numbers[0] + ");")

def setIntent(result, names, numbers):
    lastName = len(names) - 1
    if "(VALEXPR" in result:
        if (result.index("(VALEXPR") > result.index("(SETVARNAME")):
            print("\n" + (names[0]).replace('"',"") + " = "\
                  + expression(result, names[1:], numbers) + ";")
        elif (result.index("(VALEXPR") < result.index("(SETVARNAME")):
            print("\n" + (names[lastName]).replace('"',"") + " = "\
                  + expression(result, names[0 : -1], numbers) + ";")
    else:
        if len(numbers) == 1:
            print("\n" + (names[0]).replace('"',"") + " = " + numbers[0] + ";")
        elif len(names) == 2:
            if "assign" in result:
                print("\n" + (names[1]).replace('"',"") + " = " + (names[0]).replace('"',"") + ";")
            else:
                print("\n" + (names[0]).replace('"',"") + " = " + (names[1]).replace('"',"") + ";")

def methodIntent(result, names, numbers):
    if "(NAMING" in result:
        if "(MOD" in result:
            returnType = input("Enter the return type: ")
            if "private" in result:
                print("\nprivate " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "public" in result:
                print("\npublic " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "protected" in result:
                print("\nprotected " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "static" in result:
                print("\npublic static " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
        else:
            modifier = input("Enter a modifier: ")
            returnType = input("Enter the return type: ")
            if "private" in modifier:
                print("\nprivate " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "public" in modifier:
                print("\npublic " + rreplaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "protected" in modifier:
                print("\nprotected " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "static" in modifier:
                print("\npublic static " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
    else:
        methodName = input("Enter a name for the method: ")
        names.insert(0,methodName)
        if "(MOD" in result:
            returnType = input("Enter the return type: ")
            if "private" in result:
                print("\nprivate " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "public" in result:
                print("\npublic " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "protected" in result:
                print("\nprotected " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "static" in result:
                print("\npublic static " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
        else:
            modifier = input("Enter a modifier: ")
            returnType = input("Enter the return type: ")
            if "private" in modifier:
                print("\nprivate " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "public" in modifier:
                print("\npublic " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "protected" in modifier:
                print("\nprotected " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")
            elif "static" in modifier:
                print("\npublic static " + replaceDecType(returnType) + " " + (names[0]).replace('"',"")\
                      + "( ) {\n //Insert body here\n}")

def variableIntent(result, names, numbers):
    if "(DECTYPE" in result:
        if "(NAMING" in result:
            if "(ASSIGN" in result:
                if len(names) == 2 and len(numbers) == 0:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"',"") + " = "\
                            + (names[1]).replace('"',"") + ";")
                elif len(names) == 1 and len(numbers) == 1:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"',"") + " = "\
                            + numbers[0] + ";")
                else:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"',"") + " = "\
                          + expression(result, names[1 :], numbers) + ";")
            else:
                print("\n" + replaceDecType(result) + " " + (names[0]).replace('"',"") + ";")
        else:
            varName = input("Enter a variable name: ")
            names.insert(0,varName)
            if "(ASSIGN" in result:
                if len(names) == 2 and len(numbers) == 0:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"',"") + " = "\
                            + (names[1]).replace('"',"") + ";")
                elif len(names) == 1 and len(numbers) == 1:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"',"") + " = "\
                            + numbers[0] + ";")
                else:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"',"") + " = "\
                          + expression(result, names[1 :], numbers) + ";")
            else:
                print("\n" + replaceDecType(result) + " " + (names[0]).replace('"',"") + ";")
    else:
        decType = input("Enter a variable type: ")
        if "(NAMING" in result:
            if "(ASSIGN" in result:
                if len(names) == 2 and len(numbers) == 0:
                    print("\n" + replaceDecType(decType) + " " + (names[0]).replace('"',"") + " = "\
                            + (names[1]).replace('"',"") + ";")
                elif len(names) == 1 and len(numbers) == 1:
                    print("\n" + replaceDecType(dectype) + " " + (names[0]).replace('"',"") + " = "\
                            + numbers[0] + ";")
                else:
                    print("\n" + replaceDecType(decType) + " " + (names[0]).replace('"',"") + " = "\
                          + expression(result, names[1 :], numbers) + ";")
            else:
                print("\n" + replaceDecType(decType) + " " + (names[0]).replace('"',"") + ";")
        else:
            varName = input("Enter a variable name: ")
            names.insert(0,varName)
            if "(ASSIGN" in result:
                if len(names) == 2 and len(numbers) == 0:
                    print("\n" + replaceDecType(decType) + " " + (names[0]).replace('"',"") + " = "\
                            + (names[1]).replace('"',"") + ";")
                elif len(names) == 1 and len(numbers) == 1:
                    print("\n" + replaceDecType(decType) + " " + (names[0]).replace('"',"") + " = "\
                            + numbers[0] + ";")
                else:
                    print("\n" + replaceDecType(decType) + " " + (names[0]).replace('"',"") + " = "\
                          + expression(result, names[1 :], numbers) + ";")
            else:
                print("\n" + replaceDecType(decType) + " " + (names[0]).replace('"',"") + ";")
                
def expression(result, names, numbers):
    if len(names) == 2 and len(numbers) ==0:  #Printing expression
        return  ((names[0]).replace('"',"") + " "\
               + replaceOperators(result) + " " + (names[1]).replace('"',""));
    elif len(numbers) == 2 and len(names) == 0: #Printing an expression
        return  (numbers[0] + " "\
               + replaceOperators(result) + " " + numbers[1]);
    elif len(numbers) == 1 and len(names) == 1: #Printing an expression
        return  ((names[0]).replace('"',"") + " "\
               + replaceOperators(result) + " " + numbers[0]);

def replaceDecType(result):
    if "integer" in result:
        return "int";
    elif "float" in result:
        return "float";
    elif "double" in result:
        return "double";
    elif "boolean" in result:
        return "boolean";
    elif "long" in result:
        return "long";
    elif "void" in result:
        return "void";

def replaceOperators(result):
    if "plus" in result:
        return "+";
    elif "minus" in result:
        return "-";
    elif "divided" in result:
        return "/";
    elif "multiplied" in result:
        return "*";
    elif "times" in result:
        return "*";
    elif "modulus" in result:
        return "%";

def variableHelp():
    print("Variable delcarations have three parts in Java: the type, name, and assignment.")
    print("Here are examples of variable declarations this program understands:\n")
    print("Create a variable\nMake an integer called \"Joe\"\nDeclare a long equal to 7.25.")
    print("Make a new variable called \"X\" equal to \"Y\" modulus 7.\n")

def setHelp():
    print("Setting a variable has two parts in Java: the name and the quantity assigned.")
    print("Here are examples of variables being set that this program understands:\n")
    print("Set \"X\" equal to 7.\nAssign \"Jim\" plus \"Bob\" to \"Joe\"")
    print("Make \"X\" equal -8.3 times 12\nSet \"index\" to \"current\"\n")

def printHelp():
    print("For the printing, use the word print and then what you would like to print.")
    print("Here are examples of print statements that this program understands:\n")
    print("Print \"X\" plus -67\nPrint \"Hello, world!\"\nPrint 5.\n")

def commentHelp():
    print("Comments are represented by the word comment and then a string.")
    print("Here are examples of comment statements that this program understands:\n")
    print("Comment \"Look at this great comment\"\nComment \"Base Case\"\n")

def methodHelp():
    print("Methods are represented by a name, modifier, and a return type.")
    print("Here are examples of method statements that this program understands:\n")
    print("Create a method.\nMake a method called \"my_method\"\nMake a private method\n")

def methodWords():
    print("Key words for method modifiers: public, static, void, private protected")
    print("Key words for method return type: integer, void, boolean, float, double, long")

#Creates the grammar
grammar = nltk.CFG.fromstring("""
S -> VARIABLE | SET | METHOD | PRINT | COMMENT
VARIABLE -> DECLARE NAMING ASSIGN
VARIABLE -> DECLARE NAMING
VARIABLE -> DECLARE ASSIGN
VARIABLE -> DECLARE
DECLARE -> DVERB DET VAR PREPOSITION DET DECTYPE
DECLARE -> DVERB DET NEW VAR PREPOSITION DET DECTYPE
DECLARE -> DVERB DET NEW DECTYPE VAR
DECLARE -> DVERB DET NEW VAR
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
DVERB -> 'create' | 'make' | 'declare'
DET -> 'an' | 'a'
DECTYPE -> 'boolean' | 'integer' | 'float' | 'double' | 'long'
VAR -> 'variable'
SETVARNAME -> 'variable1' | 'variable2' | 'variable3'
VARVAL -> 'number1' | 'number2'
OPERATOR -> OPERATOR BY | 'plus' | 'minus' | 'divided' | 'multiplied' | 'modulus' | 'times'
PREPOSITION -> "as" | "to"
BY -> 'by'
TO -> 'to'
NEW -> 'new'
""")

#Feeds the grammar into the parser
parser = nltk.ChartParser(grammar)


print ("-------------------------------------------------------------------")
print ("\n\tWelcome to the Natural Language Program." + "\n")
print ("-------------------------------------------------------------------")
print ("\n")

#cont is 'y' if the user would like to continue the program
cont = 'y'
#If explaination is true, it prints out the steps of the program
explaination = True

variableHelp()
setHelp()
printHelp()
commentHelp()
methodHelp()

while cont == 'y':
    userInput = input("Input a string: ")
    newInput = userInput.rstrip('.') #Takes away the period from the sentence
    names = re.findall(r'"[^"]*"', newInput) #Gets anything in double quotes
    numbers =  re.findall(r"[-+]?\d*\.\d+\b|\b\d+\b|[-+]?\d+\b", newInput) #Gets all numbers

    varIndex = 1
    #For all the strings entered in the sentence, they are replaced
    #with input that the context free grammar can recognize
    for name in names:
        variableName = "variable" + str(varIndex)
        newInput = newInput.replace(name, variableName)
        varIndex = varIndex + 1

    numIndex = 1
    #For all the numbers entered in the sentence, they are replaced
    #with input that the context free grammar can recognize
    for number in numbers:
        numberName = "number" + str(numIndex)
        newInput = newInput.replace(number, numberName)
        numIndex = numIndex + 1

    #Shows what identifiers and numbers were found in the input sentence
    if explaination == True:
        if len(names) > 0: #Identifiers were in sentence
            print ("\nNames found: " + (', '.join(str(e) for e in names)).replace('"',""))
        else:
            print ("\nNo names found.")
            
        if len(numbers) > 0: #Numbers were in sentence
            print ("Numbers found: " + ', '.join(str(e) for e in numbers))
        else:
            print ("No numbers found.")

    #Puts the input sentence into lowercase for the grammar
    newInput = newInput.lower()

    #Shows the result of the replacements and lowercase
    if explaination == True:
        print ("\nSentence put into parser: " + newInput)
    sent = newInput.split()

    #successful holds if the grammar was able to be parsed
    successful = True

    #Tries to put the sentence into the parser.
    #Catches exceptions if sentence was not valid.
    try:
        #gets a list version of the parse tree
        results = list(parser.parse(sent))
        #removes the word "Tree" and brackets from results
        results = ''.join(str(e) for e in results)

        #Either shows parsing or reports success
        if explaination == True:
            print ("\nParse Of the Entered String\n")
            print (results)
        else:
            print ("Parsing successful.")
    except:
        print ("Invalid sentence. Please try again.")
        print ("Check spelling and/or help and try again.")
        successful = False

    #Determines the intent of the sentence from the LHS of the
    #parsing, teaches the user of the basics of the intent,
    #asks for more information if needed, and prints resulting
    #statement in Java syntax.
    if successful:
        if "(VARIABLE" in results:
            variableIntent(results, names, numbers)
        elif "(METHOD" in results:
            methodIntent(results, names, numbers)
        elif "(PRINT" in results:
            printIntent(results, names, numbers)
        elif "(COMMENT" in results:
            commentIntent(names)
        elif "(SET" in results:
            setIntent(results, names, numbers)
        else:
            print ("Could not figure out intent of the sentence.")
            print ("Check spelling and/or help and try again.")

    #Checks to see if the user would like to input another sentence.
    cont = input("\nEnter y to continue: ")

print ("\n-------------------------------------------------------------------")
print("\n\tThank you for using the natural language program.")
print ("\n-------------------------------------------------------------------")
