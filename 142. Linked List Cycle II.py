# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = []
        tempHead = head
        pos = 0
        
        if head == None or head.next == None:
            return None
        
        while (tempHead != None):
            if tempHead in visited:
                pos = 1
                return tempHead
            
            visited.append(tempHead)
            tempHead = tempHead.next
        
        if pos == 0:
            return None
        