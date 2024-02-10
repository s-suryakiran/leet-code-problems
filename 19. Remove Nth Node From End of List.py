# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temphead=head
        ct=0
        while(temphead):
            ct+=1
            temphead=temphead.next
        pos=ct-n+1
        temphead = head
        ct = 0
        if pos == 1:
            return head.next
        while(temphead):
            ct+=1
            if(ct==pos):
                prev.next=temphead.next if temphead else None
                return head
            prev=temphead
            temphead=   .next

        