# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []
        def findPath(root, search,path):
            if root == None:
                return None
            path.append(root)
            if root == search:
                return True
            if(findPath(root.left, search, path) or findPath(root.right,search,path)):
                return True
            path.pop(-1)
            return False

        lca = None
        if root == None:
            return -1
        findPath(root, p, p_path)
        findPath(root, q, q_path)
        min_len = min(len(p_path),len(q_path))
        for i in range(0,min_len):
            if p_path[i] == q_path[i]:
                lca = p_path[i]
            else:
                break
        return lca



# solution 2 
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if (root == None):
#             return None
#         maxValue = max(p.val, q.val)
#         minValue = min(p.val, q.val)
        
#         while(root):
#             if (root.val < minValue):
#                 root = root.right
#             elif (root.val > maxValue):
#                 root = root.left
#             else:
#                 return root
#         return None

# # Second solution    
# #         if (root == None):
# #             return None
# #         if (root.val == p.val) or (root.val == q.val):
# #             return root
        
# #         l = self.lowestCommonAncestor(root.left, p, q)
# #         r = self.lowestCommonAncestor(root.right, p, q)
        
# #         if(l == None and r == None):
# #             return None
        
# #         if(l != None and r != None):
# #             return root
                
# #         if(l != None):
# #             return l
# #         return r