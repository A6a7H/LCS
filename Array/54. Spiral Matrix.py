'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
'''

class Solution:
    def spiralOrder(self, matrix):
        result = [] 
        if not matrix:
            return matrix
            
        l = 0
        r = len(matrix[0]) -1
        t = 0
        b = len(matrix) - 1

        while l <= r  and t <= b:
            for i in range(l, r+1):
                result.append(matrix[l][i])
            t += 1
            for i in range(t, b+1):
                result.append(matrix[i][r])
            r -= 1  
            if t <= b:
                for i in range(r, l-1, -1):
                    result.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, t-1, -1):
                    result.append(matrix[i][l])
                l += 1
        return result
        