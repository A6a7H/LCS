'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.
'''
class Solution:
    def divide(self, dividend, divisor):
        f = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            f = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        l = 0
        r = max(divisor,dividend) + 1
        res = 0
        while (l <= r):
            m = int((l + r) / 2)
            if (m*divisor <= dividend and (m+1)*divisor > dividend):
                res = m
                break
            if (m*divisor > dividend):
                r = m
            if (m*divisor < dividend):
                l = m
        if f:
            res = res*(-1)
        return min(max(-2147483648, res), 2147483647)