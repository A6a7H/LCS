'''
Given a 32 bit number x, reverse its binary form and print the answer in decimal.
Input:
The first line of input consists T denoting the number of test cases. T testcases follow. Each test case contains a single 32 bit integer
Output:
For each test case, in a new line, print the reverse of integer.
'''
class Solution:

	def convert2(self, num):
		s = ''
		while num > 0:
			s += str(num % 2)
			num //= 2
		return s[::-1]

	def convert10(self, num):
		res = 0
		s = 0
		num = num[::-1]
		for digit in num:
			res += int(digit) * 2**s
			s += 1
		return res

	def reverse_biats(self, num):
		new_num = self.convert2(num)
		seme_res = [0]*32
		for i in range(len(new_num)):
			seme_res[31 - i] = new_num[len(new_num) - i - 1]
		return(self.convert10(seme_res[::-1]))
