# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        i = 0
        while(l1 != None):
            a = a + (l1.val* (10 ** i))
            l1 = l1.next
            i = i+1
            
        b = 0
        i = 0
        while(l2 != None):
            b = b + (l2.val * (10 ** i))
            l2 = l2.next
            i = i + 1
        c = a + b
        print(c)
        
        finalNode = ListNode(c % 10)
        Node = finalNode
        c = c // 10
        while (c != 0):
            Node.next = ListNode(c % 10)
            Node = Node.next
            c = c // 10
            
        return finalNode