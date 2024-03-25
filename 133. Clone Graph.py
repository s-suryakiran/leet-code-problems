"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        oldNewMap = {}

        def dfs(node):
            if node in oldNewMap:
                return oldNewMap[node]
            
            copy = Node(node.val)
            oldNewMap[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)
        