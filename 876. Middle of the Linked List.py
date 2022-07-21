# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        tempHead = head
        count = 0
        
        while(tempHead != None):
            count = count + 1
            tempHead = tempHead.next
        
        count = count - 1
        mid = count / 2
        # print(mid)
        count = 0
    
        while(head!=None):
            if(count >= mid):
                return head
            count = count + 1
            head = head.next
        return head