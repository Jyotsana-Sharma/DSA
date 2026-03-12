'''Infix to Postfix is the process of converting a mathematical expression written in infix notation (operators between operands) into postfix notation (operators after operands).
Operators are (+,-,/,*)
Infix -> operators between operands 
Postfix -> operators after operands
Prefix -> operators before operands

Example of infix to postfix are:
Infix -> A+B 
Postfix equivalent for above infix expression : AB+
Prefix equivalent for above infix experession : +AB
Example with parentheses
(A+B)*C

Whenever there is a parentheses, remeber below thumb rule:
If stack operator >= current operator
        POP
Else
        PUSH
Also when converting : 
Operand → output
Operator → stack
Another rule to memorize is push the operand ( and pop until you encounter ) 
Operands → output
( → push
) → pop until (
Operator → pop >= precedence'''



class infix_to_postfix:
    def convert_infix_to_postfix():

        
        
    