'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

class Solution:
    def check(self, ch):
        return 'a' <= ch <= 'z' or '0' <= ch <= '9'
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            while l < len(s)-1 and not self.check(s[l]):
                l += 1
            while r >= 0 and not self.check(s[r]):
                r -= 1
            if self.check(s[l]) and self.check(s[r]) and s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True