from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        def bfs(childrens, result):
            if len(childrens) == 0:
                return 
            result.append(childrens[-1].val)
            for i in range(len(childrens)):
                ch = childrens.popleft()
                if ch.left:
                    childrens.append(ch.left)
                if ch.right:
                    childrens.append(ch.right)
        
        result = []
        childrens = deque()

        if root is None:
            return result

        result.append(root.val)
        if root.left:
            childrens.append(root.left)
        if root.right:
            childrens.append(root.right)
            
        bfs(childrens, result)
        return result