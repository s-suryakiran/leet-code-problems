# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        x = ""
        while(temp != None):
            x= x+str(temp.val)
            temp = temp.next

        xr = x[::-1]
        if xr == x:
            return True
        else:
            return False