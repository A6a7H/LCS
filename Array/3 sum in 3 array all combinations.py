# a, b, c       x
# количество (i,j,k) : a[i] + b[j] + c[k] == x
# O(N^2) - T
# O(1) - M
# a, b, c - можно менять

def findTriplet(a, b, c, x):
    a.sort()
    b.sort()
    c.sort()
    
    count = 0
    for i in range(len(a)):
        l = 0
        r = len(c) - 1
        while l < len(b) and r >= 0:
            if a[i] + b[l] + c[r] == x:
                count_c = count_b = 0
                while l < len(b) - 1 and b[l] == b[l + 1]:
                    count_b += 1
                    l += 1
                while r > 0 and c[r] == b[r - 1]:
                    count_c += 1
                    r -= 1
                count += (count_b + 1) * (count_c + 1)
                r -= 1
                l += 1
            elif a[i] + b[l] + c[r] < x:
                l += 1
            elif a[i] + b[l] + c[r] > x:
                r -= 1
    return count