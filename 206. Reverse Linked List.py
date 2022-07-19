# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        temphead = head.next
        reverseNode = ListNode(head.val)
        
        while(temphead!=None):
            newHead = ListNode()
            newHead.next = reverseNode
            newHead.val = temphead.val
            reverseNode = newHead
            # print(reverseNode)
            temphead = temphead.next

        return reverseNode
