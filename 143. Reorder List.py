# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        temphead = head
        fastptr = head
        if head == None or head.next == None:
            return head
        while(fastptr and fastptr.next):
            fastptr = fastptr.next.next
            temphead = temphead.next

        while(temphead):
            stack.append(temphead)
            temphead = temphead.next

        temphead = head
        while(stack):
            tempnext = temphead.next
            temphead.next = stack.pop()
            temphead.next.next = tempnext
            temphead = temphead.next.next
        temphead.next = None
        return head