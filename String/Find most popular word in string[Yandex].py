'''
Find most popular ward in string
'''
import collections
class Solution():
	def most_popular(self, s):
		dict = collections.Counter()
		mas = s.split()
		for ch in mas:
			dict[ch] += 1
		if not mas:
			raise ValueError("gg wp")
		max, ans = 0, ''
		for ch in dict:
			if dict[ch] > max:
				max = dict[ch]
				ans = ch
		return ans