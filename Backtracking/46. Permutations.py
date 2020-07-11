def permute(self, nums: List[int]) -> List[List[int]]:
    result = []
    self.backtrack(nums, [], result)
    return result

def backtrack(self, nums, currentPermutation, result):
    if not nums:
        result.append(currentPermutation)
        return
    for i in range(len(nums)):
        self.backtrack(nums[:i] + nums[i+1:], currentPermutation + [nums[i]], result)
