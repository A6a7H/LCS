class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        self.memo = {}  # 0
        def dfs(node):  # 1
            if node.val in self.memo:  # 2
                return self.memo[node.val]
            res = Node(node.val, [])  # 3
            self.memo[node.val] = res  # 4
            for neigh in node.neighbors:  # 5
                res.neighbors.append(dfs(neigh))
            return res

        return dfs(node)
