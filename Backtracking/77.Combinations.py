class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def permute(result, path, index):
            if len(path) == k:
                result.append(path)
            for i in range(index, n+1):
                permute(result, path+[i], i+1)
                
        permute(result, [], 1)
        return result
