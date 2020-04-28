class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = left = 0
        unique = set()
        maximum = 0
        currmax = 0
        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                maximum = max(len(unique), maximum)
                right += 1
            else: # move left while right become unique
                unique.remove(s[left])
                left += 1
        return maximum