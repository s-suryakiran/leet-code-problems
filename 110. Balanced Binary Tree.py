# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
        if node == None:
            return 0
        return 1+ max(self.height(node.left), self.height(node.right))
    
    def isBalanced(self, node: Optional[TreeNode]) -> bool:
        if node == None:
            return True
        
        rh = self.height(node.right)
        lh = self.height(node.left)
        
        if (abs(lh-rh)<=1) and self.isBalanced(node.left) and self.isBalanced(node.right):
            return True
        
        return False