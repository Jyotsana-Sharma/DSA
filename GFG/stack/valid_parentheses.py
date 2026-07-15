class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'[':']','(':')','{':'}'}
        #creating an empty stack to store the open braces only 

        stack = []
        for char in s:
            if(char in open_to_close):
                #push operation for the open braces
                stack.append(char)
            else:
                if(stack and (open_to_close[stack[-1]]==char) ):
                    #pop operation for the closed braces
                    stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False
obj = Solution()
s = "[{()}]"
bool_val = obj.isValid(s)
print(bool_val)
        