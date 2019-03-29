'''
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie. Each child i has a greed factor gi, 
which is the minimum size of a cookie that the child will be content with; and each cookie j 
has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will 
be content. Your goal is to maximize the number of your content children and output the maximum number.
'''
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        res = 0
        i = 0
        for si in s:
            if i == len(g):
                break
            if si >= g[i]:
                res += 1
                i += 1
        return res