'''
given string find max length with 1 and u mast make 1 delete operation
'''
class Solution:

	def max_length(arr):
		cur_len = 0
		previus_group = -1
		current_group = -1
		zero_count = 0
		slow = fast = 0
		while slow < len(arr):
			while slow < len(arr) and arr[slow] == 0:
				slow += 1
			fast = slow
			while fast < len(arr) and arr[fast] == 1:
				fast += 1
