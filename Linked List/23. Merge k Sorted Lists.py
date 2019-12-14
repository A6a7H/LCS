# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq 

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        my_heap = []
        heapq.heapify(my_heap)
        for idx, head in enumerate(lists):
            if not head:
                continue
            heapq.heappush(my_heap, (head.val, idx, head))
        
        fake_head = ListNode(None)
        cur = fake_head
        while my_heap:
            nxt_val, idx, cur.next = heapq.heappop(my_heap)
            if cur.next.next:
                heapq.heappush(my_heap, (cur.next.next.val, idx, cur.next.next))
            cur = cur.next
        return fake_head.next