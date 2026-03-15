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
Operator → pop >= precedence
Example : Infix : A+B * (C-D)/E
Postfix result: ABCD-*E/+
Reason                             |    Stack        | Output     |
A is an operand push to output     |                 |   A        | 
+ is an operator push to stack     |      +          |   A        |
B is an operand push to output     |      +          |   AB       |
* is an operator but check the     |                 |            |
precedence if(*>=+)then push else  |                 |            |
pop the existing operator which    |                 |   AB       |
would have higher precedence       |                 |            |
class infix_to_postfix:            |                 |            |
                                   |       +*        |    AB      |
( parentheses push to stack        |     +*(         |    AB      |                                 
C is operand push to output        |   +*(           |    ABC     |
- is operator push to stack        |   +*(-          |    ABC     |
D is operand push to output        |    +*(-         |    ABCD    |
) close parenthese encounter       |                 |    ABCD    |
pop all elements enclosed in ()    |    +*(-)        |    ABCD    |
popped(-)                          |    +*           | ABCD-      |
/ check precedenc if (existing     |   +*            | ABCD-      |
operand of stack)*>=/(new operand) |   +*            |            |
this is false then pop the * first |   +             | ABCD-*     |
Now push the / to stack            |   +/            | ABCD-*     |
E  push to output                  |    +/           | ABCD-*     |
Pop all stack elements             |                 | ABCD-*/+   |
                               '''

def convert_infix_to_postfix(arr):
    stack = []
    output = []
    operands = ['+','-','*','/']
    brackets = ['(',')']
    for i in arr:
        if(i not in operands):
            output.append(i)
        #check of precedence
        elif(i in operands):
            if(len(stack)==0):
                stack.append(i)
            else:
                stack[-1]
        elif(i==')'):


        
        
    