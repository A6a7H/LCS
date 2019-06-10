'''
Find one digit without pare in given sorted array(all digits in this array have pairs except one)
'''
class Solution:
    def find_one_unique_digit(self, data):
        l = 0
        r = len(data) -1
        while l < r:
            m = (l+r) // 2
            if data[m] != data[m+1] and data[m] != data[m-1]:
                return data[m]
            elif data[m] == data[m+1]:
                if len(data[m+2:]) % 2 == 0:
                    r = m
                else:
                    l = m + 2

            elif data[m] == data[m-1]:
                if len(data[m+1:]) % 2 == 0:
                    r = m - 1
                else:
                    l = m + 1

data = [0, 1, 1, 2, 2, 3, 3, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
slt = Solution()
print(slt.find_one_unique_digit(data))

