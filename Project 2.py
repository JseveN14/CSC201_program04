#Lab 4 - Project 2 Evaluate Simple Expressions
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

    return total#integer value
