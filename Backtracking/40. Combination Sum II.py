'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.bfs(res, candidates, [], 0, target)
        return res
    
    def bfs(self, res, candidates, path, index, target):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            if (i > index and candidates[i] == candidates[i - 1]): continue
            self.bfs(res, candidates, path+[candidates[i]], i + 1, target - candidates[i])