
class Solution:
    def evalRPN(self, tokens):

        stack = []
        for num_token in tokens:
            if(num_token=='+'):
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif(num_token=='*'):
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif(num_token=='/'):
                a,b = stack.pop(),stack.pop()
                stack.append(int((b/a)))
            elif(num_token=='-'):
                a,b = stack.pop(),stack.pop()
                stack.append(int(b-a))
            else:
                stack.append(int(num_token))

        return stack[0]
# class Solution:
#     def evalRPN(self, tokens) -> int:
#         stack = []
#         for c in tokens:
#             if c == "+":
#                 stack.append(stack.pop() + stack.pop())
#             elif c == "-":
#                 a, b = stack.pop(), stack.pop()
#                 stack.append(b - a)
#             elif c == "*":
#                 stack.append(stack.pop() * stack.pop())
#             elif c == "/":
#                 a, b = stack.pop(), stack.pop()
#                 stack.append(int(float(b) / a))
#             else:
#                 stack.append(int(c))
#         return stack[0]


obj = Solution()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens=["4","13","5","/","+"]
res = obj.evalRPN(tokens)
print(res)