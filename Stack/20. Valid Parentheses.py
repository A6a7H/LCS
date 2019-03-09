'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c is '(' or c is '{' or c is '[':
                st.append(c)
            else:
                if not st: return False
                if c == ')' and st[-1] != '(': return False
                if c == '}' and st[-1] != '{': return False
                if c == ']' and st[-1] != '[': return False
                st.pop()
        return not st
            
        