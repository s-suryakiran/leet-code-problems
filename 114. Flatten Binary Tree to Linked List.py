# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    l = []
    def preorder(self, root):
        if root == None:
            return
        self.l.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return 
        self.l = []
        tempRoot = root
        self.preorder(tempRoot)
        root.val = self.l[0]
        root.left = None
        tempnewRoot = root
        self.l.pop(0)
        for i in self.l:
            newNode = TreeNode(i)
            tempnewRoot.right = newNode
            tempnewRoot.left = None
            tempnewRoot = tempnewRoot.right
        
        
        
         
                
            
            
        