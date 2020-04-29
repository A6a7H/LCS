def findTriplet(a1, a2, a3,  
                n1, n2, n3, sum): 
    s = set() 
 
    a1.sort()
    a2.sort()
    a3.sort()
    
    for i in range(n1): 
        l = 0
        r = n3 - 1
        while l < n2 and r >= 0:
            print(a1[i], a2[l], a3[r], l, r)
            if a1[i] + a2[l] + a3[r] == sum:
                return True
            elif a1[i] + a2[l] + a3[r] < sum:
                l += 1
            elif a1[i] + a2[l] + a3[r] > sum:
                r -= 1
    return False
  
# Driver code 
a1 = [1, 2, 3, 4, 5] 
a2 = [2, 3, 6, 1, 2] 
a3 = [3, 24, 5, 6] 
n1 = len(a1) 
n2 = len(a2) 
n3 = len(a3) 
sum = 14
if findTriplet(a1, a2, a3,  
               n1, n2, n3, sum) == True: 
    print("Yes") 
else: 
    print("No") 