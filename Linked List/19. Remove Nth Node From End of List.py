class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        for i in range(n - 1):
            head = head.next
        while head.next:
            first, head = first.next, head.next
        first.next = first.next.next
        return dummy.next
