'''
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

1. Insert a character into s to get t
2. Delete a character from s to get t
3. Replace a character of s to get t
'''
class Solution(object):
    def isOneEditDistance(self, s, t):
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        
        found_inequality = False
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if found_inequality:
                    return False
                found_inequality = True
                if len(s) < len(t): 
                    i -= 1
                elif len(s) > len(t): 
                    j -= 1
            i += 1
            j += 1
        
        return True