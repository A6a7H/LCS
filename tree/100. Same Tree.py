'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        stack1 = [p]
        stack2 = [q]
        while stack1 or stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not node1 and node2:
                return False
            if node1 and not node2:
                return False
            if not node1 and not node2:
                continue
            if node1.val != node2.val:
                return False
            stack1.extend([node1.left, node1.right])
            stack2.extend([node2.left, node2.right])
        return True
                