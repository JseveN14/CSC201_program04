#Lab 4 - Project 1 Validate Simple Expression
import re

def simpleExpressionIsValid(string): #function to check valid simple expression
    match_simple = re.match("^(\d+)[*+-/](\d+)$", string)#^(start), $(end)
    if match_simple: #if the regex is matched in the given string
        return True
    else:
        return False
