# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def helper(root, left_flag):
            if not root.left and not root.right and left_flag:
                self.total += root.val
            if root.left:
                helper(root.left, True)
            if root.right:
                helper(root.right, False)
            return self.total
                
        if not root:
            return 0
        
        self.total = 0
        return helper(root, False)



    def sumOfLeftLeaves_(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left :
            if not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)

    ans = 0
    def sumOfLeftLeaves_3(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if left:
                self.ans += left
        dfs(root)
        return self.ans