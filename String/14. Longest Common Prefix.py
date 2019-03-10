'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) < 1: return ''
        elif len(strs) == 1: 
            return strs[0]
        s = strs[0]
        for i in range(1, len(strs)):
            left = min(len(s), len(strs[i]))
            while strs[i][:left] != s[:left]: 
                left -= 1
            s = s[:left]
        return s

class Solution:
    def longestCommonPrefix2(self, m):
        if not m: return ''
        s1 = min(m)
        s2 = max(m)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1