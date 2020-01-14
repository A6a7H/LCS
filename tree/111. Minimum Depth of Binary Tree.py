class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        if None in [root.left, root.right]:
            l = self.minDepth(root.left)
            r = self.minDepth(root.right)
            return max(l,r) + 1
        else:
            l = self.minDepth(root.left)
            r = self.minDepth(root.right)
            return min(l,r) + 1
        
        
class Solution:
    def minDepth1(self, root):
        if not root:
            return 0
        queue, level = [root], 1
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
