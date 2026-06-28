'''
Prefix notation is just opposite of the postfix notation 

Easy method to convert the infix to prefix notation is below :
-> Reverese the infix expression 
-> Swap the '(' with ')'
-> Convert the expression to postfix
-> Reverse the postfix expression

Example :
Infix expression: A+B*C
Reversed the infix expression: C*B+A
Postfix expression: CB*A+
Reverse again : +A*BC

Why does prefix and postfix even exist?
They remove the parentheses and in result the ambiguity which makes them useful for the compilers and expression evaluation.
'''

def convert_infix_to_prefix(infix_expression):
    stack = []
    output = []
    


infix_expression = "a*(b+c)/d"
resultant_prefix_expression = convert_infix_to_prefix(infix_expression)         
print(f'\n resultant prefix expression : {resultant_prefix_expression}\n')