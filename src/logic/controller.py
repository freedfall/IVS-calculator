import eel
import re 
from expression_parser import Analyser

analyser =  Analyser()

@eel.expose
def calculate(expr, mode):
    if mode:
        expr = convertBinaryToDecimal(expr)

    result = analyser.analyse(expr)
    analyser.reinitialize_stack()
    return result

def convertBinaryToDecimal(expression):
        # Remove spaces to avoid confusion in processing
    expression = expression.replace(" ", "")
    
    # Regex to find binary numbers next to operators or at the start/end of the string
    binary_pattern = r"(?:(?<=^)|(?<=[+\-*/()=%!]))[01]+(?=[+\-*/()=%!]|$)"
    
    # List to hold parts of the new expression
    new_expression_parts = []
    last_index = 0
    
    # Iterate over each match
    for match in re.finditer(binary_pattern, expression):
        # Binary value found by regex
        binary_value = match.group()
        # Convert binary string to a decimal integer
        decimal_value = int(binary_value, 2)
        
        # Append the text before the binary number and the decimal value itself
        new_expression_parts.append(expression[last_index:match.start()])
        new_expression_parts.append(str(decimal_value))
        last_index = match.end()
    
    # Append the remaining part of the expression after the last match
    new_expression_parts.append(expression[last_index:])

    return "".join(new_expression_parts)