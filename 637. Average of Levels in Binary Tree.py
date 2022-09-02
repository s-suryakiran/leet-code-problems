# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [] 
        res = []
        q.append(root)
        
        while(q):
            qlen = len(q)
            tmp = 0
            for i in range(qlen):  
                node = q.pop(0)
                tmp += node.val
                if node.left:   
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp/qlen)
        
        return res
        