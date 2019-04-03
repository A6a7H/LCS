'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
Input: 1->1->2
Output: 1->2
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        val = None
        res = ListNode(-1)
        ans = res
        while (head):
            if (head.val != val):
                val = head.val
                res.next = ListNode(val)
                res = res.next
            head = head.next
            
        return ans.next
    
    def deleteDuplicates_better(self, head):
        first, second = head, head.next if head else None
        while second:
            if first.val == second.val:
                second = second.next
                first.next = second
            else:
                first = second
                second = second.next
                
        return head
                
        