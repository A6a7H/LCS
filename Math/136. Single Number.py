'''
Concept

- If we take XOR of zero and some bit, it will return that bit
a xor 0 = a a⊕0=a
- If we take XOR of two same bits, it will return 0
a xor a = 0a⊕a=0
- a xor b xor a = (a xor a) xor b = 0 xor b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
So we can XOR all bits together to find the unique number.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res