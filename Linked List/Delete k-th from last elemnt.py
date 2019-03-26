'''
Given a singly linked list and an integer k, remove k-th node from last.
k is guaranteed to be smaller than the length of the list.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
	def del_node(self, head, k):
		if not head:
			return None
		last = head
		for i in range(k):
			last = last.next
		k_delete = head
		before_k = None
		while last:
			before_k = k_delete
			k_delete = k_delete.next
			last = last.next
		before_k.next = k_delete.next
		return head