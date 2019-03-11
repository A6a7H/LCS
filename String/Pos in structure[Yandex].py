'''
function's input is string and output is posation in "array"(the structure in class can be not a array)
such as:
cls = Solution()
cls.pos('aaaaaa') -> 0
cls.pos('cccccc') -> 1
cls.pos('bbbbbb') -> 1
explain:
['aaaaaa', 'bbbbbb', 'cccccc']
'''
class Solution():
	def pos(s):
		self.l = []
		pos = 0
		if not self.l:
			self.l.append(s)
		for i in range(len(self.l)-1):
			if self.l[i] < s and self.l[i+1] > s:
				pos = i
