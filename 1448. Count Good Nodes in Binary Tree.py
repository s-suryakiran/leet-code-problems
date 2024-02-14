# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodnodes = 0
        def helper(node, maxparent):
            nonlocal goodnodes
            if node == None:
                return None
            if maxparent == None:
                goodnodes += 1
                maxparent = node
            else:
                if maxparent.val <= node.val:
                    goodnodes += 1
                    maxparent = node
            
            helper(node.left, maxparent)
            helper(node.right, maxparent)
        
        helper(root, None)
        return goodnodes

            
            