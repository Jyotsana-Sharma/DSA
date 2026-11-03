
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
   

    def find_max_sum(self,root):
        if root is None:
            return 0 
        
        left_path_sum = max(0,self.find_max_sum(root.left))
        right_path_sum = max(0,self.find_max_sum(root.right))

        self.maxi = max(self.maxi,left_path_sum+right_path_sum+root.val)

        return root.val+max(left_path_sum,right_path_sum)
        

    def maxPathSum(self, root) -> int:
        self.maxi = float('-inf')

        self.find_max_sum(root)
        return self.maxi


        

        