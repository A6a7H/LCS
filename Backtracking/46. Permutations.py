class Solution(object):
    def permute(self, nums):
        res = []
        self.permute_req(nums,[],res)
        return(res)
        
    def permute_req(self,nums,cur,res):
        if (len(nums) == 0):
            res.append(cur)
            return
        for i in range(len(nums)):
            nums[0],nums[i] = nums[i],nums[0]
            self.permute_req(nums[1:], cur+[nums[0]], res)