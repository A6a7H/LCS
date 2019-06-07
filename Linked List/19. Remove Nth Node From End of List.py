class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = head
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            pre = pre.next if slow != head else pre
            slow = slow.next
        if slow == head:
            head = pre.next
        else:
            pre.next = slow.next
        return head
