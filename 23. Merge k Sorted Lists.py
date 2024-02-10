# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mini_l = ListNode(float("infinity"))
        mini_i = -1
        if len(lists) == 0:
            return None
        for i,l in enumerate(lists):
            if l and mini_l.val > l.val:
                mini_l = l
                mini_i = i
        if mini_i == -1:
            return None
        lists[mini_i] = lists[mini_i].next
        merged_List = mini_l
        while(True):
            mini_2 = ListNode(float("infinity"))
            mini_i = 0
            for i,l in enumerate(lists):
                if l != None:
                    if mini_2.val > l.val:
                        mini_2 = l
                        mini_i = i
            
            if mini_2.val == float("infinity"):
                break
            merged_List.next = mini_2
            merged_List = merged_List.next
            lists[mini_i] = lists[mini_i].next
        return mini_l


        