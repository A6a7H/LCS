'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1]
'''
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            left = -1

        right = bisect_right(nums, target) - 1
        if right < 0 or nums[right] != target:
            right = -1

        return [left, right]

    def searchRange1(self, nums, target):
	    def binarySearchLeft(A, x):
	        left, right = 0, len(A) - 1
	        while left <= right:
	            mid = (left + right) / 2
	            if x > A[mid]: left = mid + 1
	            else: right = mid - 1
	        return left

	    def binarySearchRight(A, x):
	        left, right = 0, len(A) - 1
	        while left <= right:
	            mid = (left + right) / 2
	            if x >= A[mid]: left = mid + 1
	            else: right = mid - 1
	        return right
        
	    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
	    return (left, right) if left <= right else [-1, -1]