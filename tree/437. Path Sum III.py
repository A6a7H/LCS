# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        if (root == None):
            return 0;
        return self.numPathStartingAtNode(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    def numPathStartingAtNode(self, root, sum):
        if(root == None):
            return 0
        return (1 if root.val == sum else 0) + self.numPathStartingAtNode(root.left, sum - root.val) + self.numPathStartingAtNode(root.right, sum - root.val)