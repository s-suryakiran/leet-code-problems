# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(list1 == None): 
            return list2
        
        if(list2 == None):
            return list1
 
        sortedNode = ListNode()
        
        if(list1.val>list2.val):
            sortedNode.val = list2.val
            list2 = list2.next
        
        else:
            sortedNode.val = list1.val
            list1 = list1.next
            
        endNode = sortedNode
        while (list1 != None and list2!=None):
            # print(list1.val)
            # print(list2.val)
            # print(sortedNode)
            
            currNode = ListNode()
            
            if(list1.val < list2.val):
                currNode.val = list1.val 
                list1 = list1.next
                endNode.next = currNode
                endNode = endNode.next
                
            elif(list1.val > list2.val):
                currNode.val = list2.val
                list2 = list2.next
                endNode.next = currNode
                endNode = endNode.next
                 
                
            else:
                currNode.val = list1.val 
                list1 = list1.next
                endNode.next = currNode
                endNode = endNode.next
                
                currNode = ListNode()
                currNode.val = list2.val
                list2 = list2.next
                endNode.next = currNode
                endNode = endNode.next
                
        if(list1!=None):
            endNode.next = list1
        if(list2!=None):
            endNode.next = list2
            
        return sortedNode
                
