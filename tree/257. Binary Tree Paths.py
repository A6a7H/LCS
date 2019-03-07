class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, st, res):
            if not root.left and not root.right:
            	res.append(st+str(root.val))
            if root.left:
            	dfs(root.left, st + str(root.val)+'->', res)
            if root.right:
            	dfs(root.right, st + str(root.val)+'->', res)
        if not root:
            return []
        res = []
        dfs(root,'',res)
        return res

        