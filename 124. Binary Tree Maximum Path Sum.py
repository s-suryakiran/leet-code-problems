# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def traverse(root):
            nonlocal res
            if root == None:
                return 0
            
            leftMax = max(traverse(root.left), 0)
            rightMax = max(traverse(root.right), 0)

            res = max(rightMax + leftMax + root.val, res)

            return root.val + max(rightMax, leftMax)
        
        traverse(root)
        return res
