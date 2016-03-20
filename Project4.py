#Lab 4 - Project 4 Memory Capabilities
import re

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

memory_bank = []#stores valid calculated expressions
expr = None#to start while loop
while expr != "end":#if user types 'end' while loop quits, program ends
    expr = input("Enter an expression: ")#user input
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
    
    elif expr != "end":
        isValid = simpleExpressionIsValid(expr)#check if expr is valid
        if isValid == True:#if expr is valid
            evaluate = evaluateSimpleExpression(expr)#calculate given expr
            if evaluate == "Divide by Zero error":#if n/0, restart while loop
                print("Invalid expression. This expression is undefined.")
            else:#if no calculation error
                total = str(evaluate)#int converted to string
                entry = expr + " = " + total#concatenate strings
                print(entry)#print string
                memory_bank.insert(0, entry)#insert complete equation in list
                #comment line below to make 'infinite' memory bank
                memory_bank = memory_bank[:5]
                #memory bank is infinite, only displays 5 indexes
        else:#if expr not valid
            print(isValid)
