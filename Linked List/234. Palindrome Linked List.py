'''
Given a singly linked list, determine if it is a palindrome.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        while node and head:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
        return True
        