class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        unique = set()
        res = 0
        while right < len(s):
            if s[right] in unique:
                unique.remove(s[left])
                left += 1
            else:
                unique.add(s[right])
                right += 1
                res = max(res, right - left)
        return res