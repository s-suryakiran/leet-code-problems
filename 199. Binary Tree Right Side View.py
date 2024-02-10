# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        node = root
        level = [root]
        while node and level:
            nextlevel = []
            rightmost = None
            for node in level:
                rightmost = node.val
                if (node.left):
                    nextlevel.append(node.left)
                if(node.right):
                    nextlevel.append(node.right)

            ans.append(rightmost)
            level = nextlevel
            
        return ans
        