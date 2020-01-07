class Solution:
    def lemonadeChange(self, b: List[int]) -> bool:
    	counter = {5:0, 10:0, 20:0}
    	for bills in b:
    		if bills == 10:
    			if counter[5] == 0:
                    return False
    			else: 
                    counter[5] -= 1
    		elif bills == 20:
    			if counter[10] != 0 and counter[5] != 0:
                    counter[5], counter[10] = counter[5] - 1, counter[10] - 1
    			elif counter[5] >= 3: 
                    counter[5] -= 3
    			else:
                    return False
    		counter[bills] += 1
    	return True