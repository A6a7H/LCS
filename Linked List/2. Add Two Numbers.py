'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        ret = cur = ListNode(0)
        div = 0
        
        while l1 or l2 or div:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + div
            div = val // 10
            cur.next = ListNode(val % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return ret.next
            
        