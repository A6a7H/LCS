'''
Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.
'''

class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        def dfs(path, ind, res, A):
            letter = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno',
                                    '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
            if len(path) == len(digits):
                res += [path]
                return 
            for i in range(ind, len(A)):
                for ch in letter[A[i]]:
                    dfs(path+ch, i+1, res, A)
        ans = []
        if not digits:
            return []
        dfs('', 0, ans, digits)
        return ans
