# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if (left == right):
            return head
        tempHead = head
        i = 1
        tempLeft = ListNode()
        tempRight = ListNode()
        prevTempFinalList = ListNode()
        finalNode = ListNode()
        checkNode = ListNode()
        
        while (tempHead != None):
            
            if i < left:
                tempLeft = tempHead
            
            elif i > right:
                tempLeft.next = prevTempFinalList
                tempRight = tempHead
                finalNode.next = tempRight
                break
            
            elif (i >= left) and (i <= right):
                newNode = ListNode(tempHead.val, prevTempFinalList)
                prevTempFinalList = newNode
                if i == left:
                    finalNode = newNode
                
            i = i + 1
            checkNode = tempHead
            tempHead = tempHead.next

        if (left == 1) and (checkNode.next == None):
            finalNode.next = None
            return prevTempFinalList
            
        if (left == 1):
            finalNode.next = tempRight
            return prevTempFinalList
            
            
        if (checkNode.next == None):
            finalNode.next = None
            tempLeft.next = prevTempFinalList
            return head
         
        return head