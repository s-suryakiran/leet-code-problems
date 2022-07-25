# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    q = []
    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.inorder(root.left)
        self.q.append(root.val)
        self.inorder(root.right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if (root == None) or ((root.left == None) and (root.right == None)):
            return True
        self.q = []
        self.inorder(root)
        size = len(self.q)
        for i in range(1,size):
            if(self.q[i-1] >= self.q[i]):
                return False
            
        return True