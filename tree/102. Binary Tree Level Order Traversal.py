'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            nodes = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                nodes.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(nodes)   
        return res
