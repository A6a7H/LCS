class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prev_left, prev_right = 1, 1
        for i in range(1, len(nums)):
            prev_left *= nums[i - 1]
            prev_right *= nums[len(nums) - i]
            output[i] *= prev_left
            output[len(nums) - i - 1] *= prev_right
        return output