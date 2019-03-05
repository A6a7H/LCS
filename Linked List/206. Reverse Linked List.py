'''
Reverse a singly linked list.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList1(self, head: 'ListNode') -> 'ListNode':
        prev = None
        cur = head
        while (cur):
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt
        return prev

    def reverseList2(self, head: 'ListNode') -> 'ListNode':
        rev1 = None
        while head:
            rev1, rev1.next, head = head, rev1, head.next
        return rev1
            
            
            