'''
Given an unsorted array of integers, find a subarray which adds to a given number. 
If there are more than one subarrays with the sum as the given number, print any of them.
'''
class Solution:
    def findsubArrwithcursum(self, arr, sum: str):
    	map, cur_sum = {}, 0
    	for i in range(len(arr)):
    		cur_sum += arr[i]
    		if cur_sum == sum:
    			return  0, i
    		if cur_sum - sum in map:
    			return map[cur_sum-sum], i
    		map[cur_sum] = i