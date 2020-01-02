class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum = nums.copy()
        if len(nums) > 1:
            maxSum[1] = max(maxSum[0], nums[1])
        for i in range(2, len(nums)):
            maxSum[i] = max(nums[i] + maxSum[i-2], maxSum[i-1])
        return maxSum[-1]