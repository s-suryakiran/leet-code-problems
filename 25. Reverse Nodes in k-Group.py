# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupprev = dummy
        def getkthnode(node,k):
            while(node and k>0):
                node = node.next
                k-=1
            return node


        while(True):
            kth = getkthnode(groupprev,k)
            if not kth:
                break
            groupnext = kth.next
            prev = kth.next
            curr = groupprev.next
            while(curr != groupnext):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            tempprev = groupprev.next
            groupprev.next = kth
            groupprev = tempprev

        return dummy.next
            