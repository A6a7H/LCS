class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_f = [1]
        arr_b = [1]
        output = []
        for i in range(len(nums)-1):
            arr_f.append(arr_f[-1]*nums[i])
        for i in range(len(nums)-1, 0, -1):
            arr_b.append(arr_b[-1]*nums[i])
        for i in range(len(arr_b)):
            output.append(arr_f[i]*arr_b[len(arr_b)-1-i])
        return output
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for i in range(len(nums)-1):
            output.append(output[-1]*nums[i])
        r = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= r
            r *= nums[i]
        return output
