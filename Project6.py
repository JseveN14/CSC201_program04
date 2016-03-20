#Lab 4 - Project 6 Complex Expressions version 2
import re

def complexExpressionValid(string):#check if complex expression is valid
    complexMatch = re.match("^[(]\d+[*+-/]\d+[)]([*][(]\d+[*+-/]\d+[)])*$",
                              string)#1+ times, must match exactly
    if complexMatch:
        return True
    else:
        return "Invalid expression"

def simpleExpressionIsValid(string):#function to check valid simple expression
    match_simple = re.match("^(\d+)[*+-/](\d+)$", string)#^(start), $(end)
    if match_simple:#if the regex is matched in the given string
        return True
    else:
        return False

def evaluateSimpleExpression(string):#function to calculate expression
    
    if string.find("+") > -1:#if + is found
        first_number = int(string[0:string.find("+")])
        second_number = int(string[string.find("+")+1: ])
        total = first_number + second_number#add numbers
        
    if string.find("-") > -1:#if - is found
        first_number = int(string[0:string.find("-")])
        second_number = int(string[string.find("-")+1: ])
        total = first_number - second_number#subtract numbers
        
    if string.find("*") > -1:#if * is found
        first_number = int(string[0:string.find("*")])
        second_number = int(string[string.find("*")+1: ])
        total = first_number * second_number#multiply numbers
        
    if string.find("/") > -1:#if / is found
        first_number = int(string[0:string.find("/")])
        second_number = int(string[string.find("/")+1: ])
        if second_number == 0:
            return "Divide by Zero error"#n/0 is undefined
        else:
            total = first_number / second_number#otherwise, divide numbers

    return total#returns integer value

def lastExpression(string):#function for user to ask for last expressions
    match_last = re.match("last\s(\d+)$", string)#user types: 'last #'
    if match_last:
        return match_last.group(1)#group(1) in regex is (\d+) (number)
    else:
        return False

memory_bank = []
expr = None
while expr != "end":
    expr = input("Enter a complex expression: ")
    if expr != "end":
        expr_last = lastExpression(expr)# number in 'last #'
        if expr == "last":#if user only types 'last'
            if memory_bank == []:#empty memory bank condition
                print("There are no previous expressions to display")
            else:
                print(memory_bank)#prints full memory bank
            
        elif expr_last:#if expr_last has a value
            number_last = int(expr_last)#make integer
            if memory_bank == []:#empty memory bank condition
                print("There are no previous expressions to display")
            else:
                print(memory_bank[0:number_last])#index memory bank to desired #
        else:
            isComplexValid = complexExpressionValid(expr)#check if expr is valid
            if isComplexValid == True:#if expr is valid
                #findall makes list of all matches of regex '( # [+-*/] # )
                list_SimpleExpressions = re.findall("[(](\d+[*+-/]\d+)[)]",
                                                    expr)
                term_bank = []#to store evaluated expressions
                isValid = False#to check equality
                for term in list_SimpleExpressions:
                #as loop iterates, visits 'term'
                    evaluate = evaluateSimpleExpression(term)#evaluate 'term'
                    if evaluate == "Divide by Zero error":#if term is undefined
                        print("Invalid expression. One of your terms is "
                              "undefined")
                        isValid = False#reassign
                        break#exit for loop now
                    else:#if no calculation error
                        term_bank.append(evaluate)#add 'evaluate' to term bank
                        isValid = True#reassign
                #this block does not occur if divide by 0 error    
                if isValid == True:
                    product = 1#identity propery in math
                    for term_total in term_bank:#each totalled term in bank
                        product *= term_total
                        #first iteration: 1 x 1st term = product
                        #all other iterations: product = term x product
                    entry = str(expr) + " = " + str(product)#concatenate strings
                    print(entry)#print answer
                    memory_bank.insert(0, entry)
                    #insert equation into memory bank
            else:
                print(isComplexValid)
