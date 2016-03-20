#Lab 4 - Project 3 Activate User Input
import re

def simpleExpressionIsValid(string):#function to check if valid expression
    match_simple = re.match("^(\d+)[+-/*](\d+)$", string)#(\d+) multiple digits
    if match_simple:
        return True
    else:
        return "Invalid expression"
    
def evaluateSimpleExpression(string):#calculate expression
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

    return total

expr = None
while expr != "end":#"end" will exit while loop and stop program
    expr = input("Enter an expression: ")#user input
    if expr != "end":
        isValid = simpleExpressionIsValid(expr)#expr/input verified
        if isValid == True:#if expr is valid
            evaluate = evaluateSimpleExpression(expr)#expr evaluated/calculated
            if evaluate == "Divide by Zero error":#ends if block, restart loop
                print("Invalid expression. This expression is undefined.")
            else:#if no division error
                print(expr, "=", evaluate)
        else:#if input is invalid
            print(isValid)
