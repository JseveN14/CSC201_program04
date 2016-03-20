import re

def complexExpressionValid(string):#function checks if complex expression valid
    match_complex = re.match("^[(]\d+[*+-/]\d+[)][*][(]\d+[*+-/]\d+[)][*][(]"
                             "\d+[*+-/]\d+[)]$", string)#3 terms
    if match_complex:#if exact match
        return True
    else:#if not exact match
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

memory_bank = []#stores valid calculated expressions    
expr = None#to start while loop
while expr != "end":#if user types 'end' while loop quits, program ends    
    expr = input("Enter a complex expression: ")#user input
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
        isComplexValid = complexExpressionValid(expr)#check if expr is valid
        if isComplexValid == True:#if expr is valid
            list_SimpleExpressions = re.findall("[(](\d+[*+-/]\d+)[)]", expr)
            #findall makes list of all matches of regex '( # [+-*/] # )
            term_bank = []#to store evaluated expressions
            isValid = False#to check equality
            for term in list_SimpleExpressions:#as loop iterates, visits 'term'
                evaluate = evaluateSimpleExpression(term)#evaluate 'term'
                if evaluate == "Divide by Zero error":#if term is undefined
                    print("Invalid expression. One of your terms is undefined.")
                    isValid = False#reassign
                    break#exit for loop now
                else:#if no calculation error
                    term_bank.append(evaluate)#add 'evaluate' to term bank
                    isValid = True#reassign
                
            if isValid == True:#this block does not occur if divide by 0 error
                product = 1#identity propery in math
                for term_total in term_bank:#each totalled term in bank
                    product *= term_total#first iteration: 1 x 1st term = product
                    #all other iterations: product = term x product
                entry = str(expr) + " = " + str(product)#concatenate strings
                print(entry)#print answer
                memory_bank.insert(0, entry)#insert equation into memory bank         
        else:#if expr is not valid
            print(isComplexValid)
