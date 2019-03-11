class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    	def dfs(candidates, path, res, target):
    		if sum(path) > target:
    			return
    		if sum(path) == target:
    			res += [path]
    			return
    		for i in range(len(candidates)):
    			dfs(candidates[i:], path+[candidates[i]], res, target)
    	ans = []
    	dfs(candidates, [], ans, target)
    	return ans
    
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
    	def dfs(candidates, path, res, index, target):
    		if sum(path) > target:
    			return
    		if sum(path) == target:
    			res += [path]
    			return
    		for i in range(index, len(candidates)):
    			dfs(candidates, path+[candidates[i]], res, i, target)
    	ans = []
    	dfs(candidates, [], ans, 0,  target)
    	return ans
        