# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        LOlist = []
        level = [root]
        while root and level:
            sublist = []
            nextLevel = []
            for node in level:
                sublist.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            LOlist.append(sublist)
            level = nextLevel
        return LOlist