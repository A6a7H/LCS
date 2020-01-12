class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = ''
        for i in range(int(len(s) / 2)):
            pattern += s[i]
            x = int(len(s) // len(pattern))
            if (pattern)*x == s:
                return True
        return False