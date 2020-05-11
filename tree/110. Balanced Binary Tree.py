'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
	def isBalamced(self, root):

		def Maxdeth(root):
			if not root:
				return 0
			return max(Maxdeth(root.left), Maxdeth(root.right)) + 1
		if not root:
			return True
		return abs(Maxdeth(root.left) - Maxdeth(root.right)) < 2 and self.isBalamced(root.left) and self.isBalamced(root.right)
