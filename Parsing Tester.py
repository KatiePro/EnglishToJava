'''
Artificial Intelligence Project

This program takes simple english sentences and translates them into
the java programming language as commands.
'''

import nltk  # Holds the CFG and parser
import re  # Used for regular expressions


def commentIntent(names):
    print ("There are three types of comments in Java\n")
    print ("In line:")
    print ("// " + (names[0]).replace('"', "") + "\n")
    print ("One line:")
    print ("/*\t" + (names[0]).replace('"', "") + "\t*/\n")
    print ("Multi line:")
    print ("/**\n" + "*\t" + (names[0]).replace('"', "") + "\n*/")


def printIntent(result, names, numbers):
    if "(VALEXPR" in result:
        print ("System.out.println(" + (expression(result, names, numbers)).replace('"', "") + ");")
        print ("System.out.print(" + (expression(result, names, numbers)).replace('"', "") + ");")
    elif len(names) == 1 and len(numbers) == 0:  # Printing single string or variable
        print ("\nSystem.out.println(" + names[0] + ");")
        print ("System.out.print(" + names[0] + ");")
    elif len(numbers) == 1 and len(names) == 0:  # Printing a single number
        print ("\nSystem.out.println(" + numbers[0] + ");")
        print ("System.out.print(" + numbers[0] + ");")


def setIntent(result, names, numbers):
    lastName = len(names) - 1
    if "(VALEXPR" in result:
        if (result.index("(VALEXPR") > result.index("(SETVARNAME")):
            print("\n" + (names[0]).replace('"', "") + " = "\
                  + expression(result, names[1:], numbers) + ";")
        elif (result.index("(VALEXPR") < result.index("(SETVARNAME")):
            print("\n" + (names[lastName]).replace('"', "") + " = "\
                  + expression(result, names[0: -1], numbers) + ";")
    else:
        if len(numbers) == 1:
            print("\n" + (names[0]).replace('"', "") + " = " + numbers[0] + ";")
        elif len(names) == 2:
            if "assign" in result:
                print("\n" + (names[1]).replace('"', "") + " = " + (names[0]).replace('"', "") + ";")
            else:
                print("\n" + (names[0]).replace('"', "") + " = " + (names[1]).replace('"', "") + ";")


def methodIntent(result, names, numbers):
    if "(NAMING" in result:
        if "(MOD" in result:
            returnType = returnTypeMenu()
                
            if "private" in result:
                print("private " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "public" in result:
                print("public " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "protected" in result:
                print("protected " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "static" in result:
                print("public static " + replaceDecType(returnType) + " " + (names[0]).replace('"',  "")\
                        + "( ) {\n //Insert body here\n}")
        else:
            modifier = modifierMenu()
                
            returnType = returnTypeMenu()
                
            if "private" in modifier:
                print("private " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "public" in modifier:
                print("public " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "protected" in modifier:
                print("protected " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "static" in modifier:
                print("public static " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
    else:
        methodName = methodNameMenu()
                
        names.insert(0,methodName)
        if "(MOD" in result:
            returnType = returnTypeMenu()
                
            if "private" in result:
                print("private " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "public" in result:
                print("public " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "protected" in result:
                print("protected " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "static" in result:
                print("public static " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
        else:
            modifier = modifierMenu()
            
            returnType = returnTypeMenu()

            if "private" in modifier:
                print("private " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "public" in modifier:
                print("public " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "protected" in modifier:
                print("protected " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")
            elif "static" in modifier:
                print("public static " + replaceDecType(returnType) + " " + (names[0]).replace('"', "")\
                        + "( ) {\n //Insert body here\n}")


def variableIntent(result, names, numbers):
    if "(DECTYPE" in result:
        if "(NAMING" in result:
            if "(ASSIGN" in result:
                if len(names) == 2 and len(numbers) == 0:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"', "") + " = "\
                            + (names[1]).replace('"', "") + ";")
                elif len(names) == 1 and len(numbers) == 1:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"', "") + " = "\
                            + numbers[0] + ";")
                else:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"', "") + " = "\
                            + expression(result, names[1 :], numbers) + ";")
            else:
                print("\n" + replaceDecType(result) + " " + (names[0]).replace('"', "") + ";")
        else:
            varName = varNameMenu()
                
            names.insert(0,varName)
            if "(ASSIGN" in result:
                if len(names) == 2 and len(numbers) == 0:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"', "") + " = "\
                            + (names[1]).replace('"',"") + ";")
                elif len(names) == 1 and len(numbers) == 1:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"', "") + " = "\
                            + numbers[0] + ";")
                else:
                    print("\n" + replaceDecType(result) + " " + (names[0]).replace('"', "") + " = "\
                            + expression(result, names[1 :], numbers) + ";")
            else:
                print("\n" + replaceDecType(result) + " " + (names[0]).replace('"', "") + ";")
    else:
        decType = decTypeMenu()
                
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
            varName = varNameMenu()
                
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
    if len(names) == 2 and len(numbers) == 0:  # Printing expression
        return  ((names[0]).replace('"',"") + " "\
               + replaceOperators(result) + " " + (names[1]).replace('"',""));
    elif len(numbers) == 2 and len(names) == 0: # Printing an expression
        return  (numbers[0] + " "\
               + replaceOperators(result) + " " + numbers[1]);
    elif len(numbers) == 1 and len(names) == 1: # Printing an expression
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


# General Help
def helpPrompt(intent, action):
    print("Help Options: ")
    print("\tA: Options " + intent + ".")
    print("\tB: Help and additional information about " + action + ".")
    userInput = input("Select One: ")
    print()
    return userInput    


# Help Menus
def decTypeMenu():
    decType = input("Enter a variable type: ")  
    print("")
    while (decType.lower() == "help"):
        variableHelp()
        userInput = helpPrompt("for variable types", "variable types").lower()
        if (userInput == "a"):
            varTypeOptions()
        elif (userInput == "b"):
            varTypeHelp()
        decType = input("Enter a variable type: ")
        print("")
    return decType


def methodNameMenu():
    methodName = input("Enter a name for the method: ")
    print("")
    while (methodName.lower() == "help"):
        methodHelp()
        userInput = helpPrompt("for method names", "method names").lower()
        if (userInput == "a"):
            methodNameOptions()
        elif (userInput == "b"):
            methodNameHelp()
        methodName = input("Enter a name for the method: ")
        print("")
    return methodName


def modifierMenu():
    modifier = input("Enter a modifier: ") 
    print("")        
    while (modifier.lower() == "help"):
        methodHelp()
        userInput = helpPrompt("for modifiers", "modifiers").lower()
        if (userInput == "a"):
            modifierOptions()
        elif (userInput == "b"):
            modifierHelp()
        modifier = input("Enter a modifier: ")
        print("")
    return modifier


def returnTypeMenu():
    returnType = input("Enter the return type: ")
    print("")
    while (returnType.lower() == "help"):
        userInput = helpPrompt("for return types", "variable types").lower()
        if (userInput == "a"):
            returnTypeOptions()
        elif (userInput == "b"):
            returnTypeHelp()
        returnType = input("Enter the return type: ")
        print("")
    return returnType


def varNameMenu():
    varName = input("Enter a variable name: ")
    print("")
    while (varName.lower() == "help"):
        setHelp()
        userInput = helpPrompt("for variable names", "variable names").lower()
        if (userInput == "a"):
            varNameOptions()
        elif (userInput == "b"):
            varNameHelp()
        varName = input("Enter a variable name: ")
        print("")
    return varName


# Intent Help    
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
    print("Here are examples of comment statements that this program understands: ")
    print("\tComment \"Look at this great comment\"\n\tComment \"Base Case\"\n")


def methodHelp():
    print("Methods are represented by a name, modifier, and a return type.")
    print("Here are examples of method statements that this program understands: ")
    print("\tCreate a method.\n\tMake a method called \"my_method\"\n\tMake a private method")


# Intent-Specific Help
def methodNameHelp():
    print("Methods are invoked, or used, by calling method names.")
    print("Methods names can be pretty much anything, but in Java")
    print("they are usually written in camel case.\n")

                                   
def methodNameOptions():
    print("Method names can be anything, but are best as verbs.")
    print("The first letter should be lowercase.")
    print("The first letter of each internal word should be capitalized.")
    print("\thereIsAnExample")
    print("\tanotherExample\n")
              

def modifierHelp():
    print("Modifiers are keywords added to a method definition.")
    print("These access modifiers control what code is available where.")
    print("The default modifier is \"public.\" Public code can be used")
    print("anywhere in the project.\n")
                 

def modifierOptions():
    print("Method modifiers can be: ")
    print("\tPublic - Visible to the world")
    print("\tPrivate - Visible to the class only")
    print("\tProtected - Visible to the package and its subclasses\n")
                                   

def returnTypeHelp():
    print("Methods in Java have the option to return a value so that it can")
    print("be used elsewhere in the program. Return types constrain the")
    print("data type of the returned value.\n")
              

def returnTypeOptions():
    print("Return Types can be: ")
    print("\tVoid - Nothing is returned")
    print("\tInt - An integer number between  -2^31  and  (2^31)-1")
    print("\tLong - An integer number between  -2^63  and  (2^63)-1")
    print("\tFloat - Used to represent floating point (decimal) numbers")
    print("\tDouble - Used for more precise floating point numbers")
    print("\tBoolean - A variable with only two possible values: true and false\n")


def varNameHelp():
    print("Variables are  used by referring to their names. They can be")
    print("pretty much anything, but in are usually written in camel case.\n")
    

def varNameOptions():
    print("Variable names can be anything, but are best as nouns. The")
    print("first letter should be lowercase. The first letter of each")
    print("internal word should be capitalized.")
    print("\thereIsAnExample")
    print("\tanotherExample\n")
    

def varTypeHelp():
    print("Variable data types constrain the values that can be associated")
    print("with a variable.\n")
    

def varTypeOptions():
    print("Variable types can be: ")
    print("\tInt - An integer number between  -2^31  and  (2^31)-1")
    print("\tLong - An integer number between  -2^63  and  (2^63)-1")
    print("\tFloat - Used to represent floating point (decimal) numbers")
    print("\tDouble - Used for more precise floating point numbers")
    print("\tBoolean - A variable with only two possible values: true and false\n")
    
    
# Creates the grammar
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
DECTYPE -> 'boolean' | 'integer' | 'int' | 'float' | 'double' | 'long'
VAR -> 'variable'
SETVARNAME -> 'variable1' | 'variable2' | 'variable3'
VARVAL -> 'number1' | 'number2'
OPERATOR -> OPERATOR BY | 'plus' | 'minus' | 'divided' | 'multiplied' | 'modulus' | 'times'
PREPOSITION -> "as" | "to"
BY -> 'by'
TO -> 'to'
NEW -> 'new'
""")

# Feeds the grammar into the parser
parser = nltk.ChartParser(grammar)


print ("-------------------------------------------------------------------")
print ("\n\tWelcome to the Natural Language Program.\n")
print ("-------------------------------------------------------------------\n")
print ("IMPORTANT! Double quotes are mandatory for the following:")
print("\tVariable names\n\tNumbers\n\tComment content\n\tPrint content\n")
print ("Input \"Help\" at any time for a quick Java lesson or example input.\n")
print ("-------------------------------------------------------------------\n")

# cont is 'y' if the user would like to continue the program
cont = 'y'
# If explanation is true, it prints out the steps of the program
explanation = True

while cont == 'y':
    userInput = input("Input a string: ")

    if userInput.lower() == "help":
        print()
        variableHelp()
        setHelp()
        printHelp()
        commentHelp()
        methodHelp()
        
    else:
        newInput = userInput.rstrip('.') # Takes away the period from the sentence
        names = re.findall(r'"[^"]*"', newInput) # Gets anything in double quotes
        numbers =  re.findall(r"[-+]?\d*\.\d+\b|\b\d+\b|[-+]?\d+\b", newInput) # Gets all numbers

        varIndex = 1
        # For all the strings entered in the sentence, they are replaced
        # with input that the context free grammar can recognize
        for name in names:
            variableName = "variable" + str(varIndex)
            newInput = newInput.replace(name, variableName)
            varIndex = varIndex + 1

        numIndex = 1
        # For all the numbers entered in the sentence, they are replaced
        # with input that the context free grammar can recognize
        for number in numbers:
            numberName = "number" + str(numIndex)
            newInput = newInput.replace(number, numberName)
            numIndex = numIndex + 1

        # Shows what identifiers and numbers were found in the input sentence
        if explanation == True:
            if len(names) > 0: # Identifiers were in sentence
                print ("\nNames found: " + (', '.join(str(e) for e in names)).replace('"',""))
            else:
                print ("\nNo names found.")
            
            if len(numbers) > 0: # Numbers were in sentence
                print ("Numbers found: " + ', '.join(str(e) for e in numbers))
            else:
                print ("No numbers found.")

        # Puts the input sentence into lowercase for the grammar
        newInput = newInput.lower()

        # Shows the result of the replacements and lowercase
        if explanation == True:
            print ("\nSentence put into parser: " + newInput)
        sent = newInput.split()

        # successful holds if the grammar was able to be parsed
        successful = True

        # Tries to put the sentence into the parser.
        # Catches exceptions if sentence was not valid.
        try:
            # gets a list version of the parse tree
            results = list(parser.parse(sent))
            # removes the word "Tree" and brackets from results
            results = ''.join(str(e) for e in results)

            # Either shows parsing or reports success
            if explanation == True:
                print ("\nParse Of the Entered String: \n")
                print (results + "\n")
            else:
                print ("Parsing successful.\n")
        except:
            print ("Invalid sentence. Please try again.")
            print ("Check spelling and/or help and try again.")
            successful = False

        # Determines the intent of the sentence from the LHS of the
        # parsing, teaches the user of the basics of the intent,
        # asks for more information if needed, and prints resulting
        # statement in Java syntax.
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

    # Checks to see if the user would like to input another sentence.
    cont = input("\nEnter \"y\" to continue: ")
    print()

print ("\n-------------------------------------------------------------------")
print("\n\tThank you for using the natural language program.")
print ("\n-------------------------------------------------------------------")
