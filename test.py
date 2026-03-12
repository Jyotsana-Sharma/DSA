# class Solution:
#     def isValid(self, s: str) -> bool:
#         l = 0 
#         r = len(s)-1
#         bracket_dict = {'(':')','[':']','{':'}'}
#         stack = []
#         for char in s:
#             if(char in bracket_dict.keys()):
#                 stack.append(char)
#             elif(char in bracket_dict.values()):
#                 if(len(stack)!=0 and stack[-1]):  

# obj = Solution()
# s = "[]"
# op = obj.isValid(s)
# print(op)
fn = './config.txt'
def file_read(fn):
    with open(fn,'r') as f:

        op= f.readlines()
        print(op)
     
        for val in op:
            # val=val.replace('\n','').split('=')
        
            yield val.replace('\n','').split('=')

file_read(fn)

        
    # print(dict)