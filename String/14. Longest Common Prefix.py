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

class Solution1:
    def longestCommonPrefix2(self, m):
        if not m: return ''
        word1 = min(m)
        word2 = max(m)

        count = 0
        for i in range(min(len(word2), len(word1))):
            if word1[i] == word2[i]:
                count += 1

        return word1[:count]

s = Solution1()
a = [
  "abcdefgh",
  "aefghijk",
  "cbcefgh"
]
print(s.longestCommonPrefix2(a))