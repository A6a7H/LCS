# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for list in lists:
            while(list):
                heap.append(list.val)
                list = list.next
        
        heapq.heapify(heap)
        preHead = ListNode(0)
        tmp = preHead
        while heap:
            tmp.next = ListNode(heapq.heappop(heap))
            tmp = tmp.next
        
        return preHead.next
