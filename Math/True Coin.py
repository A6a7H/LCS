'''
you have to check the coin, whether it is correct or not
'''
class Solution():

	def check(self, x_s, s, n = 200, a = 0.1):
		z = (x_s - 0.5) * n**0.5 / s
		if z < 1.6 and z > -1.6: 
			return True
		else: return False
