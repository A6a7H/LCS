'''
#include <stdio.h>

Function to find the maximum sequence of continuous 1's by replacing/deleting
atmost k 0's by 1 using sliding window technique
'''
class Solution:

    def max_length_replace(salf, arr):
        res = 0
        left = right = 0
        count = 0
        while right < len(arr):
            if arr[right] == 0:
                count += 1
            while count > 1: # can put k
                if arr[left] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

    #delete 
    def max_length_delete(salf, arr):
            res = 0
            left = right = 0
            count = 0
            while right < len(arr):
                if arr[right] == 0:
                    count += 1
                while count > 1: # can put k
                    if arr[left] == 0:
                        count -= 1
                    left += 1
                res = max(res, right - left + 1 - count)
                right += 1
            return res

    #delete worst
    def max_length(salf, arr):
            previus_group = -1
            current_group = -1
            zero_count = 0
            res = 0
            slow = fast = 0
            while slow < len(arr):
                while slow < len(arr) and arr[slow] == 0:
                    slow += 1
                fast = slow
                while fast < len(arr) and arr[fast] == 1:
                    fast += 1
                current_group = fast - slow
                slow = fast
                while slow < len(arr) and arr[slow] == 0:
                    slow += 1
                    zero_count += 1
                fast = slow
                if zero_count == 1:
                    while fast < len(arr) and arr[fast] == 1:
                        fast += 1
                    previus_group = current_group
                    current_group = fast - slow
                    res = max(res, current_group + previus_group)
                else:
                    res = max(res, current_group)
                zero_count = 0
            return res


a = Solution()
print(a.max_length([]))