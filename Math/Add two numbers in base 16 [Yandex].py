'''
Add to nums in base 16
'''

class Solution1():

	def conv2_16(self, a):
		if (a >= '0' and a <= '9'):
			return int(a)
		if (a >= 'A' and a <= 'F'):
			return 10 + ord(a) - ord('A')


	def conv_from_16(self, a):
		if (a >= 0 and a <= 9):
			return str(a)
		if (a >= 10 and a <= 15):
			return chr(ord('A') + a - 10)


	def add(self, a, b):
		res = []
		res_str = ''
		conv = 0
		if (len(a) > len(b)):
			b , a = a, b
		s = ''
		for i in range(len(b) - len(a)):
		    s += '0'
		a = s + a
		for i in range(len(a)-1, -1, -1):
			num_a = self.conv2_16(a[i])
			num_b = self.conv2_16(b[i])
			res.append((num_a + num_b + conv) % 16)
			conv = (num_a + num_b + conv) // 16
		for i in range(len(a) + (len(b) - len(a)), len(b)):
			num_b = self.conv2_16(b[i])
			res.append((num_b + conv) % 16)
			conv = (num_b + conv) // 16
		if conv != 0:
			res.append(conv)
		for i in range(len(res)):
			res_str += self.conv_from_16(res[i])
		return res_str[::-1]

cls = Solution1()
a = "A15"
b = "F"
print(cls.add(a,b))