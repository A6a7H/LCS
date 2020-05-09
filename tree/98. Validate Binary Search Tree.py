'''
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        def isValid(root, left, right):
            if not root:
                return True
            return left < root.val < right and isValid(root.left, left, root.val) and isValid(root.right, root.val, right)
        return isValid(root,-float("inf"), float("inf"))

class Solution:
def isValidBST_bigger(self, root: TreeNode) -> bool:
    def helper(root, left, right):
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        if not helper(root.right, root.val, right):
            return False
        if not helper(root.left, left, root.val):
            return False
        return True

    return helper(root, float('-inf'), float('inf'))
            
        
