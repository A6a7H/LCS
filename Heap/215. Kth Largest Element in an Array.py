'''
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''
class Solution:

    def findKthLargest(self, nums, k) -> int:
        def siftdown(nums, i):
            while (2 * i + 1 < len(nums)):
                left = 2 * i + 1 
                right = 2 * i + 2
                j = left
                if right < len(nums) and nums[right] > nums[left] :
                    j = right
                if nums[i] >= nums[j]:
                    break
                nums[i], nums[j] = nums[j], nums[i]
                i = j
        for i in range(len(nums)//2, -1, -1):
            siftdown(nums, i)
        min = nums[0]
        for i in range(k):
            min = nums[0]
            nums[0] = nums[len(nums)-1]
            nums = nums[:len(nums)-1]
            siftdown(nums, 0)
        return min


    def findKthLargest1(self, nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
           heapq.heapreplace(heap, num)
    return heap[0]


    def findKthLargest2(self, nums, k):
    pos = self.partition(nums, 0, len(nums)-1)
    if pos > len(nums) - k:
        return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
    elif pos < len(nums) - k:
        return self.findKthLargest(nums[pos+1:], k)
    else:
        return nums[pos]
 
    # Lomuto partition scheme   
    def partition(self, nums, l, r):
        pivot = nums[r]
        lo = l 
        for i in xrange(l, r):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[r] = nums[r], nums[lo]
        return lo