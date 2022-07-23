"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:

    def preorder(self, root: 'Node', preOrderList:List = None) -> List[int]:
        if not root:
            return preOrderList
        
        if preOrderList == None:
            preOrderList = []
        
        preOrderList.append(root.val)
        for child in root.children:
            self.preorder(child,preOrderList)
            
        return preOrderList
        
# iterative
#      def preorder(self, root: 'Node') -> List[int]:
            
#             if not root:
#                 return []
            
#             if not root.children:
#                 return [root.val]
            
#             preOrderList = []
#             visitedList = []
#             stack = deque([])
#             preOrderList.append(root.val)
#             stack.append(root)
#             visitedList.append(root)
#             while(len(stack) > 0):
#                 flag = 0
                
#                 if (len(stack[len(stack) - 1].children) == 0):
#                     a = stack.pop()
                
#                 else:
#                     parent = stack[len(stack)-1]
                    
#                 for child in parent.children:
#                     if child not in visitedList:
#                         visitedList.append(child)
#                         preOrderList.append(child.val)
#                         stack.append(child)
#                         flag = 1
#                         break
                        
#                 if flag == 0:
#                     stack.pop()
                    
#             return preOrderList