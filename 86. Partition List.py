# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        left = ListNode()
        right = ListNode()
        tempLeft = left
        tempRight = right
        
        while (head != None):
            if head.val < x:
                newNode = ListNode(head.val)
                tempLeft.next = newNode
                tempLeft = tempLeft.next
                
            else:
                newNode = ListNode(head.val)
                tempRight.next = newNode
                tempRight = tempRight.next
            
            head = head.next
            
        tempLeft.next = right.next
        return left.next
            
            