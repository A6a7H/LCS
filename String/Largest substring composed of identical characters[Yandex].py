'''
return the length of largest substring composed of identical characters form string
'''
class Solution():
	def largeofind(self, s):
		if len(s) < 1: return 0
		if len(s) == 1: return 0
		max, cnt = 0, 1
		for i in range(1, len(s)):
			if s[i] != s[i-1]:
				max = cnt if cnt > max else max
				cnt = 0
			cnt += 1
		return max if max > cnt else cnt